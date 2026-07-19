"""
匕 (bi) — 2 strokes: 撇 + 竖弯钩. RETRY #1.

Prior attempt (retry_n=0) failed: top stroke was rendered as a
left→right slightly-descending bar (a 提/横 direction), producing
七 not 匕. Additional defect: terminal hook flicked nearly straight
up (angle -95°), reading as a rigid nub rather than a swept hook.

Fix per errata + drawer_memory (v6 principle: LABEL > GT-tracing):

Stroke 1 = 撇 (throw-away). Canonical direction: start upper-RIGHT,
throw down-and-LEFT. Thick→thin taper. Gentle rightward bow
(quadratic Bezier control pulled toward the interior — belly on the
right side / upper-right of the chord). Concretely:
    p1_start = (170, 72)     # upper-right, well above the 竖 top
    p1_end   = (78, 158)     # lower-left, TO THE LEFT of the 竖
                             # (shu_x = 88, so tip lands 10px left of it)
    ctrl     = (152, 90)     # pulled toward upper-right → rightward bow

Stroke 2 = 竖弯钩. 竖 descends from (88, 108) down to (88, 232),
smoothly arcs (tangent-continuous quarter-arc, radius ~44 px) into
a rightward 横 running to (~225, 276), and terminates with a hook
that flicks up-and-slightly-LEFT at angle -108° (image coords),
length ~40 px, sharp taper. NOT straight up.

Crossing check: the 撇 must cross the 竖. p1_end.x = 78 (left of
shu_x=88), and the 撇 passes through (~92, 132) which is right of
the 竖 near y=132 — yes, the 撇 begins right of the 竖 (at x=170,
top), enters and crosses the 竖 line as it descends, and exits on
the LEFT (tip at x=78). Signature crossing preserved.

Layout summary:
- 撇 tip at bottom-left, 竖 top just below 撇's mid-point
- 竖 top peeks slightly ABOVE the 撇's crossing point (this is why
  shu_y0 = 108, above the 撇's y=132 crossing) — MMH-style
- 横 running along baseline y=276
- hook flicks up-left at right end (~225, 276) → (~213, 238)
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


# ============================================================
# Stroke 1: 撇 (top-right → bottom-left throw, thick→thin)
# ============================================================
p1_start = (170, 72)
p1_ctrl  = (152, 90)   # bow: belly rightward (concave-left)
p1_end   = (78, 158)   # tip LEFT of shu_x=88

# 顿 press at start (upper-right)
dab(p1_start[0], p1_start[1], 7.5)
bezier_dabs(p1_start, p1_ctrl, p1_end, r0=6.8, r1=1.4, steps=400)


# ============================================================
# Stroke 2: 竖弯钩
# ============================================================
shu_x = 88
shu_y0, shu_y1 = 108, 232

# 竖 segment (uniform width, small 顿 press at top)
dab(shu_x, shu_y0, 7.0)
line_dabs(shu_x, shu_y0, shu_x, shu_y1, r0=6.2, r1=6.2, steps=350)

# tangent-continuous quarter arc: vertical → rightward horizontal
# Parameterized: x = shu_x + R*(1 - cos(t*pi/2)), y = shu_y1 + R*sin(t*pi/2)
R = 44
arc_steps = 220
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = shu_x + R * (1 - math.cos(t * math.pi / 2))
    y = shu_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, 6.2)
arc_end_x = shu_x + R          # 132
arc_end_y = shu_y1 + R          # 276

# 横 segment along the bottom, running rightward
heng_end_x = 225
heng_end_y = arc_end_y
line_dabs(arc_end_x, arc_end_y, heng_end_x, heng_end_y, r0=6.2, r1=6.2, steps=280)

# Hook base: joining dab at same radius (NOT r+2 — per drawer_memory principle 4)
dab(heng_end_x, heng_end_y, 6.2)

# Hook: flick up-and-slightly-LEFT at -108° in image coords, length ~40 px,
# taper sharply. Use a small Bezier for gentle curvature.
hook_len = 40
hook_ang = math.radians(-108)  # up + slightly left
hook_end_x = heng_end_x + hook_len * math.cos(hook_ang)
hook_end_y = heng_end_y + hook_len * math.sin(hook_ang)
# control pulled slightly right-of-straight-line so the flick curves
hook_ctrl = (heng_end_x + 2, heng_end_y - hook_len * 0.55)
bezier_dabs((heng_end_x, heng_end_y), hook_ctrl,
            (hook_end_x, hook_end_y),
            r0=6.2, r1=1.2, steps=250)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_011_匕__retry_1/01_匕.png")
print("wrote 01_匕.png")
