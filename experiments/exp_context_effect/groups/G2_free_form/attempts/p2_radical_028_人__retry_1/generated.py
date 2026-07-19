"""
Retry #1 for 人 (radical 028).

Errata diagnosis for retry_0: prior attempt drew two ruler-straight
legs meeting at a shared apex — read as ∧. Right stroke lacked the 捺
thin→thick taper with broad flat terminal foot; also a stray artifact
at right-foot base.

Fix (from errata + memory principle 7 topology): 人 = 撇 + 捺 meeting
at a SINGLE apex (both tops at same y). Right stroke must be a real
捺: start thin at apex, THICKEN toward lower-right, terminate with
broad flat foot (~10 px radius terminal dab). Left 撇 gets a subtle
rightward bow (Bezier control point pulled toward interior/right).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_pt(p0, p1, p2, t):
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    return x, y


# Shared apex for 人 (per principle 7: both tops at same y).
APEX = (150, 60)

# ---- Stroke 1: 撇 (left leg) — thick→thin, gentle rightward bow ----
# Start at apex, throw down-and-left. Bezier control pulled toward
# right/interior so the belly bows rightward.
p0 = APEX
p2 = (55, 250)
ctrl = (135, 165)   # pulled right of the chord midpoint (~102, 155)
r_start = 9.0
r_end = 1.3

# 顿笔 press at start — memory warning: at standalone scale r+2 becomes
# a visible balloon at the apex. Use plain segment radius only.
dab(p0[0], p0[1], r_start)

steps = 400
for i in range(steps + 1):
    t = i / steps
    x, y = bezier_pt(p0, ctrl, p2, t)
    r = r_start + (r_end - r_start) * t
    dab(x, y, r)

# ---- Stroke 2: 捺 (right leg) — thin→THICK with broad flat foot ----
# Start at apex thin, thicken to broad terminal press at lower-right.
# Slight downward bow (control pulled slightly down) for calligraphic
# feel; canonical 捺 body is nearly straight with a swell near the end.
q0 = APEX
q2 = (245, 245)
qctrl = (185, 175)   # slight below chord midpoint for gentle bow

r0 = 1.8               # thin start at apex
r2 = 10.0              # thick before terminal foot

steps = 400
for i in range(steps + 1):
    t = i / steps
    x, y = bezier_pt(q0, qctrl, q2, t)
    # Ease the thickening so it swells more near the end (捺 signature)
    tt = t ** 1.3
    r = r0 + (r2 - r0) * tt
    dab(x, y, r)

# Broad flat terminal foot: extend the direction of the tail slightly
# with a wide flat dab cluster so the foot reads as a press-out.
# Compute tail tangent at t=1.
def bez_deriv(p0, p1, p2, t):
    return (2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
            2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]))

dx, dy = bez_deriv(q0, qctrl, q2, 1.0)
mag = math.hypot(dx, dy)
ux, uy = dx / mag, dy / mag

# Foot: extend ~18 px along tangent with slight radius decay to make
# a broad-then-tapering press (like a brush lifting off).
foot_len = 18
foot_steps = 60
r_foot_start = 10.5
r_foot_end = 3.0
for i in range(foot_steps + 1):
    t = i / foot_steps
    x = q2[0] + ux * foot_len * t
    y = q2[1] + uy * foot_len * t
    r = r_foot_start + (r_foot_end - r_foot_start) * t
    dab(x, y, r)

out_path = ("/Users/peilinwu/Documents/AI memory research/experiments/"
            "exp_context_effect/groups/G2_free_form/attempts/"
            "p2_radical_028_人__retry_1/01_人.png")
img.save(out_path)
print("saved", out_path)
