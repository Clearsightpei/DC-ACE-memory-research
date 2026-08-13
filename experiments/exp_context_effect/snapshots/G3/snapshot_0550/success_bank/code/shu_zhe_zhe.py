# shu_zhe_zhe.py — 竖折折 (shu zhe zhe) coord primitive.
# Three joined tapered segments with 顿笔 blobs at every vertex.
# Extracted from attempts/p1_stroke_28_竖折折/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_zhe_zhe(t, ox=0, oy=0, scale=1.0, ink=10):
    """竖折折 = vertical down + rightward + downward again."""
    p1 = (ox + -55 * scale, oy + 90 * scale)
    p2 = (ox + -55 * scale, oy + 10 * scale)
    p3 = (ox + 55 * scale, oy + 10 * scale)
    p4 = (ox + 55 * scale, oy + -80 * scale)

    w = max(1, int(ink * scale))
    t.line([_to_pixel(*p1), _to_pixel(*p2)], fill=(0, 0, 0), width=w)
    t.line([_to_pixel(*p2), _to_pixel(*p3)], fill=(0, 0, 0), width=w)
    t.line([_to_pixel(*p3), _to_pixel(*p4)], fill=(0, 0, 0), width=w)

    r = w // 2
    for pt in (p1, p2, p3, p4):
        px, py = _to_pixel(*pt)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
