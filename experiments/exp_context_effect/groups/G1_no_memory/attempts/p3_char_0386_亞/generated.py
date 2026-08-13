"""G1 render of 亞 (p3_char_0386)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# 亞: symmetric character
# Top horizontal (top bar)
line(85, 70, 215, 70)

# Left outer vertical (angled slightly outward going down)
line(88, 70, 78, 210)
# Right outer vertical
line(212, 70, 222, 210)

# Middle horizontal (connects verticals across middle)
line(78, 140, 222, 140)

# Left inner small box
line(100, 140, 100, 195)     # left vert
line(135, 140, 135, 195)     # right vert
line(100, 195, 135, 195)     # bottom
line(100, 168, 135, 168)     # inner divider

# Right inner small box
line(165, 140, 165, 195)
line(200, 140, 200, 195)
line(165, 195, 200, 195)
line(165, 168, 200, 168)

# Lower cross bar joining the two verticals near bottom
line(78, 210, 222, 210)

# Bottom horizontal (widest baseline)
line(40, 240, 260, 240)

out = os.path.join(os.path.dirname(__file__), "01_亞.png")
img.save(out)
print("wrote", out)
