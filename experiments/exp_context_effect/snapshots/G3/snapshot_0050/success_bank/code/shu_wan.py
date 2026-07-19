# shu_wan.py — 竖弯 (shu wan, vertical then curve rightward) coord primitive.
# Extracted from attempts/p1_stroke_13_竖弯/generated.py after human PASS.

import math

CANVAS_SIZE = 300
TH = 14


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_wan(t, ox=0, oy=0, scale=1.0):
    """竖弯 = vertical descending + smooth quarter-arc + horizontal right."""
    ink = max(1, int(TH * scale))
    # Anchor points (converted from image coords in the pass attempt).
    x_top_m = -20 * scale
    y_top_m = 95 * scale
    x_bot_m = -20 * scale
    y_bot_m = -50 * scale
    arc_r = 30 * scale
    x_end_m = 95 * scale
    y_end_m = -80 * scale

    # vertical
    pa = _to_pixel(ox + x_top_m, oy + y_top_m)
    pb = _to_pixel(ox + x_bot_m, oy + y_bot_m)
    t.line([pa, pb], fill=(0, 0, 0), width=ink)

    # arc from (x_bot_m, y_bot_m) sweeping down-right; centered at (x_bot_m+arc_r, y_bot_m).
    turn_cx_m = x_bot_m + arc_r
    turn_cy_m = y_bot_m
    steps = 24
    for i in range(steps + 1):
        ang = math.radians(180 - (i / steps) * 90)
        dx = arc_r * math.cos(ang)
        # In image space the arc dips downward: mirror the sin term to math (-y).
        dy_img = arc_r * math.sin(ang)
        # Convert center from math to pixel then offset.
        cx_px, cy_px = _to_pixel(ox + turn_cx_m, oy + turn_cy_m)
        px = cx_px + dx
        py = cy_px + dy_img
        r = ink // 2
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # horizontal segment from arc end to x_end/y_end
    h_start_m_x = x_bot_m + arc_r
    h_start_m_y = y_bot_m - arc_r  # math: subtract because we went "down" in image
    pc = _to_pixel(ox + h_start_m_x, oy + h_start_m_y)
    pd = _to_pixel(ox + x_end_m, oy + y_end_m)
    t.line([pc, pd], fill=(0, 0, 0), width=ink)
