"""
飞 (fēi) — 3-stroke radical.

Strokes (canonical order):
  1. 横折弯钩 (heng-zhe-wan-gou): short 横 top-left → shoulder → curving 竖
     with belly on the right → smooth arc into rightward 横 along the
     baseline → terminal hook flicking up-and-left.
  2. 撇 (pie): short throw-away starting just below the top shoulder,
     going down-and-left. Sits in the middle of the character.
  3. 点 (dian): small dot in the upper-right area, riding just below the
     top-right of the main sweep (immediately after the shoulder).

PIL brush-dab technique, 300x300 white, black ink.
Image coords: y grows DOWN. Math principles per drawer_memory.md.
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


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 横折弯钩 ----------------------------------------------------
# Beat 1: short 横, slight upward tilt (left→right).
h1_start = (50, 95)
h1_end = (175, 82)          # shoulder corner
r_body = 5.5

# 顿-dab at start
dab(*h1_start, r_body + 2)
line_dabs(*h1_start, *h1_end, r_body, r_body + 1)

# Shoulder dab
sh = h1_end
dab(*sh, r_body + 3)

# Beat 2: curving 竖 with belly on the RIGHT (concave-left).
# Bezier from shoulder DOWN to the point where the arc into horizontal begins.
# End of this curving 竖 is where the tangent should be roughly vertical-down
# transitioning into the arc.
v_start = sh                 # (175, 82)
v_end   = (175, 200)         # bottom of curving 竖 — arc-entry point
v_ctrl  = (215, 130)         # control pulled RIGHT → belly on the right
bezier_dabs(v_start, v_ctrl, v_end, r_body + 1, r_body, steps=180)

# Beat 3: tangent-continuous quarter-arc from downward-motion to rightward.
# Using the KEY PRIMITIVE from memory:
#   x = x0 + R*(1 - cos(t*pi/2)); y = y0 + R*sin(t*pi/2)
# But we want the arc to bend LEFT-to-RIGHT along baseline. Since the belly
# is on the right side of the curving 竖, the tangent at v_end is roughly
# straight down; we then sweep to rightward.
R = 40
arc_steps = 100
ax0, ay0 = v_end
arc_pts = []
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = ax0 + R * (1 - math.cos(t * math.pi / 2))
    y = ay0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)
    arc_pts.append((x, y))
arc_end = arc_pts[-1]        # (ax0 + R, ay0 + R) = (215, 240)

# Beat 4: short rightward 横 along the baseline.
base_end = (arc_end[0] + 30, arc_end[1] + 2)   # ~ (245, 242)
line_dabs(*arc_end, *base_end, r_body, r_body + 0.5)

# Terminal hook: flicks UP-and-LEFT, ~-115° in image coords.
# Length ~35 px.
hook_len = 34
hook_angle_deg = -118
ha = math.radians(hook_angle_deg)
hx = base_end[0] + hook_len * math.cos(ha)
hy = base_end[1] + hook_len * math.sin(ha)
# Joining dab at the corner (equal to r_body, per hook-flick discipline).
dab(*base_end, r_body)
# Taper the flick sharp.
line_dabs(base_end[0], base_end[1], hx, hy, r_body + 0.5, 1.2, steps=80)


# ---- Stroke 2: 撇 (SHORT throw-away in the middle) --------------------------
# GT's 撇 is quite short — throw down-and-left from just below the
# shoulder. Gentle rightward bow. Thick→thin. Kept much shorter than a
# standalone 撇.
p_start = (150, 120)
p_end   = (115, 175)
p_ctrl  = (145, 150)   # slight bow (belly on right)
# small 顿-dab at start
dab(*p_start, r_body + 0.5)
bezier_dabs(p_start, p_ctrl, p_end, r_body, 1.3, steps=140)


# ---- Stroke 3: 点 (dot) ----------------------------------------------------
# Small teardrop dot in the upper area just below shoulder. Small — the GT
# dot is not a big teardrop.
d_start = (192, 112)
d_end   = (206, 132)
d_steps = 50
for i in range(d_steps + 1):
    t = i / d_steps
    x = d_start[0] + (d_end[0] - d_start[0]) * t
    y = d_start[1] + (d_end[1] - d_start[1]) * t
    tt = t ** 1.4
    r = 1.8 + (6.5 - 1.8) * tt
    dab(x, y, r)
# Terminal press (small)
dab(*d_end, 7.0)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_047_飞/01_飞.png")
