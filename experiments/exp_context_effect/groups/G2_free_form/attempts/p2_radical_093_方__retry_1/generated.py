"""
方 (radical, 4 strokes) — RETRY 1.

Errata fix ideas applied:
- Prior attempt had (a) dot floating too high with a big gap, (b) top 横
  extending too wide (crowded canvas), (c) 撇 starting inside/at top of
  横 (crossing barely visible), (d) 横折钩 top starting at the same y as
  the top 横 instead of just below it.

Applying:
- "square" aspect family from radical_position_rules — 方 fits
  ~70% x 70% of canvas centered slightly high.
- form_catalog "撇 as body-crossing diagonal" — 撇 must start ABOVE
  the top 横 (y ~65, 横 at y ~100), cross visibly.
- form_catalog "点 as roof-cap dot" adapted — dot is small teardrop
  above the 横 with modest gap (~15 px), angle down-right.
- 横折钩 sits UNDER the top 横 (top of 折 shoulder just below the
  横's y), with vertical dropping ~130 px, ending in an up-left hook.

Stroke order (canonical MMH): 点、横、横折钩、撇.
"""

from PIL import Image, ImageDraw
import math, os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200, ease=None):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = ease(t) if ease else t
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def draw_dot(x0, y0, x1, y1, r0=1.5, r1=5):
    steps = int(max(40, math.hypot(x1 - x0, y1 - y0) * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        tt = t ** 1.4
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(x1, y1, r1 + 0.5)


# ---- Stroke 1: 点 (top dot) — small teardrop angling down-right,
# sits ABOVE the top 横 with a small gap (~15 px). Positioned slightly
# right-of-center as GT shows.
draw_dot(148, 55, 168, 82, r0=1.4, r1=4.2)

# ---- Stroke 2: 横 (top horizontal) — moderate width, slight up-tilt.
# Contained within ~x=65..235 (170 px wide) — narrower than prior attempt.
h_x0, h_y0 = 65, 108
h_x1, h_y1 = 235, 100
dab(h_x0, h_y0, 4.5)                       # 顿 start
line_dabs(h_x0, h_y0, h_x1, h_y1, 3.4, 3.4)
dab(h_x1, h_y1, 4.5)                       # 顿 end

# ---- Stroke 3: 横折钩 — starts UNDER the top 横 on the right side.
# In GT the 折 shoulder sits at ~y=115 (just below the top 横 y=100..108).
# It's a slightly-diagonal drop leaning a hair left, terminating in an
# up-and-left hook. This is a fold that encloses the right-and-bottom
# of the character.
zg_top_x, zg_top_y = 218, 115
zg_bot_x, zg_bot_y = 205, 240
dab(zg_top_x, zg_top_y, 5.0)               # 折 shoulder dab
line_dabs(zg_top_x, zg_top_y, zg_bot_x, zg_bot_y, 3.6, 3.6)
# hook flick up-and-left ~-130°, ~30 px, taper r=3.6→1.0
hook_len = 34
hook_angle_deg = -128
ha = math.radians(hook_angle_deg)
hk_x = zg_bot_x + hook_len * math.cos(ha)
hk_y = zg_bot_y + hook_len * math.sin(ha)
line_dabs(zg_bot_x, zg_bot_y, hk_x, hk_y, 3.6, 1.0)

# ---- Stroke 4: 撇 — LONG body-crossing diagonal.
# MUST start ABOVE the top 横 so the crossing is visible: p0 y=70 (well
# above 横's y=100–108). Sweeps to lower-left ending near (55, 265).
# Gentle rightward bow via bezier control at (145, 175).
p0 = (172, 70)      # top ABOVE the 横
p2 = (55, 265)      # lower-left tail
p1 = (145, 175)     # control pulled right for gentle bow
bezier_dabs(p0, p1, p2, r_start=5.5, r_end=1.2, steps=280)
# 顿 press at start of the 撇
dab(p0[0], p0[1], 5.5)

out = os.path.join(os.path.dirname(__file__), "01_方.png")
img.save(out)
print(f"wrote {out} ({img.size})")
