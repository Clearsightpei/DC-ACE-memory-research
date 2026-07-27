"""Render 冫 (ice radical / two-dots-water) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 冫 in GT sits on the LEFT half of the frame. Two "dian" (dots):
#   Upper: short, curves from upper-right down to lower-left (like a small comma).
#   Lower: longer, curves from upper-right down to lower-left with more pronounced arc.

def stroke(points, width_start, width_end, steps=60):
    """Quadratic bezier tapered stroke."""
    (x0, y0), (x1, y1), (x2, y2) = points
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        w = width_start + (width_end - width_start) * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# Upper stroke: short, positioned roughly (135, 95) -> (115, 130)
# GT shows it as a small arc curving down-left
stroke([(140, 95), (138, 115), (118, 135)], width_start=4, width_end=8)

# Lower stroke: longer, positioned roughly (150, 170) -> (105, 245)
# GT shows more pronounced curve, tapering wider then thinner toward tip
stroke([(155, 170), (140, 205), (108, 250)], width_start=4, width_end=10)

out_path = os.path.join(os.path.dirname(__file__), "01_冫.png")
img.save(out_path)
print(f"Saved {out_path}")
