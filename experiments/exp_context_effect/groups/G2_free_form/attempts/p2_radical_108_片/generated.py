"""Render 片 (radical, 4 strokes) at 300x300, PIL brush-dabs.

Revised after self-check: first attempt read as 石 because the 竖 was
too tall/central and the top became a boxed cluster. GT shows:
  - long sweeping 撇 on the LEFT dominating the character
  - short 竖 (small, near top) at the upper-left area
  - short 横 at top-right (touching the 撇's upper section)
  - 横折 on the right descending well below mid-height to bottom

Stroke order (canonical for 片):
  1. 撇   — long, upper-mid start, sweeps down-left with rightward bow
  2. 竖   — SHORT vertical near the top of the 撇 (partial left wall)
  3. 横   — short horizontal at top-right, touching 撇 body
  4. 横折 — mid-height 横 rightward, shoulder, 竖 descending to bottom

Image coords, y grows DOWN. Canvas 300x300. Black ink on white.
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    """Quadratic Bezier with tapered radius."""
    x0, y0 = p0
    xc, yc = p1
    x1, y1 = p2
    for i in range(steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt * mt * x0 + 2 * mt * t * xc + t * t * x1
        y = mt * mt * y0 + 2 * mt * t * yc + t * t * y1
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------- Stroke 1: 撇 (long dominant diagonal, LEFT-side of char) ----------
# starts at top around (150,45), sweeps to lower-left (55,270), rightward bow.
pie_p0 = (150, 48)
pie_p2 = (55, 270)
pie_ctrl = (115, 175)  # control pulled slightly right → gentle rightward bow
dab(pie_p0[0], pie_p0[1], 7)  # 顿笔 press at start
bezier_taper(pie_p0, pie_ctrl, pie_p2, r0=8, r1=1.5, steps=500)

# ---------- Stroke 2: 竖 (SHORT — small partial vertical at top-left) ----------
# In 片 the 竖 is a short segment near the top of the 撇 area, roughly
# at x=100-110, from about y=90 to y=170. Short, ~80 px.
shu_top = (108, 95)
shu_bot = (108, 175)
dab(shu_top[0], shu_top[1], 6)
line_taper(shu_top, shu_bot, r0=5.5, r1=5.5, steps=300)
dab(shu_bot[0], shu_bot[1], 6)

# ---------- Stroke 3: 横 (short horizontal at top-right) ----------
# From 撇's upper region (around x=138) rightward to about x=225.
# Slight up-tilt.
heng_p0 = (138, 82)
heng_p1 = (228, 74)
dab(heng_p0[0], heng_p0[1], 6.5)
line_taper(heng_p0, heng_p1, r0=5.5, r1=5, steps=300)
dab(heng_p1[0], heng_p1[1], 7)

# ---------- Stroke 4: 横折 (mid-height 横 + long 竖 to lower right) ----------
# Short 横 at mid-height (~y=145), then shoulder, then long 竖 descending
# to bottom-right around (220,270). Blunt end.
zhe_h0 = (135, 148)   # 横 starts where 撇 body is at mid-height
zhe_h1 = (225, 142)   # 横 end at right
dab(zhe_h0[0], zhe_h0[1], 6)
line_taper(zhe_h0, zhe_h1, r0=5.5, r1=5.5, steps=300)
# shoulder dab (顿 press at corner)
dab(zhe_h1[0], zhe_h1[1], 8)
# 竖 descending
zhe_v1 = (222, 275)
line_taper(zhe_h1, zhe_v1, r0=6, r1=5.5, steps=400)
dab(zhe_v1[0], zhe_v1[1], 6)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_108_片/01_片.png"
img.save(out)
print(f"Saved: {out}")
