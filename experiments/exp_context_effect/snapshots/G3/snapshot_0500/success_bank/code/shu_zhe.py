# shu_zhe.py — 竖折 (shu zhe, vertical then turn-right horizontal) primitive.
# Extracted from attempts/p1_stroke_15_竖折/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_zhe(t, ox=0, oy=0, scale=1.0, ink=10):
    """竖折 = vertical down + right-angle turn + horizontal right."""
    v_top = (ox + -30 * scale, oy + 90 * scale)
    v_bottom = (ox + -30 * scale, oy + -70 * scale)
    h_left = (ox + -30 * scale, oy + -70 * scale)
    h_right = (ox + 70 * scale, oy + -70 * scale)

    w = max(1, int(ink * scale))
    t.line([_to_pixel(*v_top), _to_pixel(*v_bottom)], fill=(0, 0, 0), width=w)
    t.line([_to_pixel(*h_left), _to_pixel(*h_right)], fill=(0, 0, 0), width=w)
    r = w // 2
    for pt in (v_top, v_bottom, h_left, h_right):
        px, py = _to_pixel(*pt)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
