"""G1 render of 天 (sky/heaven). 4 strokes:
1. Top horizontal (short, upper)
2. Second horizontal (longer, mid)
3. Left-falling 撇 from center-top downward-left
4. Right-falling 捺 from center-top downward-right
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE = 6

# Stroke 1: short top horizontal (upper), slight upward tilt right
d.line([(95, 78), (215, 72)], fill=INK, width=STROKE)

# Stroke 2: longer second horizontal, mid area
d.line([(60, 145), (240, 138)], fill=INK, width=STROKE)

# Stroke 3: 撇 (left-falling) starts near center of stroke 2, curves down-left
# Simulate slight curve using multiple segments
import math
pts = []
x0, y0 = 150, 138
x1, y1 = 70, 260
n = 20
for i in range(n + 1):
    t = i / n
    # slight curve: control offset
    cx, cy = 120, 200
    x = (1 - t) * (1 - t) * x0 + 2 * (1 - t) * t * cx + t * t * x1
    y = (1 - t) * (1 - t) * y0 + 2 * (1 - t) * t * cy + t * t * y1
    pts.append((x, y))
for i in range(len(pts) - 1):
    d.line([pts[i], pts[i + 1]], fill=INK, width=STROKE)

# Stroke 4: 捺 (right-falling) starts near center of stroke 2, curves down-right
pts2 = []
x0, y0 = 155, 145
x1, y1 = 245, 260
for i in range(n + 1):
    t = i / n
    cx, cy = 190, 205
    x = (1 - t) * (1 - t) * x0 + 2 * (1 - t) * t * cx + t * t * x1
    y = (1 - t) * (1 - t) * y0 + 2 * (1 - t) * t * cy + t * t * y1
    pts2.append((x, y))
for i in range(len(pts2) - 1):
    d.line([pts2[i], pts2[i + 1]], fill=INK, width=STROKE)

out = os.path.join(os.path.dirname(__file__), "01_天.png")
img.save(out)
print(f"saved {out}")
