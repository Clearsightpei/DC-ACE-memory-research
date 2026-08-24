"""力 (li) — 2-stroke radical.  RETRY #1.

Prior fail: 撇 rendered as a tiny dot; result read as 几 + stray dot.

Fix per errata (curator diagnosis):
- 撇 must be a full ~150 px stroke.
- Start in the top-left of the 横折钩 (near the 横's left third).
- Its TOP must reach ABOVE the top 横 (same crossing-visibility rule as 刀).
- Sweep down to the lower-left corner.
- Taper r=8 → 1.5.

Stroke plan:
  Stroke 1: 横折钩 — short slightly-up-tilted 横 across the top, hard 折
            shoulder, then a curving 竖 (belly on the right) ending in an
            up-left hook flick.
  Stroke 2: 撇 — starts ABOVE the top 横 (~y=60), crosses through the
            横 at ~x=125, throws down-and-left to the lower-left corner
            (~35, 265).  Thick→thin taper with 顿 press at start.
"""

from PIL import Image, ImageDraw
import math

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


def bezier_dabs(p0, p1, p2, r0, r1, steps=500, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Stroke 1: 横折钩 ----
# Top 横 — short, slight up-tilt.  Positioned upper area.
h_start = (105, 100)
h_end = (225, 90)
r_h = 5.0
dab(h_start[0], h_start[1], r_h + 2)          # 顿笔 at start
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r_h, r_h, steps=300)
# 折 shoulder dab at corner (allowed to be r+3 per principle 5 corollary)
shoulder = h_end
dab(shoulder[0], shoulder[1], r_h + 3)

# Curving 竖 with belly on the RIGHT (concave toward left).
v_start = shoulder
v_end = (170, 250)
v_ctrl = (240, 175)                            # right-side control → left-concave belly
bezier_dabs(v_start, v_ctrl, v_end, r0=r_h + 1, r1=r_h + 0.5, steps=400)

# Terminal 钩 — flick up-and-left (~ -150° in image coords), taper thick→thin.
hook_len = 34
hook_angle = math.radians(-150)
hx = v_end[0] + hook_len * math.cos(hook_angle)
hy = v_end[1] + hook_len * math.sin(hook_angle)
# joining dab = segment radius (NOT r+1), per hook-base discipline
dab(v_end[0], v_end[1], r_h + 0.5)
line_dabs(v_end[0], v_end[1], hx, hy, r0=r_h + 0.5, r1=1.2, steps=200)


# ---- Stroke 2: 撇 (crosses ABOVE and THROUGH the top 横) ----
# Must be a full sweep (~230 px diagonal) from upper area down to lower-left.
# Use a gentle bow so the stroke stays visible across its whole length.
pie_p0 = (155, 55)      # START ABOVE the 横 (h_start.y=100, so 55 is 45 px above)
pie_p2 = (35, 265)      # END at lower-left corner
pie_ctrl = (110, 145)   # mild control just off the straight line → gentle bow
# 顿笔 dab at start
dab(pie_p0[0], pie_p0[1], 9.0)
# Draw with a slow taper so the middle stays thick and visible.
bezier_dabs(pie_p0, pie_ctrl, pie_p2, r0=8.5, r1=2.0, steps=700, ease=1.0)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_025_力__retry_1/01_力.png"
)
