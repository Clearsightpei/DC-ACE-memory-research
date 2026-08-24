"""
Render 欠 (4-stroke radical) using PIL brush-dabs at 300x300.

欠 structure (4 strokes, canonical):
  1. 撇 (short) — small throw at top-left of the "hat"
  2. 横钩 — small 横 at top-right of the hat + hook down-and-left
  3. 撇 (long) — begins UNDER the hat (around middle-right, x~155 y~130),
     sweeps DOWN-and-LEFT with a gentle rightward bow to the lower-left.
  4. 捺 — begins near the top of stroke 3 (~ (150, 135)), throws
     DOWN-and-RIGHT, thin→thick, ending in a broad terminal foot.

Revision notes (v2):
- Reduced stroke thickness for top "hat" (was reading as chunky bar).
- Started strokes 3 and 4 LOWER (y~130+) so they clearly begin
  BELOW the hat, matching the GT layout.
- Made the hat smaller and higher up so it stays visually separate
  from the base X.
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
        steps = max(40, int(2 * math.hypot(x1 - x0, y1 - y0)))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=220, easing=None):
    for i in range(steps + 1):
        t = i / steps
        te = easing(t) if easing else t
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r0 + (r1 - r0) * te
        dab(x, y, r)


# ---- Stroke 1: 撇 (short top) — the little curl at top-left of hat ----
# Upper-right start ~(148, 65) → lower-left ~(115, 108). Small, thin.
p0 = (148, 62)
p2 = (112, 112)
ctrl = (128, 82)
dab(p0[0], p0[1], 5.0)  # small 顿 press
bezier_dabs(p0, ctrl, p2, r0=4.5, r1=1.2, steps=180)

# ---- Stroke 2: 横钩 — small 横 at top + hook ----
# 横 begins near the top of stroke 1 (~x=132), runs right to ~x=200 y~92.
# Then hook down-and-left to ~(180, 122).
h_start = (132, 78)
h_end = (198, 92)
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r0=3.8, r1=4.0)
# Shoulder dab at corner (small, r+2 relative to segment radius)
dab(h_end[0], h_end[1], 5.5)
# Hook flick down-and-left, taper to sharp tip
hook_end = (178, 122)
line_dabs(h_end[0], h_end[1], hook_end[0], hook_end[1], r0=4.0, r1=1.1, steps=100)

# ---- Stroke 3: 撇 (long) — the big sweep down-and-left ----
# Begins BELOW the hat around (155, 128) and throws to lower-left (~72, 260).
# Thick→thin with gentle rightward bow.
p0 = (155, 128)
p2 = (72, 262)
ctrl = (135, 200)  # control pulled right/interior for gentle bow
dab(p0[0], p0[1], 6.5)  # 顿 press
bezier_dabs(p0, ctrl, p2, r0=6.0, r1=1.4, steps=300)

# ---- Stroke 4: 捺 — right diagonal ending in a broad foot ----
# Begins near stroke 3's top (~(152, 132)), throws down-and-right to (~240, 258).
# Thin→thick, ends in broad flat foot.
p0 = (152, 132)
p2 = (238, 258)
ctrl = (180, 210)  # slight bow, belly on lower-left
bezier_dabs(p0, ctrl, p2, r0=1.6, r1=6.0, steps=280, easing=lambda t: t ** 1.15)
# Terminal broad foot press — flat/broad
foot_cx, foot_cy = 244, 260
dab(foot_cx - 4, foot_cy, 7.0)
dab(foot_cx, foot_cy + 1, 7.5)
dab(foot_cx + 5, foot_cy - 1, 6.2)

# ---- Save ----
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_112_欠/01_欠.png"
img.save(out)
print(f"Saved {out}")
