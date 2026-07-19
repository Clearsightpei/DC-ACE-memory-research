# shu_ti.py — 竖提 (shu ti, vertical then flick up-right) coord primitive.
# Extracted from attempts/p1_stroke_12_竖提/generated.py after human PASS.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_ti(t, ox=0, oy=0, scale=1.0):
    """竖提 = vertical descending + tapered flick up-right."""
    # Converted from image-coord layout (150,55)->(150,235) then flick to (245,175).
    shu_top = (0 * scale, 95 * scale)
    shu_bot = (0 * scale, -85 * scale)
    ti_start = (0 * scale, -85 * scale)
    ti_end = (95 * scale, -25 * scale)

    stroke_w = max(1, int(14 * scale))
    p_a = _to_pixel(ox + shu_top[0], oy + shu_top[1])
    p_b = _to_pixel(ox + shu_bot[0], oy + shu_bot[1])
    t.line([p_a, p_b], fill=(0, 0, 0), width=stroke_w)
    # rounded top head
    r = stroke_w // 2
    t.ellipse([p_a[0] - r, p_a[1] - 6, p_a[0] + r, p_a[1] + 6], fill=(0, 0, 0))

    # ti flick
    n_seg = 24
    for i in range(n_seg):
        f0 = i / n_seg
        f1 = (i + 1) / n_seg
        xa = ti_start[0] + (ti_end[0] - ti_start[0]) * f0
        ya = ti_start[1] + (ti_end[1] - ti_start[1]) * f0
        xb = ti_start[0] + (ti_end[0] - ti_start[0]) * f1
        yb = ti_start[1] + (ti_end[1] - ti_start[1]) * f1
        w = max(1, int(round(13 * (1 - f0) + 1 * f0)))
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        t.line([pa, pb], fill=(0, 0, 0), width=w)
