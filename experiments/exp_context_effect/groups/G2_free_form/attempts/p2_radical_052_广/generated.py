"""
G2 attempt for radical 广 (3 strokes) — revised pass.

Revision notes (v2):
- Dot was too heavy: reduced max radius and length.
- 横 was too thick and had heavy end-caps that read as balloons.
  Reduced uniform radius, softened end-press.
- Shared-corner dab (heng+pie joint) was visibly bumpy; reduced to r+1.
- 撇 kept as gently bowed Bezier, slightly thinner start radius so the
  overall composition feels lighter to match GT weight.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------- Stroke 1: 点 (dot at top) ----------
# Small teardrop, angled down-right. Trimmed radius from prev.
dot_p0 = (122, 60)
dot_p1 = (138, 72)
dot_p2 = (152, 84)
steps = 80
for i in range(steps + 1):
    t = i / steps
    x = (1 - t) ** 2 * dot_p0[0] + 2 * (1 - t) * t * dot_p1[0] + t ** 2 * dot_p2[0]
    y = (1 - t) ** 2 * dot_p0[1] + 2 * (1 - t) * t * dot_p1[1] + t ** 2 * dot_p2[1]
    tt = t ** 1.4
    r = 1.8 + (6.0 - 1.8) * tt
    dab(x, y, r)
# terminal press — subtle
dab(dot_p2[0], dot_p2[1], 6.5)


# ---------- Stroke 2: 横 (horizontal) ----------
# Upper-middle. LEFT end will be the SHARED CORNER with stroke 3.
heng_x0, heng_y0 = 82, 118
heng_x1, heng_y1 = 220, 111   # slight up-tilt
# Uniform thin body, no oversized start-dab (that's replaced by joint dab).
line_dabs(heng_x0, heng_y0, heng_x1, heng_y1, 4.5, 4.0)
# Subtle terminal press at right (blunt)
dab(heng_x1, heng_y1, 5.5)


# ---------- Shared corner joint dab (r+1, subtle) ----------
dab(heng_x0, heng_y0, 5.5)


# ---------- Stroke 3: 撇 (long throw-away descending down-left) ----------
# Starts at shared corner. Gently bowed Bezier, control point pulled right.
pie_p0 = (heng_x0, heng_y0)   # (82, 118) — shared corner
pie_p2 = (58, 258)             # lower-left tip
# Chord midpoint = (70, 188). Pull ctrl to the right for a nice belly.
pie_p1 = (118, 168)
steps = 400
for i in range(steps + 1):
    t = i / steps
    x = (1 - t) ** 2 * pie_p0[0] + 2 * (1 - t) * t * pie_p1[0] + t ** 2 * pie_p2[0]
    y = (1 - t) ** 2 * pie_p0[1] + 2 * (1 - t) * t * pie_p1[1] + t ** 2 * pie_p2[1]
    r = 6.5 + (1.3 - 6.5) * t   # thick -> thin, sharp tip
    dab(x, y, r)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_052_广/01_广.png")
print("saved")
