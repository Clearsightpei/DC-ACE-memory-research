"""Render 巾 (radical, 3 strokes) as 300x300 PNG.

Structure per label + GT observation:
  Stroke 1: 竖 (short) — left vertical of the "mouth" box.
            In this radical the left stroke starts a bit above the top
            horizontal (a small vertical/slight slant nub), then drops
            down as the left side of the box.
  Stroke 2: 横折钩 — top horizontal + shoulder + right vertical.
            (In 巾 the right vertical ends blunt in most fonts, but
             MMH renders a subtle down-turn; we do a blunt end for
             clean identity, no hook flick.)  Reading GT: no hook.
            → render as 横折 (blunt).
  Stroke 3: 竖 — long central vertical piercing through, extending
            noticeably BELOW the box bottom (this is 巾's signature).

Canvas: 300x300 white, black ink.  PIL brush-dab technique.
"""
import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -------- Layout (image coords, y grows DOWN) --------
# Box is roughly:
#   top y ≈ 90
#   bottom y ≈ 220
#   left x ≈ 90
#   right x ≈ 205
# Central 竖 x ≈ 150, y from ≈ 80 down to ≈ 275
LEFT_X = 90
RIGHT_X = 205
TOP_Y = 95
BOT_Y = 220
CENTER_X = 150

R = 5.0     # base stroke radius
R_JOINT = R + 2.5  # shoulder / joint press
R_START = R + 2.0  # 顿笔 start press

# ---------- Stroke 1: left 竖/short-撇 ----------
# Per GT: shorter than the box, slight left-lean (mild 撇 feel),
# ends around mid-box, does NOT reach box bottom.  Slight taper.
s1_x0, s1_y0 = LEFT_X + 8, TOP_Y - 8
s1_x1, s1_y1 = LEFT_X - 4, BOT_Y - 25
dab(s1_x0, s1_y0, R_START)
line_dabs(s1_x0, s1_y0, s1_x1, s1_y1, R, R - 1.5)
dab(s1_x1, s1_y1, R - 1)  # tapered end

# ---------- Stroke 2: 横折 (top horizontal + right vertical), blunt ----------
# 2a: 横 from just left of stroke 1's top down to right side, slight up-tilt
h_x0, h_y0 = LEFT_X - 5, TOP_Y + 2  # start slightly left of/at stroke 1
h_x1, h_y1 = RIGHT_X, TOP_Y - 3      # slight up-tilt to the right
dab(h_x0, h_y0, R_START)
line_dabs(h_x0, h_y0, h_x1, h_y1, R, R + 0.5)
# 2b: shoulder dab at the corner
dab(h_x1, h_y1, R_JOINT)
# 2c: right 竖 with a subtle inward curve at the bottom (mild hook feel,
# per GT which shows the right vertical curving inward as it descends).
# Model as a shallow quadratic Bezier from shoulder to bottom-left-of-anchor.
v_x0, v_y0 = h_x1, h_y1
v_x1, v_y1 = RIGHT_X - 20, BOT_Y  # end noticeably inward
# quadratic bezier control biased downward-right to make the belly bow right
ctrl_x, ctrl_y = RIGHT_X + 2, (v_y0 + v_y1) / 2 + 5
bez_steps = 120
for i in range(bez_steps + 1):
    t = i / bez_steps
    x = (1 - t) ** 2 * v_x0 + 2 * (1 - t) * t * ctrl_x + t ** 2 * v_x1
    y = (1 - t) ** 2 * v_y0 + 2 * (1 - t) * t * ctrl_y + t ** 2 * v_y1
    dab(x, y, R)
dab(v_x1, v_y1, R + 0.5)  # subtle terminal

# ---------- Stroke 3: central 竖 (long) ----------
# Signature stroke: pierces the top horizontal and extends well below
# the box.
c_x0, c_y0 = CENTER_X, TOP_Y - 15
c_x1, c_y1 = CENTER_X, 278
dab(c_x0, c_y0, R_START)
line_dabs(c_x0, c_y0, c_x1, c_y1, R, R)
dab(c_x1, c_y1, R + 1.5)  # slightly weighted bottom press

# ---------- Save ----------
out_path = "01_巾.png"
img.save(out_path)
print(f"wrote {out_path}")
