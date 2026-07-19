"""G1 attempt for p2_radical_050_弓 (3 strokes)
Structure:
  1) 横折 (horizontal + downward turn) — top
  2) 横 — middle horizontal
  3) 横折弯钩 — bottom horizontal turning down with a curved hook
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
INK = 0
BG = 255
BRUSH = 6

img = Image.new("L", (SIZE, SIZE), BG)
draw = ImageDraw.Draw(img)


def line(p0, p1, w=BRUSH):
    draw.line([p0, p1], fill=INK, width=w)
    # rounded caps
    r = w // 2
    for (x, y) in (p0, p1):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def polyline(points, w=BRUSH):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], w)


# The character 弓 sits roughly centered — slightly left of center visually.
# Approx bounding box: x in [80, 210], y in [70, 240]

# Stroke 1: 横折 — starts upper-left, goes right, then turns down.
s1 = [
    (95, 82),    # start
    (195, 76),   # horizontal to right (slight upward tilt)
    (200, 118),  # vertical drop after fold — longer so it visually anchors
]
polyline(s1, w=6)

# Stroke 2: 横 — middle horizontal, tucked slightly inside
s2 = [
    (105, 138),
    (185, 135),
]
polyline(s2, w=6)

# Stroke 3: 横折弯钩 — long stroke: horizontal, fold down, curve, hook left.
# Give it clear S-shape geometry.
s3 = [
    (100, 168),   # start upper-left
    (195, 163),   # horizontal
    (205, 190),   # fold down
    (210, 220),   # keep dropping, slight rightward bulge
    (200, 248),   # bottom curve
    (170, 258),   # sweep left
    (135, 250),   # hook tip pointing up-left
    (128, 238),
]
polyline(s3, w=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_弓.png")
img.save(out_path)
print(out_path)
