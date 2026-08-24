"""Render 佾 (p3_char_0408) to 300x300 PNG.

Composition (yi4 = ancient row-of-dancers):
  Left:  亻 (person radical)  — tall-narrow, apex at ~y=90.
  Right: 八 (top) over 月 (bottom).

Revision 1: raised the 八 higher so it aligns with the 亻 apex (was
buried below the 亻 竖 top); thickened & lengthened the 八 diverging
strokes; kept 月 tall & narrower to leave breathing room.
"""

from PIL import Image, ImageDraw
from math import comb

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def line(p1, p2, width=6):
    d.line([p1, p2], fill=BLACK, width=width)


def bezier(pts, width=6, steps=80):
    n = len(pts) - 1
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][0] for k in range(n + 1))
        y = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][1] for k in range(n + 1))
        if prev is not None:
            d.line([prev, (x, y)], fill=BLACK, width=width)
        prev = (x, y)


# ==== LEFT: 亻 ====
# 撇: apex at (95, 90), curves down-left to ~(50, 215)
bezier([(95, 90), (85, 130), (68, 175), (50, 215)], width=6)
# 竖: from apex, straight down
line((95, 96), (95, 285), width=6)

# ==== RIGHT TOP: 八 (positioned high, well above 月) ====
# left 撇 — starts near top, sweeps down-left
bezier([(190, 65), (180, 90), (165, 115), (148, 138)], width=7)
# right 捺 — starts just right of the 撇 apex, sweeps down-right
bezier([(195, 72), (215, 95), (240, 118), (260, 138)], width=7)

# ==== RIGHT BOTTOM: 月 ====
# 撇 (left side of the box) — curves down-left slightly
bezier([(170, 155), (162, 200), (155, 245), (145, 288)], width=6)

# 横折钩 — top 横
line((170, 155), (250, 155), width=6)
# vertical right side (drop from top-right corner)
line((250, 155), (250, 272), width=6)
# hook at bottom-right, flick UP-and-LEFT
bezier([(250, 272), (243, 273), (230, 272), (218, 265)], width=5)

# inner 横 1 (upper)
line((175, 200), (245, 200), width=5)
# inner 横 2 (mid)
line((175, 240), (245, 240), width=5)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0408_佾/01_佾.png"
)
print("saved 01_佾.png")
