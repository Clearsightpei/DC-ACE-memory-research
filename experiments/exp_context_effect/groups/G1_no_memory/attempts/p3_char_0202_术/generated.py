"""Render 术 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# 术 = 木 + 丶 (dot on upper right)
# Strokes (order):
# 1. Horizontal (一)
# 2. Vertical (丨) through center
# 3. Left-falling (丿) from center
# 4. Right-falling (乀) from center
# 5. Dot (丶) on upper right

# Layout: center around x=150. Character occupies rows ~50..270

# 1. Horizontal stroke
d.line([(55, 130), (245, 125)], fill=INK, width=LW)

# 2. Vertical stroke (long, from top through bottom)
d.line([(150, 55), (150, 275)], fill=INK, width=LW)

# 3. Left-falling (丿) starting near horizontal, sweeping down-left
# Approximate with a curve using multiple segments
pts_left = [(150, 130), (135, 165), (115, 200), (90, 235), (60, 275)]
for i in range(len(pts_left) - 1):
    d.line([pts_left[i], pts_left[i+1]], fill=INK, width=LW)

# 4. Right-falling (乀) from center sweeping down-right
pts_right = [(150, 140), (170, 175), (200, 215), (235, 250), (265, 275)]
for i in range(len(pts_right) - 1):
    d.line([pts_right[i], pts_right[i+1]], fill=INK, width=LW)

# 5. Dot (丶) - small stroke on upper right, above horizontal
d.line([(200, 75), (225, 100)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_术.png")
img.save(out)
print("wrote", out)
