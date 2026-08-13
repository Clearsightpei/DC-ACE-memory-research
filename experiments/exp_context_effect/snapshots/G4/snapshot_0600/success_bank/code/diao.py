"""刁 (diāo, 2画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 横撇弯钩 (heng-pie-wan-gou): top 横 → bends down along right →
       hook LEFT at bottom.
  s2 — 提 (ti): short rising diagonal, lower-left → mid-right.

Joints: NONE (both strokes visually separated).
"""
from heng_pie_wan_gou import draw_heng_pie_wan_gou
from ti import draw_ti


def draw_diao(draw,
              s1_head=('ML', 0.729, 0.075), s1_corner=('TR', 0.30, 0.75),
              s1_knee=('MR', 0.45, 0.10), s1_belly=('MR', 0.30, 0.65),
              s1_hookpt=('BC', 0.412, 0.537), s1_tip=('BC', 0.15, 0.30),
              s2_head=('BL', 0.530, 0.013), s2_tail=('C', 0.828, 0.436)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng_pie_wan_gou(
        draw,
        s1_head, s1_corner, s1_knee, s1_belly, s1_hookpt, s1_tip,
        h_width=8, corner_shoulder=11,
        pie_head_w=10, pie_knee_w=7, knee_shoulder=10,
        wan_head_w=7, wan_belly_w=11,
        hook_start_w=9, tip_w=2,
    )
    draw_ti(draw, s2_head, s2_tail, head_width=12, tail_width=2, curve=0.06)
