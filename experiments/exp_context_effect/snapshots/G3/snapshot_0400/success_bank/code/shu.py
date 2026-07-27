# shu.py — 竖 (shu, vertical stroke) coord primitive.
# Extracted from attempts/p1_stroke_02_竖/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 竖 (vertical) stroke centered at (ox, oy) with given scale.

    Canonical unit 竖: length 200 px, thickness 12 px, from top to bottom.
    """
    half_len = 100.0 * scale
    thickness = max(1, int(round(12.0 * scale)))

    x_top, y_top = _to_pixel(ox, oy + half_len)
    x_bot, y_bot = _to_pixel(ox, oy - half_len)

    t.line([(x_top, y_top), (x_bot, y_bot)],
           fill=(0, 0, 0), width=thickness)
