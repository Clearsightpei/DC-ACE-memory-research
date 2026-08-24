"""
G2 retry_4 for p2_radical_011_匕 (2画).

# SIGNATURE CHECK (from sibling_signature_checklist.md row 匕):
#   top stroke is a 撇 (upper-right -> lower-left);
#   terminal hook flicks UP-and-LEFT (never DOWN).
#   Sibling risk: 七 (top 横 = left->right); do NOT render top as 横.

Retry_3 FAIL diagnosis (B4 curator): 撇 crossing was fixed, but the
TERMINAL HOOK of the 竖弯钩 flicked DOWN-and-right instead of
UP-and-LEFT. Same "draw the flick" failure across 4 retries.

Retry_4 hard fix:
  - The hook is drawn as a SEPARATE explicit segment that goes
    STRICTLY UPWARD in image coords (delta_y NEGATIVE) at ~-100 deg
    (up-and-slightly-left). Length ~40 px, tapering to a thin tip.
  - Assertion at draw-time: hook_end_y < h_y - 25 (must go up
    at least 25 px). If not, we abort — geometry bug.
  - 撇 kept LONG and BODY-CROSSING per retry_3 (that part worked).
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


# =========================================================================
# Stroke 1: 竖弯钩 — vertical -> smooth rightward arc -> STRONG UP-LEFT hook
# =========================================================================
vx = 100                # vertical x-position
v_top = 100             # top of vertical
v_bot = 205             # bottom of vertical before arc begins
r_body = 6.5

# 顿 press at top
dab(vx, v_top, r_body + 1.5)

# Vertical body
for i in range(220 + 1):
    t = i / 220
    y = v_top + (v_bot - v_top) * t
    dab(vx, y, r_body)

# Quarter arc (tangent-continuous): vertical -> rightward horizontal
R = 42
arc_end_x = vx + R
arc_end_y = v_bot + R
for i in range(180 + 1):
    t = i / 180
    x = vx + R * (1 - math.cos(t * math.pi / 2))
    y = v_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)

# Rightward 横 continuation
h_end_x = 215
h_y = arc_end_y  # ~247
for i in range(200 + 1):
    t = i / 200
    x = arc_end_x + (h_end_x - arc_end_x) * t
    dab(x, h_y, r_body)

# ---- Terminal 钩 hook: STRICTLY UP-and-slightly-LEFT, PROMINENT ----
# Image coords: y grows DOWN, so "up" = negative dy.
# GT shows a tall, obvious upward hook. Increase length so it reads
# clearly (retry_3 nub was too small to register as a hook).
hook_len = 70
hook_angle_deg = -100.0  # -90 = pure up, -100 = up + slight-left
hook_angle = math.radians(hook_angle_deg)
hook_end_x = h_end_x + hook_len * math.cos(hook_angle)
hook_end_y = h_y + hook_len * math.sin(hook_angle)

# Hard geometry assertion — must go UP at least 40 px
assert hook_end_y < h_y - 40, (
    f"HOOK GEOMETRY BUG: hook_end_y={hook_end_y:.1f} not < h_y-40={h_y-40:.1f}"
)
assert hook_end_x < h_end_x, (
    f"HOOK NOT LEFTWARD: hook_end_x={hook_end_x:.1f} not < h_end_x={h_end_x}"
)

# Joining dab at hook base (same radius as segment to avoid stray nub)
dab(h_end_x, h_y, r_body)

# Draw the hook as a thick-to-thin taper going UPWARD (long, visible)
for i in range(240 + 1):
    t = i / 240
    x = h_end_x + (hook_end_x - h_end_x) * t
    y = h_y + (hook_end_y - h_y) * t
    r = r_body + (1.8 - r_body) * t
    dab(x, y, r)


# =========================================================================
# Stroke 2: 撇 — LONG body-crossing diagonal (upper-right -> lower-left)
# =========================================================================
# Kept from retry_3 (the part that worked).
# 竖 spans y=100..205 at x=100. Start upper-right, end lower-left past 竖.
p0 = (200, 60)    # upper-right start — ABOVE the vertical's top
p1 = (140, 110)   # control near the crossing point for a natural bow
p2 = (45, 175)    # lower-left endpoint — well past the 竖

# 顿笔 press at start
dab(p0[0], p0[1], 9)

bezier_stroke(p0, p1, p2, r_start=10.0, r_end=1.4, steps=460, ease=1.15)

# =========================================================================
img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_011_匕__retry_4/01_匕.png"
)
print("hook_end_x=%.1f hook_end_y=%.1f h_end_x=%d h_y=%.1f"
      % (hook_end_x, hook_end_y, h_end_x, h_y))
