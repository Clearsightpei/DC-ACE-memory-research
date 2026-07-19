# p1_stroke_29_横折折撇 — G3 (coord-bank) attempt.
# 横折折撇 = 横 (horizontal) + 折 (down turn) + 折 (down-left turn) + 撇 (tapered
# sweep to lower-left). Four connected segments, three corner 顿笔 blobs.
# Coord format only: math-coord (center origin, +y up), converted to PIL pixels
# via _to_pixel. No 米字格, no anchors, no joint specs — numbers only.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _tapered_line(draw, p0, p1, w0, w1, steps=80):
    """Stamped-circle tapered segment (see principle_bank P3, P4)."""
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _bezier_taper(draw, p0, p1, ctrl, w0, w1, steps=80):
    """Quadratic-bezier tapered curve for the final 撇 sweep."""
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_heng_zhe_zhe_pie(draw, ox=0, oy=0, scale=1.0):
    """横折折撇 in one stroke, four connected segments.

    Segment 1: 横  short horizontal, from (-80, +80) to (-10, +80).
    Segment 2: 折  vertical drop, from (-10, +80) to (-10, +30).
    Segment 3: 折  down-left diagonal, from (-10, +30) to (+50, +5).
    Segment 4: 撇  tapered sweep down-left, from (+50, +5) to (-70, -85).
    """
    # Segment 1: 横 — uniform ink (~10 px).
    p1a = _to_pixel(ox + -80 * scale, oy + 80 * scale)
    p1b = _to_pixel(ox + -10 * scale, oy + 80 * scale)
    _tapered_line(draw, p1a, p1b, 10 * scale, 11 * scale, steps=60)

    # 顿笔 at first corner.
    dun1 = _to_pixel(ox + -10 * scale, oy + 80 * scale)
    r1 = 7 * scale
    draw.ellipse([dun1[0] - r1, dun1[1] - r1, dun1[0] + r1, dun1[1] + r1], fill=(0, 0, 0))

    # Segment 2: 折 — short vertical drop.
    p2a = _to_pixel(ox + -10 * scale, oy + 80 * scale)
    p2b = _to_pixel(ox + -10 * scale, oy + 30 * scale)
    _tapered_line(draw, p2a, p2b, 11 * scale, 10 * scale, steps=50)

    # 顿笔 at second corner.
    dun2 = _to_pixel(ox + -10 * scale, oy + 30 * scale)
    r2 = 7 * scale
    draw.ellipse([dun2[0] - r2, dun2[1] - r2, dun2[0] + r2, dun2[1] + r2], fill=(0, 0, 0))

    # Segment 3: 折 — shallow down-right diagonal (this is the second 折 in the
    # compound; it moves right-and-down before flipping into the 撇).
    p3a = _to_pixel(ox + -10 * scale, oy + 30 * scale)
    p3b = _to_pixel(ox + 55 * scale, oy + 10 * scale)
    _tapered_line(draw, p3a, p3b, 10 * scale, 11 * scale, steps=60)

    # 顿笔 at third corner (where 撇 begins).
    dun3 = _to_pixel(ox + 55 * scale, oy + 10 * scale)
    r3 = 8 * scale
    draw.ellipse([dun3[0] - r3, dun3[1] - r3, dun3[0] + r3, dun3[1] + r3], fill=(0, 0, 0))

    # Segment 4: 撇 — long tapered sweep down-left to a needle tip.
    p4a = (ox + 55 * scale, oy + 10 * scale)
    p4b = (ox + -75 * scale, oy + -90 * scale)
    ctrl = (ox + 0 * scale, oy + -55 * scale)  # bow slightly leftward-down.
    a_px = _to_pixel(*p4a)
    b_px = _to_pixel(*p4b)
    c_px = _to_pixel(*ctrl)
    _bezier_taper(draw, a_px, b_px, c_px, 12 * scale, 1.0, steps=90)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_zhe_pie(draw, ox=0, oy=0, scale=1.0)
    out_path = __file__.rsplit("/", 1)[0] + "/01_横折折撇.png"
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
