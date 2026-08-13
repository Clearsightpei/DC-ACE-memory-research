# BANK_DEVIATION
# skipped: shen_extend.py
# reason: bank 申 primitive uses absolute canvas coords (x=85..215) and scale
#   only affects widths, so it cannot compress into the right half of an L-R
#   composition; inline a narrower 申 anchored to the right.
# fresh_component: shen_variant_for_LR_right

# p3_char_0463_神 — 神 (shén), 9 strokes.
# L-R composition: 礻 (left, 4 strokes) + 申 (right, 5 strokes).
# - 礻 uses bank shi_ceremony_pang (same recipe as 社 promotion).
# - 申 inlined narrower, anchored to right half.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_ceremony_pang import draw_shi_ceremony_pang  # noqa: E402

CANVAS = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_神.png")


def draw_shen_right(d):
    # 申-shape anchored in the right half.
    x_left = 148
    x_right = 262
    y_top = 100
    y_bot = 220
    y_mid = 160
    w = 8
    w_mid = 7
    w_shu = 9

    # Stroke 1: left 竖 of box
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right)
    d.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横
    d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)],
           fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横
    d.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 5: central 竖 protrudes top & bottom
    x_center = (x_left + x_right) // 2
    d.line([(x_center, 45), (x_center, 275)],
           fill=(0, 0, 0), width=w_shu)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    # Left: 礻 (bank primitive, math-coord)
    draw_shi_ceremony_pang(d, ox=-80.0, oy=0.0, scale=0.65)
    # Right: 申 (inline variant)
    draw_shen_right(d)
    img.save(OUT_PNG)
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
