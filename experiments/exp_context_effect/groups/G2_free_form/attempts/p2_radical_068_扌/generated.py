"""
p2_radical_068_扌 — 提手旁 (hand radical), 3 strokes.

Strokes (order):
  1. 横 (short, slight up-tilt) — top bar
  2. 竖钩 (straight vertical descending through the 横, hook up-and-left at bottom)
  3. 提 (rising, thick→thin) — crosses through the 竖 in mid-body

Rendered with PIL brush-dab technique on 300x300 white canvas.
Revision-1 notes (vs first attempt): the first render was too wide and
had visible 顿-dab "balls" at 横 start and 提 start (my own memory §
"No visible 顿-dab balls at standalone endpoints" warns of exactly
this). Also the 竖 was too short and the frame was too compact. This
revision:
  - narrows the horizontal footprint (taller/narrower like GT)
  - lengthens the 竖 downward (~ 60->255)
  - drops the standalone 顿-dab sizes (r or r+0.5, not r+1.5)
  - moves 提 down slightly so it crosses the 竖 mid-body
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(80, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Stroke 1: 横 (short, slight up-tilt) --------------------------------
# Narrower than first attempt. Sits high on canvas.
h_x0, h_y0 = 130, 80
h_x1, h_y1 = 210, 72
r_heng = 4.5
# subtle start press (r+0.5, not r+2 — standalone rule)
dab(h_x0, h_y0, r_heng + 0.5)
line_dabs(h_x0, h_y0, h_x1, h_y1, r_heng, r_heng)
# blunt terminal press (subtle)
dab(h_x1, h_y1, r_heng + 0.5)


# --- Stroke 2: 竖钩 (long vertical + hook) -------------------------------
# The 竖 crosses through the 横 near its right portion, descends long,
# ends with a hook flick up-and-left.
sv_x = 187  # right portion of the heng
sv_y0 = 55  # starts above the heng (crosses through it)
sv_y1 = 255  # descends much further than first attempt
r_shu = 4.8
# tiny start press
dab(sv_x, sv_y0, r_shu + 0.5)
line_dabs(sv_x, sv_y0, sv_x, sv_y1, r_shu, r_shu)
# hook flick — up-and-slightly-left, ~-118°, length ~36 px, taper
hook_len = 36
hook_angle = math.radians(-120)
hx1 = sv_x + hook_len * math.cos(hook_angle)
hy1 = sv_y1 + hook_len * math.sin(hook_angle)
line_dabs(sv_x, sv_y1, hx1, hy1, r_shu + 0.3, 1.1)


# --- Stroke 3: 提 (rising, thick→thin) ----------------------------------
# 提 crosses the 竖 in mid-body. Thick round start on lower-left,
# tapers thin to upper-right tip. Angle ~18-22° above horizontal.
ti_x0, ti_y0 = 130, 172
ti_x1, ti_y1 = 232, 148
# start press — moderate, not a balloon
dab(ti_x0, ti_y0, 6.5)
line_dabs(ti_x0, ti_y0, ti_x1, ti_y1, 5.8, 1.1, steps=280)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_068_扌/01_扌.png"
)
