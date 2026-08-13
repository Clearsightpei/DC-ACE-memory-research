"""孑 (jié, "orphan", 3画) — B4 main promotion.

Strokes:
  s1 — 横撇 (top curl: horizontal + short pie tip landing at C).
  s2 — 弯钩 (descending curved body with left-flick hook near BC).
  s3 — 提 (rising diagonal that pierces s2 body at C).

Joints:
  s1.tail ⇆ s2.head @ C  — N (~16 px gap; do NOT weld).
  s2.mid  ⇆ s3.mid  @ C  — P (welded crossing; 提 pierces 弯钩 body).
"""
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from ti import draw_ti


def draw_jie_orphan(draw,
                    s1_head=('TL', 0.79, 0.91),
                    s1_corner=('TC', 0.75, 0.90),
                    s1_tip=('C', 0.56, 0.39),
                    s2_head=('C', 0.34, 0.32),
                    s2_belly=('C', 0.32, 0.75),
                    s2_hook_pt=('BC', 0.10, 0.74),
                    s2_tip=('BL', 0.55, 0.55),
                    s3_head=('BL', 0.50, 0.24),
                    s3_tail=('MR', 0.22, 0.54)):
    draw_heng_pie(draw, s1_head, s1_corner, s1_tip,
                  head_w=8, corner_w=11, tip_w=3)
    draw_wan_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)
    draw_ti(draw, s3_head, s3_tail,
            head_width=13, tail_width=1, curve=0.06)
