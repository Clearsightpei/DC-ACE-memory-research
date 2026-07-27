"""Render 乇 (character p3_char_0048) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 6  # stroke thickness

# Stroke 1: short 撇 (slant) at top — from upper right down to left
# In GT it goes from about (210, 80) to (140, 115)
d.line([(210, 78), (140, 118)], fill=INK, width=TH)

# Stroke 2: long horizontal 横 through the middle
# From (55, 160) to (245, 150) — slight upward slope
d.line([(55, 162), (245, 150)], fill=INK, width=TH)

# Stroke 3: 竖弯钩 — starts at intersection of stroke1 and horizontal,
# goes down, curves broadly right at bottom, ends with hook up-left
# GT: starts around (155, 115), goes down to (155, 235), curves right to (230, 260)
pts = []
x0, y0 = 160, 115
# vertical descent
for y in range(y0, 231, 3):
    pts.append((x0, y))

# broad curve at bottom: from (160, 230) sweeping right and slightly down then up
# Use a quarter arc with center at (230, 230), radius 70
cx, cy = 230, 228
r = 70
for t in range(0, 91, 3):
    ang = math.radians(180 - t)  # 180 down to 90
    x = cx + r * math.cos(ang)
    y = cy + r * math.sin(ang) * 0.5 - 0  # flatten slightly
    # Actually just standard arc
    x = cx + r * math.cos(ang)
    y = cy - r * math.sin(ang) + r  # so arc bottom at cy+... top of curve tangent at y=cy
    pts.append((x, y))

# Small hook at the end (curls up)
last = pts[-1]
pts.append((last[0] - 3, last[1] - 15))

# Draw the polyline
for i in range(len(pts) - 1):
    d.line([pts[i], pts[i+1]], fill=INK, width=TH)

out_path = os.path.join(os.path.dirname(__file__), "01_乇.png")
img.save(out_path)
print(f"Saved {out_path}")
