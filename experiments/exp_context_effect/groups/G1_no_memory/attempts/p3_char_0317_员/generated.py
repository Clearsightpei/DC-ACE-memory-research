"""Render 员 at 300x300 with PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, width=4):
    d.line([p1, p2], fill="black", width=width)

# 员 = 口 (top, small) + 贝 (bottom)
# Top 口 (small mouth): roughly centered, small
# left ~120, right ~180, top ~55, bot ~105
kx1, ky1, kx2, ky2 = 120, 55, 180, 105
# top 口 - three strokes: left vertical, top-right (horizontal + right vertical), bottom horizontal
line((kx1, ky1), (kx1, ky2), 4)               # left vertical
line((kx1, ky1), (kx2, ky1), 4)               # top horizontal
line((kx2, ky1), (kx2, ky2), 4)               # right vertical
line((kx1, ky2), (kx2, ky2), 4)               # bottom horizontal

# 贝 (bottom half, larger):
# outer rectangle
bx1, by1, bx2, by2 = 90, 115, 210, 215
# left vertical (slightly leaning)
line((bx1, by1), (bx1, by2), 4)
# top horizontal
line((bx1, by1), (bx2, by1), 4)
# right vertical
line((bx2, by1), (bx2, by2), 4)
# bottom horizontal
line((bx1, by2), (bx2, by2), 4)

# two inner horizontals (representing the two short strokes inside 贝)
line((bx1+15, by1+30), (bx2-15, by1+30), 3)
line((bx1+15, by1+60), (bx2-15, by1+60), 3)

# Two legs at bottom:
# left leg: 丿 curving down-left from bx1 area
line((bx1+15, by2), (60, 280), 4)
# right leg: 丶 (dot) short slanted stroke down-right
line((bx2-15, by2), (250, 280), 4)

out_path = os.path.join(os.path.dirname(__file__), "01_员.png")
img.save(out_path)
print("wrote", out_path)
