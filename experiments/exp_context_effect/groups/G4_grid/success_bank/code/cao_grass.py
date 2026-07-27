"""艹 (cǎo, "grass" as Phase-3 CHAR, 3画) — B4 main promotion.

Errata fix applied LITERALLY: two STRAIGHT 竖 (no curve; same x_frac
head/tail per TR8 rule 6) piercing one wide 横 (TR9 span-full-grid,
same y_frac head/tail per TR8 rule 5). Two P-class welded crossings.

Strokes:
  s1 — 横 (wide, span-full-grid at mid-band).
  s2 — 短竖 (left, straight vertical, well above AND below the 横).
  s3 — 短竖 (right, straight vertical, mirror of s2).

Joints: 2 × P (welded crossings, pixel gap 0) at s1∩s2 and s1∩s3.
"""
from _anchor import anchor_to_xy, fat_line


def draw_cao_grass(draw,
                   s1_head=('ML', 0.10, 0.85), s1_tail=('MR', 0.90, 0.85),
                   s2_head=('ML', 0.95, 0.55), s2_tail=('BL', 0.95, 0.20),
                   s3_head=('C', 0.75, 0.40),  s3_tail=('BC', 0.75, 0.20),
                   width=8):
    # Enforce TR8: horizontal shares y, verticals share x.
    p1a = anchor_to_xy(s1_head); p1b = anchor_to_xy(s1_tail)
    p1b = (p1b[0], p1a[1])
    fat_line(draw, p1a, p1b, width + 1)

    p2a = anchor_to_xy(s2_head); p2b = anchor_to_xy(s2_tail)
    p2b = (p2a[0], p2b[1])
    fat_line(draw, p2a, p2b, width)

    p3a = anchor_to_xy(s3_head); p3b = anchor_to_xy(s3_tail)
    p3b = (p3a[0], p3b[1])
    fat_line(draw, p3a, p3b, width)
