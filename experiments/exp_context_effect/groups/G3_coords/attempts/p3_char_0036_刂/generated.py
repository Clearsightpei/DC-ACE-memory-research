# p3_char_0036_刂 — character 刂 (dao_pang), 2 strokes.
#
# GT observation (gt/phase3/刂.png): identical shape to phase-2 radical
# 刂 — a short 竖 on the left and a longer 竖钩 on the right.
#
# Strategy: radical-alias family (form_catalog Character-vs-radical).
# 刂 (char) == 刂 (radical) → try IDENTITY alias first with bank
# primitive draw_dao_pang at (0, 0, 1.0). GT fills a normal canvas
# extent so no scale bump needed.
# TR1-compliant: (ox, oy, scale) chosen deliberately.

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)
from dao_pang import draw_dao_pang  # noqa: E402

CANVAS = 300
OUT_PNG = os.path.join(HERE, "01_刂.png")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_dao_pang(draw, ox=0.0, oy=0.0, scale=1.0)
    img.save(OUT_PNG)


if __name__ == "__main__":
    main()
