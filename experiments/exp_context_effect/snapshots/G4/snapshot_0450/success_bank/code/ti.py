"""提 (tí) — rising diagonal from lower-left to upper-right, tapered.

Signature:
  draw_ti(draw, from_anchor, to_anchor,
          head_width=13, tail_width=1, curve=0.09, segments=48)

Head (起笔) at lower-left is heaviest; tail (出锋) at upper-right is
needle-tipped. Bowed slightly toward the upper-left (perpendicular of
chord) for the classic rising-flick feel.

Joint: single stroke, no joints.
Ref: batch1 p1_stroke_06_提 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_ti(draw, from_anchor, to_anchor,
            head_width=13, tail_width=1, curve=0.09, segments=48,
            color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    # Perpendicular biased toward upper-left of the rising chord.
    perp_x = -dy / length
    perp_y = dx / length
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp_x * bow, mid[1] + perp_y * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
