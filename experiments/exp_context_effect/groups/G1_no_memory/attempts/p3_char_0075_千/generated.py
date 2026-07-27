"""Render 千 as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: 撇 (top diagonal) — short slanted line, goes from upper-right down to left
# In GT: starts ~ (200, 90), ends ~ (90, 120)
draw.line([(200, 88), (85, 122)], fill=INK, width=LW)

# Stroke 2: 横 (horizontal) — long horizontal across the middle
# In GT: from ~ (45, 155) to ~ (255, 150), slight upward tilt
draw.line([(40, 158), (260, 148)], fill=INK, width=LW)

# Stroke 3: 竖 (vertical) — descends from just above the horizontal, through it, down
# In GT: from ~ (150, 110) down to ~ (150, 275)
draw.line([(152, 108), (150, 278)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_千.png")
img.save(out_path)
print(f"Wrote {out_path}")
