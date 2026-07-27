"""横折折折钩 (héng zhé zhé zhé gōu) — 5-phase staircase-plus-hook stroke.
Used in 乃 and 及. Structure: 横→竖→横→竖 staircase + up-left hook.

Signature:
  draw_heng_zhe_zhe_zhe_gou(draw, head, corner1, corner2, corner3, tail, tip,
                            h_width=10, v_width=10, shoulder=13, tip_w=2)

Anchors — staircase descending toward BR, then hook flick:
  head    — 起笔 (TL).
  corner1 — end of first 横 (TR).
  corner2 — end of first 竖 (MR).
  corner3 — end of second 横 (MR, right of corner2).
  tail    — end of final 竖 (BR), base of the hook.
  tip     — hook tip, UP-and-LEFT of tail.

Joint spec: P × 3 (corner1, corner2, corner3); internal hook up-and-left.
Ref: batch2 p1_stroke_32_横折折折钩 (PASS).
"""
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_heng_zhe_zhe_zhe_gou(draw, head, corner1, corner2, corner3, tail, tip,
                              h_width=10, v_width=10, shoulder=13, tip_w=2,
                              color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_c3 = anchor_to_xy(corner3)
    p_tail = anchor_to_xy(tail)
    p_tip = anchor_to_xy(tip)

    assert p_c1[0] > p_head[0], 'seg1 must go right'
    assert p_c2[1] > p_c1[1], 'seg2 must go down'
    assert p_c3[0] > p_c2[0], 'seg3 must go right'
    assert p_tail[1] > p_c3[1], 'seg4 must go down'
    assert p_tip[0] < p_tail[0], 'hook must flick LEFT'
    assert p_tip[1] < p_tail[1], 'hook must flick UP'

    fat_line(draw, p_head, p_c1, h_width, color=color)
    fat_line(draw, p_c1, p_c2, v_width, color=color)
    fat_line(draw, p_c2, p_c3, h_width, color=color)
    fat_line(draw, p_c3, p_tail, v_width, color=color)

    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2, p_c3):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

    # Hook flick tail → tip.
    ctrl_hook = (p_tail[0] + (p_tip[0] - p_tail[0]) * 0.15,
                 p_tail[1] + (p_tip[1] - p_tail[1]) * 0.55)
    hook_pts = quad_bezier(p_tail, ctrl_hook, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [v_width + (tip_w - v_width) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
