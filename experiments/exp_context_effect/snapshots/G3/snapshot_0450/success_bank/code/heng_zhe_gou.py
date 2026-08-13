# heng_zhe_gou.py — 横折钩 (heng zhe gou) coord primitive.
# Compound: 横 + 90-deg turn down + short up-and-left hook at the base.
# Extracted verbatim from attempts/p1_stroke_22_横折钩/generated.py after human PASS.

from PIL import ImageDraw  # noqa: F401  (imported for type-hinting clarity)

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=20, ox=0, oy=0):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def draw_heng_zhe_gou(t, ox=0, oy=0, scale=1.0):
    """横折钩 = 横 (horizontal) + 折 (90-deg down) + short up-and-left 钩 at base."""
    p_h_start = (-90 * scale, 60 * scale)
    p_corner = (80 * scale, 60 * scale)
    p_v_end = (80 * scale, -70 * scale)

    _tapered_segment(t, p_h_start, p_corner, 10 * scale, 12 * scale, steps=24, ox=ox, oy=oy)

    r = int(8 * scale)
    cx, cy = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    _tapered_segment(t, p_corner, p_v_end, 12 * scale, 11 * scale, steps=24, ox=ox, oy=oy)

    h_base = (p_v_end[0] + 1 * scale, p_v_end[1] + 2 * scale)
    h_tip = (p_v_end[0] - 22 * scale, p_v_end[1] + 22 * scale)
    _tapered_segment(t, h_base, h_tip, 11 * scale, 2 * scale, steps=16, ox=ox, oy=oy)

    br = int(6 * scale)
    bx, by = _to_pixel(ox + p_v_end[0], oy + p_v_end[1])
    t.ellipse([bx - br, by - br, bx + br, by + br], fill=(0, 0, 0))
