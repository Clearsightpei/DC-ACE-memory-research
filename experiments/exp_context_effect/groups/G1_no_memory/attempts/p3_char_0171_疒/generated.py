"""Render 疒 (sickness radical) at 300x300 with PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

# Stroke 1: top dot (点) - short slanted stroke, upper-right area, above horizontal
d.line([(155, 45), (180, 70)], fill=BLACK, width=LW)

# Stroke 2: horizontal (横) - long horizontal, slight slant, from mid-left to right
d.line([(115, 105), (245, 100)], fill=BLACK, width=LW)

# Stroke 3: downward-left curve (long piě 撇) - starts near left end of horizontal, curves down/left
points = []
for i in range(40):
    t = i / 39.0
    # start at (118, 105), end at (75, 285) with leftward curve
    x = 118 - 8*t - 35*t*t
    y = 105 + 180*t
    points.append((x, y))
for i in range(len(points)-1):
    d.line([points[i], points[i+1]], fill=BLACK, width=LW)

# Stroke 4: upper dot on pie (点) - short slanted stroke to the LEFT of pie, upper portion
d.line([(75, 135), (100, 155)], fill=BLACK, width=LW)

# Stroke 5: lower tí (提) - short stroke rising to the right, at lower portion of pie
d.line([(50, 210), (90, 195)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_疒.png")
img.save(out)
print(f"Saved {out}")
