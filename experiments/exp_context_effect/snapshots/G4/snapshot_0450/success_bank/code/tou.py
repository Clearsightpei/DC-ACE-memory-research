"""亠 (tóu, "lid", 2 strokes: 点 + 横) — B1 pass.

Strokes:
  s1 — 点 (small dot, centered above the horizontal).
  s2 — 横 (top horizontal spanning left to right).

Joints: none (S-class — dot floats above the horizontal).
"""
from dian import draw_dian
from heng import draw_heng


def draw_tou(draw,
             DIAN_HEAD=('C', 0.204, 0.28), DIAN_TAIL=('C', 0.608, 0.559),
             HENG_HEAD=('ML', 0.463, 0.931),
             HENG_TAIL=('MR', 0.584, 0.857)):
    draw_dian(draw, DIAN_HEAD, DIAN_TAIL,
              head_width=2, peak_width=11, curve=0.08, segments=24)
    draw_heng(draw, HENG_HEAD, HENG_TAIL, width=10)
