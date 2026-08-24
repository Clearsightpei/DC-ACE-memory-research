"""
风 (radical 094) — retry_2

Errata history:
- Original: rendered as 冈 (boxy left wall, boxy top-right corner, inside 人-legs).
- B3 retry_1: outer 撇 attempted with curvature but "still reads too boxy —
  撇 not curved enough". Diagnosis said: Bezier P1 must be pulled
  significantly RIGHT of chord midpoint (~40 px offset) to make the
  left wall a proper curved sweep.

Structure of 风:
  Stroke 1 = 撇 (left wall)   : curves from top-middle down-and-left,
                                 sweeping outward, thick→thin taper.
  Stroke 2 = 横折弯钩 (right wall/lid): short 横 top → smooth arc-corner →
                                 long 竖 down (right wall) → smooth
                                 tangent arc into rightward-horizontal →
                                 terminal hook UP-and-LEFT.
                                 NOT a right-angle box corner!
  Stroke 3 = 撇 (inside left leg): short, from mid-top down-and-left.
  Stroke 4 = 点 (inside right dot/leg): short, from mid-top down-and-right.

Fix vs retry_1:
- Left 撇 Bezier control MOVED to (140, 175) — chord midpoint would be
  around (110, 165); pulling control ~30 px RIGHT gives proper concave-
  right belly (curves outward to the left, like a wing).
- Top-right corner uses a SHOULDER-with-arc rather than a hard 90°.
- Terminal 弯钩 uses the KEY PRIMITIVE tangent-continuous arc so the
  bottom-right corner is a smooth curve, not L-shape.
- Hook flicks up-and-left at -115°.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def bezier(P0, P1, P2, steps, r0, r1):
    """Quadratic Bezier with tapered radius r0 -> r1."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

def line(P0, P1, steps, r0, r1):
    for i in range(steps + 1):
        t = i / steps
        x = P0[0] + (P1[0] - P0[0]) * t
        y = P0[1] + (P1[1] - P0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

# ---------- Stroke 1: outer 撇 (left wall, curved sweep) ----------
# Start high-middle, sweep down-and-left, terminating near bottom-left.
# Bezier control PULLED RIGHT of chord midpoint for a proper "wing" curve.
P0_pie = (95, 65)     # top start
P2_pie = (55, 260)    # bottom-left endpoint
# chord midpoint = (75, 162). Pull control ~40 px to the RIGHT.
P1_pie = (140, 170)   # control — makes belly bow OUT to the left
bezier(P0_pie, P1_pie, P2_pie, steps=110, r0=5.5, r1=2.0)

# ---------- Stroke 2: 横折弯钩 (top lid + right wall + bottom sweep + hook) ----------
# Beat A: short 横 top with a SMOOTH ROUNDED shoulder into the 竖
# (not a hard right angle). Use a small Bezier for the whole 横+shoulder.
lid_P0 = (95, 65)
lid_P2 = (220, 82)     # shoulder end — slightly down-right
lid_P1 = (220, 60)     # control at top-right corner rounds the elbow
bezier(lid_P0, lid_P2, lid_P2, 1, 5.5, 5.5)  # anchor
# Draw the 横+shoulder as a single rounded corner.
for i in range(80 + 1):
    t = i / 80
    x = (1 - t) ** 2 * lid_P0[0] + 2 * (1 - t) * t * lid_P1[0] + t * t * lid_P2[0]
    y = (1 - t) ** 2 * lid_P0[1] + 2 * (1 - t) * t * lid_P1[1] + t * t * lid_P2[1]
    dab(x, y, 5.5)

# Beat B: 竖 dropping from shoulder — the RIGHT wall.
B0 = (222, 82)
B_end = (222, 195)
line(B0, B_end, steps=80, r0=5.5, r1=5.0)

# Beat C: tangent-continuous arc curving from downward → rightward.
# Use KEY PRIMITIVE (drawer_memory).
R = 30
arc_steps = 30
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = B_end[0] + R * (1 - math.cos(t * math.pi / 2))
    y = B_end[1] + R * math.sin(t * math.pi / 2)
    dab(x, y, 4.5)
arc_end = (B_end[0] + R, B_end[1] + R)

# Beat D: terminal HOOK — flicks UP-and-LEFT from arc_end.
# ~35 px, angle -115° in image coords (up-and-slightly-left).
hook_len = 35
hook_angle = math.radians(-115)   # image coords: -angle means UP
hook_end = (arc_end[0] + hook_len * math.cos(hook_angle),
            arc_end[1] + hook_len * math.sin(hook_angle))
# Draw taper.
hook_steps = 30
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = arc_end[0] + (hook_end[0] - arc_end[0]) * t
    y = arc_end[1] + (hook_end[1] - arc_end[1]) * t
    r = 5.0 + (1.0 - 5.0) * t
    dab(x, y, r)

# ---------- Stroke 3: inside 撇 (small left leg of 乂) ----------
P0_in_pie = (150, 130)
P2_in_pie = (100, 220)
P1_in_pie = (140, 175)
bezier(P0_in_pie, P1_in_pie, P2_in_pie, steps=60, r0=4.5, r1=1.5)

# ---------- Stroke 4: inside 点 (small right dot/leg of 乂) ----------
# Short 反捺-style dot, thin→thick, ending in a broad press.
P0_dot = (155, 140)
P2_dot = (200, 215)
P1_dot = (170, 175)
bezier(P0_dot, P1_dot, P2_dot, steps=45, r0=2.0, r1=6.0)
# Terminal press for weight.
dab(P2_dot[0], P2_dot[1], 7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_094_风__retry_2/01_风.png")
print("saved")
