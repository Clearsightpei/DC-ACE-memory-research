"""竖折折钩 (shù zhé zhé gōu) — 竖折折 with a hook flick at the tail.

Signature:
  draw_shu_zhe_zhe_gou(draw, head, corner1, corner2, hook_pt, tip,
                       v_width=10, h_width=10, shoulder=13,
                       hook_start_w=10, tip_w=1)

Anchors:
  head    — 起笔 (TL).
  corner1 — bottom of first 竖, start of 横 (ML).
  corner2 — end of 横, start of final 竖 (C).
  hook_pt — bottom of final 竖 (hook base).
  tip     — hook tip, UP-and-LEFT of hook_pt.

Joint spec: P × 2 (corner1, corner2); internal hook flick up-left.
Ref: batch2 p1_stroke_31_竖折折钩 (PASS).
"""
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_shu_zhe_zhe_gou(draw, head, corner1, corner2, hook_pt, tip,
                         v_width=10, h_width=10, shoulder=13,
                         hook_start_w=10, tip_w=1,
                         color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    assert p_c1[1] > p_head[1], 'shu1 must drop downward'
    assert p_c2[0] > p_c1[0], 'heng must go rightward'
    assert p_hook[1] > p_c2[1], 'shu2 must drop downward'
    assert p_tip[1] < p_hook[1], 'hook flick must go upward'
    assert p_tip[0] < p_hook[0], 'hook flick must go leftward'

    fat_line(draw, p_head, p_c1, v_width, color=color)
    fat_line(draw, p_c1, p_c2, h_width, color=color)
    fat_line(draw, p_c2, p_hook, v_width, color=color)

    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

    # Hook flick hook_pt → tip.
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
