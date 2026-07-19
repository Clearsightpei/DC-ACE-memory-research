# p1_stroke_26_横折折 — 横折折 (heng zhe zhe)
# Structure: horizontal (heng) -> turn 90 deg down (zhe) -> turn 90 deg
# right / horizontal again (second zhe). Ends flat, no hook.
# Coord format per G3 (numeric offsets, math coords, PIL rendering).
# Reuses idiom from heng_zhe.py (P6: concatenated tapered segments
# with 顿笔 blobs at corners).

import os
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


def draw_heng_zhe_zhe(draw, ox=0, oy=0, scale=1.0):
    """横折折 = 横 rightward + 90-deg turn down + 90-deg turn right (horizontal)."""
    # 横折折 = 横 + 竖(短) + 横. Step-down shape like ⌐ then across.
    # Segment 1: top 横 (horizontal). Left to right, upper area.
    p1a = _to_pixel(ox + -80 * scale, oy + 75 * scale)
    p1b = _to_pixel(ox + 70 * scale, oy + 75 * scale)
    _stroke_line(draw, p1a, p1b, 11 * scale, 12 * scale, steps=90)
    # 顿笔 at first corner
    r1 = 8 * scale
    dun1 = _to_pixel(ox + 70 * scale, oy + 75 * scale)
    draw.ellipse([dun1[0] - r1, dun1[1] - r1, dun1[0] + r1, dun1[1] + r1], fill=(0, 0, 0))

    # Segment 2: first 折 -> downward vertical drop (short 竖).
    p2a = _to_pixel(ox + 70 * scale, oy + 75 * scale)
    p2b = _to_pixel(ox + 70 * scale, oy + -40 * scale)
    _stroke_line(draw, p2a, p2b, 12 * scale, 11 * scale, steps=80)
    # 顿笔 at second corner
    r2 = 8 * scale
    dun2 = _to_pixel(ox + 70 * scale, oy + -40 * scale)
    draw.ellipse([dun2[0] - r2, dun2[1] - r2, dun2[0] + r2, dun2[1] + r2], fill=(0, 0, 0))

    # Segment 3: second 折 -> bottom 横 running rightward, ending flat.
    p3a = _to_pixel(ox + 70 * scale, oy + -40 * scale)
    p3b = _to_pixel(ox + -50 * scale, oy + -40 * scale)
    _stroke_line(draw, p3a, p3b, 11 * scale, 12 * scale, steps=90)
    # End 顿笔 (flat foot, no hook)
    r3 = 7 * scale
    end = _to_pixel(ox + -50 * scale, oy + -40 * scale)
    draw.ellipse([end[0] - r3, end[1] - r3, end[0] + r3, end[1] + r3], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_zhe(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_横折折.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
