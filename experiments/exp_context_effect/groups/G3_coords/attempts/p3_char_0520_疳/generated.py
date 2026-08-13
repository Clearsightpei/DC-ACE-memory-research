# p3_char_0520_疳 — 疳 = 疒 (envelope, top+left) + 甘 (inside belly).
#
# Uses bank primitive ne_sick.draw_ne_chuang for the 疒 envelope (this
# is exactly what the GT shows for the outer envelope: heng roof, top
# dot, long descending pie, two interior 冫 marks). The pie sweeps
# left; the belly cavity is right of the pie, below the heng.
#
# 甘 is inlined into that belly cavity — small enough to sit clear of
# the pie shaft (which is at x≈130 at y=155 down to x≈85 at y=278).
# 甘 layout: top heng, left shu, right shu, middle heng, bottom heng.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(
    os.path.join(_HERE, "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ne_sick import draw_ne_chuang  # noqa: E402


def _tapered_line(draw, p0, p1, w_head, w_tail, n=24):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_gan_inside(draw, x0=155, x1=240, y0=150, y1=258):
    """Inline 甘 inside the 疒 belly. Box aspect wider than tall."""
    # Stroke 1: top heng
    _tapered_line(draw, (x0, y0), (x1, y0 - 2), w_head=5.0, w_tail=4.5, n=26)
    # Stroke 2: left shu (slightly slanted-in top→bottom)
    _tapered_line(draw, (x0 + 3, y0), (x0, y1), w_head=5.0, w_tail=4.5, n=26)
    # Stroke 3: right shu (as 竖折 turning inward at bottom via bottom heng)
    _tapered_line(draw, (x1, y0 - 2), (x1 - 4, y1 - 2), w_head=5.0, w_tail=4.5, n=26)
    # Stroke 4: middle heng (short, inside the box)
    ymid = int((y0 + y1) / 2) + 2
    _tapered_line(draw, (x0 + 14, ymid), (x1 - 14, ymid - 1),
                  w_head=4.0, w_tail=3.5, n=22)
    # Stroke 5: bottom heng (closes the box)
    _tapered_line(draw, (x0, y1), (x1 - 4, y1 - 2), w_head=5.0, w_tail=4.5, n=26)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_chuang(draw)
    draw_gan_inside(draw)
    out = os.path.join(_HERE, "01_疳.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
