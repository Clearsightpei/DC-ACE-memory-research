# p3_char_0265_名 (míng, "name") — 夕 (top) + 口 (bottom-right).
#
# Structure: 6 strokes total.
#   top: 夕 (xi) — 3 strokes, its long 撇 sweeps down-left
#   bottom-right: 口 (kou) — 3 strokes, small
#
# GT observation: 夕 dominates the upper half; its 撇 tail curves down
# to the lower-left corner. 口 sits at the bottom-right, tucked under
# the sweep of the pie. Ink uniform/thin (MMH-style).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from xi import draw_xi    # noqa: E402
from kou import draw_kou  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # 夕 shifted up-right so its long 撇 tail sweeps into lower-left
    # of canvas. scale ~0.85 gives the pie enough length.
    draw_xi(t, ox=15, oy=45, scale=0.9)

    # 口 at lower-right, small — tucks beneath the 夕 sweep. Bumped up
    # from scale 0.38 (revision 1: 口 read too small vs GT).
    draw_kou(t, ox=50, oy=-78, scale=0.48)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(out_dir, "01_名.png"))


if __name__ == "__main__":
    main()
