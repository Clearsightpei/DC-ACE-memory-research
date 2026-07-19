"""
礻 (示字旁) — 4 strokes: 点 + 横撇 + 竖 + 点
PIL brush-dab technique, 300x300, black ink on white.

Analysis from GT (readable at gt/phase2/礻.png):
- Stroke 1: small 点 (dian) at top-center, slight down-right slant.
- Stroke 2: 横撇 — a short horizontal starting a bit left, then a
  bowed 撇 throwing down-and-left. This is the "shoulder" of 礻.
- Stroke 3: long 竖 (vertical), passing through the intersection of
  the 横撇, descending well below.
- Stroke 4: 点 on the RIGHT of the vertical, mid-lower area, slanting
  down-and-right (a small teardrop).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=400):
    """Straight line with linearly varying dab radius."""
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=400):
    """Quadratic Bezier with linearly varying radius."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p2[1] + 0  # placeholder to avoid confusion
        # (correct below)
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def teardrop(p0, p1, r0=2.0, r1=8.0, steps=250, ease=1.4):
    """A dot rendered as a short teardrop: thin -> thick."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(p1[0], p1[1], r1 + 1)  # terminal press


# ---------------------------------------------------------------------
# Stroke 1: 点 (top dot) — small teardrop tilted down-right, top-center.
# Position: canvas center-x is 150; the dot sits at upper area (~y=55-88).
# Slightly smaller than first pass — GT top dot is compact, not a wedge.
teardrop((136, 58), (150, 86), r0=1.5, r1=5.5)

# ---------------------------------------------------------------------
# Stroke 2: 横撇 — short slightly-uptilted 横, then a bowed 撇 tail
# tossing down-and-left. The joint is on the right side; the 撇 tip
# swings out to the lower-left.
# The horizontal spans from about (80, 118) to (180, 108) (slight up-tilt).
h_start = (85, 125)
h_end = (180, 115)
# Draw 横 body with small 顿-dab at the start.
dab(h_start[0], h_start[1], 5.5)
line_taper(h_start, h_end, 4.8, 5.2, steps=300)
# Shoulder dab (joint 顿) at h_end — modest, not a bulb.
dab(h_end[0], h_end[1], 6)
# 撇 tail: Bezier from h_end down-and-left to ~(78, 208), gentle
# rightward bow (control point pulled toward the right/interior).
pie_p0 = h_end
pie_p2 = (78, 210)
pie_p1 = (160, 170)  # control: bows the tail to the right, then swoops down-left
bezier_taper(pie_p0, pie_p1, pie_p2, r0=5.5, r1=1.3, steps=380)

# ---------------------------------------------------------------------
# Stroke 3: 竖 — vertical line passing through the 横 near x=135,
# descending from just above the 横 down to y=270. Straight, uniform.
v_x = 140
v_top = 100
v_bot = 268
dab(v_x, v_top, 6)  # 顿 start (smaller so it doesn't overlap the shoulder as a blob)
line_taper((v_x, v_top), (v_x, v_bot), 4.8, 4.8, steps=350)
dab(v_x, v_bot, 5.5)  # terminal blunt press (no hook — this is 礻, not 衤)

# ---------------------------------------------------------------------
# Stroke 4: 点 on the RIGHT — small teardrop, from around (168, 175)
# down-and-right to (198, 210), thin -> thick, terminal press.
teardrop((168, 178), (198, 212), r0=1.5, r1=6.5)


# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_116_礻/01_礻.png"
img.save(out_path)
print(f"Wrote {out_path}")
