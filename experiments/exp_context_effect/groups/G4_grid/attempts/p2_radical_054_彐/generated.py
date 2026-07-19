"""彐 (jì) — 3-stroke radical.

Anchor plan:
  stroke 1 (横折): head @ ('ML', 0.6, 0.35) [~upper-left],
                   corner @ ('MR', 0.05, 0.35) [top-right shoulder],
                   tail @ ('MR', 0.05, 0.9) [descending to middle-right]
                   width h=9, v=9
  stroke 2 (横): head @ ('ML', 0.65, 0.65) [middle-left, indented right of s1 head],
                 tail @ ('C', 0.85, 0.6) [ends left of s1 vertical] — width 8, SHORTER
  stroke 3 (横): head @ ('BL', 0.55, 0.30) [bottom-left, extends further left],
                 tail @ ('BR', 0.15, 0.30) [bottom-right, near s1 tail] — width 9

Joints:
  s1.tail (bottom of vertical) ⇆ s3.tail (right end of bottom 横) — N (small gap)
  s2.tail ⇆ s1 vertical body — N (natural gap, do not weld)

Compared to MMH endpoints:
  s1 MMH: head ML(0.885, 0.248), tail BC(0.96, 0.443). Applying TR9
    (MMH under-spans for standalone radicals) — expand to fill the grid more.
    We move head anchor left (into ML mid) and push corner into MR, tail
    to lower-MR so vertical is prominent.
  s2 MMH: head ML(0.727, 0.928), tail C(0.896, 0.878). Adjusted to
    keep same cell family (ML/C row) but at cleaner y for a horizontal.
  s3 MMH: head BL(0.771, 0.657), tail BR(0.232, 0.607). Very close to
    MMH; kept nearly verbatim.
"""

import os
import sys
from PIL import Image, ImageDraw

# Import shared primitives from success_bank/code.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402


# ---------- self-check (mandatory G4 field) ----------
SELF_CHECK = {
    'visual_ok': None,             # filled in below after inspecting the render
    'stroke_count_ok': True,       # 3 strokes as required
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ''
}


def draw_heng_zhe_inline(draw, head, corner, tail,
                         h_width=9, v_width=9, shoulder=11,
                         color=(0, 0, 0)):
    """Inline 横折: horizontal head→corner, vertical corner→tail with a
    filled shoulder disc at the corner (顿笔 press). P-weld at corner
    is implicit — corner anchor is shared by both segments."""
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)
    fat_line(draw, p_head, p_corner, h_width, color=color)
    fat_line(draw, p_corner, p_tail, v_width, color=color)
    r = shoulder / 2.0
    cx, cy = p_corner
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    return p_head, p_corner, p_tail


def draw_heng_inline(draw, from_anchor, to_anchor, width=9, color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p1 = anchor_to_xy(to_anchor)
    fat_line(draw, p0, p1, width, color=color)
    return p0, p1


def render(out_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: 横折 (top horizontal + right descent) ---
    # Revised: extend top bar further left (matches GT — top bar is long)
    # and descend vertical further so its bottom aligns near bottom 横.
    s1_head = ('ML', 0.35, 0.30)
    s1_corner = ('C', 0.85, 0.30)
    s1_tail = ('C', 0.85, 1.00)
    p1h, p1c, p1t = draw_heng_zhe_inline(
        draw, s1_head, s1_corner, s1_tail, h_width=9, v_width=9, shoulder=12
    )

    # Direction invariants for stroke 1.
    assert p1c[0] > p1h[0], "横折 horizontal should go left->right"
    assert p1t[1] > p1c[1], "横折 vertical descent should go top->bottom"
    assert abs(p1c[0] - p1t[0]) < 6, "横折 vertical should be near-straight down"

    # --- Stroke 2: middle 横 (shorter, sits inside the bracket) ---
    s2_head = ('ML', 0.45, 0.62)
    s2_tail = ('C', 0.60, 0.62)
    p2h, p2t = draw_heng_inline(draw, s2_head, s2_tail, width=8)
    assert p2t[0] > p2h[0], "middle 横 should run left->right"

    # --- Stroke 3: bottom 横 (longer, aligns with bottom of vertical) ---
    s3_head = ('BL', 0.35, 0.00)
    s3_tail = ('C', 0.90, 0.00)
    p3h, p3t = draw_heng_inline(draw, s3_head, s3_tail, width=9)
    assert p3t[0] > p3h[0], "bottom 横 should run left->right"

    # --- Joint diagnostics ---
    # s1.tail ⇆ s3.tail (near BC/BR): both endpoints should be close pixel-wise.
    import math
    j1_gap = math.hypot(p1t[0] - p3t[0], p1t[1] - p3t[1])
    # s2.tail ⇆ s1 vertical body at y=p2t[1]: horizontal distance from
    # s2.tail x to the x-position of s1 vertical at that y (constant x).
    j2_gap = abs(p2t[0] - p1c[0])  # s1 vertical has constant x = p1c[0]

    # --- Populate SELF_CHECK ---
    # Expected anchors (from brief) vs actual.
    exp_s1_head = ('ML', 0.885, 0.248)
    exp_s1_tail = ('BC', 0.96, 0.443)
    exp_s2_head = ('ML', 0.727, 0.928)
    exp_s2_tail = ('C', 0.896, 0.878)
    exp_s3_head = ('BL', 0.771, 0.657)
    exp_s3_tail = ('BR', 0.232, 0.607)

    def delta(actual, expected):
        # actual and expected are (cell, xf, yf).
        # Compare pixel positions.
        ax, ay = anchor_to_xy(actual)
        ex, ey = anchor_to_xy(expected)
        return (round(ax - ex, 1), round(ay - ey, 1))

    SELF_CHECK['endpoint_mismatches'] = [
        # We are consciously overriding MMH per TR9 (standalone radical).
        {'stroke': 1, 'field': 'head', 'expected': exp_s1_head,
         'actual': s1_head, 'delta_px': delta(s1_head, exp_s1_head),
         'reason': 'TR9 override: expand for standalone radical'},
        {'stroke': 1, 'field': 'tail', 'expected': exp_s1_tail,
         'actual': s1_tail, 'delta_px': delta(s1_tail, exp_s1_tail),
         'reason': 'TR9 override: vertical descends further (MR bottom)'},
        {'stroke': 2, 'field': 'head', 'expected': exp_s2_head,
         'actual': s2_head, 'delta_px': delta(s2_head, exp_s2_head),
         'reason': 'MMH y_frac 0.928 in ML row would put it at bottom of ML cell (y=192.8); we place at y=160 to sit visually in the middle band'},
        {'stroke': 2, 'field': 'tail', 'expected': exp_s2_tail,
         'actual': s2_tail, 'delta_px': delta(s2_tail, exp_s2_tail),
         'reason': 'shortened middle 横; stops left of s1 vertical'},
        {'stroke': 3, 'field': 'head', 'expected': exp_s3_head,
         'actual': s3_head, 'delta_px': delta(s3_head, exp_s3_head),
         'reason': 'moved slightly left to make bottom 横 the longest'},
        {'stroke': 3, 'field': 'tail', 'expected': exp_s3_tail,
         'actual': s3_tail, 'delta_px': delta(s3_tail, exp_s3_tail),
         'reason': 'aligned near s1.tail for N-class joint'},
    ]

    SELF_CHECK['joint_class_mismatches'] = []
    # Expected joint 1: s1.mid(0.79) ⇆ s2.tail — N (~32.8px). Our j2_gap
    # is horizontal distance from s2.tail to s1 vertical (which contains
    # the mid-point of s1 by construction). Log it.
    # Expected joint 2: s1.tail ⇆ s3.mid(0.81) — N (~16.4px). We record
    # j1_gap as a proxy (s1.tail to s3.tail — close enough since s3.mid
    # is between).
    SELF_CHECK['notes'] = (
        f"j1 (s2.tail<->s1 vertical body) horiz gap={j2_gap:.1f}px "
        f"(target N ~32.8, ok range 15-40); "
        f"j2 (s1.tail<->s3.tail proxy) gap={j1_gap:.1f}px "
        f"(target N ~16.4). "
        "Visual features vs GT: "
        "(1) top-right shows a horizontal + vertical L-shape (横折) with the "
        "vertical descending from the shoulder to near the bottom row; "
        "(2) three horizontal levels: top (bar of 横折), middle (short 横), "
        "bottom (long 横); "
        "(3) bottom 横 is the longest of the three, top bar is medium, "
        "middle 横 is shortest — matches GT."
    )
    # Post-revision visual audit: the revision introduced a cell-row bug
    # (mixing BL row=2 with C row=1 for stroke 3, and C row=1 for stroke 1
    # tail 'C' 0.85,1.0 -> y=200, corner C 0.85,0.3 -> y=130 is fine,
    # but stroke 3 BL(row2) -> C(row1) makes the bottom 横 diagonal, not
    # horizontal). Second render is a regression versus first. Per shared
    # rules I still submit — no third pass allowed.
    SELF_CHECK['visual_ok'] = False
    SELF_CHECK['overall_pass'] = False
    SELF_CHECK['notes'] += (
        " || POST-REVISION DEFECT: stroke 3 uses BL(row=2) head and "
        "C(row=1) tail -> renders as a diagonal, not a horizontal 横. "
        "Same-row cells must be used for a 横 (BL+BC, or BL+BR, or "
        "BC+BR). This regressed vs the first attempt. Submitting as-is "
        "per one-revision rule."
    )

    img.save(out_path)
    return SELF_CHECK


if __name__ == '__main__':
    out = os.path.join(_HERE, '01_彐.png')
    result = render(out)
    print("SELF_CHECK:", result)
    print("Wrote", out)
