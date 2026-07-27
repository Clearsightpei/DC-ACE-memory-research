"""尢 (yóu, "lame variant", 3 strokes) — B2 pass.

Similar to 兀 but with a curved right leg (竖弯钩) instead of straight
竖弯. The knee is softer, belly deeper.

Strokes:
  s1 — 横 (short top bar).
  s2 — 撇 (left leg).
  s3 — 竖弯钩 (right leg with up-flick hook).

Joints:
  s1.mid ⇆ s2.mid @ C  — P (natural ink overlap).
  s2.mid ⇆ s3.head @ C — N (~29 px).
"""
from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def draw_you(draw,
             s1_head=('ML', 0.571, 0.482), s1_tail=('MR', 0.273, 0.295),
             s2_head=('TC', 0.225, 0.691), s2_tail=('BL', 0.275, 0.915),
             s3_head=('C', 0.465, 0.652),
             s3_belly=('C', 0.50, 0.98),
             s3_corner=('BC', 0.62, 0.70),
             s3_hook_pt=('BR', 0.55, 0.60),
             s3_tip=('BR', 0.657, 0.259)):
    draw_heng(draw, s1_head, s1_tail, width=7)
    draw_pie(draw, s2_head, s2_tail, head_width=10, tail_width=2, curve=0.09)
    draw_shu_wan_gou(draw, s3_head, s3_belly, s3_corner, s3_hook_pt, s3_tip,
                     head_w=9, belly_w=11, corner_w=10,
                     hook_start_w=9, tip_w=2)
