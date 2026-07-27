"""Render 幺 (yao) to a 300x300 PNG.

幺 has 3 strokes:
  1) 撇折 (upper small): short curved piě folding into a tiny hook
  2) 撇折 (lower larger): long piě curving from upper-right down-left, folding
     back to the right in a broad curve — the main body of the character
  3) 点 (dot) at bottom-right

Rendered with PIL for smooth 300x300 output.
"""

from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def smooth_curve(control_pts, width=5, samples=80):
    """Draw a smooth curve approximated by sampling between control points.

    Uses simple Catmull-Rom style interpolation across the control points.
    """
    n = len(control_pts)
    if n < 2:
        return
    # Duplicate endpoints for Catmull-Rom
    pts = [control_pts[0]] + list(control_pts) + [control_pts[-1]]

    def cr(p0, p1, p2, p3, t):
        # Catmull-Rom spline
        t2 = t * t
        t3 = t2 * t
        x = 0.5 * ((2 * p1[0]) +
                   (-p0[0] + p2[0]) * t +
                   (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                   (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
        y = 0.5 * ((2 * p1[1]) +
                   (-p0[1] + p2[1]) * t +
                   (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                   (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
        return (x, y)

    curve = []
    for i in range(len(pts) - 3):
        for s in range(samples):
            t = s / samples
            curve.append(cr(pts[i], pts[i + 1], pts[i + 2], pts[i + 3], t))
    curve.append(control_pts[-1])

    for i in range(len(curve) - 1):
        draw.line([curve[i], curve[i + 1]], fill=BLACK, width=width)
    for p in curve:
        draw.ellipse([p[0] - width / 2, p[1] - width / 2,
                      p[0] + width / 2, p[1] + width / 2], fill=BLACK)


# Stroke 1: upper 撇折 (small) — top-right area, short piě + tiny turn
s1 = [
    (180, 55),
    (165, 75),
    (150, 100),
    (140, 118),
    (150, 122),
    (168, 118),
]
smooth_curve(s1, width=5)

# Stroke 2: lower 撇折 (large) — the main body. Starts upper-right (~ where s1 ended
# in vertical alignment but slightly lower and right), curves broadly down-left,
# then sweeps back to the right along the bottom.
s2 = [
    (195, 105),
    (170, 140),
    (135, 175),
    (105, 210),
    (100, 235),
    (130, 250),
    (170, 255),
    (210, 250),
    (235, 240),
]
smooth_curve(s2, width=5)

# Stroke 3: 点 — small tapered dot bottom-right
d_pts = [
    (225, 245),
    (238, 260),
    (248, 278),
]
for i in range(len(d_pts) - 1):
    # Taper: start thin, get thicker
    w = 4 + i * 2
    draw.line([d_pts[i], d_pts[i + 1]], fill=BLACK, width=w)
for p in d_pts:
    draw.ellipse([p[0] - 3, p[1] - 3, p[0] + 3, p[1] + 3], fill=BLACK)

out = os.path.join(os.path.dirname(__file__), "01_幺.png")
img.save(out)
print(f"Wrote {out}")
