"""
G1 no-memory attempt: 竖折撇 (vertical + turn-right + pie), as in 专.
Renders a 300x300 white-background, black-ink PNG using PIL.

Shape:
  1. 竖 (shu):  vertical stroke, starts upper-left, goes straight down.
  2. 折 (zhe):  short horizontal segment to the right at the bottom.
  3. 撇 (pie):  from the right end of the horizontal, sweeps down-left
                as a curved diagonal, tapering.
"""

from PIL import Image, ImageDraw

SIZE = 300
OUT = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_27_竖折撇/01_竖折撇.png"

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)

# ---- 1) 竖 (vertical) ----
# start near top-left of the character bounding area, drop straight down
x_v = 110
y_v_top = 70
y_v_bot = 200
w_v = 10  # vertical stroke thickness (slight taper at start)
# slight entry taper: draw as trapezoid via a few overlapping rectangles
for i, (y0, y1, w) in enumerate([
    (y_v_top, y_v_top + 15, 8),
    (y_v_top + 15, y_v_bot, w_v),
]):
    draw.rectangle([x_v - w // 2, y0, x_v + w // 2, y1], fill=INK)

# ---- 2) 折 (horizontal turn at the bottom) ----
# from bottom of vertical, extend to the right
x_h_left = x_v - w_v // 2
x_h_right = 215
y_h_top = y_v_bot - 10   # overlap with the vertical corner
y_h_bot = y_v_bot
draw.rectangle([x_h_left, y_h_top, x_h_right, y_h_bot], fill=INK)

# a small square at the corner joint for a crisp 折
draw.rectangle([x_h_right - 12, y_h_top - 2, x_h_right, y_h_bot + 2], fill=INK)

# ---- 3) 撇 (pie), curving down-left from the right end of the horizontal ----
# We draw a tapered curve using many small circles.
import math

start_x = x_h_right - 4
start_y = y_h_bot - 2
end_x = 95
end_y = 260

# Quadratic bezier control point pulls the curve down-and-right first,
# then swings left — gives the characteristic pie sweep.
ctrl_x = 210
ctrl_y = 255

N = 60
prev = None
for i in range(N + 1):
    t = i / N
    # quadratic bezier
    bx = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * ctrl_x + t * t * end_x
    by = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * ctrl_y + t * t * end_y
    # taper: thick at start, thin at tip
    r = max(1.2, 6.0 * (1 - t) + 1.0 * t)
    draw.ellipse([bx - r, by - r, bx + r, by + r], fill=INK)

img.save(OUT)
print(f"saved {OUT}  size={img.size}")
