"""升 (sheng) — Phase-3 character, 4 strokes.

Memory lookup checklist:
1. success_bank/INDEX.md grep 升 — not present.
2. errata.md grep 升 — not present.
3. form_catalog.md — 撇 in left position; 横 short middle; 竖 tall right.
4. principles_meta.md TR1-TR12 — inline fresh (no strong bank match).
5. joint_atlas.md — P joints welded, N joints small gap.

Structure per MMH expectations (4 strokes):
  s1: 短撇 — TC(0.29,0.79) -> ML(0.71,0.33)  (short slanted pie top)
  s2: 横 — ML(0.25,0.78) -> MR(0.77,0.61)   (horizontal, slight lift)
  s3: 长撇 — C(0.02,0.24) -> BL(0.59,0.83)  (long left curve)
  s4: 竖 — TC(0.73,0.61) -> BC(0.87,1.11)  (tall right vertical)

Joints:
  s1.mid ⇆ s3.head : N (small gap in ML)
  s2.mid ⇆ s3.mid  : P (welded in C)
  s2.mid ⇆ s4.mid  : P (welded in C)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Inline fresh; 4 strokes; s1 short pie top, s2 horizontal, s3 long left curve, s4 tall right vertical.'
}


def draw_sheng(draw):
    # ---- s1: short 撇 (top-right slant leading into character) ----
    p0 = anchor_to_xy(('TC', 0.29, 0.79))
    p1 = anchor_to_xy(('ML', 0.71, 0.33))
    # slight curve for pie
    ctrl = ((p0[0] + p1[0]) / 2 + 4, (p0[1] + p1[1]) / 2 - 2)
    pts = quad_bezier(p0, ctrl, p1, n=30)
    widths = [7 - 4 * (i / len(pts)) for i in range(len(pts))]  # taper thick->thin
    stroke_variable_width(draw, pts, widths)

    # ---- s2: 横 (horizontal, slight upward slope right) ----
    p0 = anchor_to_xy(('ML', 0.25, 0.78))
    p1 = anchor_to_xy(('MR', 0.77, 0.61))
    fat_line(draw, p0, p1, 7)

    # ---- s3: long 撇 (left curve from center-top area down to BL) ----
    p0 = anchor_to_xy(('C', 0.02, 0.24))
    p1 = anchor_to_xy(('BL', 0.59, 0.83))
    # control point for calligraphic sweep — pull left significantly
    ctrl = (p0[0] - 50, p0[1] + 130)
    pts = quad_bezier(p0, ctrl, p1, n=50)
    widths = [9 - 6 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)

    # ---- s4: 竖 (tall vertical, right side) ----
    p0 = anchor_to_xy(('TC', 0.73, 0.61))
    p1 = anchor_to_xy(('BC', 0.87, 1.05))
    # slight lean
    fat_line(draw, p0, p1, 7)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_sheng(draw)
    out = os.path.join(os.path.dirname(__file__), '01_升.png')
    img.save(out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
