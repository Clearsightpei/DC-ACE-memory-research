"""Render 爻 (4画 radical) as 300x300 PNG using PIL.

爻 = two 乂 stacked vertically. Each 乂 has:
  - 撇 (pie): from upper-right to lower-left, tapering
  - 捺 (na): from upper-left to lower-right, thicker at end
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def taper_stroke(draw, p0, p1, w0, w1, steps=60):
    """Draw a straight tapered stroke from p0 to p1 with widths w0->w1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = w0 + (w1 - w0) * ((t0 + t1) / 2)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=int(round(w)))


def curved_stroke(draw, p0, p1, ctrl, w0, w1, steps=80):
    """Quadratic bezier tapered stroke."""
    x0, y0 = p0
    x1, y1 = p1
    cx, cy = ctrl
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1
        pts.append((x, y))
    for i in range(steps):
        w = w0 + (w1 - w0) * (i / steps)
        draw.line([pts[i], pts[i + 1]], fill="black", width=int(round(w)))
        # dot at joint
        r = max(1, int(round(w / 2)))
        draw.ellipse(
            [pts[i][0] - r, pts[i][1] - r, pts[i][0] + r, pts[i][1] + r],
            fill="black",
        )


# --- Top 乂 ---
# 撇 (pie): top-right -> bottom-left, curved, tapers thin at end
curved_stroke(draw, (180, 50), (90, 150), ctrl=(155, 90), w0=7, w1=2)
# 捺 (na): top-left -> bottom-right, curved, thickens toward end
curved_stroke(draw, (110, 65), (200, 150), ctrl=(140, 100), w0=3, w1=8)

# --- Bottom 乂 (larger, spread wider) ---
# 撇: top-right -> bottom-left, longer curve
curved_stroke(draw, (200, 160), (60, 265), ctrl=(155, 210), w0=8, w1=2)
# 捺: top-left -> bottom-right
curved_stroke(draw, (100, 170), (245, 265), ctrl=(150, 215), w0=3, w1=9)

out_path = os.path.join(os.path.dirname(__file__), "01_爻.png")
img.save(out_path)
print(f"Saved: {out_path}")
