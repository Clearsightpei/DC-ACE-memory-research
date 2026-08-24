"""
Render 寸 (radical 045) — 3 strokes:
  1. 横 (heng) — long horizontal across the middle
  2. 竖钩 (shu gou) — vertical descending from top, crossing the 横 slightly
     right of center, ending with an up-left hook flick
  3. 丶 (dian) — short teardrop dot at lower-left, inside/below the 横 &
     to the left of the 竖钩

Design notes (from GT inspection):
- The 横 is the wider element; it sits at roughly the vertical middle.
- The 竖钩 starts ABOVE the 横 (peaks near the top), crosses the 横,
  descends to near the bottom, and hooks up-and-slightly-left.
- The 丶 sits below the 横, to the LEFT of the 竖钩 (roughly x~120, y~180).
- Uses PIL brush-dab technique (proven in memory).
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
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 横 (heng) — long horizontal across the middle ----
# Slight up-tilt (right end a hair higher), uniform width, 顿 dabs at ends
H_LEFT = (50, 152)
H_RIGHT = (255, 145)
R_H = 5
dab(H_LEFT[0], H_LEFT[1], R_H + 2)  # start 顿
line_dabs(H_LEFT[0], H_LEFT[1], H_RIGHT[0], H_RIGHT[1], R_H, R_H)
dab(H_RIGHT[0], H_RIGHT[1], R_H + 2)  # end 顿

# ---- Stroke 2: 竖钩 (shu gou) — vertical + up-left hook ----
# Starts above the 横 (peaks at ~y=85), crosses 横 slightly right of center,
# descends to near baseline, then hook flicks up-and-slightly-left.
V_TOP = (172, 78)
V_BOTTOM = (172, 258)
R_V = 5.5
dab(V_TOP[0], V_TOP[1], R_V + 2)  # 顿 at top
line_dabs(V_TOP[0], V_TOP[1], V_BOTTOM[0], V_BOTTOM[1], R_V, R_V)

# Hook flick from V_BOTTOM: LONGER + more clearly up-and-slightly-left
# to be visible (memory rule: standalone hooks need ~30-40 px length,
# angle -105° to -115°).
HOOK_LEN = 42
hook_angle = math.radians(-118)  # image-coords: negative y = up, slightly left
HX = V_BOTTOM[0] + HOOK_LEN * math.cos(hook_angle)
HY = V_BOTTOM[1] + HOOK_LEN * math.sin(hook_angle)
# Taper from segment radius to sharp tip
line_dabs(V_BOTTOM[0], V_BOTTOM[1], HX, HY, R_V, 1.0)

# ---- Stroke 3: 丶 (dian) — small teardrop dot below 横, left of 竖钩 ----
# GT shows a MUCH smaller dot than a full standalone 丶. Positioned
# just below the 横 and just left of the 竖钩.
D_START = (115, 178)
D_END = (138, 200)
steps = 60
for i in range(steps + 1):
    t = i / steps
    tt = t ** 1.5  # ease-in taper
    x = D_START[0] + (D_END[0] - D_START[0]) * t
    y = D_START[1] + (D_END[1] - D_START[1]) * t
    r = 1.5 + (6.5 - 1.5) * tt
    dab(x, y, r)
dab(D_END[0], D_END[1], 7)  # terminal press (smaller than standalone 丶)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_045_寸/01_寸.png")
