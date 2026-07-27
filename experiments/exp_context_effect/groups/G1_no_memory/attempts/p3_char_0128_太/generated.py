"""Render 太 (tài) to a 300x300 PNG using PIL.
Strokes: 1) heng (horizontal), 2) pie (left-falling), 3) na (right-falling),
4) dian (dot) below-center.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6  # stroke width


def line(p1, p2, w=W):
    draw.line([p1, p2], fill=BLACK, width=w)


def curve(points, w=W):
    # smooth polyline
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=BLACK, width=w)
    for p in points:
        draw.ellipse([p[0] - w // 2, p[1] - w // 2, p[0] + w // 2, p[1] + w // 2], fill=BLACK)


# Stroke 1: heng - horizontal, slight upward slant
line((55, 140), (240, 132), w=6)

# Stroke 2: pie - left-falling from above heng, crossing heng near center, sweeping bottom-left
pie_pts = [(155, 70), (150, 100), (140, 135), (120, 180), (85, 240)]
curve(pie_pts, w=6)

# Stroke 3: na - right-falling starting from the pie/heng intersection, curving bottom-right
na_pts = [(148, 138), (170, 175), (195, 210), (230, 250)]
curve(na_pts, w=7)

# Stroke 4: dian - small dot below-center, between the "legs"
dot_pts = [(158, 215), (172, 228)]
curve(dot_pts, w=8)

out_path = os.path.join(os.path.dirname(__file__), "01_太.png")
img.save(out_path)
print("wrote", out_path)
