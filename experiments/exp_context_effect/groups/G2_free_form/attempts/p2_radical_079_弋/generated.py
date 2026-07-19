"""
弋 (yi) — 3-stroke radical. Composition (per GT):
  1. 斜钩 (main body): long curved diagonal upper-left → lower-right,
     belly on the lower-left side, ending in an up-left hook flick.
     Standalone-scale: pronounced curvature, r=6-7 uniform.
  2. 横 (short): crosses the 斜钩's upper portion, roughly horizontal,
     starts left of the crossing and ends slightly right of it.
     Length ~ 100 px total. Slight up-tilt.
  3. 点 (dot): small teardrop in the upper-right, slanting from
     upper-left → lower-right, thin → thick.

Renderer: PIL brush-dabs; 300x300 white; black ink.
Image coords (y grows DOWN).
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_dabs(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=400):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---- Stroke 1: 斜钩 (main body) ---------------------------------------
# Standalone: pronounced curve, belly on the LOWER-LEFT side.
# Start upper-left near (90, 65), tip lower-right near (245, 250).
# Control point pulled to lower-left of chord midpoint for the belly.
P0 = (95, 70)
P2 = (235, 245)
P1 = (140, 195)  # gentler belly toward lower-left (less extreme)
# Initial 顿-dab (small at standalone scale, per principle)
dab(P0[0], P0[1], 7)
bezier_dabs(P0, P1, P2, r_start=6.5, r_end=4.5, steps=500)

# Hook flick: from P2 up-and-slightly-left (~-108°), length ~40 px.
hook_len = 42
hook_angle_deg = -108  # image coords: -90 straight up; -108 = mostly-up-slightly-left
ha = math.radians(hook_angle_deg)
hx = P2[0] + hook_len * math.cos(ha)
hy = P2[1] + hook_len * math.sin(ha)
# Joining dab (equal to segment radius per principle 5 corollary)
dab(P2[0], P2[1], 5)
stroke_dabs(P2, (hx, hy), r_start=5.0, r_end=1.2, steps=200)

# ---- Stroke 2: 横 (short, crossing the 斜钩 upper region) --------------
# Cross point on the bezier ~ t=0.25 → ((1-t)^2*P0 + 2(1-t)t*P1 + t^2*P2)
t_cross = 0.28
u = 1 - t_cross
cx = u * u * P0[0] + 2 * u * t_cross * P1[0] + t_cross * t_cross * P2[0]
cy = u * u * P0[1] + 2 * u * t_cross * P1[1] + t_cross * t_cross * P2[1]
# 横 crosses through this point, extends ~50 px left and ~55 px right.
heng_start = (cx - 55, cy + 4)  # start slightly lower-left
heng_end = (cx + 60, cy - 4)  # end slightly upper-right (slight up-tilt)
# 顿 start dab
dab(heng_start[0], heng_start[1], 6.5)
stroke_dabs(heng_start, heng_end, r_start=5.5, r_end=5.5, steps=250)
# terminal press
dab(heng_end[0], heng_end[1], 6.5)

# ---- Stroke 3: 点 (dot upper-right) -----------------------------------
# Small teardrop, thin → thick, slanting upper-left → lower-right.
# Positioned upper-right of the 横's right end, above the 斜钩 body.
d_start = (200, 55)
d_end = (220, 82)
# taper via easing (smaller so it doesn't overpower)
steps = 120
for i in range(steps + 1):
    t = i / steps
    tt = t ** 1.4
    x = d_start[0] + (d_end[0] - d_start[0]) * t
    y = d_start[1] + (d_end[1] - d_start[1]) * t
    r = 1.5 + (7.0 - 1.5) * tt
    dab(x, y, r)
# terminal press
dab(d_end[0], d_end[1], 7.5)

# --- save
out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/p2_radical_079_弋/"
    "01_弋.png"
)
img.save(out_path)
print(f"wrote {out_path}")
