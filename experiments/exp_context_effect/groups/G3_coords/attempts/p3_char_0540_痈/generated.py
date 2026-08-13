# p3_char_0540_痈 — 痈 (yōng, "carbuncle/abscess"), 10 strokes.
# Structure: 疒 (envelope, top-left) + 用 (inside/right).
#
# Compose from two bank primitives:
#   - ne_sick.draw_ne_chuang(D) — 疒 envelope, uses full canvas.
#   - yong_use.draw_yong(D, ox, oy, scale) — 用, scaled and shifted
#     to nestle inside envelope's belly on the right.
#
# Placement: 用 fits under the heng roof, right of the pie shaft.
# GT shows 用 spanning roughly x=[140, 245], y=[100, 245]. Native yong
# spans ~[60, 225] wide × ~[60, 265] tall centered at (150, 150).
# Use scale=0.60, ox=42, oy=25 -> 用 spans ~[128, 234], y=~[121, 240].
import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from ne_sick import draw_ne_chuang  # noqa: E402
from yong_use import draw_yong  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)

    # 疒 envelope, full canvas (as bank primitive was designed).
    draw_ne_chuang(D)

    # 用 nestled inside the envelope on the right.
    draw_yong(D, ox=42, oy=25, scale=0.60)

    out = os.path.join(_HERE, "01_痈.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
