"""撇 (piě) — diagonal sweep from upper-right to lower-left, tapered.

Signature:
  draw_pie(draw, from_anchor, to_anchor,
           head_width=12, tail_width=1, curve=0.10, segments=48)

`from_anchor` (head) sits in the upper-right, thick 起笔.
`to_anchor`   (tail) sits in the lower-left, needle-tip 出锋.
`curve>0` bows the belly slightly toward the perpendicular of the chord.

Joint: single stroke, no joints.
Ref: batch1 p1_stroke_03_撇 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_pie(draw, from_anchor, to_anchor,
             head_width=12, tail_width=1, curve=0.10, segments=48,
             color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Perpendicular to chord (rotate 90°), curve bows in +perp direction.
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
