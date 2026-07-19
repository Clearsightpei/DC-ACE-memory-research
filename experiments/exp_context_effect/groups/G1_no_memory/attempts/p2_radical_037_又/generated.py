"""Render 又 (radical, 2 strokes) to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke_curve(points, widths):
    """Draw a variable-width curve through points using linear interpolation."""
    n = len(points)
    # densify
    dense = []
    dense_w = []
    steps = 40
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        for s in range(steps):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            dense.append((x, y))
            dense_w.append(w)
    dense.append(points[-1])
    dense_w.append(widths[-1])
    for i, (x, y) in enumerate(dense):
        r = dense_w[i] / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# Stroke 1: 横撇 (horizontal-fold turning into a downward-left sweep)
# Start upper-left, horizontal to upper-right, then sharp turn down-left to lower-middle-left
s1_pts = [
    (90, 120),   # start (top-left)
    (110, 113),
    (150, 108),
    (190, 112),
    (205, 118),  # corner turn
    (200, 138),
    (175, 170),
    (140, 210),
    (110, 240),  # end lower-left
]
s1_w = [6, 8, 8, 8, 9, 8, 7, 6, 4]
stroke_curve(s1_pts, s1_w)

# Stroke 2: 捺 (right-falling stroke) — starts near the corner of 横撇, sweeps down-right
s2_pts = [
    (130, 140),  # start upper, near stroke1 corner region
    (155, 170),
    (180, 200),
    (210, 225),
    (235, 245),
    (250, 250),  # end lower-right, tapered
]
s2_w = [5, 7, 8, 9, 9, 4]
stroke_curve(s2_pts, s2_w)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_又.png")
img.save(out)
print(f"Saved {out}")
