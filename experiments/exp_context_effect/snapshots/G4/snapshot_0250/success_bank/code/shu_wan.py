"""竖弯 (shù wān) — straight vertical descent then rounded turn to horizontal.

Signature:
  draw_shu_wan(draw, head, belly, corner, tail,
               head_w=8, belly_w=12, corner_w=11, tail_w=9)

Anchors:
  head   — 起笔 (TC).
  belly  — Bezier control on the vertical column (keeps top straight,
           bend concentrated at bottom).
  corner — bend/turning point (BC).
  tail   — end of horizontal sweep (BR/MR region).

Joint: welded round bend at corner (single compound stroke).
Ref: batch1 p1_stroke_13_竖弯 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_shu_wan(draw, head, belly, corner, tail,
                 head_w=8, belly_w=12, corner_w=11, tail_w=9,
                 color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_corner = anchor_to_xy(corner)
    p_tail = anchor_to_xy(tail)

    # Body: bezier head → corner via belly as control (rounded bend).
    body_pts = quad_bezier(p_head, p_belly, p_corner, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w + (corner_w - belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Rounded turn: quick bezier from corner into horizontal tail direction.
    ctrl = (p_corner[0] + (p_tail[0] - p_corner[0]) * 0.25,
            p_corner[1])
    tail_pts = quad_bezier(p_corner, ctrl, p_tail, n=40)
    m = len(tail_pts) - 1
    tail_widths = [corner_w + (tail_w - corner_w) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, tail_pts, tail_widths, color=color)

    # Small terminal round-cap.
    r = tail_w / 2.0
    draw.ellipse([p_tail[0] - r, p_tail[1] - r, p_tail[0] + r, p_tail[1] + r],
                 fill=color)
