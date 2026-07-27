"""Render 乂 (yi) to a 300x300 PNG.

乂 has 2 strokes:
  1. 撇 (pie): falling-left stroke, top-right to bottom-left, slightly curved.
  2. 捺 (na):  falling-right stroke, top-left to bottom-right, curved with
              a slight tail flick at the end.
They cross near the visual center.
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)


def stroke(points, width_start=10, width_end=10, steps=40):
    """Draw a smooth thick stroke along a quadratic-ish path defined by 3
    control points using linear interpolation of thickness."""
    (x0, y0), (x1, y1), (x2, y2) = points
    prev = None
    for i in range(steps + 1):
        t = i / steps
        # Quadratic Bezier
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        w = width_start + (width_end - width_start) * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
        if prev is not None:
            draw.line([prev, (x, y)], fill="black", width=int(max(w, 1)))
        prev = (x, y)


# Stroke 1: 撇 — top-right to bottom-left, curving. Starts thicker, tapers.
# Top-right start around (200, 70), passes middle (150, 160), ends bottom-left (80, 250).
stroke(
    [(205, 65), (150, 165), (75, 255)],
    width_start=9,
    width_end=5,
    steps=60,
)

# Stroke 2: 捺 — top-left to bottom-right, curved, thickens toward the tail then
# tapers. Starts around (95, 95), through middle (150, 175), ends (240, 260).
stroke(
    [(95, 95), (155, 175), (240, 258)],
    width_start=5,
    width_end=10,
    steps=60,
)

out = os.path.join(os.path.dirname(__file__), "01_乂.png")
img.save(out)
print(f"Saved {out}")
