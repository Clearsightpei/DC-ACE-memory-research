"""橫折提 (héng zhé tí) — 横 → 90° 折 down → 提 rising flick up-right.

Signature:
  draw_heng_zhe_ti(draw, head_h, corner, knee, tail,
                   h_width=10, v_head_w=10, v_knee_w=12,
                   shoulder=13, knee_shoulder=14,
                   ti_head_w=13, ti_tail_w=1, ti_curve=0.06)

Anchors:
  head_h — 横 起笔 (ML region).
  corner — first 折 corner (MR region, top of drop).
  knee   — second 折 corner (bottom of drop, base of 提).
  tail   — needle-tip of the rising 提 flick (up-and-right of knee).

Joint spec: P (welded) at corner; P (welded) at knee.
Ref: batch1 p1_stroke_20_橫折提 (PASS).
"""
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def draw_heng_zhe_ti(draw, head_h, corner, knee, tail,
                     h_width=10, v_head_w=10, v_knee_w=12,
                     shoulder=13, knee_shoulder=14,
                     ti_head_w=13, ti_tail_w=1, ti_curve=0.06,
                     color=(0, 0, 0)):
    p_h = anchor_to_xy(head_h)
    p_c = anchor_to_xy(corner)
    p_k = anchor_to_xy(knee)
    p_t = anchor_to_xy(tail)

    # 横 segment.
    fat_line(draw, p_h, p_c, h_width, color=color)
    # Shoulder disc at corner.
    r = shoulder / 2.0
    draw.ellipse([p_c[0] - r, p_c[1] - r, p_c[0] + r, p_c[1] + r], fill=color)

    # 竖 segment corner → knee, mild taper v_head_w → v_knee_w.
    steps = 42
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        s0 = (p_c[0] + (p_k[0] - p_c[0]) * t0, p_c[1] + (p_k[1] - p_c[1]) * t0)
        s1 = (p_c[0] + (p_k[0] - p_c[0]) * t1, p_c[1] + (p_k[1] - p_c[1]) * t1)
        w = int(round(v_head_w + (v_knee_w - v_head_w) * ((t0 + t1) * 0.5)))
        w = max(1, w)
        draw.line([s0, s1], fill=color, width=w)

    # Knee shoulder disc.
    sd = knee_shoulder / 2.0
    draw.ellipse([p_k[0] - sd, p_k[1] - sd, p_k[0] + sd, p_k[1] + sd], fill=color)

    # 提 flick knee → tail, perpendicular bow.
    dx, dy = p_t[0] - p_k[0], p_t[1] - p_k[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp_x = -dy / length
    perp_y = dx / length
    bow = ti_curve * length
    mid = ((p_k[0] + p_t[0]) * 0.5, (p_k[1] + p_t[1]) * 0.5)
    ctrl = (mid[0] + perp_x * bow, mid[1] + perp_y * bow)
    ti_pts = quad_bezier(p_k, ctrl, p_t, n=42)
    m = len(ti_pts) - 1
    ti_widths = [ti_head_w + (ti_tail_w - ti_head_w) * (i / m)
                 for i in range(m + 1)]
    stroke_variable_width(draw, ti_pts, ti_widths, color=color)
