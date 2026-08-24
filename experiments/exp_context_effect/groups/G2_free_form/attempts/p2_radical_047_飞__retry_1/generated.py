"""
飞 (fēi) — retry 1 — 3-stroke radical.

Prior attempt failed: the 横折弯钩's arc direction was wrong (arc swept
DOWN-and-RIGHT with belly on the right, hook then ended at the bottom-
right corner). Comparing to the GT, the character's dominant sweep is
DOWN-and-LEFT — the 竖 after the 折 shoulder curves toward the lower-LEFT,
then arcs back rightward at the base with the hook flicking up-and-left.
In effect, the "弯" segment carries the ink from upper-right toward the
lower-left, then hooks. The belly of that arc is on the UPPER-RIGHT side
(concave toward lower-left).

Revised construction:
  Stroke 1 (横折弯钩):
    - Beat 1 (横): short 横 upper-left to shoulder at upper-right.
    - Beat 2 (折): shoulder dab, then a curving descent that sweeps
      DOWN AND LEFT (not straight down or right). Belly-on-upper-right.
    - Beat 3 (弯/arc back): near the bottom, curl back rightward and
      slightly up so the tail rises into the hook.
    - Beat 4 (钩): terminal hook flicks UP-and-LEFT ~-115°.
  Stroke 2 (点): small teardrop dot in upper-right, just below the top
    横's right end (inside the corner formed by the 折).
  Stroke 3 (撇): short 撇 in the middle, throw down-and-left.

PIL brush-dab technique, 300x300 white, black ink. Image coords y grows DOWN.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(20, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=250):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def cubic_dabs(p0, p1, p2, p3, r0, r1, steps=350):
    for i in range(steps + 1):
        t = i / steps
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t * t
        b3 = t * t * t
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


r_body = 5.5

# ---- Stroke 1: 横折弯钩 (main sweeping stroke) --------------------------
# Beat 1: short 横 upper-left to upper-right (slight up-tilt).
h_start = (55, 100)
h_end   = (200, 85)      # shoulder corner (upper-right area)
dab(*h_start, r_body + 2)                          # 顿 press start
line_dabs(*h_start, *h_end, r_body, r_body + 1)
dab(*h_end, r_body + 3)                            # shoulder dab

# Beat 2 + 3: the 弯 body — a long cubic Bezier from the shoulder
# sweeping DOWN-and-LEFT, then curling back rightward at the bottom.
# Anchors:
#   P0 = shoulder (200, 85)
#   P1 = (215, 175)   # pull first outward-then-down (control near right)
#   P2 = (120, 260)   # deep lower-left where the sweep bottoms out
#   P3 = (185, 250)   # curl back rightward-and-slightly-up (hook base)
# This produces a curve that starts by descending, bellies out to the
# right initially, then sweeps down-and-left, then returns rightward
# to the hook base.
P0 = h_end
P1 = (215, 180)
P2 = (95, 260)
P3 = (200, 268)
cubic_dabs(P0, P1, P2, P3, r_body + 1, r_body, steps=380)

# Beat 4: terminal hook flicks UP-and-LEFT (~-115°) from the hook base.
hook_base = P3
hook_len = 40
hook_angle_deg = -130
ha = math.radians(hook_angle_deg)
hx = hook_base[0] + hook_len * math.cos(ha)
hy = hook_base[1] + hook_len * math.sin(ha)
# Joining dab equal to segment radius (no r+1/r+2 to avoid stray nub).
dab(*hook_base, r_body)
line_dabs(hook_base[0], hook_base[1], hx, hy, r_body + 0.3, 1.2, steps=90)


# ---- Stroke 2: 点 (dot in upper-right, inside the 折 corner) ---------
# Small teardrop sitting just below the top 横's right end / near the
# shoulder. Runs from upper-left to lower-right, thin→thick.
d_start = (170, 110)
d_end   = (188, 132)
d_steps = 60
for i in range(d_steps + 1):
    t = i / d_steps
    x = d_start[0] + (d_end[0] - d_start[0]) * t
    y = d_start[1] + (d_end[1] - d_start[1]) * t
    tt = t ** 1.4
    r = 1.8 + (6.5 - 1.8) * tt
    dab(x, y, r)
dab(*d_end, 7.0)


# ---- Stroke 3: 撇 (short throw in the middle) ------------------------
# Short 撇 to the left of the main body, throws down-and-left.
p_start = (135, 135)
p_end   = (95, 195)
p_ctrl  = (130, 170)   # slight rightward bow
dab(*p_start, r_body + 0.5)
bezier_dabs(p_start, p_ctrl, p_end, r_body, 1.3, steps=160)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_047_飞__retry_1/01_飞.png")
