"""丬 (jiāng, "left-half of 爿", 3画) — Phase-3 char, B4 promotion.

Thin wrapper around mastered `pan.py` (p2_radical_083_丬). Character
is identical to the radical; MMH anchors passed explicitly per TR1.

Strokes: pie (top-right sweeping down-left) + ti (rising) + shu (right vertical).
Joint: 1× N at C (s1.tail ⇆ s2/s3 region), matches MMH.
"""
from pan import draw_pan


def draw_jiang_side(draw,
                    s1_head=('C', 0.342, 0.424), s1_tail=('C', 0.046, 0.081),
                    s2_head=('BL', 0.87, 0.306), s2_tail=('C', 0.576, 0.749),
                    s3_head=('TC', 0.538, 0.7), s3_tail=('BC', 0.638, 1.026)):
    # OVERRIDE anchors per TR1. s1 head/tail swapped so pie orientation
    # (head upper-right, tail lower-left) matches pan.py's curve.
    draw_pan(draw,
             s1_head=s1_head, s1_tail=s1_tail,
             s2_head=s2_head, s2_tail=s2_tail,
             s3_head=s3_head, s3_tail=s3_tail)
