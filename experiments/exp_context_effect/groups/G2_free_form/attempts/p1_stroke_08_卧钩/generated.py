"""
卧钩 (wo gou, lying hook) — stroke rendering
Shape: a shallow horizontal curve that dips down (concave-up, like a smile),
then a short upward hook flicking to the upper-left at the right end.
Used in characters like 心, 必, 志.
Output: 300x300 PNG, white background, black ink.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# --- Parameters (in image coords, y grows DOWN) ---
# Lying hook body: a shallow arc from upper-left to lower-right area,
# curving down (belly points down). Then a short hook flick up-left at the tip.

# Endpoints of the curve body
x_start, y_start = 70, 130     # upper-left start (thin entry)
x_end,   y_end   = 230, 175    # right end where the hook begins

# Control point (below the chord midpoint) makes it dip like a smile
ctrl_x = (x_start + x_end) / 2
ctrl_y = 210                   # below the endpoints -> concave-up (belly down)

# Sample quadratic Bezier for the body, varying stroke thickness
def bezier(t, p0, p1, p2):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y

P0 = (x_start, y_start)
P1 = (ctrl_x, ctrl_y)
P2 = (x_end, y_end)

# Draw the body with variable width: thin at start, thicker in the middle-belly,
# thickest near the hook base (顿笔 before the hook).
N = 220
prev = None
for i in range(N + 1):
    t = i / N
    x, y = bezier(t, P0, P1, P2)
    # Width profile: thin -> thick toward the end (calligraphic swelling before the hook)
    w = 3.0 + 6.0 * t + 2.5 * math.sin(math.pi * t)  # peaks near t=0.5 and grows to end
    r = w / 2.0
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
    prev = (x, y)

# --- 顿笔 (pause/press) at the hook base --- a small filled blob for weight
hx, hy = x_end, y_end
draw.ellipse((hx - 7, hy - 7, hx + 7, hy + 7), fill="black")

# --- Hook flick: short, sharp segment from (hx, hy) up-and-to-the-left ---
# Direction: upper-left, roughly 135 degrees (northwest)
hook_len = 26
angle_deg = 145  # measured from +x axis going counterclockwise (image coords: y down,
                 # so we negate y-component to go visually UP)
theta = math.radians(angle_deg)
tip_x = hx + hook_len * math.cos(theta)
tip_y = hy - hook_len * math.sin(theta)  # minus because image-y grows down

# Draw the hook as a tapered line: several ellipses shrinking from base to tip
M = 30
for j in range(M + 1):
    s = j / M
    x = hx + (tip_x - hx) * s
    y = hy + (tip_y - hy) * s
    w = 7.5 * (1 - s) + 1.2 * s  # thick at base, thin at tip
    r = w / 2.0
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_08_卧钩/01_卧钩.png"
)
print("saved 01_卧钩.png (300x300)")
