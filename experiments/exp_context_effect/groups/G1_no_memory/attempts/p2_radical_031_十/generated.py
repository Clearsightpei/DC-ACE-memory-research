"""G1 render for p2_radical_031_十 (radical 十, 2 strokes).

Strokes:
  1) 横 (horizontal) — slight upward-then-flat, spanning most of the width,
     placed above vertical center.
  2) 竖 (vertical) — long straight vertical stroke, slightly right of horizontal
     center, with a small hook-like start (顿笔) at the top.

Renders to a 300x300 white-background PNG with black ink using PIL.
"""

import os
from PIL import Image, ImageDraw

SIZE = 300
INK = (0, 0, 0)
BG = (255, 255, 255)


def stroke(draw, pts, width):
    """Draw a polyline with rounded joins/ends."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=width)
    # Round the joints and endpoints
    r = width / 2
    for x, y in pts:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)

    w = 6  # stroke width

    # Horizontal 横: from left to right, slight rise on left-most tip, flat middle,
    # very slight droop at right end (mimics GT which has slight upward curve).
    horiz = [
        (55, 158),   # left tip (slightly lower)
        (75, 152),   # rises
        (150, 150),  # flat center
        (225, 152),
        (250, 158),  # slight droop right tip
    ]
    stroke(draw, horiz, w)

    # Vertical 竖: from top to bottom, slightly right of center, with small
    # angled entrance (顿笔) — a short segment leaning up-left before descending.
    vert = [
        (162, 70),   # top hook start (leans left-up)
        (155, 62),   # small hook cap
        (162, 70),   # back
        (160, 150),  # crossing horizontal
        (158, 250),  # bottom tip
    ]
    stroke(draw, vert, w)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_十.png")
    img.save(out_path)
    print(out_path)


if __name__ == "__main__":
    main()
