"""竖钩 (shù gōu) — STRAIGHT vertical body then short up-left hook flick.

Signature:
  draw_shu_gou(draw, head, belly, hook_pt, tip,
               head_w=13, belly_w=11, hook_start_w=10, tip_w=2)

Anchors:
  head    — top of the vertical (TC).
  belly   — mid-body width-profile knot (SAME x_frac as head; not a
            curve control — body is straight).
  hook_pt — bottom of vertical body (BC), start of hook.
  tip     — hook tip (up-and-left of hook_pt).

Joint: single stroke; internal hook is part of the primitive.
Ref: batch1 p1_stroke_14_竖钩 (PASS).
"""
from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier


def draw_shu_gou(draw, head, belly, hook_pt, tip,
                 head_w=13, belly_w=11, hook_start_w=10, tip_w=2,
                 color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Body: straight sample_line head → hook_pt (belly used only for
    # width-profile knot, not curve control — body must stay straight).
    body_pts = sample_line(p_head, p_hook, n=50)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        # head_w → belly_w around 55%, hold near hook_start_w at bottom.
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = belly_w + (hook_start_w - belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Hook flick hook_pt → tip (up-and-left).
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
