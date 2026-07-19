"""Render 卜 (2-stroke radical) at 300x300 white, black ink.
Structure (per GT observation):
- Stroke 1: 竖 (vertical), left-center. Slight comma-head start (top curls
  in a bit) then straight down through the middle-lower canvas.
- Stroke 2: 点 (dot) attached to the right of the 竖 at mid-height,
  angling down-and-right, thin at attach, thickening slightly with a
  gentle bow (like a short teardrop-ish dot that curves down-right).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=None, ease=None):
    dist = math.hypot(p2[0] - p0[0], p2[1] - p0[1])
    if steps is None:
        steps = max(80, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        tt = t if ease is None else ease(t)
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---------- Stroke 1: 竖 with slight comma/curve at the top ----------
# Top head curls slightly right-to-left (as GT shows a small arc top).
# We render as: short bezier head + straight vertical body.

# Head: small curve from (128, 70) curving over to (120, 92)
bezier_dabs(
    p0=(128, 68),
    p1=(122, 76),
    p2=(120, 92),
    r0=3.0,
    r1=5.0,
    steps=60,
)

# Body: straight vertical from (120, 92) down to (120, 260)
line_dabs(120, 92, 120, 260, 5.0, 5.0, steps=520)

# Terminal press
dab(120, 260, 6)

# ---------- Stroke 2: 点 (dot) — short bowed dash going down-right ----------
# Attached to the right side of the 竖 around mid-height (~y=160).
# Starts thin at the attach point, thickens along the bow, ends with a
# small terminal press.
# Concave-up bow: control point pulled UP so the belly rises above the chord.
bezier_dabs(
    p0=(148, 158),
    p1=(178, 162),
    p2=(228, 200),
    r0=2.2,
    r1=5.5,
    steps=160,
    ease=lambda t: t ** 1.15,
)

# Terminal press at end of 点
dab(228, 200, 6)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_013_卜/01_卜.png"
)
