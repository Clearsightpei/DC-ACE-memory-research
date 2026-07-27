"""Render 毋 (radical, 4 strokes) to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 4

def line(p0, p1, width=LW):
    draw.line([p0, p1], fill=INK, width=width)

def polyline(pts, width=LW):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=INK, width=width)

# 毋: 4 strokes
# Layout: bounding box roughly centered, with the middle horizontal
# extending beyond the box left & right.

# Stroke 1: 竖折/撇 — left side, slight slant, top to bottom-left
polyline([(110, 70), (105, 140), (95, 210), (82, 235)], width=LW)

# Stroke 2: 横折钩 — top horizontal from stroke1 top going right,
# then bends down to form right vertical (no strong hook in this radical)
polyline([(110, 70), (210, 68), (215, 225)], width=LW)

# Stroke 3: 长横 — long horizontal through middle, extends beyond box
line((50, 155), (250, 152), width=LW)

# Stroke 4: 撇 crossing the middle horizontal — from upper-right inside
# down to lower-left, crossing through the middle horizontal
polyline([(175, 100), (150, 150), (125, 200)], width=LW)

# Save
out_path = os.path.join(os.path.dirname(__file__), "01_毋.png")
img.save(out_path)
print(f"Saved: {out_path}")
