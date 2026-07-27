# p3_char_0020_亠 — G3 attempt.
# 亠 (tou, "lid") is a 2-stroke character/radical: 点 (dot) on top, 横 (long
# horizontal) below. The G3 Success Bank already contains the exact recipe
# from B1 pos 65 (tou_radical.py — passed). Reuse it via a deliberate
# (ox, oy, scale) call at canvas center — TR-compliant per principles_meta.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(
    os.path.join(_HERE, "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from tou_radical import draw_tou_radical  # noqa: E402


CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # tou_radical: dian on top + heng below. Centered at canvas origin
    # (ox=0, oy=0). Scale 1.0 — the bank recipe (dian 0.6, heng 0.90)
    # already yields the correct proportions for the 300x300 canvas.
    draw_tou_radical(t, ox=0.0, oy=0.0, scale=1.0)

    out = os.path.join(_HERE, "01_亠.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
