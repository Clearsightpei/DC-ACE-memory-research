"""
p2_radical_086_比 — Draw radical 比 (4 strokes) with PIL brush-dabs.

Stroke decomposition (standard order):
  1. Left short 横 — sits high on the left, mild up-tilt.
  2. Left 竖提 — vertical from top of the left component down, then a
     rising 提 tail up-and-right into the middle.
  3. Right short 撇 — starts upper-right, throws down-and-left toward
     the middle. Its tip lands near the left of the right 竖.
  4. Right 竖弯钩 — long vertical descending, arcs smoothly right into
     a horizontal, ends with an up-and-slightly-left hook flick.

Canvas: 300×300 white, black ink. Image coords (y grows DOWN).
Layout roughly matches GT: left component narrower/shorter than
right; right 竖弯钩 dominates the silhouette with its long descent.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ============================================================
# LEFT COMPONENT (occupies roughly x=45..135)
# Stroke 1: Left 横 — CROSSES the 竖 near the top, going from
# left-of-竖 to right-of-竖. Small size, slight up-tilt.
# The 竖 sits at x=95. 横 runs x=55..135, y=110..104.
# ============================================================
h1_x0, h1_y0 = 55, 112
h1_x1, h1_y1 = 130, 106
dab(h1_x0, h1_y0, 6)  # 顿笔 start
line_taper(h1_x0, h1_y0, h1_x1, h1_y1, 5, 5)
dab(h1_x1, h1_y1, 6)  # small end press

# ============================================================
# Stroke 2: 竖提 — vertical from ~y=90 down to ~y=225, then
# a rising 提 up-and-right ending well WITHIN the left half
# (do not invade the right component). 提 ends near (135, 200).
# ============================================================
v2_x, v2_top, v2_bot = 95, 90, 225
dab(v2_x, v2_top, 7)  # 顿笔 start
line_taper(v2_x, v2_top, v2_x, v2_bot, 5.5, 5.5)
# joining dab at 提 root — equal to segment radius (avoid stray nub)
dab(v2_x, v2_bot, 6)
# 提 rising up-right, thick→thin, sharp tip
line_taper(v2_x, v2_bot, 138, 195, 5.5, 1.3, steps=250)

# ============================================================
# RIGHT COMPONENT (occupies roughly x=165..260)
# Stroke 3: Right 撇 — short, starts upper-right, throws down-left.
# Starts around (225, 95), tail lands near (175, 165).
# Gentle rightward bow (control pulled toward interior).
# ============================================================
dab(225, 95, 8)  # 顿笔 start
bezier_taper(
    (225, 95),
    (210, 125),
    (175, 168),
    r0=7,
    r1=1.4,
    steps=350,
)

# ============================================================
# Stroke 4: 竖弯钩 — the tall right stroke, DOMINATES the silhouette.
# 竖 descends from around (200, 95) to (200, 220), then a
# tangent-continuous quarter-arc into a rightward 横 to (250, 260),
# then hook flicks up-and-slightly-left (~ -108°).
# Uses the KEY PRIMITIVE from memory.
# ============================================================
sv_x, sv_top, sv_bot = 200, 95, 220
dab(sv_x, sv_top, 7)  # 顿笔
line_taper(sv_x, sv_top, sv_x, sv_bot, 5.5, 5.5)

# tangent-continuous arc, R=38, ends at (sv_x + 38, sv_bot + 38) = (238, 258)
R = 38
arc_steps = 90
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = sv_x + R * (1 - math.cos(t * math.pi / 2))
    y = sv_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.5)

arc_end_x, arc_end_y = sv_x + R, sv_bot + R  # (238, 258)

# short rightward 横 continuing from the arc end
h_end_x, h_end_y = 258, 258
line_taper(arc_end_x, arc_end_y, h_end_x, h_end_y, 5.5, 5.8)

# hook: flick up-and-slightly-left, angle ~ -108°, length ~ 36 px
hook_len = 36
hook_angle_deg = -108
hx = h_end_x + hook_len * math.cos(math.radians(hook_angle_deg))
hy = h_end_y + hook_len * math.sin(math.radians(hook_angle_deg))
# joining dab equal to segment radius (per memory: r+2 causes stray nub at hooks)
dab(h_end_x, h_end_y, 5.8)
line_taper(h_end_x, h_end_y, hx, hy, 5.8, 1.1, steps=220)

# ============================================================
# Save
# ============================================================
out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_086_比/01_比.png"
)
img.save(out_path)
print(f"saved {out_path}")
