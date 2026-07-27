"""Render 囗 (enclosure) to 300x300 PNG."""
import os
from PIL import Image, ImageDraw

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, "01_囗.png")

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

ink = "black"
stroke_w = 6

# 囗 has 3 strokes:
# 1. Left vertical (丨)
# 2. Top horizontal + right vertical done in one stroke (horizontal-turn: 横折)
# 3. Bottom horizontal (一) closing the box

# Bounding box for the character (leave some margin)
left = 70
right = 230
top = 55
bottom = 245

# Stroke 1: left vertical (top to bottom)
draw.line([(left, top), (left, bottom)], fill=ink, width=stroke_w)

# Stroke 2: 横折 — top horizontal then down the right side
draw.line([(left, top), (right, top)], fill=ink, width=stroke_w)
draw.line([(right, top), (right, bottom)], fill=ink, width=stroke_w)

# Stroke 3: bottom horizontal (closes the box), slightly wider than sides in real 囗
draw.line([(left - 4, bottom), (right + 4, bottom)], fill=ink, width=stroke_w)

img.save(OUT_PATH)
print(f"wrote {OUT_PATH}")
