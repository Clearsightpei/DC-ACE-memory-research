"""Render 丷 (radical) to a 300x300 PNG using PIL.

丷 = two small strokes:
  - Left: 点 (dot) slanting down-right, on the left
  - Right: 撇 (short pie) slanting down-left, on the right
Both are in the upper-middle region, spaced apart, tips point outward
(top) and bottoms angle toward center.
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def tapered_stroke(draw, x0, y0, x1, y1, w_start, w_end, steps=40):
    """Draw a straight stroke with varying width from w_start to w_end."""
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = w_start + (w_end - w_start) * ((t0 + t1) / 2)
        draw.line([(xa, ya), (xb, yb)], fill=BLACK, width=int(round(w)))
        draw.ellipse([xa - w / 2, ya - w / 2, xa + w / 2, ya + w / 2], fill=BLACK)
    # end cap
    w = w_end
    draw.ellipse([x1 - w / 2, y1 - w / 2, x1 + w / 2, y1 + w / 2], fill=BLACK)


# Left stroke: 点 — short comma-like dot, slanting down-right slightly.
# GT shows it as a small curved dot in the upper-left region.
# Start thin at top-left, thicken/curve to lower-right.
def curved_dot(draw, cx, cy, length=28, angle_deg=35, w_start=3, w_end=8, steps=30):
    import math
    rad = math.radians(angle_deg)
    for i in range(steps):
        t = i / steps
        # slight curve: use a quadratic offset
        curve = 3 * math.sin(math.pi * t)
        px = cx + length * t * math.cos(rad) - curve * math.sin(rad)
        py = cy + length * t * math.sin(rad) + curve * math.cos(rad)
        w = w_start + (w_end - w_start) * t
        draw.ellipse([px - w / 2, py - w / 2, px + w / 2, py + w / 2], fill=BLACK)

# Left 点: positioned around (100, 145), slanting down-right
curved_dot(draw, 100, 138, length=32, angle_deg=40, w_start=3, w_end=8)

# Right stroke: 撇 — starts upper-right, sweeps down-left, tapers to point.
# GT: starts around (200, 138), ends around (170, 178).
tapered_stroke(draw, 205, 135, 168, 180, w_start=8, w_end=2)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_丷.png")
img.save(out)
print(f"Saved: {out}")
