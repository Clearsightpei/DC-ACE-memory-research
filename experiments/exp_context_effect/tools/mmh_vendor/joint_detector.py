"""Joint detector — derive structural joint specs for a character from
MakeMeAHanzi graphics.txt medians.

Used by the Teacher each cycle: given a target character, return the
list of joints the Drawer must satisfy. Joints encode WHERE two strokes
meet (cell), WHICH stroke contributes its head/tail/mid at the meeting,
and HOW close the two contributing points are in the MMH skeleton (used
to grade joint confidence).

Joint spec format (one per joint):
    {
        "stroke_a": int (1-indexed, matches the Drawer's stroke order),
        "stroke_b": int,
        "frac_a": float in [0, 1] (0 = head, 1 = tail),
        "frac_b": float in [0, 1],
        "label_a": "head" | "tail" | "mid(0.xx)",
        "label_b": "head" | "tail" | "mid(0.xx)",
        "cell": cell name from anchor.py (e.g. "C"),
        "meeting_canvas": (tx, ty) midpoint in turtle math-coords,
        "dist_mmh": float, MMH-space distance of the closest segment pair
                    (proxy for confidence — small = strong joint).
    }

The algorithm:
- Segment-to-segment closest distance between each pair of strokes'
  polyline segments. Clamped on both endpoints.
- One joint per stroke pair (the minimum-distance segment pair).
- Pair retained iff distance < EPS_MMH (default 90 — validated against
  五/丘/人/入/口/中/上/下/八 in the plan's iteration 3).

Coordinate transforms:
- MMH coords are 0..1024 with y-up (math convention).
- Canvas: 800×600, origin at center, y-up. Transform: (x-512)*0.4,
  (y-512)*0.4. Same as tools/make_char_gt.py uses (no flip).
"""

import json
import math
import os
from typing import List, Dict, Tuple, Optional


EPS_MMH_DEFAULT = 90.0  # validated threshold; see plan Part 6 iteration 3

# MMH coord transform — matches tools/make_char_gt.py.
_MMH_SCALE = 0.4
_MMH_CENTER = 512


def _find_graphics_txt() -> str:
    """Walk up from this file to find draw_character/graphics.txt."""
    here = os.path.dirname(os.path.abspath(__file__))
    for depth in range(6):
        candidate = os.path.join(here, *([".."] * depth), "draw_character", "graphics.txt")
        if os.path.exists(candidate):
            return os.path.abspath(candidate)
    return os.path.abspath(os.path.join(here, "..", "..", "draw_character", "graphics.txt"))


_GRAPHICS_TXT = _find_graphics_txt()
_CHAR_CACHE: Dict[str, Dict] = {}


def _load_char(char: str) -> Dict:
    """Load and cache the graphics.txt entry for a single character."""
    if char in _CHAR_CACHE:
        return _CHAR_CACHE[char]
    with open(_GRAPHICS_TXT, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            if entry["character"] == char:
                _CHAR_CACHE[char] = entry
                return entry
    raise KeyError(f"character {char!r} not found in {_GRAPHICS_TXT}")


def mmh_to_canvas(mmh_x: float, mmh_y: float) -> Tuple[float, float]:
    """Translate MMH (0..1024, y-up) to turtle math-coords (origin canvas
    center, y-up). Identity transform after scale + center-shift, no flip.
    """
    return (mmh_x - _MMH_CENTER) * _MMH_SCALE, (mmh_y - _MMH_CENTER) * _MMH_SCALE


def get_stroke_count(char: str) -> int:
    """How many strokes MMH says this character has (= Drawer's required
    turtle-call count)."""
    return len(_load_char(char)["medians"])


def get_medians(char: str) -> List[List[List[float]]]:
    """Per-stroke MMH polylines for a character.

    Returns a list of strokes; each stroke is a list of [x, y] points in
    MMH coords. The first point is the stroke head (where the brush
    starts); the last is the tail.
    """
    return _load_char(char)["medians"]


def _seg_seg_closest(a0, a1, b0, b1):
    """Closest distance between two segments a0-a1 and b0-b1, clamped on
    both endpoints. Returns (distance, t, u, point_on_a, point_on_b).
    """
    ax = a1[0] - a0[0]; ay = a1[1] - a0[1]
    bx = b1[0] - b0[0]; by = b1[1] - b0[1]
    wx = a0[0] - b0[0]; wy = a0[1] - b0[1]
    A = ax * ax + ay * ay
    B = ax * bx + ay * by
    C = bx * bx + by * by
    D = ax * wx + ay * wy
    E = bx * wx + by * wy
    denom = A * C - B * B
    if denom < 1e-9:
        t = 0.0
        u = (E / C) if C > 1e-9 else 0.0
    else:
        t = (B * E - C * D) / denom
        u = (A * E - B * D) / denom
    t = max(0.0, min(1.0, t))
    u = max(0.0, min(1.0, u))
    pa = (a0[0] + t * ax, a0[1] + t * ay)
    pb = (b0[0] + u * bx, b0[1] + u * by)
    d = math.hypot(pa[0] - pb[0], pa[1] - pb[1])
    return d, t, u, pa, pb


def _frac_along(polyline, segment_index, t_in_segment):
    """Arc-length fraction along a polyline at the given (segment, t)."""
    seg_lens = [math.hypot(polyline[k + 1][0] - polyline[k][0],
                           polyline[k + 1][1] - polyline[k][1])
                for k in range(len(polyline) - 1)]
    total = sum(seg_lens)
    if total < 1e-9:
        return 0.0
    prefix = sum(seg_lens[:segment_index]) + t_in_segment * seg_lens[segment_index]
    return prefix / total


def _label_position(frac: float) -> str:
    """Convert arc-length fraction to a head/tail/mid label."""
    if frac < 0.15:
        return "head"
    if frac > 0.85:
        return "tail"
    return f"mid({frac:.2f})"


def find_joints(char: str, eps_mmh: float = EPS_MMH_DEFAULT) -> List[Dict]:
    """Detect joints for a character by scanning MMH medians.

    Returns a list of joint specs (see module docstring). At most one
    joint per ordered stroke pair (i < j); the minimum-distance segment
    pair wins. Joints with distance ≥ eps_mmh are filtered out.
    """
    # Local import to avoid circular imports if anchor uses joints later.
    try:
        from anchor import xy_to_cell  # type: ignore
    except ImportError:
        from .anchor import xy_to_cell  # type: ignore

    medians = get_medians(char)
    out: List[Dict] = []
    for i in range(len(medians)):
        for j in range(i + 1, len(medians)):
            best = None
            for si in range(len(medians[i]) - 1):
                for sj in range(len(medians[j]) - 1):
                    d, t, u, pa, pb = _seg_seg_closest(
                        medians[i][si], medians[i][si + 1],
                        medians[j][sj], medians[j][sj + 1],
                    )
                    if d < eps_mmh and (best is None or d < best["d"]):
                        best = dict(d=d, si=si, sj=sj, t=t, u=u, pa=pa, pb=pb)
            if best is None:
                continue
            fa = _frac_along(medians[i], best["si"], best["t"])
            fb = _frac_along(medians[j], best["sj"], best["u"])
            meet_mmh = ((best["pa"][0] + best["pb"][0]) / 2.0,
                        (best["pa"][1] + best["pb"][1]) / 2.0)
            tx, ty = mmh_to_canvas(meet_mmh[0], meet_mmh[1])
            out.append({
                "stroke_a": i + 1,
                "stroke_b": j + 1,
                "frac_a": round(fa, 3),
                "frac_b": round(fb, 3),
                "label_a": _label_position(fa),
                "label_b": _label_position(fb),
                "cell": xy_to_cell(tx, ty),
                "meeting_canvas": (round(tx, 1), round(ty, 1)),
                "dist_mmh": round(best["d"], 1),
            })
    return out


def find_corners(char: str, stroke_index: int,
                 angle_threshold_deg: float = 45.0,
                 window: int = 2) -> List[Dict]:
    """Find interior corner points inside a single MMH stroke (the bend of
    横折 / 横折钩 / etc.). Used for compound strokes that the Drawer renders
    as ONE primitive but whose internal turn is part of the anchor spec.

    MMH samples a corner across 3–4 points (it rounds the corner). So
    measuring the turn between immediate neighbors under-reports. Instead
    we use a windowed direction-change: at each interior point k, compare
    the direction over [k-window, k] against [k, k+window]. Local maxima
    of that windowed angle above `angle_threshold_deg` are corners.

    Returns a list of corners as
        {"frac": float (arc-length fraction along the stroke),
         "angle_deg": float (windowed direction change in degrees),
         "point_canvas": (tx, ty), "cell": cell_name}
    sorted by descending angle.
    """
    try:
        from anchor import xy_to_cell  # type: ignore
    except ImportError:
        from .anchor import xy_to_cell  # type: ignore

    median = get_medians(char)[stroke_index - 1]  # 1-indexed
    if len(median) < (2 * window + 1):
        return []

    # Compute windowed angle at every interior point.
    raw: List[Tuple[int, float]] = []  # (index, angle_deg)
    for k in range(window, len(median) - window):
        before = median[k - window]
        after = median[k + window]
        p = median[k]
        v0 = (p[0] - before[0], p[1] - before[1])
        v1 = (after[0] - p[0], after[1] - p[1])
        n0 = math.hypot(*v0); n1 = math.hypot(*v1)
        if n0 < 1e-6 or n1 < 1e-6:
            continue
        cos = max(-1.0, min(1.0, (v0[0] * v1[0] + v0[1] * v1[1]) / (n0 * n1)))
        raw.append((k, math.degrees(math.acos(cos))))

    # Keep only local maxima above the threshold.
    out: List[Dict] = []
    for idx, (k, angle) in enumerate(raw):
        if angle < angle_threshold_deg:
            continue
        # Local max in raw list (within a 1-step window).
        if idx > 0 and raw[idx - 1][1] > angle:
            continue
        if idx + 1 < len(raw) and raw[idx + 1][1] > angle:
            continue
        tx, ty = mmh_to_canvas(median[k][0], median[k][1])
        frac = _frac_along(median, k, 0.0)
        out.append({
            "frac": round(frac, 3),
            "angle_deg": round(angle, 1),
            "point_canvas": (round(tx, 1), round(ty, 1)),
            "cell": xy_to_cell(tx, ty),
        })
    out.sort(key=lambda c: c["angle_deg"], reverse=True)
    # Cluster adjacent corners (within 0.15 of arc-length frac): keep the
    # strongest. MMH sometimes splits a single physical corner across two
    # neighboring sample points.
    deduped: List[Dict] = []
    for c in out:
        if any(abs(c["frac"] - kept["frac"]) < 0.15 for kept in deduped):
            continue
        deduped.append(c)
    return deduped


# ─────────────────── Self-test ────────────────────────────────────
if __name__ == "__main__":
    samples = ['上', '下', '人', '入', '八', '口', '中', '五', '丘']
    for c in samples:
        n = get_stroke_count(c)
        joints = find_joints(c)
        print(f"=== {c} ({n} strokes, {len(joints)} joints) ===")
        for j in joints:
            print(f"  s{j['stroke_a']}.{j['label_a']:<11} ⇆ s{j['stroke_b']}.{j['label_b']:<11} "
                  f"@ {j['cell']:<3} {j['meeting_canvas']} d={j['dist_mmh']}")
    # Compound stroke corner detection
    print("\n=== compound-stroke corners ===")
    for c, idx in [('口', 2), ('日', 2)]:
        try:
            corners = find_corners(c, idx)
        except KeyError:
            continue
        print(f"{c} stroke {idx} corners: {corners}")
