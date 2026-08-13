"""Render 单 (dan) to 01_单.png at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width)

# 单 structure:
#  丷    (two dots at top)
#  口    (small box)
#  一    (horizontal middle)
#  十    (vertical + horizontal)

# Two dots on top (丷 - left leaning, right leaning)
# Left dot: from upper-right to lower-left
line([(115, 55), (100, 78)], width=6)
# Right dot: from upper-left to lower-right
line([(175, 55), (190, 78)], width=6)

# Upper box (口 shape) with internal horizontal
# top of box
line([(95, 85), (200, 82)])
# left side
line([(98, 85), (98, 155)])
# right side
line([(200, 82), (203, 155)])
# bottom of box
line([(98, 155), (203, 155)])
# horizontal middle inside box
line([(105, 118), (198, 118)])

# Long horizontal (much wider than box)
line([(55, 195), (245, 193)])

# Central vertical stroke (from top of box through bottom)
line([(150, 88), (150, 275)], width=6)

# Save PNG
out = os.path.join(os.path.dirname(__file__), "01_单.png")
img.save(out)
print("saved:", out)
