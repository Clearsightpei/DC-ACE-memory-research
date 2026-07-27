"""G1 draw of 口 (mouth) — 3 strokes, hand-drawn look."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# 口 has 3 strokes in standard order:
#  1. Left vertical (丨)
#  2. Top horizontal + right vertical (turn: 横折)
#  3. Bottom horizontal (一)

# Bounding box (leave margin, slightly offset like handwriting)
L, T = 80, 90
R, B = 220, 220

# Stroke 1: left vertical (slightly tilted, small hook-like top)
d.line([(L + 2, T + 5), (L, B + 5)], fill=BLACK, width=LW)

# Stroke 2: horizontal then turn down (top-right corner)
d.line([(L + 5, T), (R + 3, T - 3)], fill=BLACK, width=LW)   # top horizontal
d.line([(R + 3, T - 3), (R - 5, B - 5)], fill=BLACK, width=LW)  # right vertical

# Stroke 3: bottom horizontal (closes the box)
d.line([(L - 3, B + 8), (R - 3, B + 3)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_口.png")
img.save(out)
print(f"Saved {out}")
