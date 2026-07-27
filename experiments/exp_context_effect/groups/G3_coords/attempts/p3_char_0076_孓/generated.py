# p3_char_0076_孓 — jué. 3 strokes.
# Structure: 了 (top 横钩 + 弯钩 descender) + a long 横 crossing through mid.
# Compose: reuse draw_liao for the first two strokes, then draw the
# crossing horizontal as a fresh tapered line (starts thin on the left,
# thickens to the right with a small 顿笔).
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from liao import draw_liao  # noqa: E402


def draw_jiao(draw, ox=0, oy=0, scale=1.0):
    # 了 body — canvas-centered, unshifted.
    draw_liao(draw, ox=ox, oy=oy, scale=scale)

    # Horizontal cross stroke — long, spans wider than 了's width,
    # crossing through the descender near its mid-lower region.
    # In liao, the descender wan_gou is offset (+26, -62 scale=0.85);
    # its shaft mid-lower sits ~x=155, y=185 in PIL coords for the
    # default (ox=0, oy=0). We center the cross around there.
    y_cross = 178 + oy
    x_left = 55 + ox
    x_right = 265 + ox

    steps = 30
    w_start, w_end = 4, 9
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x_left + (x_right - x_left) * u0
        xb = x_left + (x_right - x_left) * u1
        # slight downward tilt so it looks handwritten
        ya = y_cross + 2 * u0
        yb = y_cross + 2 * u1
        w = int(w_start + (w_end - w_start) * u0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
    # 顿笔 at right tail
    r = 5
    xt = x_right
    yt = y_cross + 2
    draw.ellipse([xt - r, yt - r, xt + r, yt + r], fill="black")


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_jiao(draw)
    out = os.path.join(_HERE, "01_孓.png")
    img.save(out)


if __name__ == "__main__":
    main()
