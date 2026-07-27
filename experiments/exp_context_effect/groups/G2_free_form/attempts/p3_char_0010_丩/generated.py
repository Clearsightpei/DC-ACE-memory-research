"""Render 丩 (jiū) at 300x300, black ink on white.

Character analysis from GT:
- Two strokes.
- LEFT stroke: a 竖折-like shape — starts as a short descending
  segment from about (95, 130) going down and curving right at bottom
  (~(115, 175)), then rising back up-right briefly. It reads as a
  small "U" or hook on the left.
  Actually per closer look at GT: left mark is like a small hook —
  short 撇-into-curve that ends with a rising flick.
- RIGHT stroke: a LONG straight vertical from top (~y=55) to bottom
  (~y=255), located at ~x=185. It has a small hook at the very top
  going up-left (like a mini 顿-turn).

We render with PIL for clean lines.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=6):
    """Draw a thick smooth polyline."""
    d.line(points, fill=BLACK, width=width, joint="curve")
    # dab endpoints for a smoother look
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Right stroke: long vertical with tiny top hook going up-left ---
# The top hook: a small angle from up-left to the top of the vertical
right_top_hook = [
    (175, 62),   # start of tiny hook (upper-left curl)
    (188, 55),   # top of vertical, curl point
]
stroke(right_top_hook, width=6)

# Main long vertical (right stroke body)
right_vertical = [
    (188, 55),
    (188, 130),
    (188, 200),
    (188, 258),
]
stroke(right_vertical, width=7)


# --- Left stroke: 竖折 / U-shape that rises high on the right ---
# GT shows left mark starts high (~y=140), descends and curves at
# bottom (~y=210), then rises steeply up-right ending near y=150
# (nearly as high as it started). More like a "U" tilted right.
left_stroke = [
    (95, 140),    # top-left start
    (95, 175),
    (102, 200),
    (115, 215),   # bottom of the U
    (135, 218),   # bottom curl passing through
    (150, 205),   # rising up-right
    (158, 175),   # continuing up
    (162, 148),   # end of the rising flick — nearly at start height
]
stroke(left_stroke, width=6)


out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_丩.png")
img.save(out_path)
print(f"Wrote {out_path}")
