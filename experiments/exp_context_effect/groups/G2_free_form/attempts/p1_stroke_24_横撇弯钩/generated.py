"""
横撇弯钩 (heng-pie-wan-gou) — 4-beat compound stroke.
Structure: short 横 → 折 shoulder → 撇 (down-left, bowed) → smooth 弯 arc
curving from down-left into downward/rightward → 钩 flick up-and-left.
This is the right-ear-radical hook (阝右) shape, e.g. in 那, 队, 陈's right side.

Renders 300x300 white canvas, black ink, PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_line(x0, y0, x1, y1, r0, r1, steps=None):
    """Straight tapered stroke via brush dabs."""
    if steps is None:
        steps = max(80, int(math.hypot(x1 - x0, y1 - y0) * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def dab_bezier(p0, p1, p2, r0, r1, steps=200):
    """Quadratic bezier tapered stroke."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def dab_arc(cx, cy, R, a0, a1, r0, r1, steps=160):
    """Circular arc from angle a0 to a1 (radians), radius R, tapered."""
    for i in range(steps + 1):
        t = i / steps
        a = a0 + (a1 - a0) * t
        x = cx + R * math.cos(a)
        y = cy + R * math.sin(a)
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ------------------------------------------------------------------
# Beat 1: 横 (short, slight up-tilt), left → right at top of glyph.
# ------------------------------------------------------------------
h_start = (75, 80)
h_end   = (170, 72)     # slight up-tilt
R_UNI = 5.0
# 顿 at start
dab(h_start[0], h_start[1], R_UNI + 2)
dab_line(h_start[0], h_start[1], h_end[0], h_end[1], R_UNI, R_UNI + 1)
# shoulder dab at the corner (folded joint to 撇)
shoulder = h_end
dab(shoulder[0], shoulder[1], R_UNI + 3)

# ------------------------------------------------------------------
# Beat 2: 撇 (from shoulder → down-and-left), thick→thin, gently bowed.
# The 撇 bows toward its right side (control pulled right of chord).
# ------------------------------------------------------------------
pie_start = shoulder                     # (170, 72)
pie_tip   = (100, 175)                   # down-and-left endpoint
pie_ctrl  = (155, 130)                   # control pulled toward interior/right
# taper thick(shoulder) → medium (we'll blend into the 弯 arc so don't end razor-thin)
dab_bezier(pie_start, pie_ctrl, pie_tip, R_UNI + 2, R_UNI + 0.5)

# joining dab at the 撇 tip → transition into the smooth 弯 arc
dab(pie_tip[0], pie_tip[1], R_UNI + 1)

# ------------------------------------------------------------------
# Beat 3: 弯 — smooth curve from the 撇 tip, arcing DOWN and RIGHT.
# Think of it as the bottom of a "U" swinging from lower-left back
# under and up to the right. Tangent at pie_tip is roughly down-left
# continuing → the arc curls under and heads toward the lower right.
# Parameterize as a quarter/third arc.
#   Start: pie_tip (100, 175)
#   Arc goes down first then curves right, ending near (175, 235)
#   heading roughly downward-slightly-right, which is where the 钩
#   will flick up from.
# Use a circular arc with center to the upper-right of the arc body.
# ------------------------------------------------------------------
# Choose arc center so that arc passes through pie_tip and the target
# wan_end. Empirical: center ~ (175, 175), R ~ 75, from angle 180° to 90°
# would give a quarter arc from (100,175) DOWN to (175, 250). Then hook
# from (175, 250).
cx, cy, R = 175, 175, 75
# start angle: point pie_tip (100,175) relative to center (175,175) is
# dx=-75, dy=0 → angle = 180°(=pi)
# end angle: we want to reach roughly (175, 250), which is dx=0, dy=75
# → angle = 90°(=pi/2)  — but pi/2 in standard math is up; in image y-down
# coords "sin positive" = down, so angle pi/2 => (cx, cy+R) = (175, 250). Good.
a_start = math.pi           # 180°  → (100, 175)
a_end   = math.pi / 2       # 90°   → (175, 250)  (going CCW in image coords = curving down-right)
# We need to go from 180° DOWN to 90° passing through 135° (which is lower-left of center = (cx - R/√2, cy + R/√2) ≈ (122, 228)) — yes that traces the bottom-left curl. Since a_end < a_start, arc decreases: fine.
dab_arc(cx, cy, R, a_start, a_end, R_UNI + 0.5, R_UNI + 1.5)

wan_end = (cx + R * math.cos(a_end), cy + R * math.sin(a_end))  # (175, 250)

# ------------------------------------------------------------------
# Beat 4: 钩 — sharp flick from wan_end, up-and-to-the-LEFT.
# Length ~35 px, angle ~ -135° in image coords (upper-left).
# ------------------------------------------------------------------
hook_len = 38
hook_angle = math.radians(-135)  # up-left
hx = wan_end[0] + hook_len * math.cos(hook_angle)
hy = wan_end[1] + hook_len * math.sin(hook_angle)
# joining dab at the base of the hook (顿)
dab(wan_end[0], wan_end[1], R_UNI + 2)
dab_line(wan_end[0], wan_end[1], hx, hy, R_UNI + 1.5, 1.2)

# ------------------------------------------------------------------
# Save
# ------------------------------------------------------------------
out_dir = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_24_横撇弯钩"
os.makedirs(out_dir, exist_ok=True)
img.save(os.path.join(out_dir, "01_横撇弯钩.png"))
print("saved", os.path.join(out_dir, "01_横撇弯钩.png"))
