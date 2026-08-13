# generated.py — 卞 (biàn), 4 strokes: 丶(top) + 一 + 丨 + 丶(right).
# Inline PIL thin recipe adapted from bu_char.py (不). Top dot sits
# above heng center-left; heng spans top; shu descends from heng center;
# right dot near the shu midpoint.
import math
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_卞.png")

img = Image.new("RGB", (300, 300), "white")
t = ImageDraw.Draw(img)


def _to_pixel(mx, my):
    return 150 + mx, 150 - my


def _heng(xc, yc, half_len, thickness):
    xL, yL = _to_pixel(xc - half_len, yc)
    xR, yR = _to_pixel(xc + half_len, yc)
    t.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=thickness)


def _shu(xc, yc, half_len, thickness):
    xT, yT = _to_pixel(xc, yc + half_len)
    xB, yB = _to_pixel(xc, yc - half_len)
    t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=thickness)


def _dian(x0, y0, x1, y1, w_head, w_tail, bow_perp=-2.0):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = (x0 + x1) / 2.0 + perp_x * bow_perp
    my = (y0 + y1) / 2.0 + perp_y * bow_perp
    n = 40
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


# Stroke 1: top dian (sits above heng, slightly left of center, curving down-right).
_dian(-15, 95, 8, 65, w_head=3.0, w_tail=7.0, bow_perp=-2.0)

# Stroke 2: 横 spanning the middle-upper area.
_heng(0, 40, 105, thickness=6)

# Stroke 3: 竖 descending from heng center down through lower canvas.
_shu(0, -40, 80, thickness=6)

# Stroke 4: right dian below the heng, right of shu midpoint (curving down-right).
_dian(18, 5, 55, -40, w_head=3.0, w_tail=8.0, bow_perp=-2.0)

img.save(OUT)
print(f"wrote {OUT}")
