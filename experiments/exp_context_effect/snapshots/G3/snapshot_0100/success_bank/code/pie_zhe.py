# pie_zhe.py — 撇折 (pie zhe, pie then turn horizontal) coord primitive.
# Extracted from attempts/p1_stroke_18_撇折/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_pie_zhe(t, ox=0, oy=0, scale=1.0, ink=10):
    """撇折 = 撇 diagonal down-left + 横 horizontal right at the turn."""
    p_top = (ox + 40 * scale, oy + 80 * scale)
    p_bot = (ox + -40 * scale, oy + -50 * scale)
    h_left = (ox + -40 * scale, oy + -50 * scale)
    h_right = (ox + 60 * scale, oy + -50 * scale)

    w = max(1, int(ink * scale))
    t.line([_to_pixel(*p_top), _to_pixel(*p_bot)], fill=(0, 0, 0), width=w)
    t.line([_to_pixel(*h_left), _to_pixel(*h_right)], fill=(0, 0, 0), width=w)
    r = w // 2
    for pt in (p_top, p_bot, h_left, h_right):
        px, py = _to_pixel(*pt)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
