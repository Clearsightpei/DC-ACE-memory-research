"""
Render 户 (radical, 4 strokes) on 300x300 white canvas via PIL brush-dabs.

户 = 4 strokes:
  1. 点 (dot) — small teardrop at upper-left area, slanted down-and-right.
  2. 横 (horizontal) — short horizontal below the dot; forms the top bar.
  3. 横折钩/横折 — actually canonical 户: stroke 3 is 横折 (short 横 then
     竖 hooking down) forming the top-right box of the 尸-body. Reading
     the GT: the top-right shows a small "口"-like box, so stroke 3 is
     横折 that goes right then down (short vertical).
  4. 撇 — long swept 撇 from upper-body down to lower-left, dominates the
     silhouette and forms the left/bottom edge of the character.

Applying G2 memory principles:
- Principle 2: adjacent strokes share joints (no inset gap).
- Principle 5: hooks/flicks are the identity — but 户's stroke 3 is 横折
  (blunt), not 横折钩 (no bottom hook per canonical MMH).
- Principle 9: draw named primitives; do not merge them.
- Standalone scale-up: fill 300x300; use r=6-8 for stand-alone 顿 dabs;
  make the 撇 long and swept.
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
        steps = max(int(math.hypot(x1 - x0, y1 - y0)) * 3, 60)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def teardrop(x0, y0, x1, y1, r0, r1, steps=200, ease=1.4):
    # teardrop dot: r ramps up along the stroke with easing
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Stroke 1: 点 (dot) — clearly separated above the 横, upper-center ----
# Push it higher (y=35-58) and slightly right so it visibly sits ABOVE
# the stroke-2 横. Small teardrop slanting down-right.
teardrop(130, 38, 152, 62, r0=1.8, r1=6.5)
dab(152, 62, 7)  # terminal press

# ---- Stroke 2: 横 (short horizontal) — spans middle-upper ----
# Placed at y=95 so there is clear whitespace between the dot (ends y=62)
# and this 横. Slight up-tilt.
h2_x0, h2_y0 = 75, 100
h2_x1, h2_y1 = 210, 92
dab(h2_x0, h2_y0, 6.5)  # start 顿
line_dabs(h2_x0, h2_y0, h2_x1, h2_y1, r0=5.0, r1=5.0)
dab(h2_x1, h2_y1, 6.5)  # end 顿

# ---- Stroke 3: 横折 — short 横 then 竖 down forming top-right box ----
# Sits BELOW stroke 2 (y=125-180). Short horizontal then folds down.
s3_h_x0, s3_h_y0 = 115, 130
s3_h_x1, s3_h_y1 = 215, 122
s3_v_x1, s3_v_y1 = 210, 185
dab(s3_h_x0, s3_h_y0, 5.5)
line_dabs(s3_h_x0, s3_h_y0, s3_h_x1, s3_h_y1, r0=5.0, r1=5.0)
# Shoulder dab at corner
dab(s3_h_x1, s3_h_y1, 7.5)
# 竖 down
line_dabs(s3_h_x1, s3_h_y1, s3_v_x1, s3_v_y1, r0=5.5, r1=5.0)
dab(s3_v_x1, s3_v_y1, 6.5)  # blunt terminal press

# ---- Stroke 4: 撇 — long sweeping 撇 from upper-left body area down ----
# Start above stroke 2 (crossing visibility): top y=80, x=110 so the
# 撇 clearly pokes above the 横. Sweep to lower-left.
p0 = (115, 80)       # upper start (above stroke 2's y=95)
p1 = (105, 180)      # control point — very gentle rightward bow
p2 = (45, 275)       # lower-left tip (fills canvas)
# 顿 dab at start
dab(p0[0], p0[1], 7.5)
bezier_dabs(p0, p1, p2, r0=9.0, r1=1.2, steps=500)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_097_户/01_户.png"
)
print("wrote 01_户.png")
