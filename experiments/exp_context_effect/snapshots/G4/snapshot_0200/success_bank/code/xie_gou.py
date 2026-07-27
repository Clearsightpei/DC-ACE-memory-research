"""斜钩 (xié gōu) — slanted concave-up body, hook flicks UP (not up-left).

Signature:
  draw_xie_gou(draw, head, belly, hook_pt, tip,
               head_w=8, belly_w=15, hook_start_w=13, tip_w=2)

Anchors (米字格, PIL-native — y grows DOWN within each cell):
  head    — 起笔 upper-left (TL).
  belly   — Bezier control at the concave-up bow's low point (C region).
  hook_pt — bottom-right where body ends and hook turns (BR).
  tip     — hook tip flicks UPWARD, ~same x_frac as hook_pt (BR).

Distinguishes from:
  弯钩: curved-vertical body, hook up-left.
  竖钩: straight vertical body, hook up-left.
  卧钩: near-horizontal shallow-arc body, hook up-left.
  斜钩: SLANTED body TL→BR, gentle concave-up bow, hook straight UP.

Joint spec: single stroke; internal hook is part of the primitive.
Used in 我, 戈, 戊, 成.
Ref: batch1 p1_stroke_16_斜钩 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_xie_gou(draw, head, belly, hook_pt, tip,
                 head_w=8, belly_w=15, hook_start_w=13, tip_w=2,
                 color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Body: quad Bezier with control chosen so the curve grazes belly at t=0.5.
    # B(0.5) = (p0 + 2*ctrl + p2) / 4  ⇒  ctrl = 2*belly - (p_head + p_hook)/2.
    ctrl_body = (2 * p_belly[0] - (p_head[0] + p_hook[0]) * 0.5,
                 2 * p_belly[1] - (p_head[1] + p_hook[1]) * 0.5)
    body_pts = quad_bezier(p_head, ctrl_body, p_hook, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        # head thin → swell to belly_w at ~65% → hook_start_w at tail.
        if t <= 0.65:
            u = t / 0.65
            w = head_w + (belly_w - head_w) * u
        else:
            u = (t - 0.65) / 0.35
            w = belly_w + (hook_start_w - belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Hook flick hook_pt → tip. Curl slightly right-then-up.
    ctrl_hook = (p_hook[0] + 6.0,
                 p_hook[1] - (p_hook[1] - p_tip[1]) * 0.15)
    hook_pts = quad_bezier(p_hook, ctrl_hook, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
