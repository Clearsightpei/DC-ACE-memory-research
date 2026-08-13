"""G1 render of 佴 (person + ear)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

# Left: 亻 person radical
# Slanting stroke (top-right to bottom-left)
line((95, 70), (55, 190), w=LW)
# Vertical stroke starting from the slant
line((85, 100), (85, 260), w=LW)

# Right: 耳 (ear) radical
# Top horizontal
line((130, 90), (250, 90), w=LW)
# Left vertical (of 耳)
line((145, 90), (145, 230), w=LW)
# Right vertical (of 耳)
line((235, 90), (235, 230), w=LW)
# Middle horizontal 1
line((160, 140), (220, 140), w=LW)
# Middle horizontal 2
line((160, 185), (220, 185), w=LW)
# Bottom long horizontal extending to right
line((130, 235), (275, 235), w=LW)

out = os.path.join(os.path.dirname(__file__), "01_佴.png")
img.save(out)
print("saved", out)
