"""
飞 (fēi) — retry 2 — 3-stroke radical.

Retry 1 failed: main sweep bellied too far LEFT (down-left cubic that
overshot to x=95), and the small internal 撇 was drawn but the identity-
critical inside 提-like mark was ambiguous. Also the hook flicked too flat.

Looking at the GT PNG (gt/phase2/飞.png):
  Stroke 1 (横斜钩 / 横折弯钩): a short 横 upper-left → shoulder →
    long swept diagonal descending down-and-to-the-right side of canvas,
    with belly on LOWER-LEFT (concave toward upper-right), then a small
    hook at bottom that flicks up-and-slightly-left. This is really the
    dominant single sweep, not a tight double-curve.
  Stroke 2 (short 撇): inside the corner, sweeping down-and-left from
    upper-mid to mid.
  Stroke 3 (点/提-like short mark): small mark to the right of the 撇.

Fix per errata:
  - Draw the primary as one cleaner swept diagonal, hook at end.
  - Hook flick 40 px @ -115° to -120° with taper r=5→1.
  - Inside 撇 present, clearly ending before hitting the main body.
  - Add a small teardrop/dot near the inside of the corner.

PIL brush-dabs, 300×300, white/black.
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
        steps = max(20, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=250):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def cubic_dabs(p0, p1, p2, p3, r0, r1, steps=350):
    for i in range(steps + 1):
        t = i / steps
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t * t
        b3 = t * t * t
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


r_body = 5.5

# ---- Stroke 1: 横 (top segment, wide) + shoulder ---------------------
# Top 横 extends widely across upper canvas, sloping slightly up.
h_start = (35, 130)
h_end   = (200, 105)      # shoulder corner (upper-right area)
dab(*h_start, r_body + 2)                          # 顿 press start
line_dabs(*h_start, *h_end, r_body, r_body + 1)
dab(*h_end, r_body + 3)                            # shoulder dab

# ---- Stroke 1 continued: long swept diagonal (弯) with hook at bottom
# Body: from shoulder, curve down and sweep LEFTWARD at bottom (matching
# GT where the swoop terminates near center-bottom, having curved out
# to the left). Belly on lower-left, hook up-and-slightly-left at end.
P0 = h_end
P1 = (225, 190)   # first pulled outward-right
P2 = (175, 260)   # continues down and leftward
P3 = (140, 270)   # bottom of the swoop, center-bottom before hook
cubic_dabs(P0, P1, P2, P3, r_body + 1, r_body, steps=380)

# Terminal hook flicks UP-and-LEFT (~-120°) from the bottom.
hook_base = P3
hook_len = 38
hook_angle_deg = -120
ha = math.radians(hook_angle_deg)
hx = hook_base[0] + hook_len * math.cos(ha)
hy = hook_base[1] + hook_len * math.sin(ha)
dab(*hook_base, r_body)   # joining dab = segment radius (no bleed)
line_dabs(hook_base[0], hook_base[1], hx, hy, r_body, 1.0, steps=90)


# ---- Stroke 2: 撇 (short throw inside the corner) --------------------
# Short 撇 from upper-mid, sweeping down-and-left, ending before hitting
# the main body's left side.
p_start = (150, 155)
p_end   = (105, 220)
p_ctrl  = (145, 195)   # slight rightward bow
dab(*p_start, r_body + 0.5)
bezier_dabs(p_start, p_ctrl, p_end, r_body, 1.2, steps=160)


# ---- Stroke 3: 点 (small teardrop inside the upper-right pocket) ------
# Small teardrop sitting just below and right of the shoulder,
# thin→thick from upper-left to lower-right.
d_start = (168, 138)
d_end   = (188, 162)
d_steps = 60
for i in range(d_steps + 1):
    t = i / d_steps
    x = d_start[0] + (d_end[0] - d_start[0]) * t
    y = d_start[1] + (d_end[1] - d_start[1]) * t
    tt = t ** 1.4
    r = 1.8 + (6.0 - 1.8) * tt
    dab(x, y, r)
dab(*d_end, 6.5)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_047_飞__retry_2/01_飞.png")
