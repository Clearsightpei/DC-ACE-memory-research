"""丷 (2-stroke, two dots opening outward) — B1 pass.

Strokes:
  s1 — 点 (left, thick head at ML sweeping down-and-right).
  s2 — 撇 (right, thick head upper-right sweeping down-and-left/right).

Both strokes fan outward from a central gap. Joints: none (S-class).
"""
from dian import draw_dian
from pie import draw_pie


def draw_pian(draw,
              s1_head=('ML', 0.90, 0.40), s1_tail=('C', 0.30, 0.75),
              s2_head=('C', 0.90, 0.25), s2_tail=('C', 0.55, 0.80)):
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=12, curve=0.08, segments=24)
    draw_pie(draw, s2_head, s2_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)
