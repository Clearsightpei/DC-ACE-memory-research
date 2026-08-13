"""三 (sān, "three", 3画) — Phase-3 char, B4 promotion.

Three stacked horizontals; classic 三 proportion — top shortest, middle
medium, bottom longest. Clear vertical gaps between all three.

Related mastered: er.py (二, 2 horizontals) is the closest analog.

Joints: NONE (all-S — three separated strokes).
"""
from heng import draw_heng


def draw_san_three(draw,
                   s1_head=('TL', 0.75, 0.75), s1_tail=('TR', 0.25, 0.75),
                   s2_head=('ML', 0.65, 0.50), s2_tail=('MR', 0.35, 0.50),
                   s3_head=('BL', 0.20, 0.40), s3_tail=('BR', 0.80, 0.40)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_heng(draw, s2_head, s2_tail, width=10)
    draw_heng(draw, s3_head, s3_tail, width=11)
