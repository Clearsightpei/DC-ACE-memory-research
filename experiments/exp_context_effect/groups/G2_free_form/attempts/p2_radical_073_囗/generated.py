"""
p2_radical_073_囗 (3-stroke enclosure radical)

Structure (canonical MMH stroke order):
  1. 竖 (left vertical) - top to bottom on the left
  2. 横折 (top + right vertical) - horizontal across the top, folds down to the bottom-right
  3. 横 (bottom horizontal) - bottom edge, closes the box

Shared-corner discipline (bootstrap principle 2): stroke 2 begins at the
top-left corner where stroke 1's top sits (shares corner pixel). Stroke 3
runs across the bottom, meeting/passing through the bottom endpoints of
strokes 1 and 2 (shared corners at both bottom corners).

Slight brush/handwritten feel: subtle 顿 press at start of each stroke,
uniform mid-stroke radius, tiny press at ends. All corners share pixels
(no inset), producing a closed square-ish silhouette that matches the GT.

Canvas: 300x300 white, black ink, PIL brush-dab technique.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def linear_stroke(p0, p1, r_start, r_end, steps=400, start_press=None, end_press=None):
    x0, y0 = p0
    x1, y1 = p1
    if start_press is not None:
        dab(x0, y0, start_press)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)
    if end_press is not None:
        dab(x1, y1, end_press)


# Layout: leave ~55 px margin on left, right, top, bottom so the box
# fills the middle of the canvas.
LEFT = 60
RIGHT = 240
TOP = 60
BOT = 240

R_BODY = 5      # main stroke radius
R_PRESS = 7     # 顿 press radius at starts / corners

# Stroke 1: 竖 (left vertical), top-left -> bottom-left
linear_stroke(
    (LEFT, TOP), (LEFT, BOT),
    r_start=R_BODY, r_end=R_BODY,
    start_press=R_PRESS, end_press=R_PRESS,
)

# Stroke 2: 横折 (top horizontal + right vertical)
# Beat A: 横 across the top - shares top-left corner with stroke 1.
linear_stroke(
    (LEFT, TOP), (RIGHT, TOP),
    r_start=R_BODY, r_end=R_BODY,
    start_press=R_PRESS, end_press=None,
)
# Shoulder dab at top-right corner (折 shoulder, slightly larger)
dab(RIGHT, TOP, R_BODY + 2)
# Beat B: 竖 down the right - shares top-right corner with beat A.
linear_stroke(
    (RIGHT, TOP), (RIGHT, BOT),
    r_start=R_BODY, r_end=R_BODY,
    start_press=None, end_press=R_PRESS,
)

# Stroke 3: 横 across the bottom, closing the box.
# Shares bottom-left with stroke 1's end and bottom-right with stroke 2's end.
linear_stroke(
    (LEFT, BOT), (RIGHT, BOT),
    r_start=R_BODY, r_end=R_BODY,
    start_press=R_PRESS, end_press=R_PRESS,
)

img.save("01_囗.png")
print("wrote 01_囗.png")
