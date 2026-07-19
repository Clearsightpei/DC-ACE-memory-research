"""Render 八 (2-stroke radical) to 300x300 PNG using PIL brush-dabs.

八 has two strokes:
  1. 撇 (pie) on the LEFT — shorter, bowed, thick→thin
  2. 捺 (na) on the RIGHT — longer, thin→thick, terminal broad foot

Looking at GT: the two strokes do NOT meet at the top — they are
separated at their heads by a small gap. Both flare outward and down.
The 捺 is longer and reaches further right/down than the 撇 reaches
left/down.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=400, ease=1.0):
    """Quadratic Bezier stroke with tapered brush-dabs."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * P0[0] + 2 * u * t * P1[0] + t * t * P2[0]
        y = u * u * P0[1] + 2 * u * t * P1[1] + t * t * P2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---- Stroke 1: 撇 (pie) on the LEFT ----
# In 八, the 撇 head sits LEFT of center. The two strokes do NOT touch
# at their heads — there is a clear horizontal gap between them at top.
# The 撇 is shorter and more compact than the 捺.
P0 = (115, 95)      # head, upper-left region
P2 = (55, 220)      # tip, lower-left
P1 = (85, 155)      # control pulled toward interior for gentle bow
# Small start 顿 press for standalone (r~8 avoids balloon)
dab(P0[0], P0[1], 8)
bezier_stroke(P0, P1, P2, r_start=9, r_end=1.5, steps=400, ease=1.3)

# ---- Stroke 2: 捺 (na) on the RIGHT ----
# 捺 head sits RIGHT of center, well-separated from the 撇 head (~50 px
# gap horizontally). It runs down-and-right with a slight belly-on-
# lower-left bow, thin→thick, ending in a broad flat foot press.
Q0 = (170, 100)     # head, RIGHT of 撇 head with clear gap
Q2 = (250, 220)     # tail, lower-right
Q1 = (200, 145)     # control giving belly on lower-left
# thin start, thickens toward foot
bezier_stroke(Q0, Q1, Q2, r_start=2.5, r_end=10, steps=400, ease=0.9)
# terminal broad foot press (flat/broad foot of 捺)
dab(Q2[0], Q2[1], 11)
# slight extension of the foot to give it a broader flat terminal
for i in range(20):
    t = i / 20
    x = Q2[0] + t * 6
    y = Q2[1] + t * 2
    dab(x, y, 10 - t * 3)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_009_八/01_八.png"
)
print("wrote 01_八.png")
