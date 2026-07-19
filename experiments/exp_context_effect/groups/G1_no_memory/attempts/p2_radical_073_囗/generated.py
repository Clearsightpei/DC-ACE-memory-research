"""G1 render: 囗 (radical, 3画).

Strokes (traditional order):
  1) 竖 (left vertical)
  2) 横折 (top horizontal + right vertical, one stroke)
  3) 横 (bottom horizontal, closes the box)

Rendered with PIL at 300x300, white background, black ink.
Slightly hand-drawn feel (small wobble + non-perfect corners) to
match the GT aesthetic.
"""

from PIL import Image, ImageDraw
import os
import random

SIZE = 300
OUT = os.path.join(os.path.dirname(__file__), "01_囗.png")


def wobble_line(draw, p0, p1, width=6, segments=14, jitter=1.2, seed=0):
    """Draw a slightly wobbly line from p0 to p1 to look hand-drawn."""
    rng = random.Random(seed)
    x0, y0 = p0
    x1, y1 = p1
    pts = []
    for i in range(segments + 1):
        t = i / segments
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        if 0 < i < segments:
            x += rng.uniform(-jitter, jitter)
            y += rng.uniform(-jitter, jitter)
        pts.append((x, y))
    for a, b in zip(pts[:-1], pts[1:]):
        draw.line([a, b], fill="black", width=width)
    # rounded end caps
    r = width / 2
    for p in (p0, p1):
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


def main():
    img = Image.new("RGB", (SIZE, SIZE), "white")
    draw = ImageDraw.Draw(img)

    # Box geometry — leave margins, mimic GT which sits slightly upper-left.
    left = 70
    right = 235
    top = 55
    bottom = 235

    # Stroke 1: 竖 (left vertical) — often starts a hair above the top for the corner.
    wobble_line(draw, (left, top - 2), (left - 2, bottom + 2), width=6, seed=1)

    # Stroke 2: 横折 (top horizontal + right vertical in one stroke).
    # Top horizontal — slight downward slope on the right in the GT.
    wobble_line(draw, (left - 3, top), (right + 3, top + 4), width=6, seed=2)
    # Right vertical — connect from the just-drawn top-right corner.
    wobble_line(draw, (right + 3, top + 4), (right, bottom - 2), width=6, seed=3)

    # Stroke 3: 横 (bottom closing horizontal). Slightly shorter than top in GT.
    wobble_line(draw, (left + 4, bottom), (right - 4, bottom - 2), width=6, seed=4)

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
