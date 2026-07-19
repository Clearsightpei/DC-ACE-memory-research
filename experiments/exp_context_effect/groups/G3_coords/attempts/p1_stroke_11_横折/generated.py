"""
p1_stroke_11_横折 — heng-zhe (horizontal then 90° turn down)
G3 coord-bank format: draw with numeric offset coordinates via PIL
(turtle would require a display; PIL guarantees a clean 300x300 raster).

Shape: a horizontal stroke going right, then a corner, then a vertical
stroke going down. The vertical segment is slightly shorter than the
horizontal (typical calligraphic proportion for 横折 in a 折 shape).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Coordinates (image space: origin top-left, y grows down)
# Horizontal (heng): from (60, 90) to (230, 90)
# Then 90° down: from (230, 90) to (230, 225)
ink_w = 10  # stroke thickness

# Horizontal segment
x0, y0 = 60, 90
x1, y1 = 230, 90
draw.line([(x0, y0), (x1, y1)], fill="black", width=ink_w)

# Vertical segment (starts at end of horizontal, goes down)
x2, y2 = 230, 90
x3, y3 = 230, 225
draw.line([(x2, y2), (x3, y3)], fill="black", width=ink_w)

# Round the corner cap so the join looks like a brush turn (avoid a
# hollow miter). Draw a small filled circle at the corner.
r = ink_w // 2
draw.ellipse([(x2 - r, y2 - r), (x2 + r, y2 + r)], fill="black")

# End caps rounded too
draw.ellipse([(x0 - r, y0 - r), (x0 + r, y0 + r)], fill="black")
draw.ellipse([(x3 - r, y3 - r), (x3 + r, y3 + r)], fill="black")

out_path = os.path.join(os.path.dirname(__file__), "01_横折.png")
img.save(out_path)
print(f"Wrote {out_path} ({W}x{H})")
