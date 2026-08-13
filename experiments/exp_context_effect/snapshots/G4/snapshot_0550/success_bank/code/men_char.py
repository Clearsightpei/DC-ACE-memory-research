"""门 (mén, "door", 3画) — Phase-3 CHAR promotion (B4 main).

Thin wrapper: char-context reuse of men.py (Phase-2 radical) with
MMH Phase-3 anchor overrides per TR1. Strokes: 点 + 竖 + 横折钩.
Joints: NONE (MMH declares 0; small natural pixel gaps).
"""
from men import draw_men


def draw_men_char(draw,
                  s1_head=('TL', 0.891, 0.744), s1_tail=('C', 0.151, 0.04),
                  s2_head=('TL', 0.548, 0.964), s2_tail=('BL', 0.560, 0.871),
                  s3_head=('TC', 0.506, 0.829),
                  s3_corner=('TR', 0.75, 0.85),
                  s3_tail=('BR', 0.70, 0.80),
                  s3_tip=('BC', 0.928, 0.769)):
    draw_men(draw, s1_head, s1_tail, s2_head, s2_tail,
             s3_head, s3_corner, s3_tail, s3_tip)
