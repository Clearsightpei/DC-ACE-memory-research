# 叉 (cha) — 3 strokes: 横撇 + 捺 (X-cross like 又) + small 点 in upper crook.
# Approach: reuse you_char (又) as the base X-cross, then add a small
# tapered dian inside the upper-left crook.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from you_char import draw_you_char  # noqa: E402
from _shared_helpers import variant_dian  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # Base: 又 character (横撇 + 捺 crossing X). Identity alias from
    # you_char.py — scale 1.15 * 1.0 = larger 又 filling canvas.
    draw_you_char(draw, ox=0, oy=0, scale=1.0)

    # Extra small stroke inside the upper-left crook of 又.
    # GT shows a short thin mark, roughly heng-like / small dian.
    # Coord: math coords, center origin (150, 150), +y up.
    # Upper-left crook of the 又 sits roughly at math (-20, +40) to (+15, +30).
    variant_dian(draw,
                 head=(-30.0, +40.0),
                 tail=(+5.0, +25.0),
                 w_head=2.0, w_tail=4.0, bow_perp=-1.5, n=32)

    out = os.path.join(os.path.dirname(__file__), "01_叉.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
