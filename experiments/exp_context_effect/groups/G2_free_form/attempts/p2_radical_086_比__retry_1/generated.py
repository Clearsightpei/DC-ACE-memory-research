"""
p2_radical_086_比 — retry #1

Errata fix idea: 比 = two 匕 side by side. Prior attempt rendered as
忙-like (a 十 on left, 乚 on right). Fix: make each half CLEARLY look
like a 匕.

Left 匕 (in 比's convention): 横 + 竖提
  - 横 sits high, short, tilts slightly up-right
  - 竖提: vertical descending on the LEFT of the crossing 横 (the 横
    should cross the 竖 near the top-left), then 提 tail rises to the
    right into the middle whitespace

Right 匕: 撇 + 竖弯钩
  - 撇: starts upper-right, throws down-and-left, tail crosses the
    right 竖 near mid-height (mirroring left 匕's 横)
  - 竖弯钩: long vertical, then quarter-arc into a short horizontal,
    then hook flicks up-and-slightly-left

Sibling identity (TIER-0 A + form_catalog): the KEY signature of 匕
is that the top stroke (横 on left, 撇 on right) CROSSES the vertical
below its top — i.e., the 竖 (or 竖弯钩) extends both above and below
the crossing point. Prior attempt let the strokes meet at the vertical's
top, killing the 匕 identity. Fix: verticals should extend up ABOVE
the crossing horizontal/撇 by ~15-20 px.

Hook flick (TIER-0 B): 竖弯钩 terminal flicks UP-and-LEFT (~-108°).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ============================================================
# LEFT 匕  (x ≈ 55..140)
# The left 竖 sits at x=90. The top 横 CROSSES it near the top
# (crossing at y≈120, but 竖 starts at y=95, so 竖 extends
# above the horizontal — this is the 匕 signature).
# ============================================================

# Stroke 2 first-conceptually, but we draw in canonical order:
# Actually stroke order for 比 is: 横, 竖提, 撇, 竖弯钩.

# ---- Stroke 1: LEFT 横 ----
# short, mild up-tilt, crosses the vertical at x=90.
# 横 spans x=55..140, y=125..118.
h1_x0, h1_y0 = 55, 125
h1_x1, h1_y1 = 140, 118
dab(h1_x0, h1_y0, 6)             # 顿笔 start
line_taper(h1_x0, h1_y0, h1_x1, h1_y1, 5, 5.2)
dab(h1_x1, h1_y1, 6)             # subtle end press

# ---- Stroke 2: LEFT 竖提 ----
# vertical from y=95 down to y=225, then 提 rises up-right.
# CRUCIAL: 竖 starts ABOVE the 横 (y=95 < 118) so the horizontal
# crosses the vertical below the vertical's top — the 匕 signature.
v2_x, v2_top, v2_bot = 90, 95, 230
dab(v2_x, v2_top, 6.5)           # 顿笔 top
line_taper(v2_x, v2_top, v2_x, v2_bot, 5.5, 5.5)
# joining dab at 提 root — equal to segment radius (avoid stray nub)
dab(v2_x, v2_bot, 5.5)
# 提 rising up-right, tapered sharp tip; ends in middle whitespace
line_taper(v2_x, v2_bot, 145, 195, 5.5, 1.2, steps=260)


# ============================================================
# RIGHT 匕  (x ≈ 165..255)
# The right 竖弯钩 sits at x=210. The 撇 CROSSES it near the top.
# ============================================================

# ---- Stroke 3: RIGHT 撇 ----
# short 撇: starts (245, 90), curves down-left, tail lands (170, 155).
# It CROSSES the right vertical (x=210) at roughly y≈120.
dab(245, 90, 7)                  # 顿笔 start
bezier_taper(
    (245, 90),
    (222, 118),
    (170, 155),
    r0=6.5,
    r1=1.3,
    steps=350,
)

# ---- Stroke 4: RIGHT 竖弯钩 ----
# Long 竖 from (210, 100) down to (210, 220), then quarter-arc right
# to (250, 260), then hook flicks UP-and-slightly-LEFT (~-108°).
# CRUCIAL: 竖 starts ABOVE the 撇's crossing point (y=100 above the
# 撇's y=120 crossing) — again the 匕 signature.
sv_x, sv_top, sv_bot = 210, 100, 220
dab(sv_x, sv_top, 6.5)           # 顿笔
line_taper(sv_x, sv_top, sv_x, sv_bot, 5.5, 5.5)

# tangent-continuous arc, R=40
R = 40
arc_steps = 100
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = sv_x + R * (1 - math.cos(t * math.pi / 2))
    y = sv_bot + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.5)

arc_end_x, arc_end_y = sv_x + R, sv_bot + R  # (250, 260)

# hook: flick up-and-slightly-left, angle ~ -108°, length ~ 32 px
hook_len = 32
hook_angle_deg = -108
hx = arc_end_x + hook_len * math.cos(math.radians(hook_angle_deg))
hy = arc_end_y + hook_len * math.sin(math.radians(hook_angle_deg))
dab(arc_end_x, arc_end_y, 5.8)   # equal joining dab
line_taper(arc_end_x, arc_end_y, hx, hy, 5.8, 1.0, steps=220)


# ============================================================
# Save
# ============================================================
out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p2_radical_086_比__retry_1/01_比.png"
)
img.save(out_path)
print(f"saved {out_path}")
