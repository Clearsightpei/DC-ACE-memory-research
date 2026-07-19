"""G1 render of 丶 (dot radical). PIL, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 丶 is a short teardrop-like dot sloping from upper-left to lower-right.
# GT shows the stroke starting near center-upper and ending slightly right and below,
# widening toward the bottom. Approximate with a series of ellipses along a diagonal.

# GT: diagonal ~45deg, gently curved (concave toward lower-left),
# thin at start (upper-left), slightly wider at end (lower-right).
# Use a quadratic Bezier from P0 through P1 to P2 with a small tapering.
P0 = (120, 115)   # upper-left start
P1 = (140, 145)   # control (pulls curve concave to lower-left)
P2 = (175, 190)   # lower-right end

steps = 60
for i in range(steps + 1):
    t = i / steps
    # quadratic Bezier
    cx = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
    cy = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
    # Radius: thin at start (~1.6), modest at end (~3.2)
    r = 1.6 + 1.6 * t
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")

out = os.path.join(os.path.dirname(__file__), "01_丶.png")
img.save(out)
print(out)
