"""G1 render for p2_radical_003_丿 (撇, left-falling stroke).

Renders a 300x300 PNG: white bg, black ink. Approximates the GT shape:
starts upper-center with a small right-hook top, curves down and to the
lower-left, thicker in the belly, tapering slightly at the tail.
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
OUT_PATH = os.path.join(os.path.dirname(__file__), "01_丿.png")


def quad_bezier(p0, p1, p2, steps=200):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def main():
    img = Image.new("RGB", (SIZE, SIZE), "white")
    draw = ImageDraw.Draw(img)

    # Main 撇 curve: from upper-center down to lower-left, arcing left.
    # GT shape: starts near upper-center, briefly angles slightly right at
    # the very top (the 顿笔 head), then sweeps down-left with a smooth
    # concave-right arc, ending near lower-left.
    # In image coords (y grows DOWN).
    p0 = (155, 85)     # top start (upper-center, slight right of center)
    p1 = (170, 175)    # control biased right to create concave-right arc
    p2 = (70, 265)     # bottom-left tail

    pts = quad_bezier(p0, p1, p2, steps=260)

    # Draw with tapered width: fuller in belly, tapering to thin at tail.
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        # Width profile: fairly full at head (blunt 顿笔), thickest ~t=0.35,
        # tapering to a point at the tail.
        if t < 0.35:
            width = 6.0 + 2.0 * (t / 0.35)  # 6 -> 8
        else:
            width = 8.0 - 6.5 * ((t - 0.35) / 0.65)  # 8 -> 1.5
        r = width / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

    # Small "head" cap: GT shows a subtle rounded top (like a tiny nub).
    # A single filled circle at p0 gives a clean rounded head without a loop.
    hx, hy = p0
    draw.ellipse((hx - 4, hy - 4, hx + 4, hy + 4), fill="black")

    img.save(OUT_PATH)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
