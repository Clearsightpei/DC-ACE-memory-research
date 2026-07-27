"""幺 (yāo, "tiny", 3 strokes) — B2 pass.

Stacked pair of 撇折 (small top loop + main lower loop) plus a 点.

Strokes:
  s1 — 撇折 (small top loop).
  s2 — 撇折 (main lower loop, wider).
  s3 — 点 (bottom-right of s2).

Joints:
  s1.tail ⇆ s2.mid(0.26) @ C  — N (~12 px).
  s2.tail ⇆ s3.mid(0.65) @ BR — N (~19 px).
"""
from pie_zhe import draw_pie_zhe
from dian import draw_dian


def draw_yao_small(draw,
                   s1_head=('TC', 0.424, 0.762),
                   s1_pivot=('C', 0.05, 0.90),
                   s1_tail=('C', 0.585, 0.925),
                   s2_head=('C', 0.963, 0.356),
                   s2_pivot=('BC', 0.10, 0.85),
                   s2_tail=('BR', 0.098, 0.684),
                   s3_head=('BC', 0.91, 0.259),
                   s3_tail=('BR', 0.32, 0.927)):
    draw_pie_zhe(draw, s1_head, s1_pivot, s1_tail,
                 pie_head_w=8, pie_tip_w=3, heng_w=5, shoulder=3)
    draw_pie_zhe(draw, s2_head, s2_pivot, s2_tail,
                 pie_head_w=12, pie_tip_w=5, heng_w=7, shoulder=4)
    draw_dian(draw, s3_head, s3_tail, head_width=3, peak_width=10, curve=0.05)
