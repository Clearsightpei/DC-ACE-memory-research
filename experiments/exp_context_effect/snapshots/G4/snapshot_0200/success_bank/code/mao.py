"""毛 (máo, "hair", 4 strokes) — B2 pass.

Strokes:
  s1 — 撇 (top slanting down-right → left).
  s2 — 横 (short upper bar).
  s3 — 横 (main middle bar).
  s4 — 竖弯钩 (long spine with rightward curve and up-hook).

Joints:
  s1.mid(0.75) ⇆ s4.head @ C — N (~11 px).
  s2.mid(0.49) ⇆ s4.head @ C — T.
  s3.mid(0.53) ⇆ s4.mid(0.29) @ BC — P.
"""
from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


def draw_mao(draw,
             s1_head=('TC', 0.80, 0.74), s1_tail=('ML', 0.77, 0.18),
             s2_head=('ML', 0.72, 0.63), s2_tail=('C', 0.88, 0.40),
             s3_head=('BL', 0.27, 0.26), s3_tail=('MR', 0.19, 0.90),
             s4_head=('C', 0.10, 0.10),
             s4_belly=('C', 0.10, 0.60),
             s4_corner=('BC', 0.10, 0.65),
             s4_hook_pt=('BR', 0.60, 0.55),
             s4_tip=('BR', 0.65, 0.10)):
    draw_pie(draw, s1_head, s1_tail, head_width=10, tail_width=1, curve=0.10)
    draw_heng(draw, s2_head, s2_tail, width=8)
    draw_heng(draw, s3_head, s3_tail, width=9)
    draw_shu_wan_gou(draw, s4_head, s4_belly, s4_corner, s4_hook_pt, s4_tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)
