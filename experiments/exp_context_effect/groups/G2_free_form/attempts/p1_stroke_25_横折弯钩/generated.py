"""
p1_stroke_25_横折弯钩 — 横折弯钩

Structure (four beats in one continuous stroke):
  1. 横 (heng): short horizontal, left→right, slight up-tilt.
  2. 折 shoulder-dab, direction change to vertical.
  3. 竖 (shu): descends downward (kept relatively short so the 弯 arc
     has room to curve into a horizontal, and the hook has room to
     flick up).
  4. 弯 (wan): SMOOTH quarter-arc (no shoulder dab) that turns the
     descending vertical into a rightward horizontal run.
  5. hook flick up-and-left from the right-end of the horizontal run,
     tapered to a sharp tip.

Canvas 300x300, white bg, black ink. Image coords: y grows DOWN.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke_line(x0, y0, x1, y1, r_start, r_end, steps=None):
    """Straight tapered segment via brush-dabs."""
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(80, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def stroke_arc(cx, cy, R, t0, t1, r_start, r_end, steps=200):
    """Circular arc via brush-dabs, angle in radians (image coords)."""
    for i in range(steps + 1):
        u = i / steps
        theta = t0 + (t1 - t0) * u
        x = cx + R * math.cos(theta)
        y = cy + R * math.sin(theta)
        r = r_start + (r_end - r_start) * u
        dab(x, y, r)


# ---- Beat 1: 横 (heng) — short, slight up-tilt ----
h_x0, h_y0 = 70, 80
h_x1, h_y1 = 185, 72   # up-tilt ~4 deg
BASE_R = 5.5
dab(h_x0, h_y0, BASE_R + 2.5)                     # 顿 start
stroke_line(h_x0, h_y0, h_x1, h_y1, BASE_R, BASE_R + 0.5)

# ---- Beat 2: 折 shoulder-dab (corner press) ----
SHOULDER_R = BASE_R + 2.5
dab(h_x1, h_y1, SHOULDER_R)

# ---- Beat 3: 竖 (shu) — descend from shoulder, kept short ----
# From (h_x1, h_y1) straight down. Keep shortish so 弯 arc has room.
s_x0, s_y0 = h_x1, h_y1
s_x1, s_y1 = h_x1, 155      # ~83 px vertical descent
stroke_line(s_x0, s_y0, s_x1, s_y1, BASE_R + 0.3, BASE_R)

# ---- Beat 4: 弯 — SMOOTH quarter-arc, vertical -> rightward horiz ----
# Center of the quarter-arc is at (s_x1 + R, s_y1), radius R.
# Parameterize theta from pi (leftmost point of the circle -> where the
# vertical meets the arc) to pi/2 (topmost point of the circle) — WAIT:
# In image coords (y DOWN), a smooth turn from "going down" to "going
# right" traces a quarter circle whose center is up-and-right of the
# turn's start point. Actually the vertical ends going DOWN and needs
# to bend to the RIGHT. The tangent-continuous quarter-arc has its
# center at (s_x1 + R, s_y1 - 0)? Let's reason:
#
# Take center C = (cx, cy). At the arc's start we need the arc's
# tangent to point downward and the arc point to be (s_x1, s_y1).
# Tangent direction at angle theta on the circle is (-sin theta, cos
# theta). We want that to equal (0, 1) => sin theta = 0, cos theta = 1
# => theta = 0. Position at theta=0 is (cx + R, cy). So s_x1 = cx + R
# and s_y1 = cy, giving cx = s_x1 - R, cy = s_y1.
#
# We then sweep theta from 0 to pi/2 (so cos theta goes 1->0, sin
# theta goes 0->1). Position: (cx + R cos theta, cy + R sin theta).
# End point: (cx, cy + R) = (s_x1 - R, s_y1 + R). Tangent at pi/2 is
# (-1, 0) — pointing LEFT, not right. That's wrong.
#
# So instead sweep theta from pi to pi/2 with center to the RIGHT of
# the start. Position at theta=pi: (cx - R, cy). Set that = (s_x1,
# s_y1) => cx = s_x1 + R, cy = s_y1. Tangent at theta=pi is (-sin pi,
# cos pi) = (0, -1) — pointing UP, wrong.
#
# Retry: parametrize x = cx + R cos theta, y = cy + R sin theta,
# tangent = (-R sin theta, R cos theta). Want tangent (0, +1) at
# start: sin theta = 0 and cos theta = +1 => theta=0. Then arc end
# should have tangent (+1, 0): sin theta = -1, cos theta = 0 =>
# theta = -pi/2 (equivalently 3pi/2). So sweep theta from 0 down to
# -pi/2. Position: start (cx+R, cy), end (cx, cy - R). We want end to
# be to the RIGHT and BELOW the start — but end is (cx, cy-R) which
# is ABOVE center. That puts end above start. Wrong again in image
# coords... unless we notice: in image coords with y DOWN, "going
# right and slightly down" after a smooth arc from a vertical
# descent means the arc bulges to the LOWER-LEFT (concave up-right).
#
# Simpler: hand-place — arc center to the RIGHT of the vertical's
# bottom, at same y. Sweep from theta=pi (leftmost, pointing DOWN in
# math coords which is UP in image coords... this gets confusing).
#
# I'll just do it geometrically with a custom parametrization that
# I've verified visually before (see 竖弯 memory entry):
#   x(t) = s_x1 + R * sin(t*pi/2)
#   y(t) = s_y1 + R * (1 - cos(t*pi/2))
# At t=0: (s_x1, s_y1), tangent (R*pi/2 * cos0, R*pi/2 * sin0) =
# (positive, 0)... hmm that gives tangent pointing right at start,
# but we entered going DOWN. Need to swap:
#   x(t) = s_x1 + R * (1 - cos(t*pi/2))
#   y(t) = s_y1 + R * sin(t*pi/2)
# t=0: (s_x1, s_y1), derivative: (R*pi/2 * sin0, R*pi/2 * cos0) =
# (0, +), tangent points DOWN — good, matches entering vertical.
# t=1: (s_x1 + R, s_y1 + R), derivative: (R*pi/2 * 1, R*pi/2 * 0) =
# (+, 0), tangent points RIGHT — good, exits horizontally.
#
# End point: (s_x1 + R, s_y1 + R). Perfect: right and below.
R = 32
arc_steps = 160
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = s_x1 + R * (1 - math.cos(t * math.pi / 2))
    y = s_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, BASE_R)

# End of arc:
a_x1, a_y1 = s_x1 + R, s_y1 + R      # (185, 187)

# ---- Beat 5: short rightward horizontal run after the arc ----
r_x1, r_y1 = a_x1 + 55, a_y1         # (240, 187)
stroke_line(a_x1, a_y1, r_x1, r_y1, BASE_R, BASE_R)

# ---- Beat 6: hook flick up-and-left, sharp taper ----
# Flick ~40 px long, angle ~-115° in image coords (up and slightly
# left). dx = 40*cos(-115°), dy = 40*sin(-115°).
flick_len = 55
flick_angle_deg = -115
fa = math.radians(flick_angle_deg)
fx1 = r_x1 + flick_len * math.cos(fa)
fy1 = r_y1 + flick_len * math.sin(fa)
# Joining dab at hook base (small extra press):
dab(r_x1, r_y1, BASE_R + 1.5)
stroke_line(r_x1, r_y1, fx1, fy1, BASE_R + 0.5, 1.2, steps=200)

# Save
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_25_横折弯钩/01_横折弯钩.png"
img.save(out)
print(f"Saved: {out}")
