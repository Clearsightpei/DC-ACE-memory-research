# p3_char_0013_十 — 十 (shí, "ten"), 2 strokes: 横 crossing 竖.
# G3 rendering: reuse the mastered `draw_shi` radical primitive
# (INDEX row 46, PASSed at p2_radical_031_十, batch B1).
# The character 十 has the same shape as the 十 radical, but as a
# standalone character it should fill more of the canvas. The GT
# shows the horizontal spanning most of the canvas width and the
# vertical spanning most of the canvas height. Scale slightly up
# from the radical's canonical form.
#
# TR1-TR3 compliance: (ox, oy, scale) chosen deliberately, not defaults.
#  - ox=0, oy=0: centered on canvas (as GT).
#  - scale=1.1: slight upscale so the character occupies canvas
#    like a standalone p3 item rather than a radical.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi import draw_shi  # noqa: E402

CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shi(d, ox=0.0, oy=0.0, scale=1.1)
    img.save(os.path.join(os.path.dirname(__file__), "01_十.png"))


if __name__ == "__main__":
    main()
