"""
风 (feng) — 4-stroke radical. RETRY 1.

Errata diagnosis of prior attempt: the render read as 冈 not 风.
Root causes: (1) outer LEFT stroke rendered as a straight-ish 撇
starting only slightly left of the top, giving the outer shape a
boxy/rectangular feel; (2) top 横 too long and too horizontal, so
the top edge dominates and the shoulder read as a right-angle box
corner rather than a 折 turning into a curved sweep; (3) inner 捺
too long/thick, more like a full 捺 than an inner 点 balancing an
inner 撇 (乂 shape).

Fixes for retry (per errata + form_catalog):
1. LEFT 撇: start higher and further right (upper-center-right, near
   the shoulder region), throw strongly down-left to the lower-left
   corner with a more pronounced BELLY-ON-RIGHT bow. Length ~200 px,
   deep curve — no ambiguity that this is a curved 撇, not a straight
   left wall.
2. Top-right 横折弯钩: start ABOVE and LEFT of the 撇 start (so the
   two share a corner joint at top-left). SHORT top 横 (~90 px, not
   140), then a decisive shoulder dab, then a long belly-on-lower-left
   斜钩 sweep down to the lower-right. Terminal hook flick up-left
   at -125° length ~35 px.
3. Inner strokes form a tight 乂: 撇 short + 点 short. Both compact,
   center of the frame around y=170.

Applied memory:
- 撇 as Bezier with control pulled toward interior (belly on right for
  a left-frame 撇).
- 折 shoulder = one r+3 dab, no smooth arc at that corner.
- Hook flick 30-40 px, angle ~-125°.
- 斜钩 body Bezier belly-on-lower-left (drawer_memory 斜钩 recipe).
- form_catalog "撇 as body-crossing diagonal" scaling — but here the
  outer 撇 is the FRAME, so it goes edge-to-edge.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(p0, p1, r_start, r_end, steps=300):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Stroke 1: 撇 (left frame — curved down-left) ----
# Start UPPER-center-left. Throw down-LEFT with a STRONGER belly-on-right
# so the whole left side visually curves outward (matches GT silhouette).
# Push start further right and control point further right.
p1_start = (115, 60)
p1_end = (30, 270)
# Control pulled well to the RIGHT of the chord midpoint => belly bulges
# to the right, so the curve is pronounced from top to bottom.
p1_ctrl = (110, 170)
dab(*p1_start, r=8)  # 顿笔 start press
bezier(p1_start, p1_ctrl, p1_end, r_start=8, r_end=1.5, steps=500, ease=1.15)


# ---- Stroke 2: 横折弯钩 (top + right frame) ----
# Top 横: SHORT (~90 px), starting at the same top-joint as stroke 1,
# very slight up-tilt (calligraphic).
heng_start = (110, 60)
heng_end = (215, 55)
stroke_line(heng_start, heng_end, r_start=7, r_end=6, steps=200)
dab(*heng_start, r=8)  # 顿笔 top-left corner

# Shoulder dab at 横 end (folder corner, r+2 press — squared shoulder)
shoulder = (215, 55)
dab(*shoulder, r=9)

# 弯钩 / 斜钩 body: Bezier from shoulder curving down-right, belly on
# lower-left (concave to upper-right). Ends near the lower-right.
sk_start = shoulder
sk_end = (240, 250)
# Control point pulled to the LOWER-LEFT of the chord => belly on
# lower-left, opening to upper-right. This is the drawer_memory 斜钩
# recipe adapted.
sk_ctrl = (195, 200)
bezier(sk_start, sk_ctrl, sk_end, r_start=7, r_end=5, steps=500)

# Terminal hook flick up-and-left at -125°, length ~35 px.
hook_len = 35
ang = math.radians(-125)
hk_end = (sk_end[0] + hook_len * math.cos(ang),
          sk_end[1] + hook_len * math.sin(ang))
dab(*sk_end, r=5)  # joining dab EQUAL to segment radius (avoid stray nub)
stroke_line(sk_end, hk_end, r_start=5, r_end=1.2, steps=150)


# ---- Stroke 3: inner 撇 (short) ----
# Upper-inside → lower-left. Short, compact — part of an interior 乂.
i1_start = (150, 130)
i1_end = (105, 235)
i1_ctrl = (128, 185)
dab(*i1_start, r=5)
bezier(i1_start, i1_ctrl, i1_end, r_start=5, r_end=1.2, steps=250, ease=1.2)


# ---- Stroke 4: inner 点 (right side of 乂 — short teardrop) ----
# NOT a full 捺. Short, thin→thick down-right teardrop dot.
i2_start = (162, 140)
i2_end = (205, 220)
i2_ctrl = (180, 180)
bezier(i2_start, i2_ctrl, i2_end, r_start=2, r_end=6, steps=200, ease=0.9)
dab(*i2_end, r=6)  # terminal press (broad foot, but modest)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_094_风__retry_1/01_风.png")
