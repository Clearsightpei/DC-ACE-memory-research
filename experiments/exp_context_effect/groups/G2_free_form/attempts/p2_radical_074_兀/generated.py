"""
Render 兀 (radical p2_radical_074) — 3 strokes:
  1. 横 (top horizontal)
  2. 撇 (left leg — throw-away, curves down-and-left)
  3. 竖弯钩 (right leg — vertical descending then arcing right, subtle hook)

PIL brush-dab renderer at 300x300, black on white.
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        L = math.hypot(x1 - x0, y1 - y0)
        steps = max(80, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(P0, P1, P2, r0, r1, steps=300, ease=None):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        tt = ease(t) if ease else t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# Thinner ink to match GT's slender calligraphic feel.

# ---------------- Stroke 1: 横 (top horizontal) ----------------
# Slight upward tilt. Thinner uniform r=3.
h_x0, h_y0 = 65, 110
h_x1, h_y1 = 240, 100
dab(h_x0, h_y0, 4.5)
line_dabs(h_x0, h_y0, h_x1, h_y1, 3.2, 3.2)
dab(h_x1, h_y1, 4.5)


# ---------------- Stroke 2: 撇 (left leg) ----------------
# Bezier: throws down-and-left with clear leftward curvature (GT shows
# a visible curve). Start under the 横 near the left, tip at lower-left.
p0 = (110, 110)
ctrl = (85, 190)        # pulled left to give a rightward-belly bow
p2 = (55, 275)
dab(p0[0], p0[1], 6)
bezier_dabs(p0, ctrl, p2, 5.5, 1.2, steps=400,
            ease=lambda t: t ** 1.15)


# ---------------- Stroke 3: 竖弯钩 (right leg) ----------------
# Descends as 竖, smooth arc into rightward 横, subtle terminal press
# (GT shows nearly no hook — keep it minimal).
sx, sy = 200, 110
dab(sx, sy, 4.5)

# vertical segment (thinner)
v_end_x, v_end_y = 200, 225
line_dabs(sx, sy, v_end_x, v_end_y, 3.5, 3.5)

# tangent-continuous quarter arc: down -> rightward horizontal
R = 30
arc_steps = 100
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = v_end_x + R * (1 - math.cos(t * math.pi / 2))
    y = v_end_y + R * math.sin(t * math.pi / 2)
    dab(x, y, 3.5)

arc_end_x = v_end_x + R      # 230
arc_end_y = v_end_y + R      # 255

# short horizontal foot
h2_end_x, h2_end_y = 258, 255
line_dabs(arc_end_x, arc_end_y, h2_end_x, h2_end_y, 3.5, 3.3)

# very subtle terminal flick (small, short, to match GT's blunt end)
hook_len = 10
angle_deg = -120
ax = h2_end_x + hook_len * math.cos(math.radians(angle_deg))
ay = h2_end_y + hook_len * math.sin(math.radians(angle_deg))
line_dabs(h2_end_x, h2_end_y, ax, ay, 3.5, 1.2)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_074_兀/01_兀.png")
print("wrote 01_兀.png")
