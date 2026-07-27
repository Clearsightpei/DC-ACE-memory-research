# heng_zhe_zhe_pie.py — 横折折撇 coord primitive.
# Four connected segments: 横 + 折(down) + 折(down-right) + 撇 (tapered).
# Extracted from attempts/p1_stroke_29_横折折撇/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _tapered_line(t, p0, p1, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _bezier_taper(t, p0, p1, ctrl, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_heng_zhe_zhe_pie(t, ox=0, oy=0, scale=1.0):
    """横折折撇 in one stroke, four connected segments."""
    p1a = _to_pixel(ox + -80 * scale, oy + 80 * scale)
    p1b = _to_pixel(ox + -10 * scale, oy + 80 * scale)
    _tapered_line(t, p1a, p1b, 10 * scale, 11 * scale, steps=60)

    dun1 = _to_pixel(ox + -10 * scale, oy + 80 * scale)
    r1 = 7 * scale
    t.ellipse([dun1[0] - r1, dun1[1] - r1, dun1[0] + r1, dun1[1] + r1], fill=(0, 0, 0))

    p2a = _to_pixel(ox + -10 * scale, oy + 80 * scale)
    p2b = _to_pixel(ox + -10 * scale, oy + 30 * scale)
    _tapered_line(t, p2a, p2b, 11 * scale, 10 * scale, steps=50)

    dun2 = _to_pixel(ox + -10 * scale, oy + 30 * scale)
    r2 = 7 * scale
    t.ellipse([dun2[0] - r2, dun2[1] - r2, dun2[0] + r2, dun2[1] + r2], fill=(0, 0, 0))

    p3a = _to_pixel(ox + -10 * scale, oy + 30 * scale)
    p3b = _to_pixel(ox + 55 * scale, oy + 10 * scale)
    _tapered_line(t, p3a, p3b, 10 * scale, 11 * scale, steps=60)

    dun3 = _to_pixel(ox + 55 * scale, oy + 10 * scale)
    r3 = 8 * scale
    t.ellipse([dun3[0] - r3, dun3[1] - r3, dun3[0] + r3, dun3[1] + r3], fill=(0, 0, 0))

    p4a = (ox + 55 * scale, oy + 10 * scale)
    p4b = (ox + -75 * scale, oy + -90 * scale)
    ctrl = (ox + 0 * scale, oy + -55 * scale)
    a_px = _to_pixel(*p4a)
    b_px = _to_pixel(*p4b)
    c_px = _to_pixel(*ctrl)
    _bezier_taper(t, a_px, b_px, c_px, 12 * scale, 1.0, steps=90)
