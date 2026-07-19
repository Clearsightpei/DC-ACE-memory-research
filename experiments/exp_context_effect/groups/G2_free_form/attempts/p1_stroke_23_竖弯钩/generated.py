"""
p1_stroke_23_竖弯钩 (shu-wan-gou) — vertical, smooth arc into horizontal, upward hook.
Rendered at 300x300, white background, black ink, PIL brush-dab technique.

Structure (per drawer_memory.md):
  - Primary: 竖弯 (proven PASS) — straight 竖 top→bottom, then smooth quarter-arc
    into a rightward 横. No shoulder dab (this is 弯, not 折). Uniform radius
    through arc.
  - Terminal: 钩 flicks UP (and slightly left) from the right end of the 横,
    tapering thick→thin to a sharp tip. This is what makes it 竖弯钩 vs 竖弯.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r, fill="black"):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fill)


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---- Geometry ----
# Vertical 竖 segment
shu_x = 120         # x-position of the vertical
shu_y0 = 70         # top of vertical
shu_y1 = 200        # bottom of vertical (where arc begins)

# Quarter-arc center: the arc turns the downward motion into rightward.
# Center is to the RIGHT of the vertical's bottom by R, at the same y.
R = 38
arc_cx = shu_x + R
arc_cy = shu_y1

# Horizontal 横 after the arc
heng_y = shu_y1 + R          # y where horizontal runs (arc lands here)
heng_x_start = arc_cx        # arc lands directly below center
heng_x_end = 245             # right end of horizontal (before hook)

R_MAIN = 6                   # uniform ink radius for primary body

# 顿笔 dab at top of vertical
dab(shu_x, shu_y0, R_MAIN + 2)

# Vertical body (uniform)
line_dabs(shu_x, shu_y0, shu_x, shu_y1, R_MAIN, R_MAIN, steps=260)

# Smooth quarter arc (no shoulder dab, uniform radius)
# Parametrize: angle from pi (pointing left from center = arc entry at (shu_x, shu_y1))
# sweeping to 3*pi/2 (pointing down from center = arc exit at (arc_cx, heng_y)).
ARC_STEPS = 220
for i in range(ARC_STEPS + 1):
    t = i / ARC_STEPS
    theta = math.pi + t * (math.pi / 2)   # pi -> 3pi/2
    x = arc_cx + R * math.cos(theta)
    y = arc_cy + R * math.sin(theta)
    dab(x, y, R_MAIN)

# Horizontal body from arc exit to hook base (uniform)
line_dabs(heng_x_start, heng_y, heng_x_end, heng_y, R_MAIN, R_MAIN, steps=280)

# Small terminal press at hook base (transition ink into the hook)
dab(heng_x_end, heng_y, R_MAIN + 2)

# ---- Hook (钩) — flicks UP and slightly LEFT from right end ----
# Angle in image coords: up = -y. Slight leftward tilt so it doesn't look like a plain vertical spike.
hook_len = 42
hook_angle_deg = -100   # -90 would be straight up; -100 tilts up-and-slightly-left
rad = math.radians(hook_angle_deg)
hook_x0, hook_y0 = heng_x_end, heng_y
hook_x1 = hook_x0 + hook_len * math.cos(rad)
hook_y1 = hook_y0 + hook_len * math.sin(rad)

# Taper thick (matches primary) -> sharp tip
line_dabs(hook_x0, hook_y0, hook_x1, hook_y1, R_MAIN + 1, 1.2, steps=260)

# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_23_竖弯钩/01_竖弯钩.png"
img.save(out_path)
print(f"Saved {out_path}")
