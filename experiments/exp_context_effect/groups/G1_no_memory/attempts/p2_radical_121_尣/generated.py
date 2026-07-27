"""G1 render of radical 尣 (4 strokes) to a 300x300 PNG.

Revised. GT structure: two small detached top marks (short 撇 upper-left,
short curved stroke upper-right) — these are the "eyes" / horns of the
radical, above the body. Then a 儿-like base: a long 撇 down-left and a
竖弯钩 down-right, meeting near the top-center at a small horizontal.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 6


def poly(points, width=TH):
    draw.line(points, fill=INK, width=width, joint="curve")
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def curve(p0, p1, p2, steps=40, width=TH):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    poly(pts, width=width)


# Stroke 1: small top-left 撇 (detached, above the body)
curve((120, 80), (110, 92), (95, 110), width=TH)

# Stroke 2: small top-right curved stroke (detached, mirror-ish)
curve((195, 80), (205, 100), (200, 118), width=TH)

# Stroke 3: long 撇 — starts near top-center, sweeps down-left to bottom
curve((150, 115), (115, 185), (70, 255), width=TH)

# Stroke 4: 竖弯钩 — starts at same top-center joint, drops down,
# curves right along the bottom, then a small hook upward.
# Modeled as a polyline for the vertical, then a bezier for the turn.
# Vertical segment
poly([(155, 120), (168, 175), (180, 220)], width=TH)
# horizontal turn + hook
curve((180, 220), (200, 255), (240, 250), width=TH)
# tiny upward hook at right end
poly([(240, 250), (243, 235)], width=TH)


out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_尣.png")
img.save(out_path)
print(f"wrote {out_path}")
