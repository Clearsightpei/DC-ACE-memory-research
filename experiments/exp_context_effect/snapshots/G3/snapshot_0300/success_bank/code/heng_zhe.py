# heng_zhe.py — 横折 (heng zhe, horizontal then 90-deg down) coord primitive.
# Extracted from attempts/p1_stroke_11_横折/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_heng_zhe(t, ox=0, oy=0, scale=1.0):
    """横折 = 横 rightward + 90-deg turn + 竖 downward."""
    ink_w = max(1, int(10 * scale))
    # In math coords (converted from image (60,90)/(230,90)/(230,225)):
    p_h_start = (-90 * scale, 60 * scale)
    p_corner = (80 * scale, 60 * scale)
    p_v_end = (80 * scale, -75 * scale)

    a = _to_pixel(ox + p_h_start[0], oy + p_h_start[1])
    b = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    c = _to_pixel(ox + p_v_end[0], oy + p_v_end[1])

    t.line([a, b], fill=(0, 0, 0), width=ink_w)
    t.line([b, c], fill=(0, 0, 0), width=ink_w)
    r = ink_w // 2
    for pt in (a, b, c):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
