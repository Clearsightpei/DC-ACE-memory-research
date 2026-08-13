"""Render 理 as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

def line(x1, y1, x2, y2, w=W):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# ============ LEFT: 王/王 radical (王 as left component, taller & narrower) ============
# Three horizontals + vertical, with bottom "tick" up-right on the last stroke variant
# top horizontal
line(35, 90, 110, 82)
# middle horizontal (shorter)
line(40, 135, 100, 132)
# vertical
line(72, 85, 72, 195)
# bottom stroke (upward tilt to the right, like 提)
line(35, 200, 115, 175)

# ============ RIGHT: 里 ============
# 里 = 日 on top, 土 on bottom
# 日 rectangle (top)
# top horizontal of 日
line(145, 65, 265, 62)
# left vertical of 日
line(150, 65, 148, 165)
# right vertical of 日
line(258, 62, 260, 165)
# middle horizontal of 日
line(150, 118, 258, 116)
# bottom horizontal of 日 (also top of 土 below)
line(150, 165, 260, 163)

# vertical of 土 (down the middle, extending from bottom of 日)
line(203, 165, 203, 265)

# lower middle horizontal (short)
line(160, 215, 250, 213)

# bottom horizontal of 里 (spans right side only, widest stroke of 里)
line(140, 268, 275, 262)

out_path = os.path.join(os.path.dirname(__file__), "01_理.png")
img.save(out_path)
print(f"Wrote {out_path}")
