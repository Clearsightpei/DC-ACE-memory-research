"""艹 (cǎo, "grass" as Phase-2 RADICAL, 3画) — B4 retry PASS promotion.

Same errata fix as cao_grass.py (char): two STRAIGHT 竖 piercing a
wide 横; TR8 rules 5/6 enforced (heng shares y, shus share x); TR9
span-full-grid; two P-class welded crossings.

NOTE: near-duplicate of cao_grass.py — kept separate to record that
BOTH radical- and char-context passed with the same construction.

Strokes:
  s1 — 横 (wide, span-full-grid, centered).
  s2 — 短竖 (left, straight, well above AND below the 横).
  s3 — 短竖 (right, straight, mirror of s2).

Joints: 2 × P (welded crossings, pixel gap 0).
"""
from _anchor import anchor_to_xy, fat_line


def draw_cao_grass_radical(draw,
                           s1_head=('ML', 0.45, 0.55),
                           s1_tail=('MR', 0.55, 0.55),
                           s2_head=('TC', 0.10, 0.65),
                           s2_tail=('BC', 0.10, 0.45),
                           s3_head=('TC', 0.80, 0.65),
                           s3_tail=('BC', 0.80, 0.45),
                           width=9):
    p1a = anchor_to_xy(s1_head); p1b = anchor_to_xy(s1_tail)
    p1b = (p1b[0], p1a[1])
    fat_line(draw, p1a, p1b, width)

    p2a = anchor_to_xy(s2_head); p2b = anchor_to_xy(s2_tail)
    p2b = (p2a[0], p2b[1])
    fat_line(draw, p2a, p2b, width - 1)

    p3a = anchor_to_xy(s3_head); p3b = anchor_to_xy(s3_tail)
    p3b = (p3a[0], p3b[1])
    fat_line(draw, p3a, p3b, width - 1)
