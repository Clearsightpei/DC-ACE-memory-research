"""气 (qì) — Phase-2 radical, 4画 — RETRY #2.

Reading order followed:
1. drawer_memory.md — no chronic import maps to 气; compound stroke s4 must
   be ONE polyline (not chained beziers). Distinct-row rule applies.
2. success_bank/INDEX.md — 气 not mastered; related 乙 shape informs the
   final hook. No safe direct import.
3. errata.md p2_radical_111_气 retry_2 LITERAL fix:
     - distinct y-bands: s2 y=0.35, s3 y=0.55, s4 top-heng y=0.15
     - compound spine as ONE `stroke_variable_width` polyline

Decomposition (4 strokes per MMH):
  s1: 撇 — top-left, curls from top down-and-left
  s2: 短横 — upper row y_frac≈0.35
  s3: 短横 — middle row y_frac≈0.55 (longer than s2)
  s4: 横折弯钩 — top-horizontal (y≈0.15) → right corner → descent →
      bottom sweep → up-hook. Rendered as ONE variable-width polyline.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes: pie, heng, heng, compound polyline
    'endpoint_mismatches': [
        {'stroke': 2, 'note': 's2 moved to y=0.35 per literal errata fix'},
        {'stroke': 3, 'note': 's3 moved to y=0.55 per literal errata fix'},
        {'stroke': 4, 'note': 's4 top-heng at y=0.15 per literal errata fix; '
                              'ONE polyline (not chained beziers)'},
    ],
    'joint_class_mismatches': [],  # J1, J2 both N with visible gap
    'overall_pass': True,
    'notes': 'Retry #2. Errata fix applied verbatim.',
}

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402


def draw_qi(draw):
    # ---- s1: 撇 — top-left curl, sweeps down-and-left ----
    # Revision: increase curve (0.10 → 0.30) so it reads as a proper 撇
    # not a straight left wall; drop head slightly so s4 top-heng clears it.
    s1_head = ('TC', 0.40, 0.45)
    s1_tail = ('ML', 0.15, 0.75)
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=2, curve=0.30, segments=40)

    # ---- s2: 短横 — upper row y_frac=0.35 (literal fix) ----
    s2_head = ('TC', 0.85, 0.35)
    s2_tail = ('TC', 0.35, 0.35)
    draw_heng(draw, s2_head, s2_tail, width=8)

    # ---- s3: 短横 — middle row y_frac=0.55 (literal fix); longer than s2 ----
    s3_head = ('MR', 0.10, 0.55)
    s3_tail = ('ML', 0.40, 0.55)
    draw_heng(draw, s3_head, s3_tail, width=9)

    # ---- s4: 横折弯钩 — ONE stroke_variable_width polyline (literal fix) ----
    # Top-heng at y_frac=0.15 (literal), spanning TC left → TR right,
    # then descend to bottom-right, sweep left, up-hook.
    p_head   = anchor_to_xy(('TC', 0.45, 0.15))   # top-heng start (clears 撇 head)
    p_corner = anchor_to_xy(('TR', 0.80, 0.20))   # top-heng end / bend
    p_bottom = anchor_to_xy(('BR', 0.55, 0.75))   # descent belly bottom
    p_hook_s = anchor_to_xy(('BR', 0.30, 0.85))   # base of up-hook (sweep left)
    p_tip    = anchor_to_xy(('BR', 0.20, 0.55))   # up-flick tip

    # TR8 sanity asserts on direction
    assert p_corner[0] > p_head[0], 's4 top-heng should go rightward'
    assert p_bottom[1] > p_corner[1], 's4 descent should go downward'
    assert p_hook_s[0] < p_bottom[0], 's4 bottom sweep should curl leftward'
    assert p_tip[1] < p_hook_s[1], 's4 hook should tick upward'

    # Build ONE polyline by sampling the four continuous segments and
    # feeding them all to stroke_variable_width. quad_bezier is used only
    # as sampler; the RENDER call is a single stroke_variable_width.
    ctrl_top   = ((p_head[0] + p_corner[0]) / 2.0,
                  min(p_head[1], p_corner[1]) - 3)
    top_pts    = quad_bezier(p_head, ctrl_top, p_corner, n=28)

    ctrl_desc  = (p_corner[0] + 8, (p_corner[1] + p_bottom[1]) / 2.0)
    desc_pts   = quad_bezier(p_corner, ctrl_desc, p_bottom, n=40)

    ctrl_sweep = ((p_bottom[0] + p_hook_s[0]) / 2.0,
                  max(p_bottom[1], p_hook_s[1]) + 6)
    sweep_pts  = quad_bezier(p_bottom, ctrl_sweep, p_hook_s, n=28)

    ctrl_hook  = (p_hook_s[0] - 2, (p_hook_s[1] + p_tip[1]) / 2.0)
    hook_pts   = quad_bezier(p_hook_s, ctrl_hook, p_tip, n=20)

    # Concatenate into ONE polyline (drop duplicate joint points)
    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]

    # Widths: horizontal thin→medium, descent medium→thick, sweep thick,
    # hook thick→needle-thin.
    top_w   = [5 + (i / 28) * 3 for i in range(29)]
    desc_w  = [8 + (i / 40) * 4 for i in range(41)]
    sweep_w = [12 - (i / 28) * 2 for i in range(29)]
    hook_w  = [10 - (i / 20) * 8 for i in range(21)]
    widths  = top_w + desc_w[1:] + sweep_w[1:] + hook_w[1:]

    assert len(pts) == len(widths)
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_qi(draw)
    out = os.path.join(_HERE, '01_气.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
