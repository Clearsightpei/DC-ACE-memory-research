# wo_gou.py — 卧钩 (wo gou, lying hook) coord primitive.
# Extracted from attempts/p1_stroke_08_卧钩/generated.py after human PASS.
# Original was in raw PIL image coords; converted to math coords
# (center origin, +y up) for consistency with the rest of the bank.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_wo_gou(t, ox=0, oy=0, scale=1.0):
    """卧钩: shallow lying arc dipping down-right, then hook up-left."""
    # arc points in math coords, +y up
    arc = [
        (-72,  -10),
        (-55,    0),
        (-35,    8),
        (-15,   18),
        (  5,   26),
        ( 25,   32),
        ( 45,   36),
        ( 60,   37),
        ( 68,   35),
    ]
    widths_body = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i in range(len(arc) - 1):
        p1 = _to_pixel(ox + arc[i][0] * scale, oy - arc[i][1] * scale)
        p2 = _to_pixel(ox + arc[i + 1][0] * scale, oy - arc[i + 1][1] * scale)
        w = int(round(widths_body[i] * scale))
        w = max(1, w)
        t.line([p1, p2], fill=(0, 0, 0), width=w)
        t.ellipse([p2[0] - w / 2, p2[1] - w / 2,
                   p2[0] + w / 2, p2[1] + w / 2], fill=(0, 0, 0))

    hook = [(68, 35), (62, 22), (55, 10)]
    widths_hook = [10, 7, 3]
    for i in range(len(hook) - 1):
        p1 = _to_pixel(ox + hook[i][0] * scale, oy - hook[i][1] * scale)
        p2 = _to_pixel(ox + hook[i + 1][0] * scale, oy - hook[i + 1][1] * scale)
        w = int(round(widths_hook[i] * scale))
        w = max(1, w)
        t.line([p1, p2], fill=(0, 0, 0), width=w)
        t.ellipse([p2[0] - w / 2, p2[1] - w / 2,
                   p2[0] + w / 2, p2[1] + w / 2], fill=(0, 0, 0))
