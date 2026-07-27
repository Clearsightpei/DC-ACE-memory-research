"""Render 仝 (variant of 同) — 5 strokes:
   1. Left diagonal of 人 (roof) — from apex down-left
   2. Right diagonal of 人 (roof) — from apex down-right
   3. Short horizontal (top of 工)
   4. Short vertical (middle of 工)
   5. Long horizontal (bottom of 工)
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# Stroke 1: left diagonal of roof (piě) — wide, extends past horizontal
d.line([(148, 50), (55, 170)], fill=BLACK, width=LW)

# Stroke 2: right diagonal of roof (nà) — from apex down-right
d.line([(150, 55), (245, 170)], fill=BLACK, width=LW)

# Stroke 3: short horizontal (top of 工) — narrower than bottom
d.line([(100, 170), (200, 170)], fill=BLACK, width=LW)

# Stroke 4: short vertical (middle stem of 工)
d.line([(150, 172), (150, 235)], fill=BLACK, width=LW)

# Stroke 5: long horizontal (bottom of 工) — widest stroke
d.line([(50, 240), (250, 240)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_仝.png")
img.save(out)
print(f"Saved {out}")
