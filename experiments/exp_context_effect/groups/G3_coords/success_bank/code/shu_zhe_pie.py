# shu_zhe_pie.py — 竖折撇 (shu zhe pie) coord primitive.
# Compound: 竖 vertical down + 折 short horizontal right + 撇 tapered down-left sweep.
# Extracted from attempts/p1_stroke_27_竖折撇/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stroke_line(t, p0, p1, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_shu_zhe_pie(t, ox=0, oy=0, scale=1.0):
    """竖折撇 = vertical down + rightward horizontal + tapered 撇 sweep."""
    v_top = (ox + -30 * scale, oy + 90 * scale)
    v_bot = (ox + -30 * scale, oy + -55 * scale)
    p1a = _to_pixel(*v_top)
    p1b = _to_pixel(*v_bot)
    _stroke_line(t, p1a, p1b, 12 * scale, 12 * scale, steps=80)

    corner = _to_pixel(ox + -30 * scale, oy + -55 * scale)
    r = 8 * scale
    t.ellipse([corner[0] - r, corner[1] - r,
               corner[0] + r, corner[1] + r], fill=(0, 0, 0))

    h_left = (ox + -30 * scale, oy + -55 * scale)
    h_right = (ox + 30 * scale, oy + -55 * scale)
    p2a = _to_pixel(*h_left)
    p2b = _to_pixel(*h_right)
    _stroke_line(t, p2a, p2b, 12 * scale, 11 * scale, steps=60)

    corner2 = _to_pixel(*h_right)
    r2 = 8 * scale
    t.ellipse([corner2[0] - r2, corner2[1] - r2,
               corner2[0] + r2, corner2[1] + r2], fill=(0, 0, 0))

    x0, y0 = 30.0 * scale, -55.0 * scale
    x1, y1 = -55.0 * scale, -110.0 * scale
    mx = (x0 + x1) / 2.0 - 8.0 * scale
    my = (y0 + y1) / 2.0 + 4.0 * scale

    n_segments = 60
    w_head = max(1.0, 11.0 * scale)
    w_tail = 1.0
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        w = w_head + (w_tail - w_head) * u
        r_i = w / 2.0
        t.ellipse([px - r_i, py - r_i, px + r_i, py + r_i], fill=(0, 0, 0))
