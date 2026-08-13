# generated.py — 合 (he), Phase-3 character, 6 strokes.
# Composition: 亼 top (人-roof + 一, bank ji_meet_char) + 口 bottom (bank kou).
#
# GT observation: wide roof (人) at top, short inner 一 sitting just below
# apex, then a medium 口 sitting under the base heng. Thin uniform ink.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ji_meet_char import draw_ji_meet_char  # noqa: E402
from kou import draw_kou                    # noqa: E402

CANVAS = 300


def draw_he(t, ox=0, oy=0, scale=1.0):
    """合 (he): 亼 top + 口 bottom."""
    # 亼 top-half — 人 roof + short heng underneath.
    # Bump scale to 0.68 (roof needs to be visually dominant in 合) and
    # position oy=+18 so apex sits at ~+69 and base heng at ~-47.
    draw_ji_meet_char(t,
                      ox=ox + 0 * scale,
                      oy=oy + 18 * scale,
                      scale=0.68 * scale)

    # 口 bottom — sits directly under the base heng of 亼 (no big gap).
    # scale 0.60 → ±30. Position oy=-78 → top -48, bottom -108 — tucks
    # right under the base heng at -47.
    draw_kou(t,
             ox=ox + 0 * scale,
             oy=oy + (-78) * scale,
             scale=0.60 * scale)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_he(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_合.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
