"""竖提 (shù tí) — vertical descent then rising 提 flick up-right.

Signature:
  draw_shu_ti(draw, shu_head, shu_tail, ti_tail,
              shu_head_w=13, shu_tail_w=11,
              ti_head_w=13, ti_tail_w=1)

Anchors:
  shu_head — top of the vertical (TC).
  shu_tail — bottom bend point (BC); welded to 提 head.
  ti_tail  — needle-tip of the rising flick (up-and-right; MR region).

Joint: single compound stroke — P (welded) at shu_tail = ti_head.
Ref: batch1 p1_stroke_12_竖提 (PASS).
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_shu_ti(draw, shu_head, shu_tail, ti_tail,
                shu_head_w=13, shu_tail_w=11,
                ti_head_w=13, ti_tail_w=1,
                color=(0, 0, 0)):
    p_h = anchor_to_xy(shu_head)
    p_t = anchor_to_xy(shu_tail)
    p_ti = anchor_to_xy(ti_tail)

    # 竖 body: straight sampled line with a light head→tail taper.
    body_pts = [(p_h[0] + (p_t[0] - p_h[0]) * (i / 40),
                 p_h[1] + (p_t[1] - p_h[1]) * (i / 40))
                for i in range(41)]
    body_widths = [shu_head_w + (shu_tail_w - shu_head_w) * (i / 40)
                   for i in range(41)]
    stroke_variable_width(draw, body_pts, body_widths, color=color)

    # Rounded elbow.
    r = shu_tail_w / 2.0 + 1.5
    draw.ellipse([p_t[0] - r, p_t[1] - r, p_t[0] + r, p_t[1] + r], fill=color)

    # 提 flick: bezier bowed upward (perpendicular to chord).
    dx, dy = p_ti[0] - p_t[0], p_ti[1] - p_t[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp_x = -dy / length
    perp_y = dx / length
    bow = 0.08 * length
    fmid = ((p_t[0] + p_ti[0]) * 0.5, (p_t[1] + p_ti[1]) * 0.5)
    ctrl = (fmid[0] + perp_x * bow, fmid[1] + perp_y * bow)
    ti_pts = quad_bezier(p_t, ctrl, p_ti, n=40)
    m = len(ti_pts) - 1
    ti_widths = [ti_head_w + (ti_tail_w - ti_head_w) * (i / m)
                 for i in range(m + 1)]
    stroke_variable_width(draw, ti_pts, ti_widths, color=color)
