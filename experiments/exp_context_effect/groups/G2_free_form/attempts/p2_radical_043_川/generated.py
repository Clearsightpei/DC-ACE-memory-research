"""
川 (chuan) — Phase-2 radical, 3 strokes.

Structure (per GT):
  Stroke 1: 撇 (throw) — leftmost, starts upper-mid, curves down-and-left,
            gentle bow, thick→thin tapered tip.
  Stroke 2: 短竖 — middle, short straight vertical, uniform, blunt ends.
  Stroke 3: 长竖 — rightmost, taller straight vertical (may be 悬针 sharp tip
            or blunt). Per GT it terminates blunt-ish; render blunt for safety.

Canvas 300x300, white, black ink. PIL brush-dab technique.
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(60, int(dist * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
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


# --------------------------------------------------------------
# Stroke 1: 撇 (leftmost) — top starts around (108, 85), curves down-left
# to about (60, 235). Gentle rightward-belly bow.
# Soft start (no r=8 顿-ball at standalone scale); Bezier body → sharp tip.
p0 = (110, 82)
p2 = (55, 240)
ctrl = (98, 160)  # control toward start-side => concave-right belly
# soft start press (per memory: r=6-8 for standalones, use small)
dab(p0[0], p0[1], 6.5)
bezier_dabs(p0, ctrl, p2, r0=6.5, r1=1.2, steps=500)

# --------------------------------------------------------------
# Stroke 2: 短竖 (middle) — GT shows a subtle top-left curl (mini 撇 head)
# then straight down. Render as a very short curved head → straight body.
# Head Bezier from (162,100) hooking down-and-slightly-left to (155,120),
# then uniform vertical to (155,225).
head_p0 = (162, 98)
head_p2 = (155, 122)
head_ctrl = (155, 100)  # slight leftward top bow
dab(head_p0[0], head_p0[1], 6)
bezier_dabs(head_p0, head_ctrl, head_p2, r0=6, r1=5.5, steps=120)
line_dabs(155, 122, 155, 225, r0=5.5, r1=5.5, steps=250)
dab(155, 225, 6)

# --------------------------------------------------------------
# Stroke 3: 长竖 (rightmost) — taller vertical, x≈218, y=80→255.
# Slightly longer than middle. Blunt terminal press.
line_dabs(218, 80, 218, 258, r0=5.5, r1=5.5, steps=350)
dab(218, 80, 7)
dab(218, 258, 6.5)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_043_川/01_川.png"
)
