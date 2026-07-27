"""兀 (wù, "lame", 3 strokes) — B2 pass.

Strokes:
  s1 — 横 (top bar).
  s2 — 撇 (left leg, sweeps down-left).
  s3 — 竖弯 (right leg, straight down then rightward curve).

Joints:
  s1.head ⇆ s2.head @ ML  — N (~40 px).
  s1.mid ⇆ s3.head @ C   — N (~15 px).
"""
from heng import draw_heng
from pie import draw_pie
from shu_wan import draw_shu_wan


def draw_wu_lame(draw,
                 s1_head=('ML', 0.65, 0.08), s1_tail=('TR', 0.32, 0.96),
                 s2_head=('ML', 0.99, 0.29), s2_tail=('BL', 0.35, 0.78),
                 s3_head=('C', 0.50, 0.10),
                 s3_belly=('C', 0.50, 0.60),
                 s3_corner=('BC', 0.55, 0.85),
                 s3_tail=('BR', 0.40, 0.85)):
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_pie(draw, s2_head, s2_tail, head_width=11, tail_width=2, curve=0.08)
    draw_shu_wan(draw, s3_head, s3_belly, s3_corner, s3_tail,
                 head_w=8, belly_w=10, corner_w=10, tail_w=8)
