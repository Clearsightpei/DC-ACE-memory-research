"""Render 处 to a 300x300 PNG. G1 no-memory control. Revision 1."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

def curve(p0, p1, p2, width=5, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    stroke(pts, width)

def cubic(p0, p1, p2, p3, width=5, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = ((1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0]
             + 3*(1-t)*t*t*p2[0] + t**3*p3[0])
        y = ((1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1]
             + 3*(1-t)*t*t*p2[1] + t**3*p3[1])
        pts.append((x, y))
    stroke(pts, width)

# 处 = 夂 (outer wrap) + 卜 (inside upper-right)
# Stroke 1: 丿 — top short pie starting near center-top going down-left
curve((115, 55), (95, 85), (75, 115), width=5)

# Stroke 2: 𠃋 / 乛-ish top of 夂 — small horizontal-turn-pie:
# horizontal segment then swings down-left into a curve
# top horizontal
stroke([(105, 95), (155, 95)], width=5)
# then down-left curve
curve((155, 95), (140, 130), (85, 195), width=5)

# Stroke 3: ㇏ — the long sweeping right-down flare (from mid down to lower-right)
cubic((135, 100), (145, 190), (200, 240), (275, 260), width=6)

# Stroke 4: 丨 vertical of 卜 (upper-right)
stroke([(195, 75), (195, 195)], width=6)

# Stroke 5: 丶 dot of 卜 — a short diagonal stroke
curve((205, 150), (230, 155), (255, 165), width=6)

out = os.path.join(os.path.dirname(__file__), "01_处.png")
img.save(out)
print("wrote", out)
