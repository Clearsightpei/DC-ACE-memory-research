"""Render 高 to 01_高.png (300x300, white bg, black ink) — revision 2."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(a, b, w=LW):
    d.line([a, b], fill="black", width=w)

def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)

# 高 structure:
#   亠  (dot + long horizontal)  y ~ 25..55
#   口  (small mouth)            y ~ 60..100
#   冖  (wide cover)             y ~ 108..130
#   口  (bottom mouth)           y ~ 135..270

# 1) top dot (short slant near center-right of top)
polyline([(155, 25), (168, 40)], w=6)

# 2) long horizontal
line((50, 58), (250, 58), w=6)

# 3-5) small mouth 口 (centered, moderate size)
sx1, sy1, sx2, sy2 = 115, 70, 185, 108
line((sx1, sy1), (sx1, sy2))           # left vertical
polyline([(sx1, sy1), (sx2, sy1), (sx2, sy2)])  # top + right (横折)
line((sx1, sy2), (sx2, sy2))           # bottom

# 6-7) 冖 cover: small left dot + long horizontal ending in short hook
polyline([(58, 122), (70, 135)], w=5)  # left dot
polyline([(60, 138), (245, 138), (243, 152)])  # cover top + right hook

# 8-10) bottom 口 (larger, centered)
bx1, by1, bx2, by2 = 78, 158, 222, 272
line((bx1, by1), (bx1, by2))           # left vertical
polyline([(bx1, by1), (bx2, by1), (bx2, by2)])  # top + right (横折)
line((bx1, by2), (bx2, by2))           # bottom

out = os.path.join(os.path.dirname(__file__), "01_高.png")
img.save(out)
print("wrote", out)
