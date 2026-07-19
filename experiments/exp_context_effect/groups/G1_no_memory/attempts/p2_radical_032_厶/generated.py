"""Render 厶 (radical, 2 strokes) as 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
TH = 6

def smooth_curve(points, thickness=TH):
    n = len(points)
    if n < 2:
        return
    dense = []
    steps = 24
    for i in range(n - 1):
        p0 = points[max(i - 1, 0)]
        p1 = points[i]
        p2 = points[i + 1]
        p3 = points[min(i + 2, n - 1)]
        for t in range(steps):
            u = t / steps
            x = 0.5 * ((2 * p1[0]) +
                      (-p0[0] + p2[0]) * u +
                      (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * u * u +
                      (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * u * u * u)
            y = 0.5 * ((2 * p1[1]) +
                      (-p0[1] + p2[1]) * u +
                      (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * u * u +
                      (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * u * u * u)
            dense.append((x, y))
    dense.append(points[-1])
    for i in range(len(dense) - 1):
        draw.line([dense[i], dense[i + 1]], fill=INK, width=thickness)
    for p in dense:
        draw.ellipse([p[0] - thickness / 2, p[1] - thickness / 2,
                      p[0] + thickness / 2, p[1] + thickness / 2], fill=INK)

# Stroke 1: 撇折 (top)
# Start upper-right area, sweep down-left with a curve (撇), then fold and
# short horizontal-rightward stroke (折).
# Matching GT: the pie has a slight arc, endpoint of fold is around center.
pie = [
    (175, 100),
    (165, 115),
    (150, 135),
    (135, 155),   # pie endpoint / fold vertex
]
smooth_curve(pie, TH)

fold = [
    (135, 155),
    (155, 152),
    (180, 150),
]
smooth_curve(fold, TH)

# Stroke 2: long 撇捺-like bottom sweep. In GT this is one stroke that
# starts up-right of pie's endpoint, sweeps down-left in an arc, then
# curls back up-right (like a wide U). Actually looking again: it's
# more like a broad shallow curve from left across to right, ending
# with a rising tip on the right (捺).
bottom = [
    (80, 200),    # left tip start
    (100, 220),
    (135, 235),
    (170, 235),
    (200, 220),
    (220, 200),   # right end rising up
]
smooth_curve(bottom, TH)

out_path = os.path.join(os.path.dirname(__file__), "01_厶.png")
img.save(out_path)
print(f"Saved {out_path}")
