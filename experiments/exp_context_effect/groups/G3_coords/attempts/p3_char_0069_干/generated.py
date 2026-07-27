# p3_char_0069_干 — G3 attempt.
# 干 (gan) is a 3-stroke character: short top 横 + wide middle 横 + long 竖.
# The G3 Success Bank already contains the exact PASSed recipe from
# B1 pos 80 (gan.py — passed as radical p2_radical_048_干). Per
# memory_index priority order: try IDENTITY alias for Phase-3 char that
# matches an existing radical primitive. This is a 1-line alias.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(
    os.path.join(_HERE, "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from gan import draw_gan  # noqa: E402


CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Identity alias for gan radical — 2 hengs + shu, canvas-centered.
    draw_gan(t, ox=0.0, oy=0.0, scale=1.0)

    out = os.path.join(_HERE, "01_干.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
