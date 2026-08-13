"""彳 (chì, "step radical", 3 strokes) — B1 pass.

Left-side radical: two stacked 撇 + a short vertical.

Strokes:
  s1 — short 撇 (upper).
  s2 — longer 撇 (middle, sweeping farther).
  s3 — short 竖 (bottom center).

Joints: both are N-class (small gaps at ends).
"""
from pie import draw_pie
from shu import draw_shu


def draw_chi_step(draw,
                  s1_head=('TC', 0.535, 0.612),
                  s1_tail=('ML', 0.938, 0.576),
                  s2_head=('C', 0.614, 0.242),
                  s2_tail=('BL', 0.806, 0.479),
                  s3_head=('C', 0.456, 0.922),
                  s3_tail=('BC', 0.494, 1.094)):
    draw_pie(draw, from_anchor=s1_head, to_anchor=s1_tail,
             head_width=8, tail_width=1, curve=0.10, segments=48)
    draw_pie(draw, from_anchor=s2_head, to_anchor=s2_tail,
             head_width=10, tail_width=1, curve=0.10, segments=48)
    draw_shu(draw, from_anchor=s3_head, to_anchor=s3_tail, width=9)
