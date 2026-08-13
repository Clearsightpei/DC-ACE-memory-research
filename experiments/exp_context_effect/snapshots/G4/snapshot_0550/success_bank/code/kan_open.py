"""凵 (kǎn, "open container" as Phase-3 CHAR, 2画) — B4 retry PASS promotion.

Retry-0 failed because it used cramped MMH anchors verbatim (squashed
into BR only). Retry-1 fix: TR9 span-full-grid for standalone enclosing
radical; reuse shu_zhe primitive with overriding anchors per TR1;
share BR cell for N-joint (TR10 ≈10 px gap).

MMH declares 2 strokes (竖折 packs left wall + bottom into one), not
the naive 3 (shu + heng + shu).

Strokes:
  s1 — 竖折 (left wall descends, sharp 90° corner at BL, sweeps right to BR).
  s2 — 竖 (short right wall, straight, ends near s1.tail in BR).

Joint: s1.tail @ BR ⇆ s2.tail @ BR — N (~10 px gap; TR10 compliant).

TR8: s1.head-corner share L-column, s1.corner-tail share B-row;
     s2.head-tail share R-column.
"""
from shu_zhe import draw_shu_zhe
from shu import draw_shu


def draw_kan_open(draw,
                  s1_head=('ML', 0.55, 0.30),
                  s1_corner=('BL', 0.55, 0.65),
                  s1_tail=('BR', 0.55, 0.65),
                  s2_head=('MR', 0.55, 0.30),
                  s2_tail=('BR', 0.55, 0.75)):
    draw_shu_zhe(draw, s1_head, s1_corner, s1_tail,
                 v_width=11, h_width=11, shoulder=14)
    draw_shu(draw, s2_head, s2_tail, width=11)
