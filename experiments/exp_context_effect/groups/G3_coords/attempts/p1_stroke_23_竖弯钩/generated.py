# p1_stroke_23_竖弯钩 — 竖弯 + hook flick up at right end.
# Strategy: reuse the shu_wan geometry idiom (vertical + quarter arc +
# horizontal right), then add a short up-and-left hook off the far right
# end of the horizontal segment. Coord math convention: origin at canvas
# center, +y up.

import math
import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300
TH = 14  # ink width, same as shu_wan.


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def draw_shu_wan_gou(t, ox=0, oy=0, scale=1.0):
    """竖弯钩 = vertical descending + quarter-arc turn + horizontal right +
    short hook flick UP (with slight leftward lean) at the right terminus."""
    ink = max(1, int(TH * scale))

    # --- Body: same geometry family as shu_wan, slightly shortened tail
    # so the hook has visual room to flick up. ---
    x_top_m = -25 * scale
    y_top_m = 95 * scale
    x_bot_m = -25 * scale
    y_bot_m = -50 * scale
    arc_r = 30 * scale
    x_end_m = 80 * scale         # right terminus of the horizontal
    y_end_m = -80 * scale        # (= y_bot_m - arc_r)

    # Vertical shaft (top -> bottom-of-vertical).
    pa = _to_pixel(ox + x_top_m, oy + y_top_m)
    pb = _to_pixel(ox + x_bot_m, oy + y_bot_m)
    t.line([pa, pb], fill=(0, 0, 0), width=ink)

    # Quarter arc dipping down-right, centered at (x_bot_m+arc_r, y_bot_m).
    turn_cx_m = x_bot_m + arc_r
    turn_cy_m = y_bot_m
    cx_px, cy_px = _to_pixel(ox + turn_cx_m, oy + turn_cy_m)
    steps = 30
    for i in range(steps + 1):
        ang = math.radians(180 - (i / steps) * 90)
        dx = arc_r * math.cos(ang)
        dy_img = arc_r * math.sin(ang)
        px = cx_px + dx
        py = cy_px + dy_img
        r = ink // 2
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # Horizontal segment from arc end to (x_end_m, y_end_m).
    h_start_m_x = x_bot_m + arc_r
    h_start_m_y = y_bot_m - arc_r
    pc = _to_pixel(ox + h_start_m_x, oy + h_start_m_y)
    pd = _to_pixel(ox + x_end_m, oy + y_end_m)
    t.line([pc, pd], fill=(0, 0, 0), width=ink)

    # 顿笔 blob at the corner (arc end) to hide the join per P6.
    r_corner = ink * 0.9
    t.ellipse([pc[0] - r_corner, pc[1] - r_corner,
               pc[0] + r_corner, pc[1] + r_corner], fill=(0, 0, 0))

    # --- Hook: short flick UP with slight leftward lean from (x_end_m, y_end_m).
    # Applies principle P1 (hooks flick up, with a leftward lean).
    # Using the wan_gou hook idiom: quadratic bezier, tapered width.
    p_hook_base_m = (x_end_m, y_end_m)
    p_hook_ctrl_m = (x_end_m - 4 * scale, y_end_m + 18 * scale)
    p_hook_tip_m = (x_end_m - 14 * scale, y_end_m + 34 * scale)

    hook = _qbez(p_hook_base_m, p_hook_ctrl_m, p_hook_tip_m, 20)
    m = len(hook)
    for i in range(m - 1):
        u = i / (m - 1)
        w = 10 - (10 - 2) * u  # taper 10 -> 2
        w_int = max(2, int(round(w * scale)))
        p1 = _to_pixel(ox + hook[i][0], oy + hook[i][1])
        p2 = _to_pixel(ox + hook[i + 1][0], oy + hook[i + 1][1])
        t.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        t.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r],
                  fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    draw = ImageDraw.Draw(img)
    draw_shu_wan_gou(draw, ox=0, oy=0, scale=1.0)
    out_dir = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(out_dir, "01_竖弯钩.png"))


if __name__ == "__main__":
    main()
