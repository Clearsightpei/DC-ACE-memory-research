# heng_pie.py — 横撇 (heng pie) coord primitive.
# Compound: 横 (horizontal with slight rise) + sharp turn down-left as 撇.
# Extracted from attempts/p1_stroke_09_横撇/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_heng_pie(t, ox=0, oy=0, scale=1.0):
    """横撇 = short horizontal with subtle rise, then sharp 撇 down-left."""
    # Coords in math (center-origin, +y up). Converted from the passing PIL
    # image-coord layout: heng_start=(70,110)->math(-80,+40); heng_end=(215,100)->math(+65,+50).
    heng_start = (-80 * scale, 40 * scale)
    heng_end = (65 * scale, 50 * scale)
    corner = (68 * scale, 47 * scale)

    p_start = _to_pixel(ox + heng_start[0], oy + heng_start[1])
    p_end = _to_pixel(ox + heng_end[0], oy + heng_end[1])
    t.line([p_start, p_end], fill=(0, 0, 0), width=max(1, int(8 * scale)))

    # small 顿笔 blob at the turn
    p_c = _to_pixel(ox + corner[0], oy + corner[1])
    r = max(3, int(7 * scale))
    t.ellipse([p_c[0] - r, p_c[1] - r, p_c[0] + r + 1, p_c[1] + r + 2],
              fill=(0, 0, 0))

    # 撇 segment (down-left, tapered)
    pie_start = (68 * scale, 42 * scale)
    pie_end = (-15 * scale, -85 * scale)
    steps = 24
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        x0 = pie_start[0] + (pie_end[0] - pie_start[0]) * u0
        y0 = pie_start[1] + (pie_end[1] - pie_start[1]) * u0
        x1 = pie_start[0] + (pie_end[0] - pie_start[0]) * u1
        y1 = pie_start[1] + (pie_end[1] - pie_start[1]) * u1
        w = max(1, int(round((10 - 9 * u0) * scale)))
        p0 = _to_pixel(ox + x0, oy + y0)
        p1 = _to_pixel(ox + x1, oy + y1)
        t.line([p0, p1], fill=(0, 0, 0), width=w)
