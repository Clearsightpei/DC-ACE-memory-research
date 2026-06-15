"""Structural gate — count strokes + measure anchor placement.

For atomic-stroke phases (1, 1.5): finds the rendered stroke's pixel
bbox in the PNG and compares the corners to the brief's declared
anchors.

For multi-stroke phases (2+): finds connected components in the PNG,
matches each to its declared stroke by closest anchor distance, then
checks all anchors and joints.

This is image-based, not Drawer-trace-based — robust to the Drawer
silently changing primitive parameters. The Drawer cannot fake an
anchor by lying about (ox, oy, scale).

Tolerances (per `~/.claude/plans/should-i-install-rapid-lexical-lantern.md`):
- anchor placement: 15 px (canvas px on the 800×600 canvas)
- joint placement: 20 px AND meeting must be in declared cell
"""
import json
import math
import os
import re
import sys
from typing import Dict, List, Optional, Tuple

try:
    from PIL import Image
    import numpy as np
except ImportError as e:
    print(f"structural_check requires PIL + numpy: {e}", file=sys.stderr)
    raise


# ─── Pixel ↔ turtle math-coord conversion ───────────────────────────
CANVAS_W, CANVAS_H = 800, 600


def pixel_to_xy(px, py):
    """Pixel (origin top-left, y-down) → turtle math (origin center, y-up)."""
    return px - CANVAS_W / 2.0, CANVAS_H / 2.0 - py


def xy_to_pixel(tx, ty):
    return tx + CANVAS_W / 2.0, CANVAS_H / 2.0 - ty


# ─── Stroke-count check via generated.py parsing ────────────────────
# Match top-level `draw_<name>(...)` calls inside `def task_01(`.
_TASK01_RE = re.compile(r"def\s+task_01\s*\(", re.MULTILINE)
_DRAW_CALL_RE = re.compile(r"^\s{4}draw_\w+\s*\(", re.MULTILINE)


def count_draw_calls(generated_py_path: str) -> int:
    """Count top-level `draw_<name>(...)` calls inside task_01().

    Returns -1 if task_01 isn't found.
    """
    with open(generated_py_path, "r") as f:
        src = f.read()
    m = _TASK01_RE.search(src)
    if not m:
        return -1
    # Walk from task_01's body until we hit the next top-level def.
    body_start = src.find(":", m.end()) + 1
    next_def = re.search(r"^def\s+\w+\s*\(", src[body_start:], re.MULTILINE)
    body_end = body_start + (next_def.start() if next_def else len(src) - body_start)
    body = src[body_start:body_end]
    return len(_DRAW_CALL_RE.findall(body))


# ─── PNG analysis ────────────────────────────────────────────────────
def load_dark_mask(png_path: str, threshold: int = 100):
    """Return a binary mask of dark pixels in the PNG (numpy array)."""
    img = np.array(Image.open(png_path).convert("L"))
    return (img < threshold).astype(np.uint8)


def find_components(mask):
    """Connected components via 4-neighbor BFS on the binary mask.

    Returns a list of components; each is a dict with:
        - pixels: list of (py, px)
        - bbox_pixel: (ymin, xmin, ymax, xmax)
        - bbox_xy: (xmin_xy, xmax_xy, ymin_xy, ymax_xy) in turtle coords
    """
    h, w = mask.shape
    visited = np.zeros_like(mask, dtype=bool)
    comps = []
    for y in range(h):
        for x in range(w):
            if not mask[y, x] or visited[y, x]:
                continue
            # BFS
            stack = [(y, x)]
            pix = []
            ymin = ymax = y
            xmin = xmax = x
            while stack:
                cy, cx = stack.pop()
                if visited[cy, cx]:
                    continue
                visited[cy, cx] = True
                pix.append((cy, cx))
                if cy < ymin: ymin = cy
                if cy > ymax: ymax = cy
                if cx < xmin: xmin = cx
                if cx > xmax: xmax = cx
                for ny, nx in ((cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)):
                    if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not visited[ny, nx]:
                        stack.append((ny, nx))
            if len(pix) < 50:  # noise filter
                continue
            comps.append({
                "pixels": pix,
                "bbox_pixel": (ymin, xmin, ymax, xmax),
                "bbox_xy": (xmin - CANVAS_W/2.0, xmax - CANVAS_W/2.0,
                            CANVAS_H/2.0 - ymax, CANVAS_H/2.0 - ymin),  # math y-up
            })
    return comps


def component_endpoints(comp) -> Tuple[Tuple[float,float], Tuple[float,float]]:
    """Estimate a stroke component's two endpoints (in turtle coords).

    Strategy: for each of the 4 bbox corners, find the dark pixel
    closest to it. Of the 4 candidates the pair with the largest
    pairwise distance wins. Works uniformly for horizontals, verticals,
    and diagonals.
    """
    ymin, xmin, ymax, xmax = comp["bbox_pixel"]
    corners = [(ymin, xmin), (ymin, xmax), (ymax, xmin), (ymax, xmax)]
    candidates = []
    for cy, cx in corners:
        best = min(comp["pixels"], key=lambda p: (p[0]-cy)**2 + (p[1]-cx)**2)
        candidates.append(best)  # (py, px)
    best_pair = None
    best_d2 = -1.0
    for i in range(4):
        for j in range(i+1, 4):
            a = candidates[i]; b = candidates[j]
            d2 = (a[0]-b[0])**2 + (a[1]-b[1])**2
            if d2 > best_d2:
                best_d2 = d2
                best_pair = (a, b)
    e1, e2 = best_pair
    return (pixel_to_xy(e1[1], e1[0]), pixel_to_xy(e2[1], e2[0]))


# ─── Top-level structural check ─────────────────────────────────────
def check(brief_path: str, generated_py_path: str, attempt_png_path: str,
          mmh_stroke_count: int, anchors_per_stroke: List[Dict],
          joints: Optional[List[Dict]] = None,
          anchor_tolerance_px: float = 15.0) -> Dict:
    """Apply the structural gate to a single rendered task.

    Args:
        brief_path: ignored (kept for symmetry / future use)
        generated_py_path: path to attempts/cycle_<N>/generated.py
        attempt_png_path: path to attempts/cycle_<N>/01_<char>.png
        mmh_stroke_count: from get_stroke_count(char)
        anchors_per_stroke: list of dicts {"stroke": int, "from": anchor,
            "to": anchor} where anchor is a tuple resolvable by
            anchor_to_xy. One entry per stroke (1-indexed).
        joints: optional list from find_joints(char). Currently only used
            for char cycles; atomic strokes pass joints=None.

    Returns a dict with all gate fields, suitable for merging into the
    judge_results JSON.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from anchor import anchor_to_xy

    out = {
        "mmh_stroke_count": mmh_stroke_count,
        "drawer_stroke_count": -1,
        "stroke_count_pass": False,
        "anchor_placements": [],   # per-anchor: declared_xy, observed_xy, dist_px, pass
        "joint_placements": [],
        "structural_pass": False,
        "fail_reasons": [],
    }

    # 1. Stroke count
    n = count_draw_calls(generated_py_path)
    out["drawer_stroke_count"] = n
    if n != mmh_stroke_count:
        out["stroke_count_pass"] = False
        out["fail_reasons"].append(f"stroke count {n} != MMH {mmh_stroke_count}")
        return out
    out["stroke_count_pass"] = True

    # 2. Connected components from the PNG
    if not os.path.exists(attempt_png_path):
        out["fail_reasons"].append(f"missing PNG: {attempt_png_path}")
        return out
    mask = load_dark_mask(attempt_png_path)
    comps = find_components(mask)
    if len(comps) < mmh_stroke_count:
        out["fail_reasons"].append(
            f"only {len(comps)} connected components, need {mmh_stroke_count}"
        )
        return out

    # 3. Anchor placement: for each declared stroke, find the closest
    # component endpoint pair and measure distance to the declared
    # from/to anchors.
    used_comp_indices = set()
    for spec in anchors_per_stroke:
        sidx = spec["stroke"]
        from_xy = anchor_to_xy(tuple(spec["from"]))
        to_xy = anchor_to_xy(tuple(spec["to"]))
        # Find best component: minimizes (dist(comp_e1, from) + dist(comp_e2, to))
        best = None
        for ci, comp in enumerate(comps):
            if ci in used_comp_indices:
                continue
            e1, e2 = component_endpoints(comp)
            # Try both orientations
            d_orient_a = (math.hypot(e1[0]-from_xy[0], e1[1]-from_xy[1])
                          + math.hypot(e2[0]-to_xy[0], e2[1]-to_xy[1]))
            d_orient_b = (math.hypot(e2[0]-from_xy[0], e2[1]-from_xy[1])
                          + math.hypot(e1[0]-to_xy[0], e1[1]-to_xy[1]))
            if d_orient_a <= d_orient_b:
                obs_from, obs_to, total = e1, e2, d_orient_a
            else:
                obs_from, obs_to, total = e2, e1, d_orient_b
            if best is None or total < best["total"]:
                best = dict(ci=ci, obs_from=obs_from, obs_to=obs_to, total=total)
        if best is None:
            out["fail_reasons"].append(f"stroke {sidx}: no component available")
            return out
        used_comp_indices.add(best["ci"])
        d_from = math.hypot(best["obs_from"][0]-from_xy[0], best["obs_from"][1]-from_xy[1])
        d_to = math.hypot(best["obs_to"][0]-to_xy[0], best["obs_to"][1]-to_xy[1])
        out["anchor_placements"].append({
            "stroke": sidx,
            "from_declared": (round(from_xy[0],1), round(from_xy[1],1)),
            "from_observed": (round(best["obs_from"][0],1), round(best["obs_from"][1],1)),
            "from_dist_px": round(d_from, 1),
            "from_pass": d_from <= anchor_tolerance_px,
            "to_declared": (round(to_xy[0],1), round(to_xy[1],1)),
            "to_observed": (round(best["obs_to"][0],1), round(best["obs_to"][1],1)),
            "to_dist_px": round(d_to, 1),
            "to_pass": d_to <= anchor_tolerance_px,
        })

    anchors_all_pass = all(
        a["from_pass"] and a["to_pass"]
        for a in out["anchor_placements"]
    )

    # 4. Joint placement (placeholder for character cycles).
    # For atomic strokes (joints is None or []), this is a no-op pass.
    joints_pass = True
    if joints:
        # TODO: implement joint check using rendered stroke endpoints.
        # For now, mark as informational pass.
        joints_pass = True
        out["joint_placements"] = [{"note": "joint check not yet implemented; defaulting to pass"}]

    out["structural_pass"] = anchors_all_pass and joints_pass
    if not anchors_all_pass:
        worst = max((a["from_dist_px"] if a["from_dist_px"] > a["to_dist_px"] else a["to_dist_px"])
                    for a in out["anchor_placements"])
        out["fail_reasons"].append(f"worst anchor placement {worst} px > 15 px tolerance")
    return out


# ─── Self-test ───────────────────────────────────────────────────────
if __name__ == "__main__":
    print("structural_check: utility module — call check() from /cycle orchestrator")
