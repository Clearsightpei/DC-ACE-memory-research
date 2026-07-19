"""Render the radical 川 (3画) as a 300x300 PNG.

Structure (from GT):
- Stroke 1 (piě): left short curve, starts upper-left, curves down-left.
- Stroke 2 (shù): middle vertical, straight, slightly shorter than stroke 3.
- Stroke 3 (shùgōu-like/shù): right vertical, longest, straight down.
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
BG = 255
INK = 0
STROKE_W = 6

img = Image.new("L", (SIZE, SIZE), BG)
draw = ImageDraw.Draw(img)


def stroke_curve(points, width=STROKE_W):
    # Draw a smooth curve by connecting many small line segments.
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    # Round the endpoints
    for p in points:
        draw.ellipse(
            [p[0] - width / 2, p[1] - width / 2, p[0] + width / 2, p[1] + width / 2],
            fill=INK,
        )


# Stroke 1: left piě (curved). Starts top ~ (95, 100), curves down and slightly left, ends ~ (75, 200).
s1 = []
n = 40
for i in range(n + 1):
    t = i / n
    # Quadratic Bezier from (95,100) via (95,160) to (72,205)
    x0, y0 = 95, 100
    x1, y1 = 95, 165
    x2, y2 = 70, 210
    x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
    s1.append((x, y))
stroke_curve(s1)

# Stroke 2: middle short vertical, straight-ish. From (150, 115) to (150, 215).
s2 = [(150, 115), (150, 215)]
stroke_curve(s2, width=STROKE_W)

# Stroke 3: right long vertical. From (215, 100) to (215, 240).
s3 = [(215, 100), (215, 245)]
stroke_curve(s3, width=STROKE_W)


out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_川.png"))
print("wrote", os.path.join(out_dir, "01_川.png"))
