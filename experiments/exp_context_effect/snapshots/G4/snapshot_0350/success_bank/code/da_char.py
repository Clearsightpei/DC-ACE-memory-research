"""大 (dà, 3画) — Phase-3 char, B4 promotion.

Thin wrapper around mastered `da.py` (p2_radical_046_大). Anchors from
this Phase-3 item's MMH block matched the mastered radical's exactly.

Strokes: 横 + 撇 + 捺.
Joints: P at s1×s2 crossing (welded); N at s3.head vs s1 (~27 px, TR10
boundary — anchor-driven, na.head at C(0.424,0.74) sits below heng mid).
"""
from da import draw_da


def draw_da_char(draw,
                 heng_head=('ML', 0.615, 0.658), heng_tail=('MR', 0.373, 0.485),
                 pie_head=('TC', 0.219, 0.627), pie_tail=('BL', 0.404, 0.88),
                 na_head=('C', 0.424, 0.74), na_tail=('BR', 0.792, 0.877)):
    # OVERRIDE anchors for this composition per TR1 (identical to
    # mastered da.py defaults; passed explicitly).
    draw_da(draw,
            heng_head=heng_head, heng_tail=heng_tail,
            pie_head=pie_head, pie_tail=pie_tail,
            na_head=na_head, na_tail=na_tail)
