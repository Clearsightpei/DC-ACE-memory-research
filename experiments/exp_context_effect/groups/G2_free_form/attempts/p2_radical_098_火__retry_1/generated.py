"""
Render radical 火 (huo, "fire") — 4 strokes — RETRY 1.

Retry-1 fix, per errata for p2_radical_098_火:
- Prior attempt placed the two flanking dots inline with the 人-body
  midsection so they read as internal marks. In GT they clearly sit
  ABOVE the crossing apex — flanking sparks OUTSIDE the 人 form.
- The 人 body was too narrow/tall (apex y≈58). GT apex is lower
  (y≈75) and the 撇 sweeps to a much wider footprint.
- Both side dots in GT flick down-LEFT (both point inward/downward
  toward the 人 crossing). Not mirror-outward.
- 捺 in GT starts NEAR the 撇's top (they nearly share an apex, with
  the 捺 taking off from a bit lower and slightly right of the 撇's
  top). Broad terminal foot.

Decomposition (4 strokes) — GT-anchored:
  1. LEFT dot: short teardrop at ~(95, 115) flicking down-LEFT to ~(75, 145).
  2. RIGHT dot / 短撇: short teardrop at ~(180, 118) flicking down-LEFT to ~(160, 148).
  3. Long 撇 body: from ~(155, 72) down-left to ~(75, 265), gentle rightward bow.
  4. 捺 body: from ~(150, 105) down-right to ~(255, 265), broad thick foot.

Renderer: PIL brush-dabs, 300x300 white background, black ink.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_bezier(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        te = t ** ease
        omt = 1 - t
        x = omt * omt * x0 + 2 * omt * t * x1 + t * t * x2
        y = omt * omt * y0 + 2 * omt * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * te
        dab(x, y, r)


# ----------------------------------------------------------------------
# Stroke 1 — LEFT flanking dot (spark) — short teardrop flicking down-left
# Sits ABOVE + LEFT of the 人 apex, not fused with the body.
# ----------------------------------------------------------------------
dab(96, 115, 5.0)
taper_bezier(
    (96, 115), (85, 128), (72, 148),
    r_start=4.8, r_end=1.0, steps=220, ease=1.0
)


# ----------------------------------------------------------------------
# Stroke 2 — RIGHT flanking dot (spark) — also flicking down-left in GT.
# Moved x further right (188→198) and shortened so it stays clear of
# the 捺 body that passes through this region.
# ----------------------------------------------------------------------
dab(198, 112, 4.8)
taper_bezier(
    (198, 112), (188, 122), (176, 138),
    r_start=4.6, r_end=1.0, steps=200, ease=1.0
)


# ----------------------------------------------------------------------
# Stroke 3 — long central 撇 (top → lower-left, gentle bow)
# Apex lower (y=72) and endpoint further left+lower for wider footprint.
# ----------------------------------------------------------------------
dab(155, 72, 6.5)
taper_bezier(
    (155, 72), (128, 170), (72, 268),
    r_start=6.0, r_end=1.2, steps=520, ease=1.05
)


# ----------------------------------------------------------------------
# Stroke 4 — 捺: takes off slightly lower/right of 撇's top; belly
# swelling down-right; broad flat foot.
# ----------------------------------------------------------------------
p0 = (150, 105)
p1 = (195, 185)
p2 = (255, 262)
steps = 520
for i in range(steps + 1):
    t = i / steps
    omt = 1 - t
    x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
    y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
    if t < 0.85:
        r = 1.3 + (7.5 - 1.3) * (t / 0.85) ** 1.15
    else:
        r = 7.5
    dab(x, y, r)

# broad flat foot: extend along local tangent past p2, taper to a tip
tx, ty = p2[0] - p1[0], p2[1] - p1[1]
tl = math.hypot(tx, ty)
tx, ty = tx / tl, ty / tl
foot_len = 22
foot_steps = 70
for i in range(foot_steps + 1):
    t = i / foot_steps
    x = p2[0] + tx * foot_len * t
    y = p2[1] + ty * foot_len * t
    r = 7.5 - 6.8 * t
    dab(x, y, r)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_098_火__retry_1/01_火.png"
)
print("Saved 01_火.png")
