"""Render radical 尸 to 300x300 PNG using PIL.

尸 has 3 strokes:
  1. 横折 (horizontal top + turn down right side)
  2. 横 (middle short horizontal)
  3. 撇 (long diagonal from top-left curving down-left)
"""
import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 5  # stroke thickness

def line(p1, p2, width=TH):
    d.line([p1, p2], fill=INK, width=width)

def polyline(points, width=TH):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=width)

# Stroke 1: 横折 — top horizontal then turn down.
# Top horizontal from (~85, 95) to (~215, 95), then vertical down to (~205, 175).
polyline([(85, 95), (215, 95), (210, 175)], width=TH)

# Stroke 2: 横 — a middle short horizontal inside the box, around y=155.
line((110, 155), (205, 155), width=TH)

# Stroke 3: 撇 — the long piě going from ~(95, 95) down-left curving to (~55, 260).
# Approximate with a slight curve using multiple segments.
piě_points = [
    (100, 92),
    (95, 130),
    (88, 170),
    (78, 210),
    (65, 245),
    (50, 265),
]
polyline(piě_points, width=TH)

out = os.path.join(os.path.dirname(__file__), "01_尸.png")
img.save(out)
print("wrote", out)
