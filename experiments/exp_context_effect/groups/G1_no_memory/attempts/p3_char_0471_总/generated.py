"""Render 总 to a 300x300 PNG using PIL. Revision 2."""
from PIL import Image, ImageDraw
import os, math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def polyline(pts, w=5):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=w)

# 总 has three parts stacked:
#   Top: 丷 (two divergent dots — left \, right /)
#   Middle: 口-like compact rectangle (口/small mouth)
#   Bottom: 心 (heart: left dot, wide dish curve, middle dot, right dot)

# --- Top: 丷 (two dots) ---
# left dot (slanting down-left, like a comma)
polyline([(125, 45), (110, 75)], w=6)
# right dot (slanting down-right, curving)
polyline([(180, 40), (195, 65)], w=6)

# --- Middle: 口 shape ---
# top horizontal (slight rightward tilt)
polyline([(105, 105), (200, 100)], w=5)
# left vertical (short, slight inward)
polyline([(107, 105), (112, 155)], w=5)
# right vertical (slight inward)
polyline([(200, 100), (195, 152)], w=5)
# small internal horizontal (like the middle line in 口/日)
polyline([(115, 128), (190, 128)], w=5)
# bottom horizontal
polyline([(112, 155), (195, 152)], w=5)

# --- Bottom: 心 (heart) ---
# left dot
polyline([(75, 195), (60, 230)], w=6)

# main dish curve (wide U from left-upper to right-upper)
pts = []
for t in range(0, 25):
    u = t / 24.0
    x = 90 + (215 - 90) * u
    # dish shape (deeper in middle)
    y = 195 + 70 * (1 - (2*u - 1)**2)
    pts.append((x, y))
polyline(pts, w=6)

# middle dot (small vertical inside heart)
polyline([(140, 215), (145, 240)], w=6)

# right dot (upper-right of heart)
polyline([(220, 200), (235, 225)], w=6)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_总.png")
img.save(out)
print("saved", out)
