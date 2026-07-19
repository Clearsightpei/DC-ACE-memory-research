# heng_zhe_ti.py — 橫折提 (heng zhe ti) coord primitive.
# Compound: 横 (horizontal, slight rise) + 折 (short drop) + 提 (rising flick).
# Extracted from attempts/p1_stroke_20_橫折提/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stroke_line(t, p0, p1, w0, w1, steps=60):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_heng_zhe_ti(t, ox=0, oy=0, scale=1.0):
    """橫折提 = horizontal + downward turn + rising flick."""
    # In math coords (center origin), converted from the PIL pass layout.
    # Segment 1: 横 from (-90, +48) to (+60, +54); slight upward tilt.
    p1a = _to_pixel(ox + -90 * scale, oy + 48 * scale)
    p1b = _to_pixel(ox + 60 * scale, oy + 54 * scale)
    _stroke_line(t, p1a, p1b, 9 * scale, 11 * scale, steps=80)
    dun = _to_pixel(ox + 60 * scale, oy + 54 * scale)
    r = 8 * scale
    t.ellipse([dun[0] - r, dun[1] - r, dun[0] + r, dun[1] + r], fill=(0, 0, 0))

    # Segment 2: 折 short vertical drop, slightly left-leaning.
    p2a = _to_pixel(ox + 64 * scale, oy + 58 * scale)
    p2b = _to_pixel(ox + 54 * scale, oy + -18 * scale)
    _stroke_line(t, p2a, p2b, 12 * scale, 9 * scale, steps=60)

    # Segment 3: 提 rising flick up-right, tapered.
    p3a = _to_pixel(ox + 54 * scale, oy + -18 * scale)
    p3b = _to_pixel(ox + 108 * scale, oy + 20 * scale)
    _stroke_line(t, p3a, p3b, 11 * scale, 2 * scale, steps=80)
