"""Render 丬 (3 strokes) using PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6  # stroke width

# Stroke 1: upper-left short pie (撇) going from upper-right to lower-left
draw.line([(115, 105), (75, 140)], fill=BLACK, width=W)

# Stroke 2: lower-left short 提 (rising stroke) — from lower-left up to right
draw.line([(60, 200), (125, 180)], fill=BLACK, width=W)

# Stroke 3: long vertical on right
# Top begins slightly right and slopes down-left to main vertical position
draw.line([(190, 65), (175, 90)], fill=BLACK, width=W)
# Main vertical continues straight down
draw.line([(175, 88), (175, 275)], fill=BLACK, width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_丬.png")
img.save(out_path)
print(f"Saved: {out_path}")
