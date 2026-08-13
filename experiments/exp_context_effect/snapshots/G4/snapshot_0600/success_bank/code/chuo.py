"""屮 (chè, "sprout", 3 strokes) — B1 pass.

Strokes:
  s1 — 竖折 (J-shape via draw_shu_wan): straight-down body then bend
       right to a horizontal that passes through C center.
  s2 — 短竖 (short right vertical near the right edge).
  s3 — 竖 (tall central vertical rising through the horizontal).

Joints:
  s3 pierces s1's horizontal at ~C center → P (weld by construction).
  s1.tail ⇆ s2.mid(0.85) → N (~17 px gap on the right).
"""
from shu_wan import draw_shu_wan
from shu import draw_shu


def draw_chuo(draw,
              s1_head=('ML', 0.68, 0.312),
              s1_belly=('ML', 0.68, 0.95),
              s1_corner=('BC', 0.05, 0.00),
              s1_tail=('MR', 0.165, 0.969),
              s2_head=('MR', 0.139, 0.181),
              s2_tail=('BR', 0.282, 0.218),
              s3_head=('TC', 0.339, 0.662),
              s3_tail=('BC', 0.497, 1.05)):
    draw_shu_wan(draw, head=s1_head, belly=s1_belly,
                 corner=s1_corner, tail=s1_tail,
                 head_w=8, belly_w=10, corner_w=10, tail_w=9)
    draw_shu(draw, s3_head, s3_tail, width=10)
    draw_shu(draw, s2_head, s2_tail, width=8)
