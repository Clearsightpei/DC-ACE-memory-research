"""口 (kǒu, "mouth" as Phase-3 CHAR, 3画) — B4 main promotion.

Thin wrapper: char-context reuse of kou.py (Phase-2 radical). MMH
Phase-3 anchors match the radical defaults for this standalone glyph;
pass them explicitly per TR1. Strokes: 竖 + 横折 + 横.
Joints: 3 × N (top-left ~15 px, bottom-left ~13 px, bottom-right ~15 px).
"""
from kou import draw_kou


def draw_kou_char(draw,
                  s1_head=('ML', 0.671, 0.289), s1_tail=('BC', 0.02, 0.555),
                  s2_head=('ML', 0.891, 0.333),
                  s2_corner=('C', 0.93, 0.33),
                  s2_tail=('BC', 0.937, 0.2),
                  s3_head=('BC', 0.081, 0.458),
                  s3_tail=('BR', 0.18, 0.344)):
    draw_kou(draw,
             s1_head=s1_head, s1_tail=s1_tail,
             s2_head=s2_head,
             s2_corner=s2_corner,
             s2_tail=s2_tail,
             s3_head=s3_head, s3_tail=s3_tail)
