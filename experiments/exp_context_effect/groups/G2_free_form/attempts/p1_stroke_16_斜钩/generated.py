"""
Render 斜钩 (xie gou / 戈钩) — a slanting hook.

Per drawer_memory.md:
- Primary: slants down-and-right (从左上向右下). Not a straight ruler
  line; conventional 斜钩 has a gentle bow with the belly opening
  toward the lower-left (concave toward upper-right).
- Hook: short flick UP from the bottom-right endpoint (the tip of the
  primary), tapering to a sharp point.
- Both primary and hook rendered via brush-dabs with linearly varying
  radius to get calligraphic taper.
- Image coords: y grows DOWN. 300x300, white background, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Primary: 斜钩 body (gentle bow, upper-left -> lower-right) ----
# Start near upper-left area, end near lower-right area.
P0 = (95.0, 55.0)   # top-left start
P2 = (245.0, 245.0)  # bottom-right end (tip of the primary)
# Control point pulled toward LOWER-LEFT so the curve bows with its
# belly on the lower-left side (classic 戈钩 curvature: concave toward
# upper-right; the ink bulges down-and-left of the P0->P2 chord).
P1 = (125.0, 195.0)

# Small 顿 press at the start
dab(P0[0], P0[1], 6.5)

# Sample a quadratic Bezier
N = 420
r_start = 5.2   # thicker at head after the 顿
r_end = 3.2    # slightly thinner toward the hook joint (still visible)
for i in range(N + 1):
    t = i / N
    u = 1 - t
    x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
    y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
    r = r_start + (r_end - r_start) * t
    dab(x, y, r)

# ---- Hook: short flick UP from the bottom-right endpoint ----
# 斜钩's hook goes upward (slightly leaning up-and-slightly-right to
# up-and-slightly-left of vertical). We aim ~85 degrees above horizontal,
# short length ~28 px, tapering to a sharp tip.
hook_start = P2
hook_len = 40.0
hook_angle_deg = -115.0  # in image coords, -90 = straight up; -115 = up-and-left
rad = math.radians(hook_angle_deg)
hook_end = (hook_start[0] + hook_len * math.cos(rad),
            hook_start[1] + hook_len * math.sin(rad))

# One slightly-larger 顿 dab at the joint (per memory: press before flick)
dab(hook_start[0], hook_start[1], 6.2)

Nh = 160
rh_start = 4.6
rh_end = 1.0  # sharp tip
for i in range(Nh + 1):
    t = i / Nh
    x = hook_start[0] + (hook_end[0] - hook_start[0]) * t
    y = hook_start[1] + (hook_end[1] - hook_start[1]) * t
    r = rh_start + (rh_end - rh_start) * t
    dab(x, y, r)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_斜钩.png")
img.save(out_path)
print(f"Saved: {out_path}")
