"""
G2 attempt — p2_radical_051_廾 (gǒng, 3画 radical).

Structural read of the GT:
- Stroke 1: 横 (top horizontal), gentle up-tilt, spans across the top.
- Stroke 2: 撇 (throw-away) — the LEFT vertical-ish member, starts up
  above the 横 (poking above), crosses THROUGH the 横, descends and
  bows down-and-left to a sharp tapered tip in the lower-left.
- Stroke 3: 竖 (vertical) — the RIGHT member, starts up above the 横
  (poking above), descends nearly straight down through the 横 to a
  blunt terminal press near the lower-right.

Both stroke 2 and stroke 3 CROSS THROUGH stroke 1 — the top of each
must be visible above the 横 (rule #3 from memory: crossing must be
visible). Their tops sit ~5-15 px above the 横's y-level.

Standalone scale (300×300) — using standalone-scale discipline:
r=5-6, 顿-dab r+1 at plain endpoints (not r+2 tumors), pronounced
Bezier bow for the 撇, hook/flick angles per stroke class.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
        y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------- Stroke 1: 横 (top horizontal) ----------
# Slight up-tilt (right end ~5 px higher than left end).
# Widen span slightly to match GT proportions; keep endpoint dabs small
# (standalone scale — r+1 not r+2) to avoid balloon tumors.
H_LEFT = (32, 122)
H_RIGHT = (268, 112)
# Modest 顿-dab at start.
dab(H_LEFT[0], H_LEFT[1], 7)
line_dabs(H_LEFT[0], H_LEFT[1], H_RIGHT[0], H_RIGHT[1], 6, 6, steps=550)
# Small terminal press at right end.
dab(H_RIGHT[0], H_RIGHT[1], 6.5)


# ---------- Stroke 2: 撇 (LEFT member, crossing through 横) ----------
# Top starts ABOVE the 横 line (y ~ 90, above y=118 at that x).
# Crosses through 横, then bows down-and-left to sharp tapered tip.
# Use Bezier with control point pulled to the right (rightward bow)
# so belly is on the right, tip curls to the lower-left.
PIE_START = (105, 80)          # top, above the 横
PIE_END = (55, 260)            # tapered tip, lower-left
PIE_CTRL = (115, 175)          # control pulled right/interior for gentle bow
# 顿-dab at start.
dab(PIE_START[0], PIE_START[1], 8)
bezier_dabs(PIE_START, PIE_CTRL, PIE_END, 8.5, 1.2, steps=500)


# ---------- Stroke 3: 竖 (RIGHT member, crossing through 横) ----------
# Top starts ABOVE the 横 line (y ~ 85). Descends nearly straight
# down. Slight rightward lean (canonical for the right member of 廾).
SHU_START = (195, 82)
SHU_END = (210, 265)
# 顿-dab at start.
dab(SHU_START[0], SHU_START[1], 8)
line_dabs(SHU_START[0], SHU_START[1], SHU_END[0], SHU_END[1], 6.5, 6.5, steps=500)
# Blunt terminal press.
dab(SHU_END[0], SHU_END[1], 7)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_051_廾/01_廾.png"
)
