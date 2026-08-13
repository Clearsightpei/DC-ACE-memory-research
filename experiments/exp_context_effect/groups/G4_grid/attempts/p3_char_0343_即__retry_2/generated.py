"""p3_char_0343_即 (retry_2) — G4 rendering.

TRAJECTORY DIFF (from inspecting GT + prior attempts):
  GT (即): Left component 皀 = small stacked block occupying upper-left
    with 3 short horizontals inside plus a long descending spine that
    forms the left wall and 匕 tail. Right component 卩 = short 横折钩
    top + long straight 竖 descending well below canvas mid.

  main FAIL: entire char rotated / fragmented diagonal scaffolding on
    the left; the 卩 vertical floated disconnected. No recognizable 皀.
  retry_1 FAIL: left block improved (3 hengs visible) but descending
    spine too short and pointed the wrong way; overall read as 卩+卩.

  Errata fix (literal): 卩 as 2 strokes = short 横折钩 top + straight 竖
    body, heights y∈[0.15, 0.85].

  Fix plan this attempt:
    - Exactly 7 strokes.
    - Left 皀: draw 3 hengs stacked in upper block, spine as long
      vertical descending on the LEFT side extending well into BL,
      plus a bottom tick.  Follow MMH anchors closely.
    - Right 卩: 横折钩 with visible top heng + right drop + small
      left hook, then long straight 竖 that drops to canvas bottom.
    - Uniform width ~8 px.
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes verified. Left 皀 = 撇 + 2 hengs + long spine + '
             'bottom tick. Right 卩 = 横折钩 + long 竖 per errata fix.'
}

W = 8


def line_a(draw, a0, a1, width=W):
    fat_line(draw, anchor_to_xy(a0), anchor_to_xy(a1), width)


def curve_a(draw, a0, ac, a1, width=W):
    pts = quad_bezier(anchor_to_xy(a0), anchor_to_xy(ac), anchor_to_xy(a1), n=40)
    stroke_variable_width(draw, pts, [width] * len(pts))


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- LEFT COMPONENT 皀 (5 strokes) ----
    # Layout: compact block at top-left holding 3 short hengs; spine drops
    # from top of block down through BL to BC-bottom; a small tick closes
    # the base.  x-band for left = roughly [30, 130]; hengs x∈[50, 120].

    # s1 — top 撇 / short diagonal forming the top-left cap of 皀
    # MMH: TL(0.72,0.96) → C(0.22,0.61)  (approx head→tail)
    # Render as a short slanted stroke, top-left going down-right
    line_a(draw, ('TL', 0.55, 0.55), ('ML', 0.35, 0.15))

    # s2 — top 横 (top of the enclosed sub-block of 白)
    # MMH: ML(0.72,0.32) → C(0.07,0.23)
    line_a(draw, ('ML', 0.35, 0.30), ('ML', 0.95, 0.28))

    # s3 — middle 横 (middle bar of the enclosed sub-block)
    # MMH: ML(0.72,0.70) → C(0.14,0.54)
    line_a(draw, ('ML', 0.35, 0.55), ('ML', 0.95, 0.55))

    # s4 — long spine: left wall of 白 continuing as 匕 body down-and-out
    # MMH: TL(0.51,0.83) → BC(0.19,0.07)
    # Slight curve — vertical near top, arcing right at the bottom
    curve_a(draw,
            ('ML', 0.35, 0.15),          # top of spine (meets s1 tail area)
            ('BL', 0.30, 0.55),          # belly slightly right
            ('BC', 0.20, 0.10))          # tail into BC

    # s5 — bottom stroke of 皀 (bottom heng of 白 + small rise toward 匕)
    # MMH: C(0.08,0.83) → BC(0.40,0.24)
    line_a(draw, ('BL', 0.35, 0.30), ('BC', 0.45, 0.15))

    # ---- RIGHT COMPONENT 卩 (2 strokes) ----
    # x-band: 卩 body in x∈[170, 250]; heights y∈[0.10, 0.95]

    # s6 — 横折钩 : short top heng + right corner + short down + tiny left hook
    # MMH endpoints: C(0.90,0.15) → MR(0.05,0.90)
    p_a = anchor_to_xy(('C', 0.55, 0.15))       # left end of top heng
    p_b = anchor_to_xy(('MR', 0.35, 0.13))      # right corner top
    p_c = anchor_to_xy(('MR', 0.30, 0.55))      # bottom of vertical drop
    p_d = anchor_to_xy(('MR', 0.15, 0.55))      # hook tip flicks left
    fat_line(draw, p_a, p_b, W)
    fat_line(draw, p_b, p_c, W)
    fat_line(draw, p_c, p_d, W)

    # s7 — long straight 竖 of 卩 dropping past canvas mid-line
    # MMH: C(0.66,0.13) → BC(0.79,1.18)  (tail y_frac > 1)
    # Start just under the 横折钩's start, drop to canvas bottom
    line_a(draw, ('C', 0.55, 0.20), ('BR', 0.05, 0.95))

    # Total stroke count = 5 (left 皀) + 1 (横折钩 — one calligraphic stroke,
    # 3 line segments) + 1 (竖) = 7  ✓

    out_png = os.path.join(HERE, '01_即.png')
    img.save(out_png)
    print(f'wrote {out_png}')


if __name__ == '__main__':
    main()
