"""
仉 (zhǎng) — Phase-3 character, 4 strokes.
Structure: 亻 (left, tall-narrow ~35-40% width) + 几 (right, compressed).

Per form_catalog left-position compression:
- 亻 on the LEFT: 撇 + 竖, ~35-40% of canvas width, taller than compact.
- 几 on the RIGHT: 撇 + 横折弯钩. Shared top-left joint. Compress horizontal
  extent to fit remaining ~55-60% canvas width.

Strokes:
1. 亻 撇 — from upper-mid-left curving down-left
2. 亻 竖 — vertical dropping from midpoint of 撇
3. 几 撇 — from top-mid-right curving down-left (in 几's box)
4. 几 横折弯钩 — 横 rightward from same shared joint, 折, 竖 with slight
   inward lean, 弯 arc, small hook flicking up-left.

Renderer: PIL brush-dabs.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(p0, p1, r0, r1, steps=200):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=250, ease=1.0):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ============ 亻 (LEFT, compressed left-radical) ============
# Occupies roughly x=40..115, tall (y=55..255)
# Stroke 1: 撇
pie1_p0 = (100, 60)     # upper start
pie1_ctrl = (92, 140)
pie1_p2 = (45, 245)     # lower-left tip
dab(pie1_p0[0], pie1_p0[1], 7)
bezier_dabs(pie1_p0, pie1_ctrl, pie1_p2, r0=7.0, r1=1.5, steps=400, ease=1.3)

# Stroke 2: 竖 — drops from midpoint of 撇, straight down
shu1_top = (85, 130)
shu1_bot = (85, 258)
dab(shu1_top[0], shu1_top[1], 6.5)
line_dabs(shu1_top, shu1_bot, r0=5.5, r1=5.5, steps=220)
dab(shu1_bot[0], shu1_bot[1], 6.0)


# ============ 几 (RIGHT, compressed) ============
# Occupies roughly x=140..270, y=90..250
# Shared top-left joint of the 几
JOINT_TL = (155, 105)

# Stroke 3: 撇 — starts at joint, bows leftward, tip lands lower-mid
p0_pie2 = JOINT_TL
ctrl_pie2 = (140, 170)
p2_pie2 = (128, 245)
dab(p0_pie2[0], p0_pie2[1], 7)
bezier_dabs(p0_pie2, ctrl_pie2, p2_pie2, r0=7.0, r1=1.5, steps=320, ease=1.2)

# Stroke 4: 横折弯钩
# Beat 1: 横 — from joint rightward, tilts slightly up
heng_start = JOINT_TL
heng_end = (255, 95)
dab(heng_start[0], heng_start[1], 7)
line_dabs(heng_start, heng_end, r0=6.5, r1=6.2, steps=180)

# Shoulder dab at 折 corner
shoulder = heng_end
dab(shoulder[0], shoulder[1], 8)

# Beat 2: 竖 — slight leftward lean
shu2_end_x = 240
shu2_end_y = 210
shu2_ctrl = (232, 155)
bezier_dabs(shoulder, shu2_ctrl, (shu2_end_x, shu2_end_y),
            r0=6.5, r1=6.0, steps=220)

# Beat 3: 弯 — quarter arc into rightward horizontal
R = 26
x0, y0 = shu2_end_x, shu2_end_y
arc_end_x = x0 + R
arc_end_y = y0 + R
arc_steps = 80
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 6.0)

# Beat 4: very short 横 rightward from arc endpoint
tail_end = (arc_end_x + 10, arc_end_y - 2)
line_dabs((arc_end_x, arc_end_y), tail_end, r0=6.0, r1=5.5, steps=60)

# Hook (钩) — small up-left flick (~-115°)
hook_len = 22
hook_angle_deg = -120
rad = math.radians(hook_angle_deg)
hook_end = (tail_end[0] + hook_len * math.cos(rad),
            tail_end[1] + hook_len * math.sin(rad))
hook_ctrl = (tail_end[0] + 0.45 * hook_len * math.cos(rad) + 1,
             tail_end[1] + 0.45 * hook_len * math.sin(rad) + 2)
bezier_dabs(tail_end, hook_ctrl, hook_end, r0=5.5, r1=1.2, steps=120)


out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0113_仉/01_仉.png"
img.save(out_path)
print(f"Saved {out_path}")
