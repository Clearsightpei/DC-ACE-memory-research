"""横钩 (héng gōu) — horizontal body ending in a short DOWN-LEFT hook flick.

Signature:
  draw_heng_gou(draw, head, shoulder, tip,
                head_w=8, mid_w=6, shoulder_w=11, tip_w=2)

Anchors:
  head     — 起笔 upper-left region (TL).
  shoulder — 顿笔 at the right end of the horizontal (TR).
  tip      — hook tip (down-and-left of shoulder).

Body: subtle upward-arched Bezier head→shoulder; taper thin at head,
  slim at mid, swell to shoulder_w at the 顿笔 press.
Hook: short bezier flick shoulder→tip, tapered to a needle.

Joint spec: single stroke; internal hook is part of the primitive.
Ref: batch1 p1_stroke_10_横钩 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_heng_gou(draw, head, shoulder, tip,
                  head_w=8, mid_w=6, shoulder_w=11, tip_w=2,
                  color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_shldr = anchor_to_xy(shoulder)
    p_tip = anchor_to_xy(tip)

    # Slight upward arch: control point above chord midpoint.
    mx = (p_head[0] + p_shldr[0]) * 0.5
    my = (p_head[1] + p_shldr[1]) * 0.5 - 6  # y-up in PIL is smaller y
    ctrl_body = (mx, my)
    body_pts = quad_bezier(p_head, ctrl_body, p_shldr, n=80)

    body_widths = []
    n = len(body_pts) - 1
    for i in range(n + 1):
        t = i / n
        # head_w → mid_w at 45%, then swell to shoulder_w at end.
        if t <= 0.45:
            u = t / 0.45
            w = head_w + (mid_w - head_w) * u
        else:
            u = (t - 0.45) / 0.55
            w = mid_w + (shoulder_w - mid_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Hook flick shoulder → tip (down-left).
    ctrl_hook = (p_shldr[0] + (p_tip[0] - p_shldr[0]) * 0.15,
                 p_shldr[1] + (p_tip[1] - p_shldr[1]) * 0.55)
    hook_pts = quad_bezier(p_shldr, ctrl_hook, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [shoulder_w + (tip_w - shoulder_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)
