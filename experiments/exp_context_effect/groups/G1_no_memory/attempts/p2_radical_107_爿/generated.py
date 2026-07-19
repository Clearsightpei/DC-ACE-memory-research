"""Render 爿 (radical 107, 4 strokes) at 300x300 with PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

# 爿 has 4 strokes. Looking at GT:
# 1) Top short stroke: starts around (100, 90), goes slightly down-right to (145, 80)
# 2) Left vertical (short, tilted): from top area (100, 90) down to bottom-left (85, 235)
# 3) Middle crossbar (horizontal): from left vert (~95, 165) to right vert (~185, 165)
# 4) Right long vertical: from top (185, 55) straight down to bottom (185, 260)

# Stroke 1: top slanted stroke (curved, longer) - upper area
# Use a slight curve via multiple segments
pts1 = [(105, 105), (125, 92), (150, 85), (170, 82)]
for i in range(len(pts1) - 1):
    d.line([pts1[i], pts1[i+1]], fill="black", width=W)

# Stroke 2: left vertical (piě-like) - slants down-left from near top stroke
# Curved/slanting shape from ~(108, 108) down and slightly out to (80, 235)
pts2 = [(108, 108), (98, 150), (88, 195), (80, 240)]
for i in range(len(pts2) - 1):
    d.line([pts2[i], pts2[i+1]], fill="black", width=W)
# small bottom hook to the right (horizontal foot)
d.line([(80, 240), (115, 238)], fill="black", width=W)

# Stroke 3: middle horizontal crossbar (slightly rising to right)
d.line([(93, 170), (188, 165)], fill="black", width=W)

# Stroke 4: long right vertical from top to bottom
d.line([(188, 55), (188, 265)], fill="black", width=W)

out = os.path.join(os.path.dirname(__file__), "01_爿.png")
img.save(out)
print(f"saved {out}")
