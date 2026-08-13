"""横撇弯钩 (héng piě wān gōu) — 4-phase compound stroke:
   横 → 撇 → 弯 → 钩. Appears in 阝 (队/防/阳) and 那/邓.

Signature:
  draw_heng_pie_wan_gou(draw, head_h, corner, knee, belly, hook_pt, tip,
                        h_width=8, corner_shoulder=12,
                        pie_head_w=11, pie_knee_w=8, knee_shoulder=11,
                        wan_head_w=8, wan_belly_w=12,
                        hook_start_w=10, tip_w=2)

Anchors:
  head_h  — 横 起笔 (top-left).
  corner  — first 折 corner (top-right of 横).
  knee    — bottom of 撇 sweep, top of 弯 (down-left of corner).
  belly   — Bezier control for the 弯 curve descending below knee.
  hook_pt — base of hook.
  tip     — hook tip, UP-and-LEFT of hook_pt.

Joint spec: P at corner; P at knee; internal hook.
Ref: batch2 p1_stroke_24_横撇弯钩 (PASS).
"""
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_heng_pie_wan_gou(draw, head_h, corner, knee, belly, hook_pt, tip,
                          h_width=8, corner_shoulder=12,
                          pie_head_w=11, pie_knee_w=8, knee_shoulder=11,
                          wan_head_w=8, wan_belly_w=12,
                          hook_start_w=10, tip_w=2,
                          color=(0, 0, 0)):
    p_h = anchor_to_xy(head_h)
    p_c = anchor_to_xy(corner)
    p_k = anchor_to_xy(knee)
    p_b = anchor_to_xy(belly)
    p_hk = anchor_to_xy(hook_pt)
    p_t = anchor_to_xy(tip)

    # 横: head_h → corner.
    fat_line(draw, p_h, p_c, h_width, color=color)
    r = corner_shoulder / 2.0
    draw.ellipse([p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r], fill=color)

    # 撇: corner → knee (tapered bezier with mild bow).
    dx, dy = p_k[0] - p_c[0], p_k[1] - p_c[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = 0.05 * length
    mid = ((p_c[0] + p_k[0]) * 0.5, (p_c[1] + p_k[1]) * 0.5)
    pie_ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pie_pts = quad_bezier(p_c, pie_ctrl, p_k, n=30)
    n = len(pie_pts) - 1
    pie_widths = []
    for i in range(n + 1):
        t = i / n
        eased = t ** 1.2
        w = pie_head_w + (pie_knee_w - pie_head_w) * eased
        pie_widths.append(w)
    stroke_variable_width(draw, pie_pts, pie_widths, color=color)
    # Knee shoulder.
    r = knee_shoulder / 2.0
    draw.ellipse([p_k[0] - r, p_k[1] - r, p_k[0] + r, p_k[1] + r], fill=color)

    # 弯: knee → hook_pt via belly as control (curve descends below knee).
    body_pts = quad_bezier(p_k, p_b, p_hk, n=60)
    m = len(body_pts) - 1
    body_widths = []
    for i in range(m + 1):
        t = i / m
        if t <= 0.55:
            u = t / 0.55
            w = wan_head_w + (wan_belly_w - wan_head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = wan_belly_w + (hook_start_w - wan_belly_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # 钩: hook_pt → tip, flick up-and-left.
    hook_ctrl = (p_hk[0] + (p_t[0] - p_hk[0]) * 0.3,
                 p_hk[1] + (p_t[1] - p_hk[1]) * 0.15)
    hook_pts = quad_bezier(p_hk, hook_ctrl, p_t, n=20)
    k = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / k)
                   for i in range(k + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
