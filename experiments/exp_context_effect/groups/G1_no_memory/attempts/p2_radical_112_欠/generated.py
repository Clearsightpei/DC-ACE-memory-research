"""Render 欠 (4-stroke radical) at 300x300 PNG with PIL.

Revision 2 — adjusted to better match GT:
- Wider, more separated top structure (stroke 1 distinctly left of stroke 2)
- Head 'ク' more open
- 撇 (stroke 3) and 捺 (stroke 4) longer, meeting near the middle,
  extending further to fill the character space
"""

from PIL import Image, ImageDraw
import os

OUT_PATH = os.path.join(os.path.dirname(__file__), "01_欠.png")
SIZE = 300
BG = "white"
INK = "black"

img = Image.new("RGB", (SIZE, SIZE), BG)
draw = ImageDraw.Draw(img)


def polyline(points, width=6):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    for p in points:
        r = width / 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=INK)


def tapered(points, w_start=5, w_end=10):
    n = len(points) - 1
    for i in range(n):
        t = i / max(n - 1, 1)
        w = int(w_start + (w_end - w_start) * t)
        draw.line([points[i], points[i + 1]], fill=INK, width=w)
    for i, p in enumerate(points):
        t = i / max(n, 1)
        r = (w_start + (w_end - w_start) * t) / 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=INK)


# Stroke 1: short 撇 (small tick at top-left of the head)
# In GT this is a small slanted stroke, clearly separated from the head-corner
s1 = [(120, 70), (110, 85), (102, 100)]
polyline(s1, width=6)

# Stroke 2: 横折撇 forming the 'ク'-like head of 欠
# horizontal-ish going right, then corner, then curve down-left
s2 = [
    (130, 75),
    (155, 72),
    (180, 75),
    (198, 88),   # corner (turn point)
    (196, 108),
    (185, 130),
    (170, 150),
    (150, 168),
]
polyline(s2, width=6)

# Stroke 3: 撇 — long left-down curve
# Starts near the intersection under the head, sweeps down-left to bottom-left area
s3 = [
    (158, 148),
    (148, 168),
    (130, 195),
    (105, 225),
    (78, 255),
    (60, 272),
]
polyline(s3, width=6)

# Stroke 4: 捺 — long right-down sweep (thick, flaring)
# Starts at same neck area, sweeps down-right to bottom-right corner, flare at end
s4 = [
    (158, 150),
    (175, 175),
    (195, 205),
    (218, 235),
    (240, 262),
    (252, 275),
]
tapered(s4, w_start=5, w_end=11)

img.save(OUT_PATH)
print(f"Wrote {OUT_PATH}")
