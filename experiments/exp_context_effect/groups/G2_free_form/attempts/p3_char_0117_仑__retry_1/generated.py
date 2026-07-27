"""
G2 retry #1 for p3_char_0117_仑 (4-stroke character).

Fix idea from errata: 匕 body was too small/tight and offset.
Comparing prior attempt vs GT:
  - GT: 人-lid is BIG and thin, apex near top; 匕 body sits IN the
    lower half, wide, with a large 竖弯钩 bowl reaching down to
    ~y=260 and hook at right ~x=220.
  - Prior attempt: 匕 sat too high, was too small; hook too tight;
    the 撇 crossing was awkward.
Also GT shows thinner brush - reduce dab radii.

# SIGNATURE CHECK (from sibling_signature_checklist row 匕):
#   top stroke is a 撇 (upper-right→lower-left);
#   terminal hook flicks UP-and-LEFT.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=440, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        mt = 1 - t
        x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
        y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ============================================================
# Part A — 人-lid: SHARED APEX high, wide splay
# ============================================================
APEX = (150, 40)

# Stroke 1: 撇 (left leg) — thick→thin, gentle bow
p0 = APEX
ctrl1 = (115, 100)
p2 = (35, 210)
dab(p0[0], p0[1], 4)
bezier_stroke(p0, ctrl1, p2, r_start=4.5, r_end=1.2, steps=460, ease=1.05)

# Stroke 2: 捺 (right leg) — thin→thicker, ends with foot
q0 = APEX
qctrl = (200, 105)
q2 = (270, 215)
bezier_stroke(q0, qctrl, q2, r_start=1.5, r_end=4.5, steps=460, ease=1.3)


# ============================================================
# Part B — 匕 body, sitting in lower half under the lid
# ============================================================
# Stroke 3: 撇 of 匕 — starts upper-right, dives lower-left
sp0 = (185, 140)
sp1 = (150, 175)
sp2 = (95, 220)
dab(sp0[0], sp0[1], 4)
bezier_stroke(sp0, sp1, sp2, r_start=4.0, r_end=1.2, steps=380, ease=1.1)

# Stroke 4: 竖弯钩 — vertical → arc right → horizontal → hook up-left
vx = 135
v_top = 165
v_bot = 235
r_body = 3.5

dab(vx, v_top, r_body + 1.0)

# Vertical body (short, since arc takes over)
for i in range(180 + 1):
    t = i / 180
    y = v_top + (v_bot - v_top) * t
    dab(vx, y, r_body)

# Quarter arc: vertical → rightward
R = 30
arc_cx = vx + R  # center x of arc
arc_cy = v_bot   # center y
for i in range(160 + 1):
    t = i / 160
    ang = math.pi + t * math.pi / 2  # from pi to 3pi/2... use param instead
# Simpler param: point on quarter circle from (vx, v_bot) sweeping to (vx+R, v_bot+R)
for i in range(180 + 1):
    t = i / 180
    x = vx + R * (1 - math.cos(t * math.pi / 2))
    y = v_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)

arc_end_x = vx + R
arc_end_y = v_bot + R  # = 265

# Rightward 横 continuation
h_end_x = 220
h_y = arc_end_y
for i in range(180 + 1):
    t = i / 180
    x = arc_end_x + (h_end_x - arc_end_x) * t
    dab(x, h_y, r_body)

# Terminal 钩 UP-and-LEFT
hook_len = 22
hook_angle = math.radians(-110)
hook_end_x = h_end_x + hook_len * math.cos(hook_angle)
hook_end_y = h_y + hook_len * math.sin(hook_angle)
for i in range(120 + 1):
    t = i / 120
    x = h_end_x + (hook_end_x - h_end_x) * t
    y = h_y + (hook_end_y - h_y) * t
    r = r_body + (1.0 - r_body) * t
    dab(x, y, r)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0117_仑__retry_1/01_仑.png"
)
print("saved")
