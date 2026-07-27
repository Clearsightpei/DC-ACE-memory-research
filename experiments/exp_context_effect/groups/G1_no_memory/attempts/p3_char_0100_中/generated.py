"""Render 中 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

ink = "black"
lw = 5

# Rectangle 口 in the middle-upper area
left = 90
right = 210
top = 100
bottom = 180

# Left vertical of rectangle
draw.line([(left, top), (left, bottom)], fill=ink, width=lw)
# Top horizontal + right vertical (one stroke: 横折)
draw.line([(left, top), (right, top)], fill=ink, width=lw)
draw.line([(right, top), (right, bottom)], fill=ink, width=lw)
# Bottom horizontal
draw.line([(left, bottom), (right, bottom)], fill=ink, width=lw)

# Central vertical stroke through the whole character
cx = (left + right) // 2
draw.line([(cx, 40), (cx, 260)], fill=ink, width=lw)

out_path = os.path.join(os.path.dirname(__file__), "01_中.png")
img.save(out_path)
print(f"Wrote {out_path}")
