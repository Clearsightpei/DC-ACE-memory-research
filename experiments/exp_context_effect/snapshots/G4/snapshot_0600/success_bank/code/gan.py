"""干 (gān, 3 strokes: two 横 + one 竖) — B1 pass.

Strokes:
  s1 — short top 横 (~120 px).
  s2 — longer middle 横 (~200 px).
  s3 — 竖 piercing s2 at C (150, 160) and continuing down.

Joints: N at s1 vs s3 (~14 px, small gap where 竖 head sits just below
top bar); P at s2 × s3 (welded crossing by construction).
"""
from heng import draw_heng
from shu import draw_shu


def draw_gan(draw,
             s1_head=('TL', 0.80, 0.10), s1_tail=('TC', 1.00, 0.10),
             s2_head=('ML', 0.50, 0.60), s2_tail=('MR', 0.50, 0.60),
             s3_head=('TC', 0.50, 0.20), s3_tail=('BC', 0.50, 0.60)):
    draw_heng(draw, s1_head, s1_tail, width=10)
    draw_heng(draw, s2_head, s2_tail, width=10)
    draw_shu(draw, s3_head, s3_tail, width=10)
