"""弯钩 (wān gōu) — curved-vertical body ending in a short up-left hook.

Signature:
  draw_wan_gou(draw, head, belly, hook_pt, tip,
               head_w=8, belly_w=12, hook_start_w=10, tip_w=2)

Anchors:
  head    — top of body (near TC).
  belly   — Bezier control for the body (roughly on the vertical column;
            leftward drift concentrated near the bottom).
  hook_pt — where body ends and hook begins.
  tip     — hook flick terminus (up-and-left of hook_pt).

Joint: single stroke; internal hook is part of the primitive.
Ref: batch1 p1_stroke_07_弯钩 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_wan_gou(draw, head, belly, hook_pt, tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2,
                 color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Body: quadratic bezier through belly as control point.
    body_pts = quad_bezier(p_head, p_belly, p_hook, n=60)
    body_widths = []
    n = len(body_pts) - 1
    for i in range(n + 1):
        t = i / n
        # Head thin, swell to belly_w around 55%, then hook_start_w at tail.
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w + (hook_start_w - belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Hook flick hook_pt → tip. Control biased slightly left/down to curl.
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.3,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.15)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=20)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
