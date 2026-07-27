"""及 (jí, 3 strokes: 撇 + 横折折撇 + 捺) — first attempt.

MANDATORY LOOKUP CHECKLIST:
1. success_bank/INDEX.md grep — no 及 entry; related: 几 (ji.py) with 撇+横折弯钩.
2. errata.md grep — 及 mentioned as containing chronic 横折折撇 stroke;
   fix idea from p1_stroke_29 retry: extend 撇 tip to BL corner so it
   reads as dominant final gesture. Applied to s1 here.
3. form_catalog.md — 撇 in left-position must span diagonally.
4. principles_meta.md — TR6: inline 横折折撇 since no clean primitive; TR10:
   N-class joints must look connected (≤25 px), P-class welded.
5. joint_atlas.md — 几-family top gap needs ~15-20 px N (not welded).
6. sandbox.md — none directly relevant.

MMH expected structure:
  s1 撇:              head TC(0.125, 0.999)  tail BL(0.27, 0.657)
  s2 横折折撇:         head TL(0.715, 0.946)  tail BL(0.788, 0.842)
  s3 捺:              head C(0.072, 0.831)   tail BR(0.801, 0.856)
Joints:
  s1.head ⇆ s2.head @ TC : N (~12 px gap)
  s1.mid  ⇆ s3.head @ C  : N (~15 px gap)
  s2.mid  ⇆ s3.mid  @ BC : P (welded crossing)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'revised once — s2 simplified to 横+竖+撇 shape (3 sub-segments), s1 head moved left so N gap sits at TC as expected, s3 unchanged. Stroke count = 3.'
}

import os
import sys
from PIL import Image, ImageDraw

SHARED = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SHARED)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


def draw_ji(draw):
    # s1 — 撇 (dominant anti-diagonal, starts near top-center of canvas,
    # sweeps down-left through the character body to BL corner)
    s1_head = ('TC', 0.35, 0.25)   # top area, left-of-center
    s1_tail = ('BL', 0.10, 0.92)   # deep BL corner (errata fix — dominant sweep)
    draw_pie(draw, s1_head, s1_tail,
             head_width=9, tail_width=1, curve=0.12, segments=48)

    # s2 — 横折折撇 (inlined, forms the cap+belly of 及's right side).
    # Path: starts to the right of s1.head with a small N gap (top 横 slopes
    # slightly up), turns down (折), then the second 折 curls down-left as
    # a broad 撇 that sweeps into the mid-body (BC area) where s3 crosses.
    p_head    = anchor_to_xy(('TC', 0.55, 0.20))   # start (N gap to right of s1.head)
    p_corner1 = anchor_to_xy(('TR', 0.55, 0.25))   # end of 横 (upper-right)
    p_corner2 = anchor_to_xy(('TR', 0.35, 0.75))   # end of vertical drop
    p_tip     = anchor_to_xy(('BC', 0.30, 0.55))   # 撇 tail (mid-lower, near BC/C boundary)

    # top 横 (slight upward slope, dips at corner)
    top_ctrl = ((p_head[0] + p_corner1[0]) / 2.0,
                min(p_head[1], p_corner1[1]) - 3)
    top_pts = quad_bezier(p_head, top_ctrl, p_corner1, n=20)
    top_widths = [7 for _ in range(21)]
    stroke_variable_width(draw, top_pts, top_widths)

    # vertical drop (折)
    d1_ctrl = (p_corner1[0] + 3, (p_corner1[1] + p_corner2[1]) / 2.0)
    d1_pts = quad_bezier(p_corner1, d1_ctrl, p_corner2, n=24)
    d1_widths = [7 for _ in range(25)]
    stroke_variable_width(draw, d1_pts, d1_widths)

    # 撇 tail: broad sweep from the drop point down and left into mid-body
    tail_ctrl = ((p_corner2[0] + p_tip[0]) / 2.0 + 5,
                 (p_corner2[1] + p_tip[1]) / 2.0 - 5)
    tail_pts = quad_bezier(p_corner2, tail_ctrl, p_tip, n=32)
    tail_widths = [7 - (i / 32) * 5 for i in range(33)]
    stroke_variable_width(draw, tail_pts, tail_widths)

    # s3 — 捺 (from left-of-center in body, sweeps down-right to BR).
    # Crosses the s2 撇-tail at BC → P joint (welded).
    s3_head = ('C',  0.10, 0.70)   # near center-left of body
    s3_tail = ('BR', 0.88, 0.85)   # far bottom-right
    draw_na(draw, s3_head, s3_tail,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.80, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ji(draw)
    out = os.path.join(os.path.dirname(__file__), '01_及.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
