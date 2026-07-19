"""Render 片 (radical 108, 4 strokes) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 6  # stroke thickness


def line(pts, width=TH):
    draw.line(pts, fill=BLACK, width=width, joint="curve")


# Canonical stroke order for 片 (4 strokes):
#   1. 撇 (pie) — long left falling stroke, curving down-left
#   2. 竖 — short vertical on the upper-mid area (left inner)
#      Actually per standard order: 1.撇 2.竖 3.横 4.横折
#      But 片 order commonly given: 撇, 竖, 横, 横折 -> 4 strokes
#   Looking at GT: shape is like a mirrored 月 with an open bottom.

# Stroke 1: 撇 (long curved falling stroke) from upper area down-left
pie_pts = []
x0, y0 = 118, 60
x1, y1 = 70, 265
cx, cy = 120, 175
for i in range(41):
    t = i / 40
    x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1
    pie_pts.append((x, y))
line(pie_pts, width=6)

# Stroke 2: 横 (upper horizontal) — the top of the box, from left area to right,
# with a slight hook at end that becomes stroke 4 (横折).
# Actually stroke 2 in 片 is 竖 (a short vertical). But visually the top horizontal
# is very short/tick-like. Let's follow the GT shape:
#
# Top-right of GT: there's a short horizontal that starts near (135, 95) and goes
# right to (220, 100), then turns down forming the right side of the box.

# Stroke 2: middle horizontal — bar crossing from left-vertical to right-vertical
line([(108, 165), (222, 168)], width=6)

# Stroke 3: top horizontal — short segment top of box
line([(138, 95), (225, 92)], width=6)

# Stroke 4: 横折 continuation — right vertical dropping from top-right corner
line([(225, 92), (218, 265)], width=6)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_片.png")
img.save(out)
print(f"wrote {out}")
