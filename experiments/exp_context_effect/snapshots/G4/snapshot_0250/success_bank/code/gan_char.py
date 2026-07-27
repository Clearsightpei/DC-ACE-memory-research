"""干 (gān, Phase-3 CHAR, 3画) — B4 main promotion.

Thin wrapper: char-context reuse of gan.py (Phase-2 radical 干) with
OVERRIDING MMH Phase-3 anchors per TR1. Strokes: 短横 + 长横 + 竖.
Joints: s1.mid ⇆ s3.head @ TC — N (~25 px gap; do NOT weld);
        s2.mid ⇆ s3.mid  @ C  — P (welded crossing by construction).
"""
from gan import draw_gan


def draw_gan_char(draw,
                  s1_head=('TL', 0.923, 0.826), s1_tail=('TR', 0.165, 0.691),
                  s2_head=('ML', 0.305, 0.69),  s2_tail=('MR', 0.736, 0.588),
                  s3_head=('TC', 0.362, 0.923), s3_tail=('BC', 0.482, 1.103)):
    draw_gan(draw,
             s1_head=s1_head, s1_tail=s1_tail,
             s2_head=s2_head, s2_tail=s2_tail,
             s3_head=s3_head, s3_tail=s3_tail)
