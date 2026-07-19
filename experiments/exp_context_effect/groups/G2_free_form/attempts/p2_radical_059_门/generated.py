"""
Render 门 (radical, 3 strokes) at 300x300 white canvas, black ink, PIL brush-dabs.

Stroke order (simplified 门):
  1. 点 (dian, dot) — top-left of the frame, a short teardrop dab.
  2. 竖 (shu) — left vertical from below the dot down to the baseline.
  3. 横折钩 (heng-zhe-gou) — top 横 spanning the top of the right pane,
     shoulder-dab, 竖 dropping down, terminal hook flicking up-and-left.

Layout on 300x300 (image coords, y grows DOWN):
  - Dot near (95, 85) → (108, 108): teardrop thin→thick.
  - Left 竖 from (78, 120) to (78, 255): straight uniform vertical
    with 顿-dabs at both ends. Sits BELOW the dot (dot is separate).
  - 横折钩: 横 from (135, 90) to (240, 88) with slight up-tilt,
    shoulder dab at (240, 88), 竖 to (232, 255), hook flick to
    (200, 228) at ~-140° in image coords.

Notes:
- Standalone-scale discipline: keep 顿 dabs modest (r+1), not r+2 balloons.
- Left 竖 does NOT touch the top-横 of the right side (open-top gap
  is a signature of 门).
- The dot goes ABOVE the left 竖, floating; MMH renders this as a
  short throw-away toward lower-left (like 撇 but tiny). We render it
  as a short teardrop 点 slanted down-left.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# --------------------------------------------------------------
# Stroke 1: 点 (top-left dot) — short slanted teardrop, thin→thick,
# oriented down-and-slightly-left (as MMH renders it on 门).
# --------------------------------------------------------------
# Start upper-right, end lower-left. Keep it modest, not blobby.
p_start = (110, 75)
p_end = (92, 105)
line_dabs(p_start[0], p_start[1], p_end[0], p_end[1],
          r_start=1.5, r_end=5.0, steps=120)
# Small terminal press to seat the dot's foot (subtle).
dab(p_end[0], p_end[1], 5.5)

# --------------------------------------------------------------
# Stroke 2: 竖 (left vertical). Straight, uniform, y from 120 → 258.
# Sits below the dot, x aligned with dot's foot roughly.
# --------------------------------------------------------------
LEFT_X = 78
V_TOP = (LEFT_X, 120)
V_BOT = (LEFT_X, 258)
R_V = 5.5
# 顿 dab at top
dab(V_TOP[0], V_TOP[1], R_V + 1.5)
line_dabs(V_TOP[0], V_TOP[1], V_BOT[0], V_BOT[1],
          r_start=R_V, r_end=R_V, steps=250)
# 顿 dab at bottom (blunt terminal)
dab(V_BOT[0], V_BOT[1], R_V + 1.5)

# --------------------------------------------------------------
# Stroke 3: 横折钩
#   3a. 横 from (135, 92) → (240, 86) with slight up-tilt.
#   3b. shoulder dab at (240, 86).
#   3c. 竖 from (232, 90) → (232, 258).
#   3d. hook flick from (232, 258) to (196, 232), ~ -140° image coords.
# --------------------------------------------------------------
R = 5.5

# 3a. 横
H_START = (138, 92)
H_END = (238, 86)
# 顿 dab at start of 横
dab(H_START[0], H_START[1], R + 1.5)
line_dabs(H_START[0], H_START[1], H_END[0], H_END[1],
          r_start=R, r_end=R + 1.0, steps=200)

# 3b. Shoulder dab (slightly larger) at the corner
SHOULDER = (238, 88)
dab(SHOULDER[0], SHOULDER[1], R + 2.5)

# 3c. 竖 descending, slightly leaning left (characteristic of 横折钩 in 门)
V2_TOP = (238, 92)
V2_BOT = (230, 258)
line_dabs(V2_TOP[0], V2_TOP[1], V2_BOT[0], V2_BOT[1],
          r_start=R + 0.5, r_end=R, steps=250)

# 3d. Hook flick: from V2_BOT up-and-left. Angle ~ -135° in image coords.
# Make it long and clearly directional. Use a straight tapered line to
# avoid accidental curl artifacts.
hook_len = 42
angle_deg = -135  # image coords: 0=+x, -90=up, so -135 is up-and-left 45°
angle_rad = math.radians(angle_deg)
HOOK_END = (V2_BOT[0] + hook_len * math.cos(angle_rad),
            V2_BOT[1] + hook_len * math.sin(angle_rad))
line_dabs(V2_BOT[0], V2_BOT[1], HOOK_END[0], HOOK_END[1],
          r_start=R + 0.5, r_end=1.0, steps=180)

# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_059_门/01_门.png"
img.save(out_path)
print(f"saved {out_path}")
