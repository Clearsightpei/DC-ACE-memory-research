"""竖弯钩 (shù wān gōu) — vertical descent, rounded turn to horizontal,
ending in short UPWARD hook flick.

Signature:
  draw_shu_wan_gou(draw, head, belly, corner, hook_pt, tip,
                   head_w=8, belly_w=12, corner_w=11,
                   hook_start_w=10, tip_w=2)

Anchors:
  head    — 起笔 top of vertical (TC).
  belly   — Bezier control on the vertical column (keeps upper body
            straight; bend concentrated at bottom).
  corner  — bend / turning point (BC).
  hook_pt — end of horizontal sweep, base of the hook (right side).
  tip     — hook tip pointing UPWARD from hook_pt.

Joint: welded round bend at corner; internal UP hook at hook_pt→tip.
Ref: batch2 p1_stroke_23_竖弯钩 (PASS). Used in 儿, 見, 元, 光.
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_shu_wan_gou(draw, head, belly, corner, hook_pt, tip,
                     head_w=8, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2,
                     color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_belly = anchor_to_xy(belly)
    p_corner = anchor_to_xy(corner)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Body: bezier head → corner via belly.
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

    # Rounded turn corner → hook_pt (horizontal sweep).
    ctrl = (p_corner[0] + (p_hook[0] - p_corner[0]) * 0.25, p_corner[1])
    tail_pts = quad_bezier(p_corner, ctrl, p_hook, n=40)
    m = len(tail_pts) - 1
    tail_widths = [corner_w + (hook_start_w - corner_w) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, tail_pts, tail_widths, color=color)

    # Rounded knee at hook_pt.
    r = hook_start_w / 2.0 + 1.0
    draw.ellipse([p_hook[0] - r, p_hook[1] - r,
                  p_hook[0] + r, p_hook[1] + r], fill=color)

    # Hook flick hook_pt → tip (UP; hook tip y is LESS than hook_pt y in PIL).
    hook_ctrl = (p_hook[0] + 4.0,
                 p_hook[1] + (p_tip[1] - p_hook[1]) * 0.35)
    hook_pts = quad_bezier(p_hook, hook_ctrl, p_tip, n=24)
    k = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / k)
                   for i in range(k + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
