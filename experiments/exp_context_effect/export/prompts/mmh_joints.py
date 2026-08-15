"""mmh_joints.py — Phase-3 joint expectations for G4, derived from MMH.

Wraps run_6's `joint_detector` + `classify_joints` and translates
results into G4's coordinate system (300x300 PIL, y-DOWN, 3x3 米字格).

Two callers:
- `dispatcher` uses `render_joint_brief_block(char)` to append
  expected-joints text to a G4 Phase-3 Drawer prompt.
- The G4 Drawer uses `expected_joints(char)` for its pre-submit
  self-check (compare declared joints vs expected classes).

Not needed for Phase 1 (strokes) or Phase 2 (radicals) — MMH does not
cover them. Callers should only invoke this for phase == 'character'.
"""
import os
import sys
from typing import List, Dict, Tuple

# Point sys.path at run_6's tools so we can import the vetted MMH modules.
_HERE = os.path.dirname(os.path.abspath(__file__))
_RUN6_TOOLS = os.path.abspath(os.path.join(_HERE, "..", "..", "..", "runs", "run_6", "tools"))
if _RUN6_TOOLS not in sys.path:
    sys.path.insert(0, _RUN6_TOOLS)

from joint_detector import (  # noqa: E402
    find_joints,
    get_stroke_count,
    get_medians,
)
from classify_joints import classify, gap_canvas_px  # noqa: E402


# ── G4 coordinate system ───────────────────────────────────────────
# G4 renders on 300x300 PIL canvas (y grows DOWN). MMH is 0..1024
# (y grows UP). Both use the same 3x3 米字格 partition of the drawing
# region, so cell mapping is: cell column from x, cell row from y-flipped.

CANVAS = 300
CELL = CANVAS / 3.0  # 100 px

_COL_NAMES = ("L", "C", "R")   # left, center, right
_ROW_NAMES = ("T", "M", "B")   # top, middle, bottom -> paired: TL, TC, ...

_MMH_MAX = 1024.0


def mmh_to_g4_px(mmh_x: float, mmh_y: float) -> Tuple[float, float]:
    """MMH (0..1024, y-up) → G4 PIL pixel coords (0..300, y-down)."""
    px = mmh_x / _MMH_MAX * CANVAS
    py = (_MMH_MAX - mmh_y) / _MMH_MAX * CANVAS
    return px, py


def px_to_anchor(px: float, py: float) -> Tuple[str, float, float]:
    """G4 pixel (px, py) → (cell, x_frac, y_frac) with y_frac growing DOWN
    within its cell (PIL convention, matches groups/G4_grid/success_bank/code/_anchor.py).
    """
    col_i = min(2, max(0, int(px // CELL)))
    row_i = min(2, max(0, int(py // CELL)))
    cell = _ROW_NAMES[row_i] + _COL_NAMES[col_i]
    if cell == "MC":  # G4 uses bare 'C' for middle-center
        cell = "C"
    x_frac = (px - col_i * CELL) / CELL
    y_frac = (py - row_i * CELL) / CELL
    return cell, round(x_frac, 3), round(y_frac, 3)


def _polyline_to_g4(polyline_mmh):
    return [mmh_to_g4_px(x, y) for x, y in polyline_mmh]


# ── Public API ─────────────────────────────────────────────────────

def expected_joints(char: str) -> Dict:
    """Return the full G4 joint expectations for a Phase-3 character.

    {
      "char": "口",
      "stroke_count": 3,
      "medians_g4_px": [ [(x,y), ...], ... ],
      "endpoints": [
          {"stroke": 1, "head_anchor": ('TL',0.66,0.20), "tail_anchor": ('BL',0.85,0.90)},
          ...
      ],
      "joints": [
          {"stroke_a":1, "stroke_b":2, "class":"N", "cell":"TR",
           "meeting_anchor":('TR',0.10,0.20), "expected_gap_px": 13.2,
           "label_a":"tail", "label_b":"head", "dist_mmh":32.9},
          ...
      ],
    }
    """
    stroke_count = get_stroke_count(char)
    medians = get_medians(char)
    medians_g4 = [_polyline_to_g4(p) for p in medians]

    endpoints = []
    for i, poly in enumerate(medians_g4, start=1):
        head = poly[0]
        tail = poly[-1]
        endpoints.append({
            "stroke": i,
            "head_anchor": px_to_anchor(*head),
            "tail_anchor": px_to_anchor(*tail),
        })

    joints_raw = find_joints(char)
    joints_out = []
    for j in joints_raw:
        cls = classify(j)
        # meeting_canvas is in run_6 turtle math coords — recompute in
        # G4 pixels from the underlying medians.
        # find_joints returns meeting_canvas via mmh_to_canvas + midpoint;
        # regenerate the meeting point in G4-pixels from label + frac.
        sa = j["stroke_a"] - 1
        sb = j["stroke_b"] - 1
        pa = _point_at_frac(medians_g4[sa], j["frac_a"])
        pb = _point_at_frac(medians_g4[sb], j["frac_b"])
        mx, my = (pa[0] + pb[0]) / 2.0, (pa[1] + pb[1]) / 2.0
        meeting_anchor = px_to_anchor(mx, my)
        joints_out.append({
            "stroke_a": j["stroke_a"],
            "stroke_b": j["stroke_b"],
            "label_a": j["label_a"],
            "label_b": j["label_b"],
            "class": cls,
            "cell": meeting_anchor[0],
            "meeting_anchor": meeting_anchor,
            "meeting_px": (round(mx, 1), round(my, 1)),
            "dist_mmh": round(j["dist_mmh"], 2),
            "expected_gap_px": round(gap_canvas_px(j), 1) if cls == "N" else 0.0,
        })

    return {
        "char": char,
        "stroke_count": stroke_count,
        "medians_g4_px": medians_g4,
        "endpoints": endpoints,
        "joints": joints_out,
    }


def _point_at_frac(polyline_px, frac):
    """Point along a polyline at cumulative arc-length fraction (0..1)."""
    if frac <= 0.0:
        return polyline_px[0]
    if frac >= 1.0:
        return polyline_px[-1]
    seg_lens = []
    total = 0.0
    for i in range(len(polyline_px) - 1):
        dx = polyline_px[i + 1][0] - polyline_px[i][0]
        dy = polyline_px[i + 1][1] - polyline_px[i][1]
        L = (dx * dx + dy * dy) ** 0.5
        seg_lens.append(L)
        total += L
    target = frac * total
    accum = 0.0
    for i, L in enumerate(seg_lens):
        if accum + L >= target:
            t = (target - accum) / L if L > 1e-9 else 0.0
            x = polyline_px[i][0] + t * (polyline_px[i + 1][0] - polyline_px[i][0])
            y = polyline_px[i][1] + t * (polyline_px[i + 1][1] - polyline_px[i][1])
            return (x, y)
        accum += L
    return polyline_px[-1]


def render_joint_brief_block(char: str) -> str:
    """Human-readable expectations block to append to a Drawer prompt."""
    exp = expected_joints(char)
    lines = [
        f"## MMH-derived structural expectations (G4 Phase-3 mandatory)",
        f"",
        f"Character: **{char}**",
        f"Expected stroke count: **{exp['stroke_count']}** (your `generated.py` must produce exactly this many strokes).",
        f"",
        f"### Per-stroke endpoint anchors (from MMH medians → G4 米字格)",
        f"",
    ]
    for ep in exp["endpoints"]:
        lines.append(
            f"  - stroke {ep['stroke']}: head @ {ep['head_anchor']} · tail @ {ep['tail_anchor']}"
        )

    if exp["joints"]:
        lines.append("")
        lines.append(f"### Joint expectations ({len(exp['joints'])} joint{'s' if len(exp['joints'])!=1 else ''})")
        lines.append("")
        lines.append("Class key:  **P** piercing (welded crossing) · **T** tangent (tip touches body) · **N** neighbor (small natural gap = correct calligraphy — DO NOT weld).")
        lines.append("")
        for j in exp["joints"]:
            gap = f"expected gap ≈ {j['expected_gap_px']} px" if j["class"] == "N" else "welded"
            lines.append(
                f"  - s{j['stroke_a']}.{j['label_a']} ⇆ s{j['stroke_b']}.{j['label_b']} "
                f"@ cell {j['cell']} ({j['meeting_anchor']}) : **{j['class']}** — {gap}   "
                f"(MMH dist={j['dist_mmh']})"
            )
    else:
        lines.append("")
        lines.append("### Joint expectations: NONE (strokes do not meet — clear separation).")

    lines.extend([
        "",
        "### MANDATORY pre-submit self-check",
        "",
        "Before writing your final PNG, your `generated.py` code (or a comment block in it) MUST include:",
        "",
        "1. **Stroke count**: verify the number of stroke primitives you called matches the expected count above.",
        "2. **Endpoint anchors**: for each stroke, state the anchor you actually used for head and tail; compare vs expected. Anchors within ±0.20 x_frac / y_frac of expected (same cell OR immediately adjacent cell) count as a match.",
        "3. **Joint classes**: for each expected joint, state the class you implemented (P/T/N) and confirm it matches. If class is N, note the actual pixel gap between the two strokes at that joint (should be near `expected_gap_px`, not 0).",
        "",
        "Log the self-check outcome as a Python dict at the top of `generated.py`:",
        "",
        "```python",
        "SELF_CHECK = {",
        "    'visual_ok': True,          # visual comparison of PNG vs GT (see G4 rules step 5a)",
        "    'stroke_count_ok': True,    # or False + note",
        "    'endpoint_mismatches': [],  # list of {stroke, expected, actual, delta}",
        "    'joint_class_mismatches': [], # list of {joint, expected_class, actual_class}",
        "    'overall_pass': True,       # visual_ok AND all structural fields OK",
        "    'notes': '...'",
        "}",
        "```",
        "",
        "If `overall_pass` is False, **revise `generated.py` once** to fix the specific defect, re-run, submit the new PNG. Only one revision (max 2 render passes). If the second render still fails, submit it and append a note to `sandbox.md`.",
        "",
    ])
    return "\n".join(lines)


# ── Self-test ──────────────────────────────────────────────────────
if __name__ == "__main__":
    # Validate against a few characters run_6 has already vetted.
    for c in ["口", "八", "半", "力", "人"]:
        try:
            exp = expected_joints(c)
        except Exception as e:
            print(f"[{c}] ERROR: {e}")
            continue
        print(f"\n=== {c} ({exp['stroke_count']} strokes, {len(exp['joints'])} joints) ===")
        for ep in exp["endpoints"]:
            print(f"  s{ep['stroke']}: {ep['head_anchor']} → {ep['tail_anchor']}")
        for j in exp["joints"]:
            print(
                f"  joint s{j['stroke_a']}.{j['label_a']} ⇆ s{j['stroke_b']}.{j['label_b']} "
                f"@ {j['cell']}: {j['class']}  gap≈{j['expected_gap_px']}px  (dist_mmh={j['dist_mmh']})"
            )
