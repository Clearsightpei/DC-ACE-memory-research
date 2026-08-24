"""
Render radical 火 (huo, "fire") — 4 strokes.

Revision 1 vs previous attempt:
- Right short 撇 was being absorbed by the long 撇 — move it further right
  and shift its slant so it clearly reads as separate.
- Long 撇 was too vertical near the top — start it more to the right of
  center and bow more strongly leftward.
- Overall strokes were too thick vs the light GT — reduce base radius
  from ~8 to ~5-6.
- Reduce 顿 dabs at standalone endpoints (memory: "No visible 顿-dab
  balls at standalone endpoints").

Canonical decomposition (4 strokes):
  1. Left 点/短撇 in upper-left, throws down-and-left
  2. Right 短撇 to the right of center (mirror position of 1), throws
     down-and-left (toward middle)
  3. Long central 撇 from top-center-right down to lower-left (bowed)
  4. 捺 from mid-upper crossing the 撇, down-and-right with broad foot

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
# Stroke 1 — left short 撇 (upper-left, throw down-left)
# ----------------------------------------------------------------------
dab(112, 118, 5.5)
taper_bezier(
    (112, 118), (100, 132), (78, 158),
    r_start=5.0, r_end=1.2, steps=250, ease=1.0
)


# ----------------------------------------------------------------------
# Stroke 2 — right short 撇 (upper-right, throw down-left)
# Positioned further right so it doesn't get absorbed by the long 撇.
# ----------------------------------------------------------------------
dab(215, 122, 5.5)
taper_bezier(
    (215, 122), (200, 138), (178, 158),
    r_start=5.0, r_end=1.2, steps=250, ease=1.0
)


# ----------------------------------------------------------------------
# Stroke 3 — long central 撇 (top → lower-left, strongly bowed)
# Start further right at top so we have room to bow left.
# ----------------------------------------------------------------------
dab(168, 58, 6.5)
taper_bezier(
    (168, 58), (140, 160), (60, 260),
    r_start=6.0, r_end=1.2, steps=500, ease=1.05
)


# ----------------------------------------------------------------------
# Stroke 4 — 捺 (thin start high, thick belly, broad flat foot to lower-right)
# ----------------------------------------------------------------------
p0 = (150, 100)
p1 = (190, 175)
p2 = (255, 250)
steps = 500
for i in range(steps + 1):
    t = i / steps
    omt = 1 - t
    x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
    y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
    # thin start (r≈1.5) growing to thick belly (~8.5) then broad foot
    if t < 0.85:
        r = 1.5 + (8.5 - 1.5) * (t / 0.85) ** 1.15
    else:
        r = 8.5
    dab(x, y, r)

# Broad flat foot extending past p2 along the local tangent, tapering to tip
tx, ty = 255 - 190, 250 - 175
tl = math.hypot(tx, ty)
tx, ty = tx / tl, ty / tl
foot_len = 24
foot_steps = 70
for i in range(foot_steps + 1):
    t = i / foot_steps
    x = 255 + tx * foot_len * t
    y = 250 + ty * foot_len * t
    r = 8.5 - 7.0 * t
    dab(x, y, r)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_098_火/01_火.png"
)
print("Saved 01_火.png")
