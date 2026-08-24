"""
这 (zhe) — Phase-3 character, 7 strokes.
Composition: 文 (top-right, compressed) INSIDE 辶 (walk-radical wrapping bottom-left).

Stroke order (per 辶-compound convention):
  Interior 文 FIRST:
    1. 点 (top dot above 文's lid)
    2. 横 (lid)
    3. 撇 (body diagonal down-left)
    4. 捺 (body diagonal down-right, degraded to 反捺/dot inside 辶 to
       avoid double-捺 with the 平捺)
  Then 辶:
    5. 点 (upper-left dot of 辶)
    6. 横折折撇 (Z-body of 辶, left column)
    7. 平捺 (long sweep across bottom, cradles the 文)

Layout (300x300):
  - 文 compressed, sits upper-right, x in [120, 265], y in [30, 200].
  - 辶 dot upper-left ~ (85, 55).
  - 辶 Z-body left column, x in [55, 105], y in [80, 175].
  - 平捺 sweeps from (~50, 225) rightward to (~275, 235), belly at
    (~165, 265). This carries the whole ground.

Uses PIL brush-dabs (proven technique from prior 辶 and 文 PASSes).
Applying TIER-0 hook rule: 辶 has no hook (Z is a fold). No hooks in 这.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy)
    if steps is None:
        steps = max(30, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bez_dabs(p0, p1, p2, r0, r1, steps=200, ease=None):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        te = ease(t) if ease else t
        r = r0 + (r1 - r0) * te
        dab(x, y, r)


# =====================================================================
# Interior 文 (compressed, upper-right)
# =====================================================================

# ---- 1. 点 (top dot above 文's lid) ----
bez_dabs(p0=(185, 40), p1=(180, 52), p2=(170, 62),
         r0=1.5, r1=3.2, steps=100)

# ---- 2. 横 (lid) — medium horizontal, slight up-tilt ----
line_dabs(130, 92, 262, 86, 3.2, 3.2)
dab(128, 92, 5)   # left 顿
dab(262, 86, 5)   # right 顿

# ---- 3. 撇 (body diagonal down-left) ----
bez_dabs(p0=(205, 105), p1=(170, 150), p2=(125, 195),
         r0=4.2, r1=1.6, steps=220)
dab(205, 105, 5)  # 顿 at start

# ---- 4. 捺 → 反捺 point (degraded because 平捺 will be under) ----
# Short thin-to-thick dot going down-right from lid interior.
bez_dabs(p0=(170, 108), p1=(200, 145), p2=(235, 185),
         r0=1.6, r1=4.6, steps=200)
dab(238, 187, 5)  # terminal press

# =====================================================================
# 辶 walk-radical (wraps bottom-left)
# =====================================================================

# ---- 5. 点 (upper-left dot of 辶) ----
bez_dabs(p0=(70, 40), p1=(78, 52), p2=(92, 65),
         r0=1.5, r1=3.8, steps=100)

# ---- 6. 横折折撇 (Z-body, left column) ----
# short 横 -> shoulder -> down-left slant -> shoulder -> short 横 -> bowed 撇
a  = (60, 100)
b  = (108, 92)
c  = (75, 130)
dd = (115, 125)
tail_tip = (55, 185)
r_body = 3.2

dab(a[0], a[1], r_body + 1.5)
line_dabs(a[0], a[1], b[0], b[1], r_body, r_body)
dab(b[0], b[1], r_body + 1.5)
line_dabs(b[0], b[1], c[0], c[1], r_body, r_body)
dab(c[0], c[1], r_body + 1.5)
line_dabs(c[0], c[1], dd[0], dd[1], r_body, r_body)
dab(dd[0], dd[1], r_body + 1.5)
bez_dabs(dd, (105, 158), tail_tip, r_body + 0.3, 1.0, steps=240)

# ---- 7. 平捺 (long sweeping "smile" across bottom) ----
p0 = (48, 232)
p2 = (272, 240)
p1 = (165, 278)   # control pulls down -> concave-up belly
steps = 320
for i in range(steps + 1):
    t = i / steps
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    if t < 0.85:
        r = 1.6 + (7.0 - 1.6) * (t / 0.85)
    else:
        r = 7.0 - (7.0 - 5.2) * ((t - 0.85) / 0.15)
    dab(x, y, r)
# terminal foot: broaden then trail off
fx, fy = p2
for k in range(0, 14):
    dab(fx + k * 0.7, fy + k * 0.15, 6.0 - k * 0.2)
dab(p0[0], p0[1], 3)

out = ("<REPO_ROOT>/experiments/"
       "exp_context_effect/groups/G2_free_form/attempts/"
       "p3_char_0291_这/01_这.png")
img.save(out)
print("Saved:", out)
