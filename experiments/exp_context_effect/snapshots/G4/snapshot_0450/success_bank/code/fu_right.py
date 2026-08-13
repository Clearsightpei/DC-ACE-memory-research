"""阝 (fù-right, right-ear radical, 2 strokes) — B1 pass.

Strokes:
  s1 — 横撇弯钩 (heng-pie-wan-gou compound). Right-hanging ear shape.
  s2 — 竖 (straight vertical descending on the right).

Joints:
  s1.tail-region touches s2 near lower body — S/N (visually stacked; MMH
  spec treats this as a T-touch near the ear base).
"""
from heng_pie_wan_gou import draw_heng_pie_wan_gou
from shu import draw_shu


def draw_fu_right(draw,
                  s1_head_h=('TC', 0.55, 0.75),
                  s1_corner=('TC', 0.90, 0.75),
                  s1_knee=('C', 0.75, 0.28),
                  s1_belly=('C', 1.00, 0.55),
                  s1_hook=('C', 0.65, 0.90),
                  s1_tip=('C', 0.30, 0.72),
                  s2_head=('TC', 0.40, 0.80),
                  s2_tail=('BC', 0.45, 0.95)):
    draw_heng_pie_wan_gou(draw,
                          s1_head_h, s1_corner, s1_knee, s1_belly,
                          s1_hook, s1_tip,
                          h_width=8, corner_shoulder=12,
                          pie_head_w=11, pie_knee_w=8, knee_shoulder=11,
                          wan_head_w=8, wan_belly_w=12,
                          hook_start_w=10, tip_w=2)
    draw_shu(draw, s2_head, s2_tail, width=11)
