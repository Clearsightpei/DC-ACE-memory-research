"""
子 (zi) — 3-stroke radical.
Strokes:
  1. 横撇 (heng-pie): a short horizontal at top curving into a downward-left slanting tail
     (looks like a small hook/curl at top). Image coords, top of the character.
  2. 弯钩 (wan-gou): the main central curved vertical descending, with a hook at the
     bottom flicking up-and-slightly-left.
  3. 横 (heng): a wide horizontal crossing through the middle of the 弯钩 — the
     "shoulders" of 子, running left→right past both sides.
Canvas 300x300, white bg, black ink. PIL brush-dabs.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        d = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(d * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ----- Stroke 1: 横撇 (top little hook / curl) -----
# Short horizontal at top, then curl down-left. Longer and more pronounced.
h1_x0, h1_y0 = 85, 78
h1_x1, h1_y1 = 190, 72
dab(h1_x0, h1_y0, 7)  # 顿 press start
line_dabs(h1_x0, h1_y0, h1_x1, h1_y1, 5.5, 5.5)
# shoulder dab
dab(h1_x1, h1_y1, 8)
# 撇 tail (bowed) down-and-left, longer and more sweeping
bezier_dabs(
    (h1_x1, h1_y1),
    (183, 105),      # control pulls right/down (bowed rightward)
    (135, 125),      # tip lands near/into the 弯钩 top area
    r0=7.0, r1=1.5,
)

# ----- Stroke 2: 弯钩 (main central curved vertical + hook) -----
# Primary curved vertical: starts near top-right (just under stroke 1's endpoint),
# curves down (slight left concavity) to near bottom-center, then hooks up-and-left.
wg_p0 = (155, 115)   # top start (near where stroke-1 tail ends)
wg_p2 = (128, 245)   # bottom endpoint (before hook)
wg_ctrl = (180, 185) # control pulls right → belly on the right, opens left (canonical 子)
# 顿 dab at start
dab(*wg_p0, 7)
bezier_dabs(wg_p0, wg_ctrl, wg_p2, r0=6.5, r1=5.5, steps=350)
# joining dab at hook base (radius == segment radius per principle 5 corollary)
dab(*wg_p2, 5.5)
# hook flick: up-and-slightly-left, ~-115° from horizontal, length ~35 px
hook_len = 48
hook_angle_deg = -150  # up-and-left in image coords (y grows down)
hx = wg_p2[0] + hook_len * math.cos(math.radians(hook_angle_deg))
hy = wg_p2[1] + hook_len * math.sin(math.radians(hook_angle_deg))
line_dabs(wg_p2[0], wg_p2[1], hx, hy, 5.5, 1.2)

# ----- Stroke 3: 横 (the wide horizontal shoulders of 子) -----
# Crosses the 弯钩 around y=165 (middle-ish), extending well past both sides.
h3_x0, h3_y0 = 55, 168
h3_x1, h3_y1 = 260, 160  # slight up-tilt (canonical 横)
dab(h3_x0, h3_y0, 7)     # 顿 start
line_dabs(h3_x0, h3_y0, h3_x1, h3_y1, 5.5, 5.5)
dab(h3_x1, h3_y1, 7)     # terminal press

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_082_子/01_子.png")
