"""
对 (duì) — 5 strokes: LEFT 又 (2 strokes: 横撇 + 捺) + RIGHT 寸 (3 strokes: 横 + 竖钩 + 丶).

Composition plan (from GT inspection):
- Left 又 sits in left ~45% width, compressed & tucked slightly high.
- Right 寸 fills right ~55% width; the vertical 竖钩 is the tallest
  element and extends both above and below the 又.
- Small whitespace gap between the two halves.
- The 寸's 横 sits at mid-height, its 竖钩 begins ABOVE the 横 and
  descends to near the baseline with an up-left hook.
- The 寸's 丶 sits below+left of the 竖钩 (inside the interior).

Techniques inherited from drawer_memory: PIL brush-dabs, quadratic
Bezier for curved strokes, tapered radius for pie-tails and hooks.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = max(60, int(math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# =========================================================================
# LEFT: 又 (compressed to left ~45%)
# =========================================================================
# Stroke 1: 横撇 — short 横 then long down-left 撇
# Short slanted 横 (slightly up-tilted right)
line_dabs(35, 120, 118, 112, 4.0, 4.0)
dab(118, 112, 5.5)  # shoulder 顿笔
# 撇 tail: long bowed sweep from shoulder ending lower-left
bezier_dabs((118, 112), (85, 175), (30, 240), 4.5, 1.3)

# Stroke 2: 捺 — starts near shoulder area, sweeps down-right past 撇 tip
bezier_dabs((60, 140), (100, 190), (140, 235), 1.8, 6.5)
# Broad terminal foot
for k in range(12):
    dab(140 + k * 0.6, 235 + k * 0.05, 6.5 - k * 0.4)


# =========================================================================
# RIGHT: 寸 (right ~55% of canvas)
# =========================================================================
# Stroke 3: 横 — long horizontal across mid-height of right side
H_LEFT = (155, 148)
H_RIGHT = (280, 142)
R_H = 4.5
dab(H_LEFT[0], H_LEFT[1], R_H + 1.5)
line_dabs(H_LEFT[0], H_LEFT[1], H_RIGHT[0], H_RIGHT[1], R_H, R_H)
dab(H_RIGHT[0], H_RIGHT[1], R_H + 1.8)  # 顿 at right

# Stroke 4: 竖钩 — starts above the 横, crosses it right-of-center,
# descends near baseline, hook flicks up-and-slightly-left.
V_TOP = (222, 70)
V_BOTTOM = (222, 260)
R_V = 5.0
dab(V_TOP[0], V_TOP[1], R_V + 1.5)  # 顿 at top
line_dabs(V_TOP[0], V_TOP[1], V_BOTTOM[0], V_BOTTOM[1], R_V, R_V)

# Hook flick (up-and-slightly-left, per TIER-0 rule)
HOOK_LEN = 36
hook_angle = math.radians(-118)
HX = V_BOTTOM[0] + HOOK_LEN * math.cos(hook_angle)
HY = V_BOTTOM[1] + HOOK_LEN * math.sin(hook_angle)
line_dabs(V_BOTTOM[0], V_BOTTOM[1], HX, HY, R_V, 1.0)

# Stroke 5: 丶 — small teardrop dot, below 横 and left of 竖钩
D_START = (172, 178)
D_END = (192, 198)
steps = 60
for i in range(steps + 1):
    t = i / steps
    tt = t ** 1.5
    x = D_START[0] + (D_END[0] - D_START[0]) * t
    y = D_START[1] + (D_END[1] - D_START[1]) * t
    r = 1.4 + (5.8 - 1.4) * tt
    dab(x, y, r)
dab(D_END[0], D_END[1], 6.2)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0164_对/01_对.png"
)
