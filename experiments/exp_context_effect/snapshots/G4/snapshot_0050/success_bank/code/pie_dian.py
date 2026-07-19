"""撇点 (piě diǎn) — 撇 sweep down-left then sharp turn into a 点 press down-right.

Signature:
  draw_pie_dian(draw, head, pivot, tail,
                pie_head_w=13, pie_tip_w=4,
                dian_head_w=4, dian_tail_w=11)

Anchors:
  head  — 撇 起笔 (TC region, upper).
  pivot — welded elbow shared by both segments (C region, lower-left).
  tail  — 点 press tail (BC region, down-right of pivot).

Segments:
  1. 撇 head → pivot: tapered, mild leftward bow.
  2. 点 pivot → tail: swells thin → press, rounded terminal.

Joint spec: P (welded) at pivot — pivot is SHARED between 撇 tail
and 点 head.
Ref: batch1 p1_stroke_17_撇点 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def _tapered_bezier(draw, p0, p2, w0, w1, curve=0.08, segments=32,
                    color=(0, 0, 0)):
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [w0 + (w1 - w0) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)


def draw_pie_dian(draw, head, pivot, tail,
                  pie_head_w=13, pie_tip_w=4,
                  dian_head_w=4, dian_tail_w=11,
                  color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_pivot = anchor_to_xy(pivot)
    p_tail = anchor_to_xy(tail)

    # 撇: head → pivot, tapered thick → thin.
    _tapered_bezier(draw, p_head, p_pivot, pie_head_w, pie_tip_w,
                    curve=0.08, segments=44, color=color)
    # 点: pivot → tail, thin → press, opposite bow direction.
    _tapered_bezier(draw, p_pivot, p_tail, dian_head_w, dian_tail_w,
                    curve=-0.06, segments=32, color=color)
    # Rounded terminal press.
    cap_r = dian_tail_w / 2.0
    draw.ellipse([p_tail[0] - cap_r, p_tail[1] - cap_r,
                  p_tail[0] + cap_r, p_tail[1] + cap_r], fill=color)
