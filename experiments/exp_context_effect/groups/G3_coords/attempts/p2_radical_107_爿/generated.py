# p2_radical_107_爿 — G3 coord attempt.
#
# GT observation (thin-brush, hand-drawn style):
#   - S1: 撇 stroke — top-LEFT curved sweep, from around (~-25, +55) curving
#         down-left to (~-70, +15). Prominent, thin.
#   - S2: short 横 — top horizontal, meeting the pie tail on left and going
#         right toward the top of the long vertical (~-50, +50) to (~+45, +55).
#   - S3: 竖 — short vertical dropping from the middle-left of the top-horiz,
#         from (~-35, +45) down to (~-35, -25).
#   - S4: 横 or 提 — bottom horizontal from (~-70, -55) to (~+55, -50).
#   - Plus long right 竖 — from (~+45, +100) down to (~+45, -95).
# 爿 is nominally 4 strokes in MMH; the top-horiz + short-vertical merge into
# one 横折 stroke, and the bottom-horiz + long-right-vertical is drawn as two
# marks but count as two strokes total for the character. Standard order:
#   1) 撇 (top-left)
#   2) 横折 (top-horiz + short-drop) — one L-shape stroke
#   3) 竖 (long right vertical)
#   4) 横 (bottom)
# Alternate 4-stroke reading: pie / heng / short-shu / heng — with long right
# vertical being the "shu" in position 3.
# I'll draw all five visible marks with thin taper matching GT's thinness.
#
# All coords: PIL 300x300, math-coord helper (center origin, +y up).

from PIL import Image, ImageDraw
import os

CANVAS_SIZE = 300

def _to_pixel(ox, oy):
    """math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_tapered_line(draw, p0, p1, w_start, w_end, n=40):
    x0, y0 = p0
    x1, y1 = p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w_start + (w_end - w_start) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_tapered_bezier(draw, p0, ctrl, p1, w_start, w_end, n=50):
    x0, y0 = p0
    cx, cy = ctrl
    x1, y1 = p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        w = w_start + (w_end - w_start) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    draw = ImageDraw.Draw(img)

    # ---- S1: top-left 撇 (prominent thin curve, upper-left) ----
    # Head at ~(-15, +55), tail at (-75, +10). Bowed left.
    p0 = _to_pixel(-15, 60)
    ctrl = _to_pixel(-50, 45)
    p1 = _to_pixel(-75, 15)
    draw_tapered_bezier(draw, p0, ctrl, p1, w_start=5, w_end=2, n=50)

    # ---- S2: top 横 (short horizontal, top of the box) ----
    # From near S1's tail region rightward to top of long vertical.
    top_left = _to_pixel(-55, 50)
    top_right = _to_pixel(45, 55)
    draw_tapered_line(draw, top_left, top_right, w_start=4, w_end=5, n=40)

    # ---- S3: short 竖 (left inner vertical, drops from top horizontal) ----
    v_top = _to_pixel(-40, 45)
    v_bot = _to_pixel(-40, -30)
    draw_tapered_line(draw, v_top, v_bot, w_start=5, w_end=4, n=40)

    # ---- S4: bottom 横 (long, spans left to right side) ----
    bh_left = _to_pixel(-75, -55)
    bh_right = _to_pixel(55, -50)
    draw_tapered_line(draw, bh_left, bh_right, w_start=4, w_end=5, n=40)

    # ---- Long right 竖 (tall, right side, spans nearly full height) ----
    rv_top = _to_pixel(45, 105)
    rv_bot = _to_pixel(45, -95)
    draw_tapered_line(draw, rv_top, rv_bot, w_start=5, w_end=4, n=60)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_爿.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
