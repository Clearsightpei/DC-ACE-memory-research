"""G2 first attempt at 车 (4-stroke simplified radical).

Decomposition (per GT observation):
  1) 横 — short top horizontal
  2) 撇折 — 撇 dropping down-left, then short 横 rightward
     forming the small "bowl"/eye shape below the top 横.
     Right end of the 折's 横 aligns roughly under the top 横's right end.
  3) 横 — LONG middle crossbar spanning wide (much wider than the top)
  4) 竖 — vertical descending through the whole assembly, ending blunt
     (no hook — this is 车 not 事)

PIL brush-dab technique. Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(dist * 3), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 1: top 横 — short horizontal near the top
# ---------------------------------------------------------------
h1_x0, h1_y0 = 115, 78
h1_x1, h1_y1 = 205, 72   # slight up-tilt
line_dabs(h1_x0, h1_y0, h1_x1, h1_y1, r_start=5, r_end=5)
dab(h1_x0, h1_y0, 6)     # subtle start (standalone: no bulge)
dab(h1_x1, h1_y1, 6)

# ---------------------------------------------------------------
# Stroke 2: 撇折  (forms the "bowl" under the top 横)
#   beat A = 撇 tapering down-left from just under the right of top 横
#            to the lower-left, gentle bow
#   beat B = shoulder dab + short 横 rightward
# ---------------------------------------------------------------
# 撇 tip lands lower-left, forming the bowl's left side
pie_p0 = (188, 88)           # start upper-right (under top 横 right side)
pie_p2 = (95, 148)           # tip lower-left
pie_ctrl = (170, 128)        # bow control (rightward interior bow)
bezier_dabs(pie_p0, pie_p2, pie_ctrl, r_start=8, r_end=3, steps=180)
dab(pie_p0[0], pie_p0[1], 9)  # 顿 at start

# shoulder dab at the 撇 tip (joint of 撇折)
dab(pie_p2[0], pie_p2[1], 7)

# 折's 横 — short rightward with slight up-tilt
zh_x0, zh_y0 = pie_p2
zh_x1, zh_y1 = 215, 143
line_dabs(zh_x0, zh_y0, zh_x1, zh_y1, r_start=5, r_end=5)
dab(zh_x1, zh_y1, 7)  # terminal press

# ---------------------------------------------------------------
# Stroke 3: LONG middle 横 — wide crossbar
# ---------------------------------------------------------------
h3_x0, h3_y0 = 45, 188
h3_x1, h3_y1 = 268, 178    # slight up-tilt
line_dabs(h3_x0, h3_y0, h3_x1, h3_y1, r_start=6, r_end=6)
dab(h3_x0, h3_y0, 7)
dab(h3_x1, h3_y1, 7)

# ---------------------------------------------------------------
# Stroke 4: 竖 — vertical through center, blunt end (no hook)
# ---------------------------------------------------------------
v_x0, v_y0 = 152, 55
v_x1, v_y1 = 152, 262
line_dabs(v_x0, v_y0, v_x1, v_y1, r_start=6, r_end=6)
dab(v_x0, v_y0, 7)
dab(v_x1, v_y1, 7)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_089_车/01_车.png"
img.save(out)
print("wrote", out)
