# p1_stroke_27_竖折撇 — 竖折撇
# 竖 (vertical down) + 折 (right-angle horizontal) + 撇 (tapered down-left sweep)
# Coord format (math coords, center origin, +y up), 300x300, PIL.

import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stroke_line(t, p0, p1, w0, w1, steps=80):
    """Tapered line via stamped ellipses from p0 to p1, width w0 -> w1."""
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_shu_zhe_pie(t, ox=0, oy=0, scale=1.0):
    """竖折撇 = vertical down + right-turn horizontal + tapered 撇 sweep."""
    # Segment 1: 竖 vertical down. Uniform ~12 px.
    v_top = (ox + -30 * scale, oy + 90 * scale)
    v_bot = (ox + -30 * scale, oy + -55 * scale)
    p1a = _to_pixel(*v_top)
    p1b = _to_pixel(*v_bot)
    _stroke_line(t, p1a, p1b, 12 * scale, 12 * scale, steps=80)

    # 顿笔 blob at the corner to hide the miter.
    corner = _to_pixel(ox + -30 * scale, oy + -55 * scale)
    r = 8 * scale
    t.ellipse([corner[0] - r, corner[1] - r,
               corner[0] + r, corner[1] + r], fill=(0, 0, 0))

    # Segment 2: 折 short horizontal to the right at the turn.
    h_left = (ox + -30 * scale, oy + -55 * scale)
    h_right = (ox + 30 * scale, oy + -55 * scale)
    p2a = _to_pixel(*h_left)
    p2b = _to_pixel(*h_right)
    _stroke_line(t, p2a, p2b, 12 * scale, 11 * scale, steps=60)

    # Second corner 顿笔 where the 撇 will launch.
    corner2 = _to_pixel(*h_right)
    r2 = 8 * scale
    t.ellipse([corner2[0] - r2, corner2[1] - r2,
               corner2[0] + r2, corner2[1] + r2], fill=(0, 0, 0))

    # Segment 3: 撇 tapered down-left sweep from second corner.
    # Bezier: thick head at corner, tapers to needle tip at lower-left.
    x0, y0 = 30.0 * scale, -55.0 * scale     # head at horizontal's right end
    x1, y1 = -55.0 * scale, -110.0 * scale   # thin lower-left tail
    mx = (x0 + x1) / 2.0 - 8.0 * scale       # bow slightly left
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


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_shu_zhe_pie(draw, ox=0, oy=0, scale=1.0)
    out_path = os.path.join(os.path.dirname(__file__), "01_竖折撇.png")
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
