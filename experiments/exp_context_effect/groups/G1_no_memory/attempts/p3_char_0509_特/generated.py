"""Render 特 (ox radical + 寺) at 300x300, PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def poly(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- LEFT: 牜 (ox radical) — narrow tall on left ----
# 1) short 丿 (top-left slanted)
poly([(70, 60), (60, 82), (55, 100)])
# 2) short horizontal (top of ox)
line((55, 108), (120, 105))
# 3) long 丿 (big slant from upper right area down to lower-left)
poly([(105, 75), (85, 130), (60, 185), (40, 235)])
# 4) vertical stroke through center
line((105, 115), (105, 260))
# 5) 提 (short rising horizontal near bottom-left)
poly([(50, 205), (115, 195)])

# ---- RIGHT: 寺 = 土 (top) + 寸 (bottom) ----
# 土 top:
# short horizontal 1
line((175, 55), (240, 58))
# vertical
line((205, 40), (205, 125))
# horizontal 2 (widest of 土)
line((160, 125), (265, 125))

# 寸 bottom:
# horizontal
line((150, 175), (280, 175))
# vertical + hook 亅
poly([(215, 175), (215, 265), (200, 278)])
# small dot 丶 (short stroke)
poly([(225, 210), (240, 225)])

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_特.png"))
print("wrote", os.path.join(out_dir, "01_特.png"))
