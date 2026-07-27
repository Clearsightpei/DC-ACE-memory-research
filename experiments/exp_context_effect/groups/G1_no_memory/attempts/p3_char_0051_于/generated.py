"""Render 于 (yu) as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os
import math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 7  # stroke width

# Stroke 1: top short horizontal, positioned slightly right of center-top
# GT shows it spanning roughly from x~110 to x~215, y ~85
draw.line([(105, 88), (218, 82)], fill="black", width=W)

# Stroke 2: longer horizontal (main), spans wider - roughly x~50 to x~255, y~150
draw.line([(50, 152), (255, 148)], fill="black", width=W)

# Stroke 3: vertical (starting from just above the main horizontal) descending,
# then hooking left at bottom.
# Vertical part: from ~(168, 100) down to ~(160, 235)
# Draw as a smooth curve using multiple segments
pts = []
# vertical descending, slight lean
for i in range(0, 141, 5):
    t = i / 140.0
    x = 168 - 8 * t  # slight lean left as it descends
    y = 100 + i
    pts.append((x, y))
# Hook: curve left and slightly up
for i in range(0, 45, 3):
    t = i / 44.0
    # arc from (160, 240) curving left-up
    angle = math.pi * 0.5 + t * math.pi * 0.55  # from pointing down to pointing up-left
    cx, cy = 145, 240
    r = 18
    x = cx + r * math.cos(angle) * -1 + 15  # mirror to go left
    y = cy + r * math.sin(-angle) + 15
    # simpler: parametric
    x = 160 - 30 * t
    y = 240 + 12 * math.sin(math.pi * t) - 8 * t
    pts.append((x, y))

# Draw as connected line
for i in range(len(pts) - 1):
    draw.line([pts[i], pts[i+1]], fill="black", width=W)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_于.png")
img.save(out)
print(f"Saved {out}")
