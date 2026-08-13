"""Render 亨 (Phase 3, character) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

# 1. Top dot (点) - upper area, small diagonal
d.line([(158, 38), (172, 60)], fill="black", width=LW)

# 2. Long horizontal stroke (一) - the top bar (wider)
d.line([(50, 80), (250, 80)], fill="black", width=LW)

# 3. Small 口 in the middle - more compact/square, centered
# Left vertical
d.line([(115, 105), (115, 145)], fill="black", width=LW)
# Top horizontal + right turn (横折)
d.line([(115, 105), (185, 105)], fill="black", width=LW)
d.line([(185, 105), (185, 145)], fill="black", width=LW)
# Bottom horizontal
d.line([(115, 145), (185, 145)], fill="black", width=LW)

# 4. Bottom horizontal stroke
d.line([(75, 170), (225, 170)], fill="black", width=LW)

# 5. 了-shape hook: vertical descent from center of horizontal, curves left with hook up
# Start at ~x=155, y=170. Descend curving left, then hook up.
points = []
# straight vertical for a bit, then curve
for i in range(0, 80):
    t = i / 80.0
    # gentle curve: starts vertical, curves left near bottom
    x = 155 - (t ** 2.2) * 55
    y = 170 + t * 85
    points.append((x, y))
# hook: sharp turn upward-left at the end
hx, hy = points[-1]
for i in range(0, 25):
    t = i / 25.0
    x = hx - t * 18
    y = hy - t * 22
    points.append((x, y))

for i in range(len(points) - 1):
    d.line([points[i], points[i+1]], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_亨.png")
img.save(out)
print(f"Saved {out}")
