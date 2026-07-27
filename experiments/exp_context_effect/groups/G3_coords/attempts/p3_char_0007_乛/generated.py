# p3_char_0007_乛 — heng-gou radical character
# Reuses success_bank/code/heng_gou_radical.py (mastered at bootstrap pos 36).
# Single-stroke: thin horizontal with a small down-left hook at right end.

import os
import sys
from PIL import Image, ImageDraw

# Import the mastered primitive from the success bank
BANK_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_DIR)

from heng_gou_radical import draw_heng_gou_radical  # noqa: E402

CANVAS = 300
OUT = os.path.join(os.path.dirname(__file__), "01_乛.png")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Deliberate (ox, oy, scale) per TR1-TR3:
    # As a standalone character, 乛 occupies most of the canvas horizontally
    # (a bit above middle). The bootstrap PASS placed it mid-canvas at
    # PIL 90..205, y~128..168. For a character-scale rendering, slightly
    # widen (scale up) so the stroke fills more of the 300x300 box.
    #
    # scale=1.35 stretches around canvas center (150,150), taking the
    # horizontal to roughly x=69..224 and hook down to y~183. That gives
    # a comfortable margin (~75px each side) and centered composition.
    draw_heng_gou_radical(t, ox=0.0, oy=-10.0, scale=1.35)

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
