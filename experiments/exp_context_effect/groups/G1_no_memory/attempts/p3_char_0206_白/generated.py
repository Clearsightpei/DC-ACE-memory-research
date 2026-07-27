"""Render 白 (bái) at 300x300."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 6

# 白 = 5 strokes:
# 1. short slanting stroke (撇) on top
# 2. left vertical (竖) of the 日-like box
# 3. top-right corner (横折) forming top and right side
# 4. middle horizontal
# 5. bottom horizontal (closing the box)

# 1. Top short 撇 - descends from upper-right area to top-left of box
d.line([(150, 45), (118, 82)], fill=INK, width=LW)

# 2. Left vertical of box (starts a bit below top slant)
d.line([(108, 90), (105, 245)], fill=INK, width=LW)

# 3. Top horizontal + right vertical (横折)
d.line([(108, 90), (215, 90)], fill=INK, width=LW)      # top horizontal
d.line([(215, 90), (218, 250)], fill=INK, width=LW)     # right vertical

# 4. Middle horizontal
d.line([(115, 160), (215, 160)], fill=INK, width=LW)

# 5. Bottom horizontal (closes box)
d.line([(108, 248), (218, 248)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_白.png")
img.save(out)
print("wrote", out)
