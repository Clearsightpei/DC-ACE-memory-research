"""九 (jiǔ, 2 strokes: 撇 + 横折弯钩) — Phase-3 attempt (v2 vs clean GT).

MMH-derived anchors:
  stroke 1 撇:      head TC(0.178, 0.633) → tail BL(0.229, 0.856)
  stroke 2 横折弯钩: head ML(0.448, 0.617) → tail BR(0.771, 0.218)
  joint (P, welded): s1.mid(0.35) ⇆ s2.mid(0.19) @ C(0.242, 0.492)

Prior attempt was drawn against a corrupted GT. Clean GT shows:
  - s1: smooth pie sweeping from upper-mid down to bottom-left.
  - s2: a nearly-horizontal top, a soft rounded corner (not
    right-angle), a moderate descent down the right side, wide
    U-belly across the bottom, and a small up-flick.
  - The horizontal (top) of s2 crosses s1 near the middle → P weld.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'v2 vs clean GT: smoother rounded corner on s2, thinner ink, wider belly.'
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

_BANK = Path(__file__).resolve().parents[3] / 'G4_grid' / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402


def draw_jiu(draw):
    # -------- stroke 1: 撇 (smooth diagonal sweep) --------
    draw_pie(draw,
             ('TC', 0.178, 0.633),
             ('BL', 0.229, 0.856),
             head_width=6, tail_width=1, curve=0.10, segments=56)

    # -------- stroke 2: 横折弯钩 (single continuous smooth curve) --------
    # Design (revision — vs clean GT):
    #   1. short horizontal top from ML → past C into MR
    #   2. soft rounded corner in MR
    #   3. descend right side of BR with subtle inward curve
    #   4. wide U-belly sweeping LEFT into BC
    #   5. back up-right to the up-flick tip at BR(0.771, 0.218)
    p_head   = anchor_to_xy(('ML', 0.448, 0.617))   # horizontal start
    p_topR   = anchor_to_xy(('MR', 0.60, 0.60))     # end of top, before corner
    p_corner = anchor_to_xy(('MR', 0.75, 0.85))     # rounded corner apex
    p_side   = anchor_to_xy(('BR', 0.80, 0.45))     # right side descent
    p_belly  = anchor_to_xy(('BC', 0.90, 0.92))     # bottom of U — deep in BC
    p_tip    = anchor_to_xy(('BR', 0.771, 0.218))   # up-flick tip (MMH)

    # Segment A: horizontal head → topR (very slight downward drift)
    ctrl_top = ((p_head[0] + p_topR[0]) / 2.0,
                (p_head[1] + p_topR[1]) / 2.0 - 1)
    top_pts = quad_bezier(p_head, ctrl_top, p_topR, n=48)
    top_widths = [4 + (i / 48) * 1 for i in range(49)]

    # Segment B: rounded corner topR → corner → side (smooth arc)
    corner_pts = quad_bezier(p_topR, p_corner, p_side, n=40)
    corner_widths = [5 + (i / 40) * 1 for i in range(41)]

    # Segment C: wide U-belly p_side → p_belly (sweeping left & down)
    ctrl_belly = (p_side[0] - 8, p_belly[1] + 6)
    belly_pts = quad_bezier(p_side, ctrl_belly, p_belly, n=50)
    belly_widths = [6 - (i / 50) * 1 for i in range(51)]

    # Segment D: up-flick from belly → tip (rising to upper-right)
    ctrl_hook = ((p_belly[0] + p_tip[0]) / 2.0 + 8,
                 (p_belly[1] + p_tip[1]) / 2.0 + 10)
    hook_pts = quad_bezier(p_belly, ctrl_hook, p_tip, n=36)
    hook_widths = [5 - (i / 36) * 4 for i in range(37)]

    pts = top_pts + corner_pts[1:] + belly_pts[1:] + hook_pts[1:]
    widths = top_widths + corner_widths[1:] + belly_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_jiu(d)
    out = Path(__file__).parent / '01_九.png'
    img.save(out)
    print(f'wrote {out}')
