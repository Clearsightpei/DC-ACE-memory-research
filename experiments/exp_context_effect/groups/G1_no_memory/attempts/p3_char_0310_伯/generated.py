"""Render 伯 (bo) - person radical 亻 + 白."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def stroke(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# ============== 亻 (person radical, left side) ==============
# Slanting downward stroke (撇): from upper-right to lower-left
pier_pts = [(100, 60), (90, 95), (72, 145), (45, 200)]
stroke(pier_pts)

# Vertical stroke (竖): meets the pier near the top
stroke([(90, 95), (90, 250)])

# ============== 白 (right side) ==============
# 白 has: 撇 (short slant top), 竖 (left vertical), 横折 (top+right vertical), 横 (middle), 横 (bottom)

# Top short 撇 (small slant on top)
stroke([(175, 55), (162, 78)])

# Top horizontal + right vertical (横折): top of the box
stroke([(155, 78), (245, 78), (245, 235)])

# Left vertical of box
stroke([(160, 82), (160, 235)])

# Bottom horizontal (closes the box)
stroke([(160, 235), (245, 235)])

# Middle horizontal (inside the box)
stroke([(165, 155), (240, 155)])

out = os.path.join(os.path.dirname(__file__), "01_伯.png")
img.save(out)
print("saved", out)
