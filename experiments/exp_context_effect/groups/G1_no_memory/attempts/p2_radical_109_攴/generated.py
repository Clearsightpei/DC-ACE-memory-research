"""Render 攴 (radical 109) to a 300x300 PNG using PIL.

4 strokes:
  1. 竖 (short vertical) at top-center
  2. 一 (short horizontal) crossing near top of vertical, tilted slightly
  3. 撇 (long left-falling diagonal) starting from top area, curving down-left
  4. 捺 (right-falling) crossing the 撇, going down-right
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
OUT_PATH = os.path.join(os.path.dirname(__file__), "01_攴.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6  # stroke width


def stroke(points, width=W):
    """Draw a polyline stroke with round joints."""
    draw.line(points, fill=BLACK, width=width, joint="curve")
    # cap ends with a small circle for rounded look
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Stroke 1: short vertical (top-center), slight tilt ---
# From about (150, 60) down to (150, 115)
stroke([(150, 60), (150, 115)])

# --- Stroke 2: short horizontal tick, slight up-slant, right of vertical top ---
stroke([(150, 105), (200, 100)])

# --- Stroke 3: long 撇 (left-falling diagonal), starts near upper-center,
# crosses HIGH (around y=170), curves down-left to lower-left corner ---
stroke([
    (160, 130),
    (145, 160),
    (120, 200),
    (90, 240),
    (65, 275),
])

# --- Stroke 4: 捺 (right-falling), starts higher and further left so the
# cross with 撇 happens near the top, ends with a flatter tail to lower-right ---
stroke([
    (115, 135),
    (145, 170),
    (180, 210),
    (215, 245),
    (245, 270),
])

img.save(OUT_PATH)
print(f"wrote {OUT_PATH}")
