"""Render 冫 (two-dots-water radical) to 300x300 PNG.

冫 is two dots stacked vertically, both on the LEFT side of the frame:
- Top dot: 点-like short slash going from upper-left to lower-right, thin->thick.
- Bottom dot: 提-like rising stroke going from lower-left to upper-right,
  thick->thin.

Rendered with PIL brush-dabs technique (see drawer_memory.md).
"""

from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_taper(p0, p1, r0, r1, steps=400):
    """Straight tapered stroke via brush-dabs."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# REVISION 1: previous attempt was too bulky/heavy for the delicate GT
# and both dots sat too central. GT shows both dots on the LEFT half,
# top dot small and short, bottom dot longer and thicker.
#
# Top dot (点): short slash upper-right to lower-left orientation —
# actually re-reading GT: top is a small stroke tilted with LEFT end
# lower and RIGHT end higher, like a small 撇 or 反捺. In canonical 冫
# it's a small 点 slanting from upper-left down to lower-right.
# Keep it short and thin.
p0_top = (128, 100)
p1_top = (150, 135)
stroke_taper(p0_top, p1_top, r0=2.0, r1=5.5, steps=400)
# small terminal head
dab(p1_top[0], p1_top[1], 6.0)

# Bottom dot (提-like): longer stroke on the left, slanted, thick at
# bottom tapering thin at top. GT bottom is clearly longer than top and
# leans more.
p0_bot = (120, 235)
p1_bot = (158, 175)
stroke_taper(p0_bot, p1_bot, r0=6.5, r1=1.8, steps=400)
# 顿笔 at start (subtle)
dab(p0_bot[0], p0_bot[1], 7.5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_冫.png"))
print("wrote", os.path.join(out_dir, "01_冫.png"))
