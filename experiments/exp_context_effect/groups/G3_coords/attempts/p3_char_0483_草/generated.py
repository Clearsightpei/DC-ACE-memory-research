# generated.py — p3_char_0483_草 (cǎo, "grass") — 9 strokes.
# Composition: 艹 (top, 3 strokes) + 早 (bottom, 6 strokes = 日 + 十).
#
# Bank usage:
#   - draw_cao_zi_tou → top 艹, compressed to top ~1/3 (scale 0.75, oy=+105)
#   - 日 inlined fresh as a small tall rectangle in the mid-band
#   - 十 (long heng + descending shu) inlined fresh below 日
#
# GT observation: the 早 horizontal is the widest stroke of the whole
# character, wider than 艹's heng; vertical descends through 日 to the
# baseline.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "..", "..", "success_bank", "code")
)
sys.path.insert(0, _BANK)

from cao_zi_tou import draw_cao_zi_tou  # noqa: E402

CANVAS = 300
W = 7

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


# ---- TOP: 艹 radical (rising heng + two short verticals) ----
draw_cao_zi_tou(d, ox=0, oy=105, scale=0.75)

# ---- MIDDLE: 日 (small tall rectangle with middle bar) ----
# 日 box: image coords, small and centered
x_l, x_r = 108, 192
y_t, y_b = 115, 205
y_mid = 162
w_box = 6
# left 竖
line((x_l, y_t), (x_l, y_b), w=w_box)
# top 横 + right 竖 (横折)
line((x_l, y_t), (x_r, y_t), w=w_box)
line((x_r, y_t), (x_r, y_b), w=w_box)
# middle 横 (short)
line((x_l + 3, y_mid), (x_r - 5, y_mid), w=5)
# bottom 横
line((x_l, y_b), (x_r, y_b), w=w_box)

# ---- BOTTOM: 十 (long wide heng + vertical descending from 日 top) ----
# Long heng — widest stroke of the character, spans most of canvas.
line((18, 238), (282, 238), w=8)
# Vertical descending from top of 日 through 日 and long heng down to baseline.
line((150, y_t - 3), (150, 290), w=7)

img.save(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "01_草.png"))
