"""Render radical 韦 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4

def line(x1, y1, x2, y2, w=T):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

def curve(points, w=T):
    d.line(points, fill=INK, width=w, joint="curve")

# 韦 has 4 strokes:
#  S1: short horizontal at top (slight down-right slope, small tail)
#  S2: main long horizontal below S1 (slight upward slope to right)
#  S3: right-side "彐" hook — short horizontal from center to right, then vertical
#      down, ending with a hook back to the left (like a J-hook / 竖折)
#  S4: long vertical down center from top of S1 through bottom

# S1 - top short horizontal (with slight down curl at end)
curve([(128, 78), (150, 76), (175, 78), (185, 82)], w=T)

# S2 - main long horizontal, slight upward tilt to right
curve([(72, 128), (140, 122), (210, 116), (228, 116)], w=T)

# S3 - right side hook + bottom curl (drawn as 3-part path):
#   horizontal from center-right at ~y=190, then curve down and hook left
curve([
    (155, 195), (185, 192), (210, 193),           # short horizontal top of hook
    (216, 205), (218, 225), (215, 245),           # vertical down curving
    (205, 258), (185, 262), (165, 258), (152, 250)  # hook back to lower-left
], w=T)

# S4 - long vertical through center
line(155, 72, 155, 282, w=T)

out = os.path.join(os.path.dirname(__file__), "01_韦.png")
img.save(out)
print("Saved:", out)
