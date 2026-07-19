"""G1 render of radical 小 (3画).

Three strokes:
  1. 竖钩 (center): vertical descending, small hook curling left at bottom.
  2. 撇 (left):  diagonal downward-left dot/stroke.
  3. 点 (right): short arc-shaped dot curving down-right.

Output: 01_小.png, 300x300 white bg, black ink.
"""

import os
from PIL import Image, ImageDraw


W, H = 300, 300
OUT = os.path.join(os.path.dirname(__file__), "01_小.png")


def draw_polyline(draw, pts, width):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=0, width=width)
    for p in pts:
        draw.ellipse([p[0] - width / 2, p[1] - width / 2,
                      p[0] + width / 2, p[1] + width / 2], fill=0)


def main():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)

    ink = 7

    # Stroke 1: 竖钩 -- vertical bar with a clear left-curling hook at bottom.
    vpts = [
        (152, 85),
        (151, 120),
        (150, 160),
        (149, 200),
        (148, 235),
        (144, 250),
        (135, 255),
        (122, 253),
    ]
    draw_polyline(d, vpts, ink)

    # Stroke 2: 撇 -- upper-right to lower-left, slight rightward-concave curve.
    lpts = [
        (120, 150),
        (112, 165),
        (102, 185),
        (90, 210),
        (78, 235),
    ]
    draw_polyline(d, lpts, ink)

    # Stroke 3: 点 -- curving arc, concave toward the center, descending down-right.
    rpts = [
        (180, 155),
        (188, 170),
        (198, 188),
        (210, 205),
        (220, 218),
    ]
    draw_polyline(d, rpts, ink)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
