"""G1 render of radical 户 (4 strokes)."""
from PIL import Image, ImageDraw
import os, math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, width=6):
    # Draw a smooth polyline through control points (quadratic-ish via subdivision)
    if len(points) < 2:
        return
    # Interpolate with Catmull-Rom-ish smoothing
    pts = []
    n = len(points)
    for i in range(n - 1):
        p0 = points[i - 1] if i > 0 else points[i]
        p1 = points[i]
        p2 = points[i + 1]
        p3 = points[i + 2] if i + 2 < n else p2
        steps = 20
        for t in range(steps):
            u = t / steps
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * u
                      + (2*p0[0] - 5*p1[0] + 4*p2[0] - p3[0]) * u*u
                      + (-p0[0] + 3*p1[0] - 3*p2[0] + p3[0]) * u*u*u)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * u
                      + (2*p0[1] - 5*p1[1] + 4*p2[1] - p3[1]) * u*u
                      + (-p0[1] + 3*p1[1] - 3*p2[1] + p3[1]) * u*u*u)
            pts.append((x, y))
    pts.append(points[-1])
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        draw.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill="black")

# Stroke 1: 点 (dot) at top — small diagonal stroke sloping down-right
stroke([(115, 45), (145, 68)], width=8)

# Stroke 2: 横 (horizontal) — the top bar (short, tilted slightly up-right)
stroke([(100, 95), (205, 88)], width=6)

# Stroke 3: 横折 — inner horizontal + turn down forming right side of the 口
# Horizontal bar then vertical down with a small hook curl at the bottom
stroke([(115, 135), (205, 128), (210, 140), (200, 195)], width=6)

# Stroke 4: 撇 — long left-falling stroke starting near top-left of horizontal,
# sweeping through body and extending to bottom-left corner
stroke([(120, 95), (110, 150), (85, 210), (50, 270)], width=8)

out = os.path.join(os.path.dirname(__file__), "01_户.png")
img.save(out)
print(f"Saved {out}")
