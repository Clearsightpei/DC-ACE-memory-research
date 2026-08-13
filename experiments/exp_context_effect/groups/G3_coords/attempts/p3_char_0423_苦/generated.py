# generated.py — p3_char_0423_苦 (kǔ, "bitter") — 8 strokes.
# Composition: 艹 (top, 3 strokes) + 古 (bottom, 5 strokes: 十 + 口).
#
# Bank usage:
#   - draw_cao_zi_tou → top 艹 (compressed to top ~1/3, thin scale)
#   - draw_kou       → bottom 口 (small, sits near canvas bottom)
#   - 十 (heng + shu) inlined fresh at correct position between them.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "..", "..", "success_bank", "code")
)
sys.path.insert(0, _BANK)

from cao_zi_tou import draw_cao_zi_tou  # noqa: E402
from kou import draw_kou                # noqa: E402

CANVAS = 300
W = 6

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


# ---- TOP: 艹 radical ----
# Push up (oy=+95) and use scale 0.55 → matches thin MMH style, same
# recipe used in hua_char.py (花) which PASSed B10.
draw_cao_zi_tou(d, ox=0, oy=95, scale=0.75)

# ---- MIDDLE: 十 (heng + shu of 古) ----
# Long heng across, wider than 艹 heng: GT shows it as the widest stroke.
# Heng at y≈150 (canvas middle).
line((22, 152), (278, 152))
# Shu of 十: vertical from just above heng down into the 口 area.
line((150, 115), (150, 200))

# ---- BOTTOM: 口 ----
# draw_kou uses math coords (y up), centered at canvas midpoint.
draw_kou(d, ox=0, oy=-85, scale=0.50)

img.save(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "01_苦.png"))
