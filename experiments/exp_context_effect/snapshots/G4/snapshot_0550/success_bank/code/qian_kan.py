"""凵 (qiǎn/kǎn, open-top-container, 2 strokes) — B1 pass.

Strokes:
  s1 — 竖折 (left wall + bottom).
  s2 — 竖 (right wall).

Joints: s1.tail (right end of bottom) ⇆ s2.tail → N (small gap at
bottom-right corner); s1's own corner is P (internal to primitive).
"""
from shu_zhe import draw_shu_zhe
from shu import draw_shu


def draw_qian(draw,
              s1_head=('ML', 0.55, 0.60),
              s1_corner=('BL', 0.55, 0.75),
              s1_tail=('BR', 0.60, 0.75),
              s2_head=('MR', 0.30, 0.55),
              s2_tail=('BR', 0.35, 0.75)):
    draw_shu_zhe(draw, s1_head, s1_corner, s1_tail,
                 v_width=10, h_width=10, shoulder=13)
    draw_shu(draw, s2_head, s2_tail, width=10)
