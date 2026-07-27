# p3_char_0049_子 — 子 (zǐ, "child"), 3 strokes.
# Strokes: (1) 横撇 short at top; (2) 弯钩 long curving descender with hook;
#          (3) 横 horizontal crossing the descender at middle.
# Approach: reuse draw_liao (top 横钩 + wan_gou descender) as the base
# skeleton (子 shares 了's spine), then overlay a horizontal 横 across
# the middle. Note: 子's top is really 横撇 not 横钩, but the GT shows a
# broadly similar small top segment; liao's inline _hengou is close
# enough for a first attempt.
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from liao import draw_liao  # noqa: E402
from heng import draw_heng  # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # 了's skeleton — top 横钩 and wan_gou descender.
    # draw_liao expects PIL ImageDraw as first arg.
    draw_liao(draw, ox=0, oy=0, scale=1.0)

    # Add the crossing 横 (stroke 3 of 子). Math coords: center-origin, +y up.
    # GT crossing sits slightly below center at ~y=-15..-20 (math) and
    # is centered on the descender (which the wan_gou places near x=+15).
    draw_heng(draw, ox=15, oy=-20, scale=1.0)

    out = os.path.join(_HERE, "01_子.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
