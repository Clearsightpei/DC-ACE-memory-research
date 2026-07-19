"""点 (diǎn) — short diagonal dot, thin head → rounded 顿笔 press.

Signature:
  draw_dian(draw, from_anchor, to_anchor,
            head_width=2, peak_width=11, curve=0.08, segments=24)

Compact — both anchors typically inside a single cell (C).
head=fine 起笔 (upper-left), tail=rounded press (lower-right).

Joint: single stroke, no joints.
Ref: batch1 p1_stroke_05_点 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_dian(draw, from_anchor, to_anchor,
              head_width=2, peak_width=11, curve=0.08, segments=24,
              color=(0, 0, 0)):
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (peak_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
    # Rounded press terminal.
    r = peak_width / 2.0
    draw.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=color)
