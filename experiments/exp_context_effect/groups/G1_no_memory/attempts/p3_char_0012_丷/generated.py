"""Render 丷 (inverted-八, two dots)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# 丷 = two small dots slanting inward-down, positioned in the middle band.
# Left dot: short stroke going down-left (like 丶 mirrored / 撇 short).
# Right dot: short stroke going down-right (like 丶).
# In GT they're roughly in the vertical center, forming an inverted-V gap.

def tapered_stroke(draw, p0, p1, w0, w1, steps=40):
    """Draw a line tapered from width w0 at p0 to w1 at p1 using overlapping circles."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# Left stroke (丿-like short pie): starts upper-right, ends lower-left
# GT shows it slightly higher and shorter, curved
def curved_stroke(draw, points, widths):
    """Draw a stroke through a series of points with varying widths."""
    n = len(points)
    for i in range(n - 1):
        p0 = points[i]
        p1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        tapered_stroke(draw, p0, p1, w0, w1, steps=15)

# 丷 = two divergent dots at top. In GT:
#   Left stroke: short curved dot, thin top slanting down-RIGHT (a left-dot 丶 that curves).
#     Looking at GT: the left stroke curves from upper-right to lower-left-ish,
#     appearing like a comma/left-dot.
#   Right stroke: a 丿 pie going from upper-left down to lower-right, tapering.
#     Wait — looking again: right stroke goes from upper-LEFT down to lower-RIGHT,
#     ending in a taper (like a mirror of pie, i.e., 捺 or a right-slanting pie).

# Based on GT: Left stroke = short curve ending down-left, thick at bottom.
# Left dot (丶 left-leaning): thin start upper-right, thick middle, taper lower-left
left_pts = [(125, 148), (118, 158), (108, 170), (100, 178)]
left_widths = [5, 8, 8, 3]
curved_stroke(draw, left_pts, left_widths)

# Right stroke (丿 short pie or right-slanting dot): thin start upper-left,
# thickening as it goes down-right, tapered at end
right_pts = [(165, 148), (172, 158), (182, 170), (192, 180)]
right_widths = [5, 7, 8, 3]
curved_stroke(draw, right_pts, right_widths)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_丷.png")
img.save(out_path)
print(f"Saved: {out_path}")
