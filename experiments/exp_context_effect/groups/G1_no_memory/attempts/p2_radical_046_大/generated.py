"""Render 大 (radical) as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, widths):
    """Draw a variable-width stroke through points using circles between segments."""
    n = len(points)
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# Stroke 1: 横 — horizontal, slight upward slant, thicker at ends
# Roughly from (60, 145) to (245, 138)
horiz_pts = [(60, 148), (100, 144), (160, 141), (210, 140), (245, 140)]
horiz_w = [7, 8, 8, 8, 9]
stroke(horiz_pts, horiz_w)

# Stroke 2: 撇 — starts up-right area, curves down to lower-left
# Top of 撇 is around (168, 60), sweeps through the horizontal crossing
# near (150, 145), then curves out to lower-left (60, 260).
pie_pts = [
    (172, 62),
    (168, 78),
    (162, 100),
    (155, 125),
    (148, 148),
    (135, 180),
    (115, 215),
    (90, 245),
    (65, 265),
]
pie_w = [9, 10, 10, 9, 8, 7, 6, 5, 3]
stroke(pie_pts, pie_w)

# Stroke 3: 捺 — starts near the horizontal-撇 intersection, sweeps down-right
# Starts around (155, 145), curves out to (255, 265) with a flat tail.
na_pts = [
    (155, 150),
    (170, 175),
    (188, 200),
    (208, 225),
    (228, 248),
    (248, 260),
    (260, 262),
]
na_w = [5, 7, 9, 11, 12, 10, 4]
stroke(na_pts, na_w)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_大.png"))
