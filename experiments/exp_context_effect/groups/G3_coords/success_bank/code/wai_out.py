# generated.py — 外 (wài, outside), 5 strokes.
# Composition: 夕 on the left (3 strokes, bank) + 卜 on the right (2 strokes, inlined thin).
# Revised: 卜 inlined with thin ~5px shu + small pie-like dian to match MMH-thin GT.
import math
import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from xi import draw_xi   # noqa: E402


CANVAS = 300


def _to_pixel(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def _thin_shu(t, xc_math, y_top_math, y_bot_math, thickness=5):
    a = _to_pixel(xc_math, y_top_math)
    b = _to_pixel(xc_math, y_bot_math)
    t.line([a, b], fill=(0, 0, 0), width=thickness)


def _thin_dian(t, x0_m, y0_m, x1_m, y1_m, w_head=3.0, w_tail=8.0, bow_perp=-2.0):
    x0, y0 = _to_pixel(x0_m, y0_m)
    x1, y1 = _to_pixel(x1_m, y1_m)
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
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # 夕 on the left — shifted left of center
    draw_xi(t, ox=-50.0, oy=-5.0, scale=0.90)

    # 卜 on the right — thin tall shu + small dian near top-middle of shu
    # shu: math x=+55, from y=+115 down to y=-115 (tall, slightly right of center)
    _thin_shu(t, xc_math=55, y_top_math=115, y_bot_math=-115, thickness=5)
    # dian: high on the right side of shu, small
    _thin_dian(t, x0_m=65, y0_m=55, x1_m=100, y1_m=15,
               w_head=2.0, w_tail=7.0, bow_perp=-1.5)

    out = os.path.join(os.path.dirname(__file__), "01_外.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
