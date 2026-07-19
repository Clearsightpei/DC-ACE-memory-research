"""G1 render: radical 冂 (2 strokes).
Stroke 1: left vertical (丨)
Stroke 2: 横折钩 (horizontal-turn) forming top and right side.
"""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), "01_冂.png")
SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

INK = "black"
W = 7

# Radical 冂 - centered, occupies roughly x:[70,230], y:[80,255].
# Stroke 1: left vertical (丨). GT shows a small nub/entry at top-left.
# Draw with slight inward curve at top and straight down.
d.line([(72, 90), (74, 260)], fill=INK, width=W)

# Stroke 2: 横折 - top horizontal + right vertical.
# Horizontal from left edge to right edge (slight upward slope in GT).
d.line([(70, 85), (232, 82)], fill=INK, width=W)
# Right vertical, drop straight down from the corner.
d.line([(230, 82), (226, 250)], fill=INK, width=W)
# Small tick at bottom-right (subtle hook inward, characteristic of 冂 ending)
d.line([(226, 250), (218, 258)], fill=INK, width=W)

img.save(OUT)
print(f"Saved {OUT}")
