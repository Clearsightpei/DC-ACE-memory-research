"""卧钩 (wò gōu) — shallow lying-hook: nearly-horizontal concave arc, hook up-left.

Signature:
  draw_wo_gou(draw, start, belly, exit, tip,
              head_w=3, belly_w=10, exit_w=10, tip_w=1)

Anchors (米字格, PIL-native — y grows DOWN within each cell):
  start — thin entry, upper-left.
  belly — Bezier control at the low point (lowest of the arc).
  exit  — thickest 顿笔 press before the hook (right end).
  tip   — hook tip, flicks UP-and-LEFT of exit.

Joint: single stroke; internal hook is part of the primitive.
Used in 心, 必, 忘, 志.
Ref: batch1 p1_stroke_08_卧钩 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_wo_gou(draw, start, belly, exit, tip,
                head_w=3, belly_w=10, exit_w=10, tip_w=1,
                color=(0, 0, 0)):
    p0 = anchor_to_xy(start)
    p1 = anchor_to_xy(belly)
    p2 = anchor_to_xy(exit)
    p3 = anchor_to_xy(tip)

    # Body arc start → exit via belly as control point.
    body_pts = quad_bezier(p0, p1, p2, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        # Thin start, swell to belly_w around 55%, hold to exit_w at tail.
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w + (exit_w - belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Hook flick exit → tip (up-and-left).
    ctrl = (p2[0] + (p3[0] - p2[0]) * 0.3,
            p2[1] + (p3[1] - p2[1]) * 0.15)
    hook_pts = quad_bezier(p2, ctrl, p3, n=20)
    m = len(hook_pts) - 1
    hook_widths = [exit_w + (tip_w - exit_w) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
