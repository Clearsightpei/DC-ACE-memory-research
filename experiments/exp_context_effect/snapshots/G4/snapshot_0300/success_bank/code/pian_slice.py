"""片 (piàn, "slice", 4 strokes) — B2 pass.

All strokes inlined (bank imports not used for primitives; the s4 tail
extends past the canvas which no bank primitive expresses cleanly).

Note: file is `pian_slice.py` to avoid collision with `pian.py` (丷).

Strokes:
  s1 — 撇 (top-left curved, tapered).
  s2 — 竖 (short top-right).
  s3 — 横 (middle bar).
  s4 — 横折 (bottom bar + right descent, extends past canvas).

Joints:
  s1.mid ⇆ s3.head — N.
  s1.mid ⇆ s4.head — N.
  s2.tail ⇆ s3     — N (~10 px).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def draw_pian_slice(draw,
                    s1_head=('TC', 0.20, 0.20), s1_tail=('BL', 0.55, 0.90),
                    s2_head=('TC', 0.75, 0.30), s2_tail=('C', 0.75, 0.25),
                    s3_head=('C', 0.05, 0.25),  s3_tail=('MR', 0.10, 0.25),
                    s4_head=('C', 0.10, 0.55),
                    s4_corner=('MR', 0.10, 0.55),
                    s4_tail=('MR', 0.10, 1.40)):
    color = (0, 0, 0)
    p_head = anchor_to_xy(s1_head)
    p_tail = anchor_to_xy(s1_tail)
    mid = ((p_head[0]+p_tail[0])*0.5, (p_head[1]+p_tail[1])*0.5)
    ctrl = (mid[0]+35, mid[1]-10)
    pts = quad_bezier(p_head, ctrl, p_tail, n=48)
    widths = [12 + (2-12)*(i/48) for i in range(49)]
    stroke_variable_width(draw, pts, widths, color=color)

    fat_line(draw, anchor_to_xy(s2_head), anchor_to_xy(s2_tail), width=8)
    fat_line(draw, anchor_to_xy(s3_head), anchor_to_xy(s3_tail), width=7)

    p_s4h = anchor_to_xy(s4_head)
    p_s4c = anchor_to_xy(s4_corner)
    p_s4t = anchor_to_xy(s4_tail)
    fat_line(draw, p_s4h, p_s4c, width=8)
    fat_line(draw, p_s4c, p_s4t, width=8)
    r = 6
    draw.ellipse([p_s4c[0]-r, p_s4c[1]-r, p_s4c[0]+r, p_s4c[1]+r], fill=color)
