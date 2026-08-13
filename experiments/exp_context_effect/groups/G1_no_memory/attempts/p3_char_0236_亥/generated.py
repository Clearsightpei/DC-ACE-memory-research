"""Render 亥 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

# 亥 has 6 strokes:
# 1. Top dot (short slash) 丶 upper center
# 2. Horizontal 一 across middle-upper
# 3. Left-falling piě 丿 (short) below horizontal on left
# 4. Small hook / na on right below horizontal
# 5. Long piě 丿 sweeping left-down from center
# 6. Long right-falling nà 乀 crossing from center to lower right

# 1. Top dot - short diagonal
d.line([(150, 55), (163, 72)], fill=BLACK, width=LW)

# 2. Horizontal stroke (slight rise)
d.line([(55, 115), (245, 105)], fill=BLACK, width=LW)
# tiny tail dot on right end of horizontal
d.line([(240, 100), (250, 115)], fill=BLACK, width=LW)

# 3. Short left piě under horizontal (middle-left small 人-like)
d.line([(135, 125), (110, 165)], fill=BLACK, width=LW)

# 4. Right small piě/hook mirror
d.line([(165, 125), (150, 150)], fill=BLACK, width=LW)
d.line([(150, 150), (185, 170)], fill=BLACK, width=LW)

# 5. Long piě - sweeps from upper-center down to lower-left
# starts around (140,130), curves through (100,190), ends (55,255)
points = []
import math
for t in range(0, 101):
    u = t / 100.0
    # quadratic bezier: P0=(140,130), P1=(70,220), P2=(55,265)
    x = (1-u)**2 * 140 + 2*(1-u)*u * 70 + u**2 * 55
    y = (1-u)**2 * 130 + 2*(1-u)*u * 220 + u**2 * 265
    points.append((x, y))
for i in range(len(points)-1):
    d.line([points[i], points[i+1]], fill=BLACK, width=LW)

# 6. Long nà - from center-upper down to lower-right
points2 = []
for t in range(0, 101):
    u = t / 100.0
    # quadratic bezier: P0=(145,155), P1=(190,215), P2=(255,270)
    x = (1-u)**2 * 145 + 2*(1-u)*u * 200 + u**2 * 255
    y = (1-u)**2 * 155 + 2*(1-u)*u * 235 + u**2 * 270
    points2.append((x, y))
for i in range(len(points2)-1):
    d.line([points2[i], points2[i+1]], fill=BLACK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_亥.png"))
print("saved", os.path.join(out_dir, "01_亥.png"))
