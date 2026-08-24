"""
Render 巳 (radical 071, 3画) at 300x300, PIL brush-dabs.

Structure: 3 strokes.
  1. 横折 — top-left corner: 横 rightward, then 竖 down (forms the
     left+top of the closed upper box).
  2. 横 — middle horizontal that closes the top-right box (this is
     THE distinguishing feature from 己: 巳's top box is CLOSED).
  3. 竖弯钩 — from the top (starting near stroke-1's top-left area),
     descending, curving right into a horizontal, ending with a
     hook flicking up-and-left.

Note: In 巳, stroke 3 (竖弯钩) shares its origin with stroke 1's top-
left; the full outer body forms a "P-like" closed loop with a hook
at the bottom-right.

Actually re-examining GT: stroke 1 is a 横折 forming the top of an
upper enclosure. Stroke 2 is a short middle 横 closing the top box.
Stroke 3 is a 竖弯钩 that starts from the top-left (same origin as
stroke 1's start), descends down the left side, curves right along
the bottom, and terminates with an up-left hook. This matches the
standard 巳 stroke order.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def segment(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


R = 5.0  # base stroke radius

# ------------------------------------------------------------------
# Stroke 1: 横折 — top box's top + right side.
# Start top-left at (90, 90); 横 rightward to (215, 85);
# shoulder dab; 竖 down to (215, 155).
# ------------------------------------------------------------------
p1_start = (90, 90)
p1_corner = (215, 85)   # slight up-tilt on the 横
p1_end = (215, 155)

# 顿 dab at start
dab(*p1_start, R + 2)
# 横 primary
segment(p1_start[0], p1_start[1], p1_corner[0], p1_corner[1], R, R)
# shoulder dab
dab(*p1_corner, R + 2.5)
# 竖 down
segment(p1_corner[0], p1_corner[1], p1_end[0], p1_end[1], R, R)
# blunt end dab
dab(*p1_end, R + 1)

# ------------------------------------------------------------------
# Stroke 2: middle 横 — closes the top box.
# Runs from left side (touching stroke 3's vertical) to right side
# (touching stroke 1's vertical).  This is THE 巳 vs 己 signature.
# ------------------------------------------------------------------
p2_start = (95, 152)
p2_end = (215, 148)   # slight up-tilt

dab(*p2_start, R + 1.5)
segment(p2_start[0], p2_start[1], p2_end[0], p2_end[1], R, R)
dab(*p2_end, R + 1.5)

# ------------------------------------------------------------------
# Stroke 3: 竖弯钩 — starts at same top-left origin as stroke 1,
# descends down the left side past the middle 横, arcs right into a
# horizontal along the bottom, then hooks up-left.
#
# Using the tangent-continuous arc primitive from memory:
#   x = x0 + R_arc*(1 - cos(t*pi/2)); y = y0 + R_arc*sin(t*pi/2)
# ------------------------------------------------------------------
s3_top = (90, 90)         # shares origin with stroke 1
s3_bot_v = (90, 220)      # bottom of vertical descent

# 顿 press at top (already dabbed by stroke 1's start dab, but add
# a tiny bit for continuity of thickness downward)
dab(*s3_top, R + 1)
# vertical descent
segment(s3_top[0], s3_top[1], s3_bot_v[0], s3_bot_v[1], R, R)

# quarter-arc from (90, 220) sweeping into rightward horizontal.
# ends at (90 + R_arc, 220 + R_arc)
R_arc = 40
arc_steps = 120
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = s3_bot_v[0] + R_arc * (1 - math.cos(t * math.pi / 2))
    y = s3_bot_v[1] + R_arc * math.sin(t * math.pi / 2)
    dab(x, y, R)

arc_end = (s3_bot_v[0] + R_arc, s3_bot_v[1] + R_arc)  # (130, 260)

# rightward horizontal along the bottom
h_end = (225, 260)
segment(arc_end[0], arc_end[1], h_end[0], h_end[1], R, R)

# hook — up-and-left flick, angled ~-115° in image coords
hook_len = 38
hook_angle_deg = -115
hook_angle = math.radians(hook_angle_deg)
hook_end = (
    h_end[0] + hook_len * math.cos(hook_angle),
    h_end[1] + hook_len * math.sin(hook_angle),
)
# taper the hook thick->thin
steps_h = 90
for i in range(steps_h + 1):
    t = i / steps_h
    x = h_end[0] + (hook_end[0] - h_end[0]) * t
    y = h_end[1] + (hook_end[1] - h_end[1]) * t
    r = R + (1.2 - R) * t
    dab(x, y, r)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_071_巳/01_巳.png"
img.save(out)
print(f"saved {out}")
