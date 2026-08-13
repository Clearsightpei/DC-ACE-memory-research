# p3_char_0259_回 (huí, "return") — outer 囗 + inner 口
#
# Structure: 6 strokes total.
#   outer:  竖 + 横折 + 横  (via wei_radical, large enclosing box)
#   inner:  竖 + 横折 + 横  (via kou, small centered box)
#
# GT observation: outer square is ~2/3 canvas; inner square is ~1/3
# canvas, positioned roughly centered (slightly upper). Ink is thin/
# uniform (MMH-style), consistent with wei_radical's stamp widths.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from wei_radical import draw_wei_radical  # noqa: E402
from kou import draw_kou                  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Outer 囗 at default scale (already fills the canvas nicely per
    # its B4 identity-alias PASS at wei_char).
    draw_wei_radical(t, ox=0, oy=0, scale=1.0)

    # Inner 口: smaller (scale ~0.50), centered but nudged up slightly
    # to match GT's upper-centered inner square.
    draw_kou(t, ox=0, oy=5, scale=0.55)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(out_dir, "01_回.png"))


if __name__ == "__main__":
    main()
