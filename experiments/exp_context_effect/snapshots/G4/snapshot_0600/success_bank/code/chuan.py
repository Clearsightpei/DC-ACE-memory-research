"""川 (chuān, "river", 3 strokes: 撇 + 竖 + 竖) — B1 pass.

Strokes:
  s1 — 撇 (curved sweep upper-mid-right down to lower-left, bowed).
  s2 — 竖 (short middle vertical).
  s3 — 竖 (tall right vertical).

Joints: none (S-class; three separate strokes).
"""
from pie import draw_pie
from shu import draw_shu


def draw_chuan(draw,
               s1_head=('ML', 0.727, 0.102),
               s1_tail=('BL', 0.352, 0.771),
               s2_head=('C', 0.386, 0.204),
               s2_tail=('BC', 0.456, 0.508),
               s3_head=('TC', 0.995, 0.727),
               s3_tail=('BR', 0.13, 1.0)):
    draw_pie(draw, from_anchor=s1_head, to_anchor=s1_tail,
             head_width=12, tail_width=2, curve=0.14, segments=48)
    draw_shu(draw, from_anchor=s2_head, to_anchor=s2_tail, width=10)
    draw_shu(draw, from_anchor=s3_head, to_anchor=s3_tail, width=11)
