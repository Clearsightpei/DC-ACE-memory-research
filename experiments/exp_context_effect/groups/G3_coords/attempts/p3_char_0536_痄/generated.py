# p3_char_0536_痄 (zhà) — 疒 envelope + 乍 (zuò) interior.
#
# Composition: 疒 wraps top+left; 乍 sits in the right belly.
# GT decomposition (from gt/phase3/痄.png):
#   1. 疒 envelope: top-right small dot, thin heng roof, long left-descending
#      撇, two 冫 marks (upper 点 + lower 提) tucked inside upper-left belly.
#   2. 乍 (5 strokes):
#      a. Short 撇 slashing down-left near top of interior region.
#      b. Short 横 at top of 乍 (attached to 撇 head).
#      c. 竖 dropping down from the left end of the top 横 to bottom.
#      d. Short 横 mid-way (crossing 竖).
#      e. Bottom 横 at base (crossing 竖).
#
# Bank reuse:
#   - Envelope: reuse draw_ne_chuang from ne_sick.py (v9 rerun graduate).
#   - Interior 乍: inline (no 乍 in bank yet; follow pattern from 疝 attempt).
#
# No BANK_DEVIATION — envelope is used as-is.

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line  # noqa: E402

_CANVAS = 300


def draw_zuo_interior(draw, w=5):
    """乍 rendered inline in the right belly of 疒.

    5 strokes:
      1. 撇 short, top of the interior region.
      2. 横 short, at top of 乍 (from 撇 head area).
      3. 竖 dropping from left end of top 横 down to base.
      4. Short middle 横 crossing 竖.
      5. Bottom 横 at base (longer than middle).
    """
    # Stroke 1: 撇 — short down-left slash at top of interior region.
    _tapered_line(draw, (185, 130), (162, 160),
                  w_head=4.5, w_tail=3.0, n=18)

    # Stroke 2: 横 — short top horizontal, extends right from 撇's tail area.
    draw.line([(162, 160), (245, 160)], fill=(0, 0, 0), width=w)

    # Stroke 3: 竖 — vertical from left end of top 横 down to base.
    draw.line([(170, 155), (170, 275)], fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横 — short horizontal crossing 竖.
    draw.line([(170, 210), (238, 210)], fill=(0, 0, 0), width=w)

    # Stroke 5: bottom 横 — horizontal at base.
    draw.line([(170, 260), (250, 260)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank.
    draw_ne_chuang(draw)
    # Interior 乍 in right belly.
    draw_zuo_interior(draw, w=5)
    out = os.path.join(_HERE, "01_痄.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
