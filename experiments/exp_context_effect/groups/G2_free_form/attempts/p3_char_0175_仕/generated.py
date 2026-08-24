"""Render 仕 (p3_char_0175) to 300x300 PNG.

# SIGNATURE CHECK (士 sibling row, copied verbatim from checklist):
# 士 | TOP 横 LONGER than bottom (~1.5x) | sibling: 土
# So on the right side of 仕: top 横 is the LONGER one, bottom 横 shorter.
# (土 would be the opposite.)

Composition:
  Left: 亻 (person radical) - short 撇 apex meeting top of 竖, ~40% width.
  Right: 士 - top 横 (long, ~150px), 竖 through both 横, bottom 横 (~100px).
Revision 1: pushed top-横 longer, bottom-横 shorter to hit 1.5x ratio;
attached 撇 apex to 竖 top; slight upward slant on top 横 mimicking GT.
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


# ---- LEFT: 亻 (person radical) ----
# 撇: apex at (95, 70), curves down-left to (45, 195)
bezier([(95, 70), (85, 115), (65, 165), (45, 200)], width=6)

# 竖: starts at apex of 撇 (95, 70) and drops straight down
line((95, 78), (95, 275), width=6)

# ---- RIGHT: 士 ----
# Top 横 (LONG ~155px, ~1.55x bottom's 100px). Slight upward slant.
line((125, 100), (280, 92), width=6)

# 竖: through both 横
line((200, 100), (200, 245), width=6)

# Bottom 横 (SHORTER ~100px, roughly centered on the 竖)
line((150, 245), (250, 245), width=6)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0175_仕/01_仕.png"
)
print("saved 01_仕.png")
