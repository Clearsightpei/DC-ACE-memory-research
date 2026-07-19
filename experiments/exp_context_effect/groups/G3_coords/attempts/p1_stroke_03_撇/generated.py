# attempts/p1_stroke_03_撇/generated.py
#
# 撇 (pie) — a tapered sweep from upper-right to lower-left.
# Uses the shared draw_pie primitive from the success bank.

import os
import sys

from PIL import Image, ImageDraw

# Allow importing the success_bank primitive.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402


CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Canonical placement: centered at origin, unit scale.
    draw_pie(draw, ox=0, oy=0, scale=1.0)

    out = os.path.join(_HERE, "01_撇.png")
    img.save(out, "PNG")
    print(out)


if __name__ == "__main__":
    main()
