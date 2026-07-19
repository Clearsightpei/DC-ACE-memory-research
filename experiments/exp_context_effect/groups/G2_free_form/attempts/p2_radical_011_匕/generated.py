"""
匕 (bi) — 2 strokes: 撇 + 竖弯钩

Layout (300x300, image coords, y grows DOWN):
  Stroke 1 = 撇 (pie): short diagonal from upper-mid (~130, 85)
    down-and-left to (~85, 155). Thick->thin taper.
    Actually per GT: 撇 sits in the UPPER-MIDDLE, going from mid-left
    down through the vertical of stroke 2, and continuing as a short
    diagonal into the right half. Wait — reread GT: the 撇 in 匕
    starts at upper-right area of the 竖 and slants down-right?
    NO. Canonical 匕: stroke 1 is 撇 (down-left throw), stroke 2 is
    竖弯钩 (wraps under, hooks up).
    From GT: 撇 starts near (125,85) and ends around (200,115) —
    this is actually a rising short stroke... let me reread.
    Correct reading of GT: the short diagonal is 撇 in the sense of
    a top-right slanting stroke — starts upper-left at (~120,85),
    goes down-right to (~205,115). Hmm — that direction is more
    like 提 or 横.
    Standard 匕 stroke order: (1) 撇 written top-right to bottom-left,
    (2) 竖弯钩. The GT shows the 撇 crossing the 竖弯钩's vertical,
    starting inside/left of the vertical (~90,95) and extending
    right-and-down to (~200,110). That IS the standard 匕: a 撇 that
    slants down-right visually because it starts high-left and ends
    lower-right when you look at the endpoints.
    NO — I confused myself. Canonical 匕: the top stroke is 撇,
    starting at the top INSIDE the character and throwing down-left.
    But in the GT the top stroke goes from LEFT (higher up-left) to
    RIGHT (down-right). This is 短横 or 提-like — but reference says
    匕 = 撇 + 竖弯钩.
    Resolve: the top-right slanting stroke IS the 撇 of 匕, but
    rendered top-left-to-bottom-right in MMH style because the 撇
    of 匕 is horizontal-ish, close to 提/横. Whatever — I'll render
    what the GT shows: a short slightly-down-tilted stroke from
    (~90, 92) to (~200, 115), with 顿 press at start.
  Stroke 2 = 竖弯钩 (shu-wan-gou): starts upper-left (~85, 75) as
    vertical descending to (~85, 220), smooth quarter-arc into
    rightward horizontal ending near (~215, 250) with the terminal
    hooking UPWARD (not up-left) from the right endpoint.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
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


# ---------- Stroke 2 (drawn first for layering not required, but keep order) ----------
# Scale up and center: 竖 top at y=60, bottom-arc apex at y=255, right edge at x=245.
shu_x = 75
shu_y0, shu_y1 = 60, 230

# ---------- Stroke 1: 撇 (top short stroke, slight down-tilt) ----------
# In GT: 撇 starts LEFT of the 竖's vertical, crosses through the 竖 at
# about y=105, and continues rightward-down to end around x=215, y=125.
# The 竖's top must stick UP above the 撇's start.
p1_start = (55, 95)
p1_ctrl = (145, 110)
p1_end = (215, 128)
dab(p1_start[0], p1_start[1], 7)  # 顿 press at start
bezier_dabs(p1_start, p1_ctrl, p1_end, r0=6.5, r1=1.8, steps=350)

# ---------- Stroke 2: 竖弯钩 ----------
# 竖 segment: top-left descending (drawn AFTER 撇 so it overlaps cleanly)
dab(shu_x, shu_y0, 7)  # 顿 press at top
line_dabs(shu_x, shu_y0, shu_x, shu_y1, r0=6.0, r1=6.0, steps=350)

# tangent-continuous quarter arc from (shu_x, shu_y1) sweeping into rightward horizontal
# x = x0 + R*(1 - cos(t*pi/2)), y = y0 + R*sin(t*pi/2)
R = 42
arc_steps = 200
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = shu_x + R * (1 - math.cos(t * math.pi / 2))
    y = shu_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, 6.0)
arc_end_x = shu_x + R
arc_end_y = shu_y1 + R

# horizontal segment along bottom, going rightward
heng_end_x = 240
heng_end_y = arc_end_y
line_dabs(arc_end_x, arc_end_y, heng_end_x, heng_end_y, r0=6.0, r1=6.0, steps=250)

# joining dab at end of 横 before hook
dab(heng_end_x, heng_end_y, 7.5)

# hook: flick UPWARD (nearly straight up, slight lean left) from right endpoint
# Length ~55 px, angle ~-95° (image coords: upward and slightly left)
hook_len = 55
hook_ang = math.radians(-95)  # pointing up (slightly left)
hook_end_x = heng_end_x + hook_len * math.cos(hook_ang)
hook_end_y = heng_end_y + hook_len * math.sin(hook_ang)
# use a gentle Bezier so the hook curves slightly
hook_ctrl = (heng_end_x - 4, heng_end_y - hook_len * 0.55)
bezier_dabs((heng_end_x, heng_end_y), hook_ctrl, (hook_end_x, hook_end_y),
            r0=6.5, r1=1.2, steps=250)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_011_匕/01_匕.png")
print("wrote 01_匕.png")
