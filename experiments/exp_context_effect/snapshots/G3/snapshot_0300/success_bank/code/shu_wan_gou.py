# shu_wan_gou.py — 竖弯钩 (shu wan gou, vertical curve + hook) coord primitive.
# Reconstructed after Phase-2 restart file surgery. Originally graduated
# from batch-3 retry (p1_stroke_23_竖弯钩) after batch-2 FAIL.

import math

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_wan_gou(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 竖弯钩: vertical shaft descending, curving right, ending with an upward hook.

    Canonical unit: shaft ~80 px down, curve arc radius ~40 px, tail
    horizontal ~60 px, upward hook ~22 px. Thickness 12 px.
    """
    thickness = max(1, int(round(12.0 * scale)))

    # Vertical shaft — from (ox, oy+70*s) down to (ox, oy-30*s)
    shaft_top = (ox, oy + 70.0 * scale)
    shaft_bot = (ox, oy - 30.0 * scale)
    x0, y0 = _to_pixel(*shaft_top)
    x1, y1 = _to_pixel(*shaft_bot)
    t.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=thickness)

    # Quarter-circle arc — center at (ox+40*s, oy-30*s), radius 40*s
    # From angle 180° (arc start = shaft bottom) to 270° (arc bottom-right point)
    arc_cx = ox + 40.0 * scale
    arc_cy = oy - 30.0 * scale
    r = 40.0 * scale
    n_arc = 12
    prev = None
    for i in range(n_arc + 1):
        u = i / n_arc
        angle = math.pi + u * (math.pi / 2)  # 180° -> 270°
        px = arc_cx + r * math.cos(angle)
        py = arc_cy + r * math.sin(angle)
        curr = _to_pixel(px, py)
        if prev is not None:
            t.line([prev, curr], fill=(0, 0, 0), width=thickness)
        prev = curr

    # Tail horizontal — from arc end (ox+40*s, oy-70*s) to (ox+80*s, oy-70*s)
    tail_start = (ox + 40.0 * scale, oy - 70.0 * scale)
    tail_end = (ox + 80.0 * scale, oy - 70.0 * scale)
    xs, ys = _to_pixel(*tail_start)
    xe, ye = _to_pixel(*tail_end)
    t.line([(xs, ys), (xe, ye)], fill=(0, 0, 0), width=thickness)

    # Upward hook — from tail end up-and-slightly-left, tapered
    hook_base = tail_end
    hook_tip = (ox + 75.0 * scale, oy - 48.0 * scale)
    n_seg = 8
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((thickness - 2) * (1 - (u0 + u1) / 2) + 2)))
        a, b = _to_pixel(*p0)
        c, d = _to_pixel(*p1)
        t.line([(a, b), (c, d)], fill=(0, 0, 0), width=w)
