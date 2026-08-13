# 度 (dù) — 9 strokes.
# Structure: 广 envelope (top-left) + 廿-body (inside) + 又 (bottom-right).
# Uses bank primitives guang.py and you.py.

import os
import sys
from PIL import Image, ImageDraw

_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, _BANK)

from guang import draw_guang  # noqa: E402
from you import draw_you  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_du(d):
    # ---- 广 envelope: dian + heng roof + long pie down-left ----
    draw_guang(d, ox=-15.0, oy=25.0, scale=1.15)

    # ---- 廿-like inner body: top heng + 2 verticals + bottom heng ----
    # Wider and centered under 广's roof.
    # top heng of the inner box
    draw_heng(d, ox=20.0, oy=25.0, scale=0.60)
    # left vertical (shu)
    draw_shu(d, ox=-25.0, oy=0.0, scale=0.42)
    # right vertical (shu)
    draw_shu(d, ox=65.0, oy=0.0, scale=0.42)
    # bottom heng closing the box (slightly wider than top for calligraphic feel)
    draw_heng(d, ox=20.0, oy=-25.0, scale=0.65)

    # ---- 又 tucked below the 廿-body, centered ----
    # Smaller scale so na doesn't shoot off canvas.
    draw_you(d, ox=15.0, oy=-75.0, scale=0.70)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_du(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_度.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
