"""横折钩 (héng zhé gōu) — 横折 body + short UP-LEFT hook flick at tail.

Signature:
  draw_heng_zhe_gou(draw, head, corner, tail, tip,
                    h_width=10, v_width=10, shoulder=13, tip_w=2)

Anchors:
  head   — 起笔 upper-left (TL).
  corner — 折 point (top-right, MR/TR boundary).
  tail   — bottom of vertical drop (BR), hook base.
  tip    — hook tip, UP-and-LEFT of tail.

Segments (single compound stroke): 横 → 竖 → hook flick.

Joint spec: P (welded) at corner; internal hook up-and-left.
Ref: batch2 p1_stroke_22_横折钩 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from heng_zhe import draw_heng_zhe


def draw_heng_zhe_gou(draw, head, corner, tail, tip,
                      h_width=10, v_width=10, shoulder=13, tip_w=2,
                      color=(0, 0, 0)):
    # Body is exactly a 横折 head→corner→tail.
    draw_heng_zhe(draw, head, corner, tail,
                  h_width=h_width, v_width=v_width, shoulder=shoulder,
                  color=color)

    # Hook flick tail → tip (up-and-left).
    p_tail = anchor_to_xy(tail)
    p_tip = anchor_to_xy(tip)
    ctrl_hook = (p_tail[0] + (p_tip[0] - p_tail[0]) * 0.15,
                 p_tail[1] + (p_tip[1] - p_tail[1]) * 0.55)
    hook_pts = quad_bezier(p_tail, ctrl_hook, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [v_width + (tip_w - v_width) * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
