"""巾 (jīn, "cloth", 3 strokes) — B1 pass.

Strokes:
  s1 — short left 竖 (near-vertical drop with slight rightward drift).
  s2 — 横折 (top-right bracket: horizontal + descending vertical).
  s3 — long center 竖 (piercing through the horizontal down to bottom).

Joints:
  s1.head ⇆ s2.head → N (~10-15 px gap on the left).
  s2 horizontal × s3 vertical → P (weld at C cell by construction).
"""
from shu import draw_shu
from heng_zhe import draw_heng_zhe


def draw_jin(draw,
             s1_head=('ML', 0.724, 0.356), s1_tail=('BL', 0.788, 0.353),
             s2_head=('ML', 0.899, 0.389),
             s2_corner=('C', 0.805, 0.389),
             s2_tail=('BC', 0.805, 0.095),
             s3_head=('TC', 0.336, 0.647),
             s3_tail=('BC', 0.474, 1.0)):
    draw_shu(draw, from_anchor=s1_head, to_anchor=s1_tail, width=9)
    draw_heng_zhe(draw, head=s2_head, corner=s2_corner, tail=s2_tail,
                  h_width=9, v_width=9, shoulder=11)
    draw_shu(draw, from_anchor=s3_head, to_anchor=s3_tail, width=10)
