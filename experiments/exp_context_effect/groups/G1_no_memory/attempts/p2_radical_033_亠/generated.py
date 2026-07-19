"""
G1 render for p2_radical_033_亠 (2 strokes), revision 1.

Structure:
  - Stroke 1: 点 (dian / dot) — short curved diagonal, top-center,
    curving from upper-left to lower-right like GT.
  - Stroke 2: 横 (heng / horizontal) — long, curved, dipping in the
    middle and rising on the right end (like GT).
"""

from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(points, width=6):
    """Draw a smooth polyline with round joins."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill="black", width=width)
    # Round caps at each vertex
    for p in points:
        r = width / 2
        draw.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill="black")


# --- Stroke 1: dian (dot) ---
# GT dot: curves gently, upper-left tail thin, lower-right head thicker.
# Model as small arc from ~(148, 108) curving down-right to ~(168, 138).
dot_pts = []
# Parametric arc — quadratic bezier-ish
for t in [0.0, 0.15, 0.3, 0.5, 0.7, 0.85, 1.0]:
    # p0 = (148,108), p1 (control) = (150,128), p2 = (170,138)
    x = (1 - t) ** 2 * 148 + 2 * (1 - t) * t * 150 + t ** 2 * 170
    y = (1 - t) ** 2 * 108 + 2 * (1 - t) * t * 128 + t ** 2 * 138
    dot_pts.append((x, y))
# Taper: thin at top, thick at bottom
for i in range(len(dot_pts) - 1):
    w = 3 + int(i * 0.9)  # 3..~8
    draw.line([dot_pts[i], dot_pts[i + 1]], fill="black", width=w)
# Rounded head
draw.ellipse((166, 134, 174, 142), fill="black")

# --- Stroke 2: heng (horizontal) ---
# GT heng: starts ~(55, 175), sags to ~(150, 190), rises to ~(250, 168).
# Small "start" tick at left, and right end lifts up.
heng_pts = []
p0 = (52, 178)
p1 = (150, 195)   # control (below middle for sag)
p2 = (252, 165)
for t in [i / 24 for i in range(25)]:
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    heng_pts.append((x, y))
# Draw with slightly varying width (thicker in middle, thinner at ends)
for i in range(len(heng_pts) - 1):
    # width envelope: 5 at ends, 7 in middle
    frac = i / (len(heng_pts) - 2)
    w = 5 + int(2 * math.sin(math.pi * frac))
    draw.line([heng_pts[i], heng_pts[i + 1]], fill="black", width=w)
# End caps: small round on left, slight "lift" thickening on right
draw.ellipse((48, 174, 58, 184), fill="black")
draw.ellipse((247, 161, 257, 171), fill="black")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_亠.png")
img.save(out_path)
print(f"Saved: {out_path}")
