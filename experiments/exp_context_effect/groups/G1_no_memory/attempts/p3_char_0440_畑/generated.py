"""G1 render of 畑 = 火 (left) + 田 (right)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=5):
    d.line([p0, p1], fill="black", width=w)

# ---- LEFT: 火 (fire) ----
# center around x~85, vertical range ~90..250
# left dot (short diagonal going down-left)
line((70, 125), (55, 155), 5)
# right dot (short diagonal going down-right)
line((100, 125), (115, 155), 5)
# central 人: 撇 (left sweep) from top peak down to lower-left
line((85, 110), (40, 240), 5)
# central 人: 捺 (right sweep) from upper-middle down to lower-right
line((85, 165), (135, 245), 5)

# ---- RIGHT: 田 (field) ----
# a rectangle with a plus inside
x0, y0, x1, y1 = 165, 110, 265, 230
# top
line((x0, y0), (x1, y0 - 2), 5)
# left vertical (slightly slanted like GT)
line((x0, y0), (x0 + 5, y1), 5)
# right vertical
line((x1, y0 - 2), (x1 - 5, y1), 5)
# bottom
line((x0 + 5, y1), (x1 - 5, y1), 5)
# horizontal middle
mid_y = (y0 + y1) // 2
line((x0 + 3, mid_y), (x1 - 3, mid_y), 5)
# vertical middle
mid_x = (x0 + x1) // 2
line((mid_x, y0 + 2), (mid_x, y1 - 2), 5)

out = os.path.join(os.path.dirname(__file__), "01_畑.png")
img.save(out)
print("wrote", out)
