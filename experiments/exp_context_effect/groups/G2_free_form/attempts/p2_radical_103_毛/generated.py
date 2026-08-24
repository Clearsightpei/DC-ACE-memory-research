"""
毛 (radical, 4 strokes) — PIL brush-dabs, 300x300, black ink on white.

Stroke order (canonical for 毛):
  1. 撇 (pie)         — short throw-away at the top, right→left-down.
  2. 横 (heng, upper) — short-medium horizontal, sits below the 撇.
  3. 横 (heng, middle)— longer horizontal, extends further left than the
                        upper 横.
  4. 竖弯钩 (shu-wan-gou) — vertical descending, curving smoothly into
                            a rightward horizontal, ending in an up-and-
                            left hook flick.

Reference memory:
  - Length-ratio for stacked horizontals (principle 6): the upper 横 is
    SHORTER than the middle 横 in 毛.
  - 竖弯 uses the tangent-continuous quarter-arc primitive.
  - 弯钩 flick goes up-and-left, ~-110° in image coords.
  - Hook joining-dab must equal segment radius (principle 5 corollary):
    r+2 at hook base bleeds a stray nub.
  - Standalone-scale: bigger curvature, smaller start-press than the
    inside-character calibration.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(p0, p1, r0, r1, steps=None):
    """Linear stroke with per-step radius ramp."""
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def stroke_bezier(p0, p1, p2, r0, r1, steps=200):
    """Quadratic Bezier stroke with taper."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 撇 (top) — short pie throw ----
# Starts upper-right, curves down and left, tapers to a point.
# Gentle rightward bow, thick→thin. Scaled up for standalone canvas.
p0_pie = (185, 40)
p2_pie = (100, 95)
p1_pie = (165, 60)  # control pulled toward interior (right)
dab(*p0_pie, 7)  # 顿 start
stroke_bezier(p0_pie, p1_pie, p2_pie, r0=6, r1=1.4)


# ---- Stroke 2: 横 (upper, shorter) ----
# Sits below the pie's tip, extends rightward.
# Slight upward tilt (~3-5°).
p0_h1 = (105, 118)
p1_h1 = (220, 105)
dab(*p0_h1, 6)  # 顿 start
stroke_line(p0_h1, p1_h1, r0=5, r1=5)
dab(*p1_h1, 6)  # small terminal press


# ---- Stroke 3: 横 (middle, longer) — extends further LEFT ----
# This 横 is longer, and its left edge extends further left than the
# upper 横. Slight upward tilt.
p0_h2 = (45, 175)
p1_h2 = (230, 160)
dab(*p0_h2, 6)  # 顿 start
stroke_line(p0_h2, p1_h2, r0=5, r1=5)
dab(*p1_h2, 6)


# ---- Stroke 4: 竖弯钩 ----
# Vertical descends from top (starts near the pie/upper-horizontals
# intersection region), curves smoothly right, ends with up-left hook.
# Use the tangent-continuous quarter-arc primitive from memory.

# 4a. Vertical segment (straight down)
v_top = (155, 75)   # top starts up near the pie/upper-heng zone
v_bot = (155, 235)  # bottom of vertical, before arc begins
dab(*v_top, 6)      # 顿 start
stroke_line(v_top, v_bot, r0=5, r1=5)

# 4b. Tangent-continuous quarter-arc from (v_bot) sweeping into
#     rightward horizontal. R chosen so arc lands at reasonable width.
R = 45
arc_x0, arc_y0 = v_bot
arc_steps = 90
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = arc_x0 + R * (1 - math.cos(t * math.pi / 2))
    y = arc_y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5)

# arc ends at (arc_x0 + R, arc_y0 + R)
arc_end = (arc_x0 + R, arc_y0 + R)

# 4c. Continue horizontal rightward from arc end
h_end = (255, arc_end[1])
stroke_line(arc_end, h_end, r0=5, r1=5)

# 4d. Hook flick — up and slightly left from h_end
# Flick length ~34 px, angle ~-110° (up-and-slightly-left).
# Per corollary: joining-dab at hook base = segment radius (NOT r+2).
angle = math.radians(-110)  # measured from +x axis, y-down (so -110 = up-left)
# In screen coords: angle in math sense, y grows DOWN. We want up-and-left:
# dx negative, dy negative. Use direct components.
flick_len = 36
dx = math.cos(angle) * flick_len       # cos(-110°) ≈ -0.342  -> dx negative
dy = math.sin(angle) * flick_len       # sin(-110°) ≈ -0.940  -> dy negative
# But our image coords have y grow DOWN. For up-motion we want dy negative,
# so we want the flick's screen-y delta negative. The math above already
# gives that (sin(-110°) is negative), good.
flick_end = (h_end[0] + dx, h_end[1] + dy)
# Joining dab at hook base — equal to segment radius (NOT r+2)
dab(*h_end, 5)
stroke_line(h_end, flick_end, r0=5, r1=1.2)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_103_毛/01_毛.png"
)
print("wrote 01_毛.png")
