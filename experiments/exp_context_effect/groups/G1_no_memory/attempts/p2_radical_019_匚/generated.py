"""G1 render: 匚 (2-stroke radical).

Strokes (per MMH/standard order):
  1) 横 (top horizontal) — starts left-top, goes right.
  2) 竖折 (vertical-then-horizontal) — starts at left-top just below stroke 1,
     drops straight down, then turns right along the bottom.

Rendered at 300x300, white bg, black ink, via PIL.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
STROKE = 6

# Rough bounding box of the radical (matches GT: shifted slightly left of center,
# vertically middle-ish, occupies ~55% of frame).
LEFT   = 70
RIGHT  = 235
TOP    = 110
BOTTOM = 245

# Stroke 1: top horizontal (横). Slight downward tilt visible in GT is mild;
# draw essentially horizontal, thickening at the ends via double-pass.
# Small dip at the start (顿笔).
draw.line([(LEFT - 2, TOP + 4), (LEFT + 6, TOP)], fill=INK, width=STROKE)
draw.line([(LEFT + 6, TOP), (RIGHT, TOP + 2)], fill=INK, width=STROKE)

# Stroke 2: 竖折 — vertical down from just below stroke1's left end, then right along bottom.
# Vertical segment
draw.line([(LEFT, TOP + 2), (LEFT, BOTTOM)], fill=INK, width=STROKE)
# Horizontal bottom segment (the fold / 折)
draw.line([(LEFT, BOTTOM), (RIGHT - 5, BOTTOM - 2)], fill=INK, width=STROKE)

# Smooth the corner with a filled circle at the joint.
r = STROKE // 2
draw.ellipse([LEFT - r, BOTTOM - r, LEFT + r, BOTTOM + r], fill=INK)
draw.ellipse([LEFT - r, TOP - r, LEFT + r, TOP + r], fill=INK)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_匚.png")
img.save(out_path)
print(f"wrote {out_path}")
