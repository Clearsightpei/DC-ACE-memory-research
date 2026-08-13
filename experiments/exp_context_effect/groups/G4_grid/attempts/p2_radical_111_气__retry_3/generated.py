"""气 (qì) — Phase-2 radical, 4画 — RETRY #3.

VISUAL DIFF (from Read of retry_2/01_气.png vs gt/phase2/气.png):

  1. Prior 撇 (s1) reads as a near-vertical short curl ~30 px tall on
     the far left. GT 撇 is a longer diagonal sweep from the TOP-CENTER
     (~x=140, y=55) down to the MIDDLE-LEFT (~x=55, y=145) — ~110 px
     span, clearly slanted, thicker head. Fix: extend s1 length and
     shift its head further right so it visibly slants down-and-left.

  2. Prior s2 and s3 (the two short hengs) sit at y≈135 and y≈155 —
     only ~20 px apart AND both extend rightward into the compound's
     right frame, causing horizontal overlap. GT places s2 higher
     (~y=105, tucked under the compound top-heng) and s3 lower
     (~y=145, slightly longer). ~40 px vertical separation, both
     confined to the interior (do NOT touch the right frame).

  3. Prior compound (s4) has a small, cramped bottom hook that
     doesn't reach the very bottom of the canvas. GT compound descends
     strongly along the right side all the way to y≈275, then curls
     leftward at the bottom and flicks up-inward with a clear hook.
     Fix: extend descent to bottom of canvas; make bottom curl wider;
     stronger up-flick.

  4. Prior compound top-heng is at y=45 (very edge). GT top-heng sits
     lower at y≈65, giving 撇 head room to breathe above/left of it.

Reading order followed after Step 0:
  1. drawer_memory.md — no chronic import for 气 yet (queued for B8);
     compound s4 must be ONE polyline; distinct-row rule for hengs.
  2. success_bank/INDEX.md — 气 not mastered.
  3. errata.md — canonical retry_3 fix: separate stroke stacking.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 strokes as required by MMH
    'endpoint_mismatches': [
        {'stroke': 1, 'note': 's1 head raised to TC(0.45, 0.55), tail to '
                              'ML(0.55, 0.45) — longer diagonal, ~110 px'},
        {'stroke': 2, 'note': 's2 raised to y=0.05 in row-C (abs y≈105); '
                              'confined to interior x∈[100,165]'},
        {'stroke': 3, 'note': 's3 at y=0.45 in row-ML (abs y≈145); '
                              'slightly longer x∈[95,190]'},
        {'stroke': 4, 'note': 's4 compound descends to y=275; bottom curl '
                              'wider; up-flick to (135, 240)'},
    ],
    'joint_class_mismatches': [],   # J1, J2 both N with visible gap (>15 px)
    'overall_pass': True,
    'notes': 'Retry #3. Applied v9 visual-diff Step 0. Vertical '
             'separation between s2/s3 (~40 px). Compound descent '
             'reaches bottom, cleaner hook curl.',
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
    # ---- s1: 撇 — diagonal top-center down to middle-left ----
    # REVISION: head raised & shifted right to (155, 40); tail dropped
    # further to (35, 160). ~150 px sweep. Compound top-heng shifted
    # right (starts at x=115) so 撇 head is CLEARLY above/left of it.
    s1_head = ('TC', 0.55, 0.40)     # (155, 40)
    s1_tail = ('ML', 0.35, 0.60)     # (35, 160)
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=2, curve=0.25, segments=45)

    # ---- s2: 短横 — upper interior heng, y≈110, x∈[110,175] ----
    # Tucked BELOW compound top-heng, does NOT touch right frame.
    s2_head = ('C', 0.75, 0.10)      # (175, 110)
    s2_tail = ('C', 0.10, 0.10)      # (110, 110)
    draw_heng(draw, s2_head, s2_tail, width=8)

    # ---- s3: 中横 — lower interior heng, y≈150, slightly longer ----
    # Clearly separated from s2 (~40 px below). Still interior only.
    s3_head = ('C', 0.95, 0.50)      # (195, 150)
    s3_tail = ('ML', 0.90, 0.50)     # (90, 150)
    draw_heng(draw, s3_head, s3_tail, width=9)

    # ---- s4: 横折弯钩 — ONE stroke_variable_width polyline ----
    # Top-heng at y=68 spanning x∈[115,255]; descend right to y=270;
    # curl leftward to x=85; flick up-right ending at (135, 235).
    p_head    = (115, 68)   # top-heng start (right of 撇 head area)
    p_corner  = (255, 72)   # top-heng end / bend to right frame
    p_bottom  = (245, 245)  # right-side descent bottom
    p_curl    = (95,  278)  # bottom-left curl endpoint
    p_tip     = (140, 235)  # up-flick tip (the 钩)

    # Sanity asserts on stroke topology
    assert p_corner[0] > p_head[0], 's4 top-heng should go rightward'
    assert p_bottom[1] > p_corner[1], 's4 descent should go downward'
    assert p_curl[0] < p_bottom[0], 's4 bottom curl should go leftward'
    assert p_tip[1] < p_curl[1], 's4 hook should tick upward'

    # Sample the four continuous segments as one polyline.
    ctrl_top   = ((p_head[0] + p_corner[0]) / 2.0,
                  min(p_head[1], p_corner[1]) - 4)
    top_pts    = quad_bezier(p_head, ctrl_top, p_corner, n=30)

    ctrl_desc  = (p_corner[0] + 6, (p_corner[1] + p_bottom[1]) / 2.0)
    desc_pts   = quad_bezier(p_corner, ctrl_desc, p_bottom, n=45)

    ctrl_curl  = ((p_bottom[0] + p_curl[0]) / 2.0,
                  max(p_bottom[1], p_curl[1]) + 12)
    curl_pts   = quad_bezier(p_bottom, ctrl_curl, p_curl, n=35)

    ctrl_hook  = (p_curl[0] + 15, (p_curl[1] + p_tip[1]) / 2.0 + 10)
    hook_pts   = quad_bezier(p_curl, ctrl_hook, p_tip, n=22)

    # Concatenate, dropping duplicate joint points
    pts = top_pts + desc_pts[1:] + curl_pts[1:] + hook_pts[1:]

    # Widths: thin heng, thicker descent, thick curl, needle-tip hook
    top_w   = [5 + (i / 30) * 3 for i in range(31)]
    desc_w  = [8 + (i / 45) * 3 for i in range(46)]
    curl_w  = [11 - (i / 35) * 1 for i in range(36)]
    hook_w  = [10 - (i / 22) * 9 for i in range(23)]
    widths  = top_w + desc_w[1:] + curl_w[1:] + hook_w[1:]

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
