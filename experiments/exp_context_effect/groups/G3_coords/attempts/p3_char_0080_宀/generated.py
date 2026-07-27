# p3_char_0080_宀 — identity alias of the mastered Phase-2 radical 宀
# (bao_gai_tou, "roof"). Per form_catalog.md "Character-vs-radical scaling":
# Phase-3 characters orthographically identical to a Phase-2 radical are
# tried as IDENTITY aliases first (scale=1.0, ox=0, oy=0).
#
# GT inspection: the character 宀 renders at the same size and position as
# the radical GT. No scale bump needed.

from PIL import Image, ImageDraw
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from bao_gai_tou import draw_bao_gai_tou  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # Identity alias — deliberate (0, 0, 1.0): the bank primitive's native
    # coord range already matches the GT position.
    draw_bao_gai_tou(t, ox=0.0, oy=0.0, scale=1.0)

    out = os.path.join(HERE, "01_宀.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
