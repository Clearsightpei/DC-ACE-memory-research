"""横 (héng) — horizontal stroke primitive.

Signature: draw_heng(draw, from_anchor, to_anchor, width=10, color=(0,0,0))

Renders a straight, near-uniform-width horizontal stroke between two
米字格 anchors (typically along the mid-band or another horizontal band).

Joint: single stroke, no joints.
Ref: batch1 p1_stroke_01_横 (PASS).
"""
from _anchor import anchor_to_xy, fat_line


def draw_heng(draw, from_anchor, to_anchor, width=10, color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p1 = anchor_to_xy(to_anchor)
    fat_line(draw, p0, p1, width, color=color)
