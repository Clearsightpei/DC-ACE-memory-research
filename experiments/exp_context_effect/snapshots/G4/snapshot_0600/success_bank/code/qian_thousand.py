"""千 (qiān, "thousand", 3画) — B4 main promotion.

Strokes:
  s1 — 短撇 (short flat pie sweeping down-left across the top).
  s2 — 长横 (long middle bar, roughly wall-to-wall, slight rise).
  s3 — 长竖 (vertical spine; pierces s2 at C, extends slightly below BC).

Joints:
  s1.mid ⇆ s3.head @ TC — N (~16 px gap; do NOT weld).
  s2.mid ⇆ s3.mid  @ C  — P (welded crossing by construction).
"""
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


def draw_qian_thousand(draw,
                       s1_head=('TR', 0.021, 0.724),
                       s1_tail=('ML', 0.835, 0.081),
                       s2_head=('ML', 0.381, 0.72),
                       s2_tail=('MR', 0.675, 0.649),
                       s3_head=('TC', 0.383, 0.987),
                       s3_tail=('BC', 0.497, 1.07)):
    draw_pie(draw, from_anchor=s1_head, to_anchor=s1_tail,
             head_width=11, tail_width=2, curve=0.06, segments=48)
    draw_heng(draw, from_anchor=s2_head, to_anchor=s2_tail, width=10)
    draw_shu(draw, from_anchor=s3_head, to_anchor=s3_tail, width=10)
