# p3_char_0006_乚 — draw 乚 as a standalone character (300x300 PNG).
# 乚 is a single 竖弯钩-family sweep. It coincides with the already-mastered
# radical `ya_radical` (INDEX #32), which wraps shu_wan_gou at
# (ox=-45, oy=-12, scale=1.2). For a standalone character we want it a
# touch more centered on the canvas than the radical bootstrap render
# (the GT shows the shape occupying most of the canvas), so we pass a
# small extra offset via (ox, oy) to place it more centrally.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ya_radical import draw_ya_radical  # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    # Revision: first render at scale=1.0 was too small vs GT (GT shape
    # spans most of canvas, shaft ~from y=75 down to y=225, tail extending
    # to x~225). Bump scale to 1.5 and shift left/down to match GT footprint.
    # ya_radical internally offsets by (-45,-12) then scales shu_wan_gou 1.2×;
    # composite ox/oy here is applied on the outer origin.
    draw_ya_radical(t, ox=15.0, oy=-5.0, scale=1.5)
    out = os.path.join(_HERE, "01_乚.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
