"""Render radical 耂 (top of 老/考) at 300x300, black ink on white.

Structure (4 strokes, per GT observation):
  1) 横 (long horizontal, upper) — top bar of the radical
  2) 竖 (short vertical) — descends from above the 横 through it, ends
     around the middle where the small internal 横 sits
  3) 横 (short mid horizontal) — the small internal horizontal below
     the first 横, forming a short cross with the 竖 tail area
  4) 撇 (long sweeping throw-away) — dominant stroke, starts at upper
     right (above the top 横 on the right side), sweeps down-and-left
     all the way to lower-left corner, bowed rightward (belly on lower-right)

PIL brush-dab technique per drawer_memory principles.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        steps = max(80, int(math.hypot(x1 - x0, y1 - y0) * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=None):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    if steps is None:
        steps = 300
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# GT is drawn with thin, wispy brush lines (like fountain pen), not
# heavy calligraphic 顿-dab presses. Use thin uniform strokes.
THIN = 2.5

# --- Stroke 1: long top 横 (heng) --------------------------------------
# Slight up-tilt. Sits in upper-middle area.
h1_start = (55, 118)
h1_end = (235, 108)
dab(h1_start[0], h1_start[1], THIN + 1)
line_taper(h1_start, h1_end, THIN, THIN)
dab(h1_end[0], h1_end[1], THIN + 0.5)

# --- Stroke 2: 竖 (shu) crossing top 横 -------------------------------
# In GT, the 竖 pokes out above the 横 by ~30 px and descends short
# below it to the level of the internal 横.
v_start = (128, 70)
v_end = (128, 170)
line_taper(v_start, v_end, THIN, THIN)

# --- Stroke 3: short internal 横 (below top 横, right of 竖 tail) -----
# In GT this small horizontal is roughly at mid-height and extends
# from just left of the 竖 to about 2/3 across.
h2_start = (100, 165)
h2_end = (195, 160)
dab(h2_start[0], h2_start[1], THIN + 0.5)
line_taper(h2_start, h2_end, THIN, THIN)
dab(h2_end[0], h2_end[1], THIN + 0.5)

# --- Stroke 4: dominant 撇 (long sweeping throw-away) -----------------
# In GT this stroke starts HIGH above the top 横 on the right side,
# sweeps down through/past the horizontals, and exits at lower-left.
# Bowed rightward (belly on lower-right).
pie_p0 = (200, 55)
pie_p2 = (55, 275)
# chord mid ~ (127, 165). Pull control toward lower-right for belly-lower-right.
pie_ctrl = (200, 190)
bezier_taper(pie_p0, pie_ctrl, pie_p2, THIN + 1.5, 1.0, steps=420)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_102_耂/01_耂.png")
print("wrote 01_耂.png")
