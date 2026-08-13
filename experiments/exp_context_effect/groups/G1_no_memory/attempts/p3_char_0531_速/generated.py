"""G1 render of 速 using PIL — pass 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- 束 (upper-right portion) ----
# Top horizontal
line([(120, 60), (255, 60)], w=6)
# Left vertical of the 口 box
line([(150, 60), (150, 155)], w=6)
# Right vertical of the 口 box
line([(230, 60), (230, 155)], w=6)
# Middle horizontal of the box
line([(150, 110), (230, 110)], w=6)
# Bottom horizontal of the box
line([(150, 155), (230, 155)], w=6)
# Central vertical through 束 (long)
line([(190, 50), (190, 250)], w=6)
# Left piě from box bottom center
line([(188, 155), (135, 240)], w=6)
# Right nà from box bottom center
line([(192, 155), (255, 240)], w=6)

# ---- 辶 (walk radical, lower-left) ----
# Upper small dot
line([(60, 55), (72, 72)], w=6)
# Second short stroke below
line([(50, 88), (80, 105)], w=6)
# Folded descender: down-left, then across-right, then a curve
line([(75, 118), (58, 155)], w=6)
line([(58, 155), (85, 195)], w=6)
# Big flat bottom sweep — smoother arc using many segments
pts = []
import math
# arc from (48, 205) curving down and out to (275, 260) with slight upflick
xs = [48, 65, 90, 130, 175, 220, 260, 278]
ys = [205, 235, 258, 268, 268, 262, 252, 245]
sweep = list(zip(xs, ys))
line(sweep, w=7)

out = os.path.join(os.path.dirname(__file__), "01_速.png")
img.save(out)
print("wrote", out)
