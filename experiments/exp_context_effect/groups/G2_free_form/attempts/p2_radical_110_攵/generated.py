"""
攵 (pū / rap-radical) — 4-stroke radical.

Compared to 夂 (3画) — the difference is that 攵 splits the top "hat"
into TWO separate strokes: a short 撇 at top, then a short 横 below it.
The bottom X (long 撇 + 捺) is the same as 夂's second and third strokes.

Stroke order (MMH canonical for 攵):
  1. 撇 (short, top): top-right → down-left, small pie at top.
  2. 横 (short): near-horizontal segment sitting below-right of stroke 1's
     tail, ending around mid-upper of the character.
  3. 撇 (long): starts near the right end of the 横, bows down-and-left
     to lower-left corner. This is the long left leg of the bottom X.
  4. 捺 (long): starts on the long 撇 near mid-height, sweeps
     down-and-right to a broad flat foot in the lower-right quadrant.

Reference: shared_rules v6; drawer_memory principle 5 (stroke identity),
principle 2 (shared joints for compound corners), principle 7 (X-shape
crossing). Standalone-scale radical → generous canvas use, ink weight
moderate. No hooks in 攵 — all terminals are taper tips or the 捺 foot.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dab(p0, p1, r_start, r_end, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dab(p0, p1, p2, r_start, r_end, steps=200, ease=1.0):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------------- Stroke 1: short 撇 at top -------------------------------
# Small pie throw from upper-right toward lower-left. Placed to the LEFT
# side of the top region. In 攵 (vs 夂), this 撇 is a fully-separate
# stroke — no continuous joint into the 横.
s1_start = (135, 62)
s1_end = (100, 108)
dab(s1_start[0], s1_start[1], 5)
bezier_dab(s1_start, (120, 78), s1_end, r_start=4.5, r_end=1.2, ease=1.3)


# ---------------- Stroke 2: short 横 --------------------------------------
# Sits BELOW-RIGHT of stroke 1's tail, clearly disjoint. Placed roughly
# on the right side of the top area, angled slightly up. This gives the
# 攵-characteristic "two separate marks at top" look, distinguishing it
# from 夂's continuous 横撇 hat.
h_start = (128, 128)
h_end = (210, 118)
line_dab(h_start, h_end, r_start=4, r_end=4, steps=160)
dab(h_start[0], h_start[1], 5)
dab(h_end[0], h_end[1], 5)


# ---------------- Stroke 3: long 撇 (left leg of bottom X) ---------------
# Starts at/near the right end of the 横, bows down-and-left to the
# lower-left. Dominant left-going stroke.
pie_p0 = (200, 128)
pie_p2 = (70, 248)
pie_ctrl = (175, 190)   # control pulled interior → gentle bow
bezier_dab(pie_p0, pie_ctrl, pie_p2, r_start=5.5, r_end=1.2, ease=1.35)


# ---------------- Stroke 4: 捺 (right leg of bottom X) --------------------
# Starts on the long 撇 near mid-height, sweeps down-and-right, thin→thick,
# ending in a broad flat foot. Crosses the 撇 to form the X signature.
na_p0 = (140, 168)     # sits on the 撇 body
na_p2 = (250, 248)     # broad foot in lower right
na_ctrl = (185, 190)   # gentle bow
bezier_dab(na_p0, na_ctrl, na_p2, r_start=1.8, r_end=8.5, ease=1.2)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_110_攵/01_攵.png")
