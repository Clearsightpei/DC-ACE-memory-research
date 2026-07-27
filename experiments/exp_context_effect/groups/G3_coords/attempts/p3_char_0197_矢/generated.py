# p3_char_0197_矢 (shǐ, "arrow"), 5 strokes.
# Inline-fresh: short top pie + short heng + longer heng + long pie + long na.
# Bottom composition is a 大-family pie×na crossing at ~(150, 148).

from PIL import Image, ImageDraw

CANVAS = 300


def _stamp(d, prev, p, w):
    wi = max(1, int(round(w)))
    d.line([prev, p], fill=(0, 0, 0), width=wi)
    r = w / 2.0
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))


def _line(d, p0, p1, w0, w1, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        p = (p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u)
        w = w0 + (w1 - w0) * u
        if prev is not None:
            _stamp(d, prev, p, w)
        prev = p


def _bez(d, p0, p1, p2, w_head, w_tail, n=60, belly_pos=1.0, w_belly=None):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        p = (bx, by)
        if prev is not None:
            _stamp(d, prev, p, w)
        prev = p


def draw_shi_arrow(d, ox=0, oy=0, scale=1.0):
    """矢, 5 strokes, PIL pixel coords."""
    # 1. Short top pie: tick going down-left, upper center area
    _bez(d, (158, 58), (145, 75), (125, 92), w_head=5, w_tail=1, n=30)
    # 2. Short upper heng: attaches to right of the pie's base
    _line(d, (115, 102), (205, 96), 5, 5, n=30)
    # 3. Longer middle heng: main horizontal, sits well below the top heng
    _line(d, (68, 158), (232, 154), 6, 6, n=40)
    # 4. Long pie: from just above middle heng, curves down-left
    _bez(d, (152, 150), (118, 205), (68, 270),
         w_head=7, w_tail=1, n=60)
    # 5. Long na: from crossing point at ~(150, 156), sweeps down-right (thinner)
    _bez(d, (150, 156), (185, 210), (248, 272),
         w_head=2, w_tail=3, belly_pos=0.75, w_belly=8, n=60)


img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)
draw_shi_arrow(d)
img.save("01_矢.png")
