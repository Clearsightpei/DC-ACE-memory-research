"""广 (guǎng, "shelter", 3 strokes: 点 + 横 + 撇) — B1 pass.

Strokes:
  s1 — 点 (SE-diagonal dot on top).
  s2 — 横 (long horizontal beam at ~y=125 across most of canvas).
  s3 — 撇 (long left-sweeping stroke down to bottom-left).

Joint: s2.head ⇆ s3.head → N (small ~14-18 px gap; NOT welded).
"""
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie


def draw_guang(draw,
               s1_head=('TC', 0.307, 0.642), s1_tail=('TC', 0.731, 0.888),
               s2_head=('ML', 0.932, 0.283), s2_tail=('MR', 0.341, 0.184),
               s3_head=('ML', 0.753, 0.254), s3_tail=('BL', 0.331, 0.98)):
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=9, curve=0.06, segments=24)
    draw_heng(draw, s2_head, s2_tail, width=9)
    draw_pie(draw, s3_head, s3_tail,
             head_width=11, tail_width=1, curve=0.09, segments=48)
