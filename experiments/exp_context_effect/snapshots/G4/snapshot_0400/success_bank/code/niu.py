"""牛 (niú, "ox", 4 strokes) — B2 pass.

Strokes:
  s1 — 撇 (short top-left).
  s2 — 横 (short upper).
  s3 — 横 (long middle bar).
  s4 — 竖 (spine, extends slightly past bottom edge for prominence).

Joints:
  s1.mid ⇆ s2.head @ ML — N (~15–20 px).
  s2 × s4 @ C           — P (x=150).
  s3 × s4 @ C           — P (x=150).
"""
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


def draw_niu(draw,
             s1_head=('TL', 0.92, 0.97), s1_tail=('ML', 0.61, 0.69),
             s2_head=('ML', 0.999, 0.37), s2_tail=('MR', 0.15, 0.21),
             s3_head=('BL', 0.30, 0.15),  s3_tail=('MR', 0.70, 0.90),
             s4_head=('TC', 0.50, 0.35),  s4_tail=('BC', 0.50, 1.05)):
    draw_pie(draw, s1_head, s1_tail, head_width=11, tail_width=1, curve=0.10)
    draw_heng(draw, s2_head, s2_tail, width=9)
    draw_heng(draw, s3_head, s3_tail, width=11)
    draw_shu(draw, s4_head, s4_tail, width=11)
