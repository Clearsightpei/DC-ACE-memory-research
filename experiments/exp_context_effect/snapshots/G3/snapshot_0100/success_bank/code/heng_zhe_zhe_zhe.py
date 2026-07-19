# heng_zhe_zhe_zhe.py — 横折折折 (heng zhe zhe zhe) coord primitive.
# Four straight tapered segments joined at three 顿笔 corners in a zig-zag.
# Extracted from attempts/p1_stroke_30_横折折折/generated.py after human PASS.

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


def draw_heng_zhe_zhe_zhe(t, ox=0, oy=0, scale=1.0):
    """横折折折 = 横 right + 竖 down + 横 right + 竖 down."""
    p0 = (ox + -95 * scale, oy + 95 * scale)
    p1 = (ox + -10 * scale, oy + 95 * scale)
    p2 = (ox + -10 * scale, oy + 20 * scale)
    p3 = (ox + 75 * scale, oy + 20 * scale)
    p4 = (ox + 75 * scale, oy + -80 * scale)

    px0 = _to_pixel(*p0)
    px1 = _to_pixel(*p1)
    px2 = _to_pixel(*p2)
    px3 = _to_pixel(*p3)
    px4 = _to_pixel(*p4)

    ink_w = 11 * scale

    _stroke_line(t, px0, px1, ink_w, ink_w, steps=90)
    r = 7 * scale
    t.ellipse([px1[0] - r, px1[1] - r, px1[0] + r, px1[1] + r], fill=(0, 0, 0))

    _stroke_line(t, px1, px2, ink_w, ink_w * 0.9, steps=80)
    t.ellipse([px2[0] - r, px2[1] - r, px2[0] + r, px2[1] + r], fill=(0, 0, 0))

    _stroke_line(t, px2, px3, ink_w * 0.95, ink_w, steps=90)
    t.ellipse([px3[0] - r, px3[1] - r, px3[0] + r, px3[1] + r], fill=(0, 0, 0))

    _stroke_line(t, px3, px4, ink_w, ink_w * 0.85, steps=100)
