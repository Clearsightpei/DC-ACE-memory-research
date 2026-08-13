"""大 (dà, "big", 3 strokes: 横 + 撇 + 捺) — B1 pass.

Strokes:
  s1 — 横 spanning ML→MR.
  s2 — 撇 from upper-mid-TC down-left to BL (concave-right, curve<0).
  s3 — 捺 from just below the heng (C) down-right to BR.

Joints: P at s1×s2 crossing; N at s3.head vs s1 (~19 px); N at s3 vs
s2 (well separated, ~60 px).
"""
from heng import draw_heng
from pie import draw_pie
from na import draw_na


def draw_da(draw,
            heng_head=('ML', 0.615, 0.658), heng_tail=('MR', 0.373, 0.485),
            pie_head=('TC', 0.219, 0.627), pie_tail=('BL', 0.404, 0.88),
            na_head=('C', 0.424, 0.74), na_tail=('BR', 0.792, 0.877)):
    draw_heng(draw, heng_head, heng_tail, width=8)
    draw_pie(draw, pie_head, pie_tail,
             head_width=10, tail_width=1, curve=-0.12, segments=48)
    draw_na(draw, na_head, na_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)
