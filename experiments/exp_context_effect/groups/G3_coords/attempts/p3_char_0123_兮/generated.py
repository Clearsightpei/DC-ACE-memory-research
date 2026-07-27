# p3_char_0123_兮 — 兮 (xi)
# Structure (from GT):
#   top: 八 (pie + na, splayed) covering upper half
#   middle: short heng under the 八, offset slightly right
#   bottom: wan-gou-like stroke starting at right end of heng, curving
#           down and left with a small leftward hook flick at the tail
#
# Recipe:
#   - reuse ba (pie + na) for the top, shrunk slightly and lifted
#   - inline a short heng in the middle-right region
#   - reuse wan_gou for the bottom curve, positioned so its head aligns
#     with the right end of the heng

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ba import draw_ba  # noqa: E402
from heng import draw_heng  # noqa: E402
from wan_gou import draw_wan_gou  # noqa: E402

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # Top 八: wider spread covering upper portion of canvas.
    draw_ba(t, ox=0, oy=40, scale=0.75)

    # Middle heng: narrower and lifted up, slightly right of center.
    draw_heng(t, ox=5, oy=-10, scale=0.45)

    # Bottom stroke: wan-gou style curve. Anchor head near right end
    # of heng (~+50, -10) and let hook flick end low-left near (-10, -100).
    # canonical wan_gou head at (+5, +110), end at (-10, -95), hook (-38, -75).
    # With scale=0.6: head offset = (3, 66), so ox=47, oy=-76 places
    # head at (50, -10) and tail near (41, -133) — too low.
    # Use smaller scale=0.5: head offset=(2.5, 55); ox=48, oy=-65
    # -> head (50.5, -10), end (43, -112.5), hook (29, -102.5).
    draw_wan_gou(t, ox=48, oy=-65, scale=0.5)

    out = os.path.join(os.path.dirname(__file__), "01_兮.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
