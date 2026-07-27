"""宀 (mián, "roof" as Phase-3 CHAR, 3画) — B4 main promotion.

Thin wrapper: char-context reuse of mian.py (Phase-2 radical) with
OVERRIDING MMH Phase-3 anchors per TR1. Strokes: 点 + 点 + 横钩.

Joints (both N, do NOT weld):
  s1.tail well above s3 body — N (~32 px gap).
  s2.head near s3.head       — N (~13 px gap).

Shoulder of 横钩 chosen at (MR, 0.90, 0.90) so the horizontal spans
right, then the hook flicks down-left to tip in BR.
"""
from mian import draw_mian


def draw_mian_roof(draw,
                   s1_head=('C', 0.23, 0.195), s1_tail=('C', 0.579, 0.506),
                   s2_head=('ML', 0.668, 0.696), s2_tail=('BL', 0.536, 0.253),
                   s3_head=('ML', 0.791, 0.796),
                   s3_shoulder=('MR', 0.90, 0.90),
                   s3_tip=('BR', 0.115, 0.036)):
    draw_mian(draw,
              s1_head=s1_head, s1_tail=s1_tail,
              s2_head=s2_head, s2_tail=s2_tail,
              s3_head=s3_head, s3_shoulder=s3_shoulder, s3_tip=s3_tip)
