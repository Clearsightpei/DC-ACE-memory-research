"""尸 (shī, "corpse", 3 strokes: 横折 + 横 + 撇) — B1 pass.

Strokes:
  s1 — 横折 (top horizontal + right descent — the outer L).
  s2 — 横 (inner short horizontal in the middle).
  s3 — 撇 (long sweep down to lower-left).

Joints (all N-class, ~20 px gaps):
  s1.tail ⇆ s2.mid(0.78) on the right side.
  s1.head ⇆ s3.head near TC.
  s2.head ⇆ s3.mid(0.32) inside C.
"""
from heng_zhe import draw_heng_zhe
from heng import draw_heng
from pie import draw_pie


def draw_shi_corpse(draw,
                    s1_head=('TL', 0.95, 0.85),
                    s1_corner=('TR', 0.05, 0.85),
                    s1_tail=('MR', 0.00, 0.55),
                    s2_head=('C', 0.15, 0.55), s2_tail=('C', 0.80, 0.55),
                    s3_head=('TC', 0.15, 0.90), s3_tail=('BL', 0.20, 0.95)):
    draw_heng_zhe(draw, s1_head, s1_corner, s1_tail,
                  h_width=9, v_width=9, shoulder=11)
    draw_heng(draw, s2_head, s2_tail, width=8)
    draw_pie(draw, s3_head, s3_tail,
             head_width=12, tail_width=2, curve=0.08, segments=48)
