# generated.py — 只 (zhi), Phase-3 character, 5 strokes.
# Composition: 口 on top (bank kou at scale ~0.55) + 八 splayed wide below
# (bank ba at scale ~0.75 for the wider 八 legs of 只).
#
# GT observation: kou is a medium-sized box in the upper half. Below it,
# two long divergent strokes (pie left-down, na/dian right-down) that
# spread wider than 八 alone — spanning the character's full width.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from kou import draw_kou  # noqa: E402
from ba import draw_ba    # noqa: E402

CANVAS = 300


def draw_zhi(t, ox=0, oy=0, scale=1.0):
    """只 (zhi).

    口 in upper half: scale 0.55, oy ≈ +35 (sits above center).
    八 below the box: scale 0.90, oy ≈ -55 (splayed feet spanning wider).
    """
    # kou (口) in upper half, larger box
    draw_kou(t,
             ox=ox + 0 * scale,
             oy=oy + 40 * scale,
             scale=0.65 * scale)

    # ba (八) below with clear gap and legs spanning full width
    draw_ba(t,
            ox=ox + 0 * scale,
            oy=oy + (-75) * scale,
            scale=1.00 * scale)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_zhi(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_只.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
