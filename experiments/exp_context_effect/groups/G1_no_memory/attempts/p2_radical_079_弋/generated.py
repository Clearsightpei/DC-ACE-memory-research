"""G1 render: 弋 (radical, 3 strokes) — revised.

Revisions from pass 1:
  - 斜钩 is now curved (belly to the left, sweeping to a lower-right hook)
    with a longer/rounder hook, matching the GT.
  - 横 given a gentle upward arc.
  - 点 rendered as a short arced dash rather than a hard corner.
"""
from PIL import Image, ImageDraw
import math
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width_start, width_end, steps=80):
    """Draw a variable-width stroke as filled circles along interpolated segments."""
    dense = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        for t in range(steps):
            u = t / steps
            dense.append((x0 + (x1 - x0) * u, y0 + (y1 - y0) * u))
    dense.append(points[-1])
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        u = i / max(1, n - 1)
        r = (width_start + (width_end - width_start) * u) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def bezier(p0, p1, p2, p3, n=40):
    """Cubic Bezier sample points."""
    pts = []
    for i in range(n + 1):
        t = i / n
        x = ((1 - t) ** 3) * p0[0] + 3 * ((1 - t) ** 2) * t * p1[0] \
            + 3 * (1 - t) * (t ** 2) * p2[0] + (t ** 3) * p3[0]
        y = ((1 - t) ** 3) * p0[1] + 3 * ((1 - t) ** 2) * t * p1[1] \
            + 3 * (1 - t) * (t ** 2) * p2[1] + (t ** 3) * p3[1]
        pts.append((x, y))
    return pts


# --- Stroke 1: 横 — gentle upward-arced horizontal, crossing left of center ---
s1 = bezier((55, 162), (85, 155), (125, 150), (162, 148), n=30)
stroke(s1, 7, 7, steps=6)

# --- Stroke 2: 斜钩 (xie-gou) — long S-curve down to lower-right, then hook ---
# Body: curve with belly to the left, sweeping down-right.
body = bezier((110, 75), (110, 140), (160, 200), (215, 255), n=50)
stroke(body, 9, 9, steps=6)
# Hook: from the end of the body, sweep upward-right.
hook = bezier((215, 255), (220, 250), (228, 240), (238, 228), n=20)
stroke(hook, 9, 3, steps=6)

# --- Stroke 3: 点 — short arced dash, top-right ---
dot = bezier((188, 82), (194, 92), (200, 100), (208, 105), n=20)
stroke(dot, 5, 9, steps=6)

out_path = os.path.join(os.path.dirname(__file__), "01_弋.png")
img.save(out_path)
print(f"Wrote {out_path}")
