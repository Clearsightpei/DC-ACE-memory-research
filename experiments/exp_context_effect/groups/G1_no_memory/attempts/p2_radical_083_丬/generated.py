"""G1 render for radical 丬 (3 strokes)."""
from PIL import Image, ImageDraw
import os

OUT = os.path.join(os.path.dirname(__file__), "01_丬.png")

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: short 撇 (upper-right to lower-left curve) in upper-mid area
pts1 = [(155, 95), (140, 115), (125, 140), (115, 160)]
for a, b in zip(pts1, pts1[1:]):
    d.line([a, b], fill=INK, width=LW)

# Stroke 2: short 提 or slanted stroke middle (lower-left to upper-right, into vertical)
d.line([(85, 210), (170, 190)], fill=INK, width=LW)

# Stroke 3: vertical with a small curved top (top curves from upper-left to right, then straight down)
# top curve
curve = [(180, 65), (192, 62), (200, 68), (203, 80)]
for a, b in zip(curve, curve[1:]):
    d.line([a, b], fill=INK, width=LW)
# long vertical
d.line([(203, 80), (203, 270)], fill=INK, width=LW)

img.save(OUT)
print(f"Wrote {OUT}")
