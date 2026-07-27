"""匚 (fāng, 2-stroke enclosing radical) — B1 pass.

Strokes:
  s1 — 横 (top horizontal).
  s2 — 竖折 (left wall + bottom).

Joints:
  s1.head @ TL(0.28, 0.28) ⇆ s2.head @ TL(0.15, 0.45)  → N (gap ~20 px)
"""
from heng import draw_heng
from shu_zhe import draw_shu_zhe


def draw_fang(draw,
              s1_head=('TL', 0.28, 0.28), s1_tail=('TR', 0.85, 0.28),
              s2_head=('TL', 0.15, 0.45),
              s2_corner=('BL', 0.15, 0.70),
              s2_tail=('BR', 0.80, 0.70)):
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_shu_zhe(draw, s2_head, s2_corner, s2_tail,
                 v_width=10, h_width=10, shoulder=12)
