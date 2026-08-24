"""
p1_stroke_29 横折折撇 (heng-zhe-zhe-pie)
A 4-beat compound stroke:
  1) 横 short horizontal, slight up-tilt
  2) 折 shoulder-dab, then short slanted segment going down-and-left
     (like a mini 撇 body)
  3) 折 shoulder-dab, then short near-horizontal segment going right
     (short middle horizontal)
  4) final 撇: bowed throw-away going down-and-left, thick->thin,
     ending in a sharp tip
Canonical example: the outer stroke in 及 / 建-family radicals.

Reasoning:
- Uses PIL brush-dab technique per drawer_memory.md.
- Each 折 corner gets ONE slightly-larger 顿 dab to visualize the press
  and hide the seam.
- The final 撇 uses a quadratic Bezier bow (not ruler-straight) and
  tapers to a sharp point.
- Middle beats are noticeably shorter than the final 撇, which is the
  visual anchor of the whole stroke.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


R = 5           # base uniform stroke radius
R_SHOULDER = 8  # 顿 press-dab at each 折 corner
R_START_DAB = 7 # initial 顿 dab

# ---- Beat 1: 横 (short horizontal, slight up-tilt) ----
# start upper-left area, tilt up 3-5 degrees
p1_start = (70, 78)
p1_end   = (170, 70)     # ~100 px wide, tiny rise
dab(*p1_start, R_START_DAB)                       # 顿笔 at start
line_dabs(*p1_start, *p1_end, R, R, steps=300)
# ramp up radius slightly toward the corner (press-in)
line_dabs(p1_end[0] - 6, p1_end[1] + (p1_end[1]-p1_start[1]) * 6 / 100,
          p1_end[0], p1_end[1], R, R_SHOULDER, steps=60)

# 折 shoulder dab #1
corner1 = p1_end
dab(*corner1, R_SHOULDER)

# ---- Beat 2: short slanted segment going down-and-left (mini 撇 body) ----
# This is the "second beat" of 横折折撇 — a short down-left slant
# leading to the next corner. About 45-55 px long, ~45deg down-left.
p2_start = corner1
p2_end   = (135, 120)    # down and left
line_dabs(*p2_start, *p2_end, R_SHOULDER, R, steps=250)

# 折 shoulder dab #2
corner2 = p2_end
dab(*corner2, R_SHOULDER)

# ---- Beat 3: short horizontal segment going right (middle 横) ----
# The 3rd beat runs rightward again, ~50 px, slight up-tilt so the
# next 撇 has room to sweep down-left across the canvas.
p3_start = corner2
p3_end   = (200, 118)
line_dabs(*p3_start, *p3_end, R, R, steps=250)
# ramp up at the joint to prepare for the final 撇
dab(*p3_end, R_SHOULDER)

# ---- Beat 4: final 撇 (bowed throw-away, thick -> thin) ----
# Long sweeping 撇 going down-and-left, with gentle rightward bow
# (Bezier control point pulled toward the interior/right).
# Thick at joint, tapering to a sharp tip.
pie_p0 = p3_end                 # (200, 118)
pie_p2 = (70, 250)              # lower-left tip
pie_p1 = (185, 190)             # control point: rightward bow
bezier_dabs(pie_p0, pie_p1, pie_p2, R_SHOULDER, 1.2, steps=500)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p1_stroke_29_横折折撇/01_横折折撇.png")
print("saved 01_横折折撇.png (300x300)")
