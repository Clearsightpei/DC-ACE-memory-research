# p3_char_0088_川 — first attempt.
# 川 (chuan, "river") — 3 strokes:
#   1. left curved 撇-scoop
#   2. middle short 竖
#   3. right long 竖
#
# Character is orthographically identical to the mastered `chuan` radical
# (success_bank/code/chuan.py). Per memory_index Char↔Radical alias rule
# (form_catalog "Character-vs-radical scaling"), try IDENTITY alias first.
# The GT shows the shape roughly centered and filling ~60% of the canvas —
# a small scale bump (~1.15) and slight downward nudge (oy negative) should
# center it nicely for the character exam frame.

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from chuan import draw_chuan  # noqa: E402

CANVAS = 300
OUT = os.path.join(_HERE, "01_川.png")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    # Identity alias with a small scale bump (character fills more of frame
    # than the standalone radical would). Slight oy nudge negative to sit a
    # touch below dead center per GT.
    draw_chuan(t, ox=0.0, oy=-5.0, scale=1.15)
    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
