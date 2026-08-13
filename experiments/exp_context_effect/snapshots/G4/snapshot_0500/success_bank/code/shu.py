"""竖 (shù) — vertical stroke primitive.

Signature: draw_shu(draw, from_anchor, to_anchor, width=10, color=(0,0,0))

Straight, near-uniform-width vertical, top→bottom.

Joint: single stroke, no joints.
Ref: batch1 p1_stroke_02_竖 (PASS).
"""
from _anchor import anchor_to_xy, fat_line


def draw_shu(draw, from_anchor, to_anchor, width=10, color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p1 = anchor_to_xy(to_anchor)
    fat_line(draw, p0, p1, width, color=color)
