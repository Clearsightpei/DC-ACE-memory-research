"""
冂 (radical, 2 strokes): 竖 (left) + 横折钩 (top-right, with small hook).

Looking at GT: left vertical starts a bit high, extends down. Right side:
horizontal starts around the top of the left 竖 (very slightly higher than
left top actually — the two tops don't align exactly), goes right, shoulder-
dabs, drops down as a 竖, and finishes with a small hook flicking up-and-
slightly-left. The radical is tall — occupies most of the canvas vertically.

Approach: standalone-scale discipline (from memory) — 顿 dabs r+1 at plain
endpoints, r+3 at the shoulder. Slight up-tilt on the top 横 (~3°).
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
        d = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(d * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: left 竖 ----
# Standalone scale — plain-radius endpoints, no r+2 balloons.
sx0, sy0 = 82, 78
sx1, sy1 = 78, 258
# subtle start press (r+1 only) and plain terminal
dab(sx0, sy0, 6)
line_dabs(sx0, sy0, sx1, sy1, 5.0, 5.0)
dab(sx1, sy1, 5.0)  # plain blunt end (no balloon)

# ---- Stroke 2: 横折钩 ----
# GT: the top 横 sits slightly higher than the left 竖 top, and hangs
# a hair *over* the 竖 to the left of it. Top 横 tilts up ~4°.
hx0, hy0 = 78, 74   # start slightly left of/above the 竖 top (typical 冂)
hx1, hy1 = 232, 62  # rises 12 px over 154 px → ~4.5° up-tilt
# subtle start press
dab(hx0, hy0, 6)
line_dabs(hx0, hy0, hx1, hy1, 5.0, 5.0)

# shoulder dab (real 折 corner — r+3 IS legitimate here)
dab(hx1, hy1, 7.5)

# 竖 down. Terminal 竖 of 横折钩 leans slightly inward.
vx0, vy0 = hx1, hy1
vx1, vy1 = 224, 250
line_dabs(vx0, vy0, vx1, vy1, 5.0, 5.0)

# hook flick from bottom endpoint — small, up-and-slightly-left.
hook_len = 26
hook_angle_deg = -120
ang = math.radians(hook_angle_deg)
hkx1 = vx1 + hook_len * math.cos(ang)
hky1 = vy1 + hook_len * math.sin(ang)
# joining dab equal to segment r (avoid sub-hook nub — memory rule)
dab(vx1, vy1, 5.0)
line_dabs(vx1, vy1, hkx1, hky1, 5.0, 1.2)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_024_冂/01_冂.png"
)
