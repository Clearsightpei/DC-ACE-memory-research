"""Render 乚 (p3_char_0006_乚) using PIL, 300x300, white bg, black ink.

Shape: single stroke.
  - Small starting tick at top-left (顿笔), pointing up-left
  - Descend nearly vertically
  - Round the bottom-left corner
  - Sweep right along the bottom
  - Small upward hook at the right end
"""
from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

pts = []

# 1. Starting tick — a short segment going up-left from the top of the vertical
tick_top = (85, 68)
vert_top = (100, 82)
pts.append(tick_top)
pts.append(vert_top)

# 2. Vertical descent from (100, 82) down to about (100, 210), with tiny rightward drift
for y in range(82, 210, 4):
    x = 100 + (y - 82) * 0.02  # very gentle drift
    pts.append((x, y))

# 3. Rounded corner: quarter arc from (100, 210) curving to (140, 245).
#    Center at (140, 210), radius 35. Angle sweeps from 180deg -> 270deg (in math coords),
#    which corresponds to going from point (105, 210) down/right to (140, 245).
cx, cy = 140, 210
r = 35
for deg in range(180, 271, 5):
    rad = math.radians(deg)
    x = cx + r * math.cos(rad)
    y = cy - r * math.sin(rad)  # PIL: y grows down, but sin(180..270) is 0..-1, so -sin is 0..1 -> y grows down: good
    pts.append((x, y))

# 4. Horizontal sweep from (140, 245) to (235, 245) with a very slight downward belly then back up
for x in range(140, 236, 4):
    t = (x - 140) / 95.0
    y = 245 + 3 * math.sin(t * math.pi)  # slight belly
    pts.append((x, y))

# 5. Upward hook at right end: from (235, 245) up to about (235, 218)
pts.append((236, 240))
pts.append((238, 230))
pts.append((236, 218))

draw.line(pts, fill=INK, width=LW, joint="curve")

out_path = os.path.join(os.path.dirname(__file__), "01_乚.png")
img.save(out_path)
print(f"Saved {out_path}")
