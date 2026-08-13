# p3_char_0344_佝 (gōu) — 亻 (left) + 句 (right, = 勹 wrapping 口)
# Compose from bank: ren_pang (left column) + bao_char (envelope, right)
# + kou (small square inside bao envelope, bottom).
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from bao_char import draw_bao_char  # noqa: E402
from kou import draw_kou            # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # Left radical 亻 — compressed like men_plural (ox=-45, scale=0.55).
    # 佝's 亻 sits in the left ~35% of canvas; use similar recipe.
    draw_ren_pang(t, ox=-55, oy=0, scale=0.65)

    # Right: 句 = 勹 envelope + 口 inside. Bao envelope spans ~(60..230)
    # x (45..255) at scale 1. Shrink to 0.55 and shift right so envelope
    # sits in right ~55% of canvas.
    draw_bao_char(t, ox=45, oy=-15, scale=0.55)

    # 口 inside bao envelope — small, placed lower-right within envelope.
    # kou native spans roughly (85..215)x(100..200) centered at 150,150.
    # At scale 0.30 → ~40×30 px. Offset (+55, +55) puts center near (205,205).
    draw_kou(t, ox=55, oy=55, scale=0.32)

    out = os.path.join(os.path.dirname(__file__), "01_佝.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
