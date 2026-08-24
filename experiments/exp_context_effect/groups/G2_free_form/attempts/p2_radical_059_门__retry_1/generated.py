"""
Retry #1 for 门 (radical, 3 strokes).

Errata diagnosis (from curator, prior fail):
  Three of four components present (点 + 竖 + 横折钩) but the right
  横折钩's top 横 did not reach the left 竖 (visible ~40 px gap at
  top). Canonical 门 has the top 横 spanning between the two verticals
  as a single visual bar.

Fix applied here:
  Extend the top 横 leftward so it (nearly) touches the top of the
  left 竖. Target visual gap < ~10 px.
  Concretely: 横 now starts at x=85 (was 138), i.e. just past the
  left 竖's inner edge (LEFT_X=78, radius ~5.5), and left 竖 top
  raised to y≈88 so it visually meets the 横 line.

Stroke order (simplified 门, 3 strokes):
  1. 点 (top-left dot) — short teardrop above left 竖.
  2. 竖 (left vertical) — from just under the dot down to baseline,
     top raised so it reads as meeting the 横 line at the top-left.
  3. 横折钩 — top 横 spanning from just past the left 竖 all the way
     right; shoulder; 竖 dropping; hook flick up-and-left.
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


# --------------------------------------------------------------
# Stroke 1: 点 (top-left dot) — short slanted teardrop, thin→thick.
# Sits ABOVE the top of the left 竖. Small, not blobby.
# --------------------------------------------------------------
p_start = (108, 58)
p_end = (88, 88)
line_dabs(p_start[0], p_start[1], p_end[0], p_end[1],
          r_start=1.5, r_end=5.0, steps=120)
dab(p_end[0], p_end[1], 5.5)

# --------------------------------------------------------------
# Stroke 2: 竖 (left vertical). Straight uniform vertical.
# TOP raised to y≈105 so its top comfortably sits at the same
# altitude as the 横 line of the right 横折钩 (below-and-close, so
# the horizontal bar spans overhead as one visual unit).
# --------------------------------------------------------------
LEFT_X = 78
V_TOP = (LEFT_X, 110)
V_BOT = (LEFT_X, 262)
R_V = 5.5
# 顿 dab at top
dab(V_TOP[0], V_TOP[1], R_V + 1.5)
line_dabs(V_TOP[0], V_TOP[1], V_BOT[0], V_BOT[1],
          r_start=R_V, r_end=R_V, steps=260)
# 顿 dab at bottom (blunt terminal)
dab(V_BOT[0], V_BOT[1], R_V + 1.5)

# --------------------------------------------------------------
# Stroke 3: 横折钩
#   3a. 横 from (86, 100) → (245, 92) — extends far LEFT so the
#       visual gap to left 竖's top is < ~10 px (fix per errata).
#   3b. shoulder dab at (245, 92).
#   3c. 竖 from (245, 96) → (238, 262).
#   3d. hook flick from (238, 262) up-and-left.
# --------------------------------------------------------------
R = 5.5

# 3a. 横 — starts at x=86 (just past LEFT_X=78 + radius, so it visually
# meets/near-meets the top of the left 竖), ends at x=245.
H_START = (86, 100)
H_END = (245, 92)
# 顿 dab at start of 横 (left end) — modest so it doesn't blob into 竖
dab(H_START[0], H_START[1], R + 0.5)
line_dabs(H_START[0], H_START[1], H_END[0], H_END[1],
          r_start=R, r_end=R + 1.0, steps=220)

# 3b. Shoulder dab at the corner
SHOULDER = (245, 92)
dab(SHOULDER[0], SHOULDER[1], R + 2.5)

# 3c. 竖 descending, slight leftward lean (characteristic of 门 right)
V2_TOP = (245, 96)
V2_BOT = (238, 262)
line_dabs(V2_TOP[0], V2_TOP[1], V2_BOT[0], V2_BOT[1],
          r_start=R + 0.5, r_end=R, steps=260)

# 3d. Hook flick: from V2_BOT up-and-left at ~-140°.
hook_len = 40
angle_deg = -140
angle_rad = math.radians(angle_deg)
HOOK_END = (V2_BOT[0] + hook_len * math.cos(angle_rad),
            V2_BOT[1] + hook_len * math.sin(angle_rad))
line_dabs(V2_BOT[0], V2_BOT[1], HOOK_END[0], HOOK_END[1],
          r_start=R + 0.5, r_end=1.0, steps=180)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_059_门__retry_1/01_门.png"
img.save(out_path)
print(f"saved {out_path}")
