"""Render 日 (radical, 4 strokes) to a 300x300 PNG.

Stroke plan (image coords, y grows DOWN):
  1. 竖 (left vertical): left wall of the box, top → bottom.
  2. 横折 (top + right vertical): top 横 across, shoulder, then 竖 down
     to the bottom-right corner. Blunt terminal (no hook).
  3. 横 (middle): interior horizontal across the middle.
  4. 横 (bottom): bottom 横 closing the box, spanning left→right walls.

Looking at the GT: the character is tall and narrow, slightly taller
than wide. The middle 横 does not touch the right wall (short interior
stroke). The top 横折 shows a slight overhang / notch at the top-left
where 横 sits atop 竖. The bottom 横 spans the full width.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        steps = max(60, int(math.hypot(x1 - x0, y1 - y0) * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# Box corners (tall & narrow). Canvas 300x300.
LEFT = 95
RIGHT = 210
TOP = 55
BOT = 260

R = 5.0  # main stroke radius
JOINT = R + 2

# ---- Stroke 1: 竖 (left vertical), top-left → bottom-left
dab(LEFT, TOP, R + 1)  # small 顿 at top
line_dabs(LEFT, TOP, LEFT, BOT, R, R)
dab(LEFT, BOT, R + 1)

# ---- Stroke 2: 横折 (top horizontal + right vertical)
# top 横: from top-left (shares corner with 竖) to top-right, tiny up-tilt
top_left_x, top_left_y = LEFT, TOP
top_right_x, top_right_y = RIGHT, TOP - 3  # tiny lift for calligraphic tilt

# 顿 at start of 横 (shared with stroke 1 top)
dab(top_left_x, top_left_y, JOINT)
line_dabs(top_left_x, top_left_y, top_right_x, top_right_y, R, R)
# shoulder dab
dab(top_right_x, top_right_y, JOINT)
# 竖 (right vertical) down to bottom-right, straight down
right_bot_x, right_bot_y = RIGHT, BOT
line_dabs(top_right_x, top_right_y, right_bot_x, right_bot_y, R, R)
dab(right_bot_x, right_bot_y, R + 1)  # blunt terminal (no hook)

# ---- Stroke 3: 横 (middle) — interior horizontal
# In GT the middle 横 sits noticeably ABOVE geometric center — upper third.
mid_y = 140
mid_left_x = LEFT + 8   # starts just inside left wall
mid_right_x = RIGHT - 12  # doesn't quite touch right wall (per GT)
dab(mid_left_x, mid_y, R + 1)
line_dabs(mid_left_x, mid_y, mid_right_x, mid_y - 2, R, R)
dab(mid_right_x, mid_y - 2, R + 1)

# ---- Stroke 4: 横 (bottom) — closes the box across full width
# spans between the two verticals; small 顿 both ends
bot_left_x, bot_left_y = LEFT, BOT
bot_right_x, bot_right_y = RIGHT, BOT
dab(bot_left_x, bot_left_y, JOINT)
line_dabs(bot_left_x, bot_left_y, bot_right_x, bot_right_y, R, R)
dab(bot_right_x, bot_right_y, JOINT)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_114_日/01_日.png"
)
