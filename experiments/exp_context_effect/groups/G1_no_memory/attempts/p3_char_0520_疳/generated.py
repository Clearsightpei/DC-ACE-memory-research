"""Render 疳 (p3_char_0520) as 300x300 PNG using PIL — revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, w=4):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

def poly(pts, w=4):
    for i in range(len(pts)-1):
        line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], w)

# --- 疒 radical (illness) ---
# 1) small top dot (top of radical, slightly right of falling-stroke top)
line(122, 40, 138, 55, 5)

# 2) long horizontal top stroke of 疒
line(80, 78, 250, 72, 5)

# 3) long left-falling stroke (piě) from top-left down to bottom-left corner
poly([(108, 75), (95, 130), (75, 195), (50, 270)], 5)

# 4) two short dot-strokes on the left side (inside the 疒 "belly")
line(78, 118, 96, 130, 5)   # upper small stroke (falling)
line(65, 175, 88, 185, 5)   # lower small stroke (falling)

# --- 甘 inside (lower-right within the radical) ---
# top horizontal
line(150, 135, 235, 135, 5)
# left vertical (slightly slanted inward)
line(155, 135, 152, 245, 5)
# right vertical
line(228, 132, 232, 245, 5)
# middle horizontal (short, centered)
line(170, 190, 215, 190, 5)
# bottom horizontal
line(150, 245, 235, 245, 5)

out = os.path.join(os.path.dirname(__file__), "01_疳.png")
img.save(out)
print("saved:", out)
