# heng.py — 横 (heng, horizontal stroke) coord primitive.
# Reconstructed after Phase-2 reset parser mishap. The passing attempt
# (attempts/p1_stroke_01_横/generated.py) imports this module and calls
# draw_heng at canvas center; per that attempt's own docstring, the
# canonical unit is a 200 x 12 px horizontal stroke centered on a
# 300x300 canvas. Format mirrors the sibling shu.py: math-coord center
# origin (+y up), converted to PIL pixel coords for rendering.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_heng(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw one 横 (horizontal) stroke centered at (ox, oy) with given scale.

    Canonical unit 横: length 200 px, thickness 12 px, drawn left-to-right.
    """
    half_len = 100.0 * scale
    thickness = max(1, int(round(12.0 * scale)))

    x_left, y_left = _to_pixel(ox - half_len, oy)
    x_right, y_right = _to_pixel(ox + half_len, oy)

    t.line([(x_left, y_left), (x_right, y_right)],
           fill=(0, 0, 0), width=thickness)
