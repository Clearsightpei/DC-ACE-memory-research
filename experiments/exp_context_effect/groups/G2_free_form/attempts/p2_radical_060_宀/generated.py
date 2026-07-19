"""
宀 (bǎo gài tóu) — Phase-2 radical, 3 strokes.

Decomposition per MMH (3画):
  1. 点 (top center dot) — small teardrop, thin→thick, angled down-right.
  2. 左点 / short 竖点 — short near-vertical dot on the left "shoulder"
     of the horizontal (slightly slanted, thin→thick).
  3. 横钩 — long 横 sweeping left→right across the top, ending with a
     hook flicking down-and-left from the right endpoint.

Renderer: PIL brush-dabs (per drawer_memory principles).
Canvas: 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def teardrop(x0, y0, x1, y1, r0, r1, steps=200, ease=1.4):
    """Thin→thick tapered stroke (used for 点 dots)."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


def line_uniform(x0, y0, x1, y1, r, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        dab(x, y, r)


def taper_line(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# Revision notes (self-check vs GT):
# - GT strokes are thinner/more delicate (~3–4 px). Reduce radii.
# - Top 点: shorter, positioned slightly right of centre, less thick.
# - 左点: GT shows it as a very short, near-vertical stub — shorten.
# - 横钩: primary should be uniform-thin (no ramp-up); hook a bit
#   longer and steeper (~130°).
# ---------------------------------------------------------------

# Stroke 1: 点 top-center dot. Small teardrop, thin→thick, angled
# down-slightly-right.
teardrop(x0=147, y0=88, x1=158, y1=118, r0=1.2, r1=4.5, ease=1.4)
dab(158, 118, 5)

# Stroke 2: 左点 — short near-vertical dot on the left side of the
# horizontal, hanging below the 横's left endpoint. Slight down-left
# slant, thin→thick.
teardrop(x0=78, y0=148, x1=72, y1=185, r0=1.2, r1=4.2, ease=1.4)
dab(72, 185, 4.7)

# Stroke 3: 横钩 — long horizontal left→right (slight up-tilt),
# then shoulder + hook flicking down-and-left at the right endpoint.
hx0, hy0 = 78, 148            # left endpoint
hx1, hy1 = 240, 140           # right endpoint slightly higher (up-tilt ~3°)

# starting 顿 dab (initial press) — modest
dab(hx0, hy0, 5.5)

# main horizontal body — near-uniform thin
steps = 500
r_body = 3.8
for i in range(steps + 1):
    t = i / steps
    x = hx0 + (hx1 - hx0) * t
    y = hy0 + (hy1 - hy0) * t
    # very slight ramp up toward shoulder
    r = r_body + 1.5 * (t ** 2.2)
    dab(x, y, r)

# shoulder dab at the corner (顿 press) — moderate
dab(hx1, hy1, 6.0)

# hook: flicks DOWN-and-LEFT from the right endpoint.
# angle ~130° from +x axis (down-and-slightly-left). Length ~38 px.
hook_len = 38
hook_angle = math.radians(130)
hx2 = hx1 + hook_len * math.cos(hook_angle)
hy2 = hy1 + hook_len * math.sin(hook_angle)

hook_steps = 240
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = hx1 + (hx2 - hx1) * t
    y = hy1 + (hy2 - hy1) * t
    r = 5.5 + (1.0 - 5.5) * t  # taper thick→sharp
    dab(x, y, r)

dab(hx2, hy2, 1.0)

# ---------------------------------------------------------------
# Save
# ---------------------------------------------------------------
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_宀.png"))
print("wrote", os.path.join(out_dir, "01_宀.png"))
