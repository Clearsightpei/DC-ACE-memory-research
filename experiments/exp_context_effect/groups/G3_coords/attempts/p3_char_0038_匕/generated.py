# p3_char_0038_匕 (bǐ) — 2 strokes: 撇 (short crossing) + 竖弯钩.
# Recipe: reuse bank shu_wan_gou (mastered) as the dominant right-side
# shape, plus a variant_pie for the short crossing 撇 that runs from
# upper-right down to lower-left, crossing the 竖弯钩 shaft mid-upper.
#
# GT observation: 竖弯钩 dominant, occupying middle-lower. 撇 is short,
# starts high on the right shaft and slants down-left to about 1/3 up
# from the base, ending outside the shaft on the left side.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402
from _shared_helpers import variant_pie  # noqa: E402

CANVAS = 300


def draw_bi(draw, ox=0, oy=0, scale=1.0):
    # 1) 竖弯钩 — the dominant frame stroke.
    # shu_wan_gou canonical shaft top at (ox, oy+70), curves at bottom
    # right, hook up. Shift right a bit so 撇 has room on the left.
    draw_shu_wan_gou(draw, ox=ox + 5 * scale, oy=oy - 5 * scale, scale=1.0 * scale)

    # 2) 撇 — starts at top-right (near shaft top), sweeps down and left,
    # ending below the lower-left. In 匕 the 撇 is a distinct calligraphic
    # stroke: head at shaft top, curving down-left, tail well below-left.
    # Should NOT extend above the shaft top.
    pie_head = (ox + 25 * scale, oy + 60 * scale)
    pie_tail = (ox - 55 * scale, oy - 15 * scale)
    variant_pie(draw, pie_head, pie_tail, bow_perp=-6.0,
                w_head=8.0, w_tail=1.5)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_bi(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_匕.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
