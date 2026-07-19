"""厶 (sī, "private", 2 strokes: 撇折 + 点) — B1 pass.

Strokes:
  s1 — 撇折 (pie_zhe): downward-left curve + a small rightward heng.
  s2 — 点 (small dot on the right side sealing the shape).

Joint: s1.tail (right end of the small heng) ⇆ s2.head → N (small gap
on the right side).
"""
from pie_zhe import draw_pie_zhe
from dian import draw_dian


def draw_si(draw,
            s1_head=('C', 0.40, 0.05),
            s1_pivot=('BL', 0.30, 0.55),
            s1_tail=('BR', 0.13, 0.40),
            s2_head=('C', 0.85, 0.85), s2_tail=('BR', 0.40, 0.70)):
    draw_pie_zhe(draw, s1_head, s1_pivot, s1_tail,
                 pie_head_w=12, pie_tip_w=5, heng_w=7, shoulder=4)
    draw_dian(draw, s2_head, s2_tail,
              head_width=3, peak_width=10, curve=0.05, segments=24)
