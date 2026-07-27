"""土 (tǔ, "earth/soil", 3 strokes) — B2 pass.

土 is a 十 with a bottom-longer horizontal (士 has top-longer; that's the
distinguishing feature).

Strokes:
  s1 — 横 (top, short).
  s2 — 竖 (spine).
  s3 — 横 (bottom, long).

Joints:
  s1 × s2 @ C          — P (welded cross).
  s2.tail ⇆ s3.mid @ BC — N (~18 px).
"""
from heng import draw_heng
from shu import draw_shu


def draw_tu(draw,
            s1_head=('ML', 0.829, 0.717), s1_tail=('MR', 0.171, 0.579),
            s2_head=('TC', 0.351, 0.773), s2_tail=('BC', 0.395, 0.552),
            s3_head=('BL', 0.378, 0.71),  s3_tail=('BR', 0.701, 0.622)):
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_shu(draw, s2_head, s2_tail, width=10)
    draw_heng(draw, s3_head, s3_tail, width=10)
