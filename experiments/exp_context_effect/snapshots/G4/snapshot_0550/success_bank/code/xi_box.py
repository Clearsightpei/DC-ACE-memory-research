"""匸 (xì, "left-opening box", 2 strokes) — B1 pass.

Similar to 匚 (fang) but the top and bottom bars close on opposite
side; here the right side is closed by the 竖折 wrap.

Strokes:
  s1 — 横 (top horizontal).
  s2 — 竖折 (right wall + bottom horizontal).

Joint: s1.tail-region ⇆ s2.head → N (small gap at top-right corner).
"""
from heng import draw_heng
from shu_zhe import draw_shu_zhe


def draw_xi_box(draw,
                s1_head=('ML', 0.398, 0.072),
                s1_tail=('TR', 0.385, 0.888),
                s2_head=('ML', 0.87, 0.175),
                s2_corner=('BR', 0.604, 0.81),
                s2_tail=('BL', 0.87, 0.81)):
    draw_heng(draw, s1_head, s1_tail, width=10)
    draw_shu_zhe(draw, s2_head, s2_corner, s2_tail,
                 v_width=10, h_width=10, shoulder=13)
