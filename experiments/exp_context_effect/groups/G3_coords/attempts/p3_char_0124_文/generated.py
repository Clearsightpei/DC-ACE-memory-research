# p3_char_0124_文 — identity alias of draw_wen (bank #85).
# The Phase-2 radical 文 (wen.py) PASSed at B3 pos 151 with a coord
# recipe centered on a 300x300 canvas — the Phase-3 char shares shape,
# so we call draw_wen at (0, 0, 1.0) with no transform.
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from wen import draw_wen  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_wen(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_文.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
