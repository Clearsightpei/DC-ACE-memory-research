# p1_stroke_30_横折折折 — heng-zhe-zhe-zhe
# 4 segments, 3 corners: 横 rightward -> 折 down -> 折 rightward -> 折 down.
# PIL, coord format (math convention, center origin, +y up), 300x300.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stroke_line(draw, p0, p1, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_heng_zhe_zhe_zhe(draw, ox=0, oy=0, scale=1.0):
    """横折折折 = 横 right + 竖 down + 横 right + 竖 down.
    Four straight tapered segments joined at three 顿笔 corners.
    Occupies most of the canvas as a zig-zag shape."""

    # Anchors in math coords (center origin, +y up).
    p0 = (ox + -95 * scale, oy + 95 * scale)   # top-left start
    p1 = (ox + -10 * scale, oy + 95 * scale)   # first corner (top)
    p2 = (ox + -10 * scale, oy + 20 * scale)   # second corner (mid-left of second heng)
    p3 = (ox + 75 * scale, oy + 20 * scale)    # third corner
    p4 = (ox + 75 * scale, oy + -80 * scale)   # bottom-right end

    px0 = _to_pixel(*p0)
    px1 = _to_pixel(*p1)
    px2 = _to_pixel(*p2)
    px3 = _to_pixel(*p3)
    px4 = _to_pixel(*p4)

    ink_w = 11 * scale

    # Segment 1: 横 (top horizontal, uniform width).
    _stroke_line(draw, px0, px1, ink_w, ink_w, steps=90)

    # Corner 1 顿笔.
    r = 7 * scale
    draw.ellipse([px1[0] - r, px1[1] - r, px1[0] + r, px1[1] + r], fill=(0, 0, 0))

    # Segment 2: 竖 (down), slight taper end.
    _stroke_line(draw, px1, px2, ink_w, ink_w * 0.9, steps=80)

    # Corner 2 顿笔.
    draw.ellipse([px2[0] - r, px2[1] - r, px2[0] + r, px2[1] + r], fill=(0, 0, 0))

    # Segment 3: 横 (mid horizontal).
    _stroke_line(draw, px2, px3, ink_w * 0.95, ink_w, steps=90)

    # Corner 3 顿笔.
    draw.ellipse([px3[0] - r, px3[1] - r, px3[0] + r, px3[1] + r], fill=(0, 0, 0))

    # Segment 4: 竖 (final down), slight taper to a slightly rounded foot.
    _stroke_line(draw, px3, px4, ink_w, ink_w * 0.85, steps=100)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_zhe_zhe(draw, ox=0, oy=0, scale=1.0)
    import os
    out_path = os.path.join(os.path.dirname(__file__), "01_横折折折.png")
    img.save(out_path, "PNG")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
