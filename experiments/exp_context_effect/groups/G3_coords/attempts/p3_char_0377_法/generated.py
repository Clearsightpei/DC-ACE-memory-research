# p3_char_0377_法 — 法 (fǎ, law), 8 strokes.
# L-R composition: 氵 (san_dian_shui, 3 strokes, bank) + 去 (5 strokes, inline).
# 去 = 土 top (heng-short + shu + heng-long) + 厶 bottom (撇折 + 点).
#
# Revision 2 (after GT compare):
#  - 氵 scaled up to 0.95 and centered slightly high — GT dots span most
#    of the canvas height on the left third.
#  - Right 去 stretched vertically: top-heng oy=+95, shu 88..30, long
#    heng at oy=+25, 厶 spans oy=+10 down to oy=-95.
#  - Long-heng scale up to 0.65 so it clearly outreaches the top-heng.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from san_dian_shui import draw_san_dian_shui  # noqa: E402
from heng import draw_heng                    # noqa: E402
from shu import draw_shu                      # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_pie_zhe(t, x0, y0, x1, y1, x2, y2, width=9):
    """撇折 = curved 撇 (x0,y0)->(x1,y1) then straight (x1,y1)->(x2,y2)."""
    ctrl_x = (x0 + x1) / 2.0 - 5.0
    ctrl_y = (y0 + y1) / 2.0 + 3.0
    n = 30
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * ctrl_x + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * ctrl_y + u ** 2 * y1
        pt = _to_pixel(bx, by)
        if prev is not None:
            t.line([prev, pt], fill=(0, 0, 0), width=width)
        prev = pt
    p1 = _to_pixel(x1, y1)
    p2 = _to_pixel(x2, y2)
    t.line([p1, p2], fill=(0, 0, 0), width=width)
    r = width / 2
    px, py = p1
    t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_dian_at(t, x0, y0, x1, y1, w_head=3, w_tail=12):
    mx = (x0 + x1) / 2.0 - 3.0
    my = (y0 + y1) / 2.0 - 3.0
    n = 30
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        pt = _to_pixel(bx, by)
        if prev is not None:
            w = w_head * (1 - u) + w_tail * u
            t.line([prev, pt], fill=(0, 0, 0), width=max(1, int(round(w))))
            r = w / 2.0
            t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                      fill=(0, 0, 0))
        prev = pt


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # ---- LEFT: 氵 (bank primitive) ------------------------------------
    # Canonical san_dian_shui at scale=0.95 spans ~140px vertically.
    # Center slightly high so top dot lands around canvas top-quarter.
    draw_san_dian_shui(t, ox=-85.0, oy=-5.0, scale=0.95)

    # ---- RIGHT: 去 (inline) -------------------------------------------
    RX = 40.0  # right-side x-center

    # 1) top short heng
    draw_heng(t, ox=RX, oy=95.0, scale=0.32)   # length 64
    # 2) vertical shu: centered oy=+58, span 88..30 -> length 58
    draw_shu(t, ox=RX, oy=58.0, scale=0.30)
    # 3) long middle heng
    draw_heng(t, ox=RX + 4, oy=22.0, scale=0.68)  # length 136

    # ---- 厶 bottom (撇折 + 点) -----------------------------------------
    # 撇折: starts upper (RX+10, +8), curves down-left to (RX-35, -70),
    # then turns and goes rightward to (RX+38, -70).
    draw_pie_zhe(t,
                 x0=RX + 10, y0=+8,
                 x1=RX - 35, y1=-70,
                 x2=RX + 38, y2=-65,
                 width=9)

    # closing 点: dot to the right, slanting down-right, meets end of the
    # horizontal so the 厶 closes.
    draw_dian_at(t,
                 x0=RX + 35, y0=-45,
                 x1=RX + 60, y1=-75,
                 w_head=3, w_tail=12)

    out = os.path.join(os.path.dirname(__file__), "01_法.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
