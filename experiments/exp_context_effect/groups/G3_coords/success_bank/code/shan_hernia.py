# shan_hernia.py — 疝 — promoted from p3_char_0378_疝 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# p3_char_0378_疝 (shàn) — 疒 envelope + 山 (mountain) interior.
#
# Composition: 疒 wraps top+left; 山 sits in the lower-right belly.
# GT decomposition (from gt/phase3/疝.png):
#   1. 疒: top-right small dot, thin heng roof, long left-descending 撇,
#      two 冫 marks (upper 点 + lower 提) tucked inside upper-left belly.
#   2. 山: middle tall 竖 + 竖折 (left+base) + short right 竖, positioned
#      in the belly (roughly right of pie shaft, below heng).
#
# Bank reuse:
#   - Envelope: reuse draw_ne_chuang from ne_sick.py (v9 rerun graduate).
#     Its coords fit the full canvas well.
#   - Interior 山: inline (bank shan_char uses turtle-like ox/oy math
#     coords; here we render on the same PIL canvas as the envelope,
#     which is much cleaner than mixing coord systems).
#
# No BANK_DEVIATION — envelope is used as-is; interior 山 is a fresh
# inline render because the bank's shan_char uses a different coord API.

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line  # noqa: E402

_CANVAS = 300


def draw_shan_interior(draw, cx=178, cy_top=170, cy_bot=245,
                       half_w=42, mid_up=15, w=6):
    """山 rendered inline in the belly of 疒.

    cx  = middle vertical's x
    cy_top / cy_bot = top and base y for the outer verticals
    mid_up = additional height for the middle 竖 above cy_top
    half_w = horizontal half-width (left/right verticals sit at cx ± half_w)
    w = line width
    """
    # Stroke 1: middle 竖 (tall).
    draw.line([(cx, cy_top - mid_up), (cx, cy_bot)],
              fill=(0, 0, 0), width=w)
    # Stroke 2: 竖折 — left vertical + base horizontal.
    left_x = cx - half_w
    right_x = cx + half_w
    draw.line([(left_x, cy_top + 5), (left_x, cy_bot)],
              fill=(0, 0, 0), width=w)
    draw.line([(left_x, cy_bot), (right_x, cy_bot)],
              fill=(0, 0, 0), width=w)
    # Stroke 3: short right 竖.
    draw.line([(right_x, cy_top + 18), (right_x, cy_bot)],
              fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank.
    draw_ne_chuang(draw)
    # Interior 山 (belly, right of pie shaft, below heng).
    draw_shan_interior(draw, cx=185, cy_top=175, cy_bot=250,
                       half_w=45, mid_up=20, w=6)
    out = os.path.join(_HERE, "01_疝.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
