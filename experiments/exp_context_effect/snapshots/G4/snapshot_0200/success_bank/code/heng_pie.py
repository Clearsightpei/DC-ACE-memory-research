"""横撇 (héng piě) — horizontal opening then diagonal 撇 down-left, tapered.

Signature:
  draw_heng_pie(draw, head, corner, tip,
                head_w=7, corner_w=11, tip_w=2)

Anchors:
  head   — 起笔 upper-left (near TL).
  corner — 折 pivot, top-right (顿笔 press).
  tip    — 撇 needle tip, lower-left (BL region).

Segments:
  1. 横 head → corner: near-straight, subtle taper down then swell at corner.
  2. 撇 corner → tip: tapered curved sweep, thick head → needle tip.

Joint spec: P (welded, single stroke) at corner. corner is SHARED
between the 横's tail and the 撇's head.

Ref: batch1 p1_stroke_09_横撇 (PASS).
"""
from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier


def draw_heng_pie(draw, head, corner, tip,
                  head_w=7, corner_w=11, tip_w=2,
                  color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_tip = anchor_to_xy(tip)

    # Segment 1: 横 (straight sample_line, small swell to corner).
    heng_pts = sample_line(p_head, p_corner, n=30)
    n = len(heng_pts) - 1
    heng_widths = [head_w + (corner_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, heng_pts, heng_widths, color=color)

    # Segment 2: 撇 (tapered bezier corner → tip; bow with mild perp offset).
    dx, dy = p_tip[0] - p_corner[0], p_tip[1] - p_corner[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = 0.08 * length
    mid = ((p_corner[0] + p_tip[0]) * 0.5, (p_corner[1] + p_tip[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pie_pts = quad_bezier(p_corner, ctrl, p_tip, n=40)
    m = len(pie_pts) - 1
    pie_widths = []
    for i in range(m + 1):
        t = i / m
        # Ease from corner_w down to tip_w along the sweep.
        eased = t ** 1.4
        w = corner_w + (tip_w - corner_w) * eased
        pie_widths.append(w)
    stroke_variable_width(draw, pie_pts, pie_widths, color=color)
