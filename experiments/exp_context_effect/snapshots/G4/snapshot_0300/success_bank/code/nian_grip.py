"""卄 (niàn, "grip / twenty", 3画) — Phase-3 char, B4 promotion.

Like 廾 / 井: two 竖 flanking one 横 crossing both. Cannot reuse
shi_ten.py (that draws ONE 十, we need 3 strokes with 2 crossings) —
inlined per TR6. TR8 applied: horizontal endpoints share y=0.75 (row);
each vertical shares its own column.

Strokes:
  s1 — 横 (long horizontal across middle, ML→MR at y_frac 0.75).
  s2 — 竖 (LEFT vertical, ML→BC).
  s3 — 竖 (RIGHT vertical, TC→BC).

Joints: s1 × s2 and s1 × s3 both P (welded crossings).
"""
from heng import draw_heng
from shu import draw_shu


def draw_nian_grip(draw,
                   s1_head=('ML', 0.30, 0.75), s1_tail=('MR', 0.75, 0.75),
                   s2_head=('ML', 0.95, 0.20), s2_tail=('BC', 0.05, 0.60),
                   s3_head=('TC', 0.85, 0.80), s3_tail=('BC', 0.85, 1.00)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng(draw, s1_head, s1_tail, width=10)
    draw_shu(draw, s2_head, s2_tail, width=10)
    draw_shu(draw, s3_head, s3_tail, width=10)
