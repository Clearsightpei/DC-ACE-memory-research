"""丫 (yā, "fork", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — LEFT branch (inlined tapered line, TL→C, gentle bow).
  s2 — RIGHT branch (inlined tapered line, TR→C, gentle bow other way).
  s3 — 竖 (center vertical, C→BC, slight clip past bottom edge).

Joint: s2.tail ⇆ s3.head @ C — N (~22 px gap, TR10 ≤25 px OK).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from shu import draw_shu


def _tapered_line(draw, a0, a1, w0, w1, curve=0.0, segments=32,
                  color=(0, 0, 0)):
    p0 = anchor_to_xy(a0)
    p2 = anchor_to_xy(a1)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    if abs(curve) > 1e-6:
        perp = (-dy / length, dx / length)
        bow = curve * length
        mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
        ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
        pts = quad_bezier(p0, ctrl, p2, n=segments)
    else:
        pts = [(p0[0] + (i / segments) * (p2[0] - p0[0]),
                p0[1] + (i / segments) * (p2[1] - p0[1]))
               for i in range(segments + 1)]
    widths = [w0 + (w1 - w0) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_ya_fork(draw,
                 s1_head=('TL', 0.718, 0.809), s1_tail=('C', 0.131, 0.257),
                 s2_head=('TR', 0.051, 0.662), s2_tail=('C', 0.535, 0.4),
                 s3_head=('C', 0.318, 0.359), s3_tail=('BC', 0.441, 1.041)):
    _tapered_line(draw, s1_head, s1_tail, w0=9, w1=3, curve=0.10)
    _tapered_line(draw, s2_head, s2_tail, w0=9, w1=3, curve=-0.08)
    draw_shu(draw, s3_head, s3_tail, width=10)
