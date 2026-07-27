"""Render 自 (self) as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# 自: a small diagonal top stroke (丿) + a rectangle box with 3 horizontal lines inside
# Layout centered. Box roughly 60 wide, 160 tall, top around y=90
box_left, box_right = 110, 200
box_top, box_bottom = 100, 250

# Stroke 1: 丿 (short slanting stroke at top center)
d.line([(160, 55), (135, 100)], fill="black", width=5)

# Stroke 2: left vertical (丨)
d.line([(box_left, box_top), (box_left, box_bottom)], fill="black", width=5)

# Stroke 3: top horizontal + right vertical (橫折)
d.line([(box_left, box_top), (box_right, box_top)], fill="black", width=5)
d.line([(box_right, box_top), (box_right, box_bottom)], fill="black", width=5)

# Stroke 4: middle horizontal 1
d.line([(box_left, box_top + 45), (box_right, box_top + 45)], fill="black", width=5)

# Stroke 5: middle horizontal 2
d.line([(box_left, box_top + 90), (box_right, box_top + 90)], fill="black", width=5)

# Stroke 6: bottom horizontal (closing the box)
d.line([(box_left, box_bottom), (box_right, box_bottom)], fill="black", width=5)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_自.png")
img.save(out)
print("wrote", out)
