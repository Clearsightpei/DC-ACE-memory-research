"""G1 render of 龶 (4 strokes: top-horiz, vertical, mid-horiz, long bottom-horiz).

The GT shows the character positioned in the upper portion of the canvas,
with a wide, slightly wavy long bottom stroke.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 4  # line width

# Stroke 1: top short horizontal, roughly centered upper area, slight rightward tilt up
# From ~ (100, 70) to (185, 62)
d.line([(100, 72), (188, 62)], fill=INK, width=LW)

# Stroke 2: vertical through center of top horiz, extending down through second horiz
# From ~ (142, 55) down to (142, 155)
d.line([(142, 55), (140, 155)], fill=INK, width=LW)

# Stroke 3: middle horizontal, similar length to top, positioned below top-horiz
# From ~ (95, 118) to (195, 108)
d.line([(92, 118), (198, 108)], fill=INK, width=LW)

# Stroke 4: long bottom horizontal spanning almost full width, with slight wave/curve
# From ~ (35, 165) to (270, 152)  - slightly curved
# Draw as short segments to give a subtle wave
import math
pts = []
x0, y0 = 35, 168
x1, y1 = 275, 152
N = 40
for i in range(N + 1):
    t = i / N
    x = x0 + (x1 - x0) * t
    # slight sinusoidal wave in y
    y = y0 + (y1 - y0) * t + 2.0 * math.sin(t * math.pi * 1.5)
    pts.append((x, y))
for i in range(len(pts) - 1):
    d.line([pts[i], pts[i + 1]], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_龶.png")
img.save(out_path)
print(f"Wrote {out_path}")
