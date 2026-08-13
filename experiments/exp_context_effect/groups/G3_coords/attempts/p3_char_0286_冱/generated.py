# p3_char_0286_冱 (hù, "freeze/mutual").
# Composition: 冫 (left, ice radical) + 互 (right, mutual).
# G3: bing_char from bank for LEFT, inline PIL for 互.
# Revision 1: bumped 冫 scale so top dot is visible; redrew 互 middle
# as a proper zigzag (𠃍 + 𠃊-hook) instead of a closed rectangle.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from bing_char import draw_bing_char  # noqa: E402


CX, CY = 150, 150


def _px(ox, oy):
    return (CX + ox, CY - oy)


def draw_line(t, p0, p1, w0, w1, n=24):
    x0, y0 = _px(*p0)
    x1, y1 = _px(*p1)
    prev = (x0, y0)
    for i in range(1, n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 * (1 - u) + w1 * u
        w_int = max(1, int(round(w)))
        t.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
        r = w / 2
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_hu_right(t):
    """互 inline. 4 strokes in the right half.
    Layout: top heng, upper 𠃍 (heng+shu), middle 𠃊 (heng+up-tick),
    bottom heng. Occupies x from -10 to +90, y from -75 to +75.
    """
    # (1) Top heng — spans body width
    draw_line(t, (-5, 70), (80, 68), w0=5, w1=6)

    # (2) 横折 upper-left corner: short heng then descend to middle
    #     Start at top-left, cross short, then drop straight down.
    draw_line(t, (-5, 55), (-5, 5), w0=6, w1=6)

    # (3) Middle heng with up-tick (𠃊-shape): long heng across body,
    #     turning up slightly at right end.
    draw_line(t, (-5, 5), (70, 5), w0=5, w1=5)
    draw_line(t, (70, 5), (75, 20), w0=5, w1=3)  # small up-tick

    # (4) Bottom-right corner: from middle-heng right end, drop down,
    #     then bottom heng extends widest.
    draw_line(t, (72, -5), (72, -60), w0=5, w1=5)
    draw_line(t, (-15, -70), (95, -70), w0=6, w1=8)


def draw_char(t):
    # Left: 冫 at larger scale so both dots read clearly. Positioned
    # left of centre. Slight shift up so it sits mid-height.
    draw_bing_char(t, ox=-90, oy=0, scale=0.9)

    # Right: 互 inline
    draw_hu_right(t)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_char(t)
    out = os.path.join(os.path.dirname(__file__), "01_冱.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
