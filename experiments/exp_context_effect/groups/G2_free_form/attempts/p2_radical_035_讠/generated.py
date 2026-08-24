"""
讠 (yán) — speech radical, 2 strokes.
Composition (from GT):
  1. 点 (dian) at top-left — small stroke sloping down-and-right,
     thin→thick (a right-facing dot).
  2. 横折提 (heng-zhe-ti) below and slightly right of the 点:
       (a) short 横 (left→right, slight up-tilt),
       (b) 折 shoulder (small 顿 press),
       (c) 竖 descending (slight left lean, per drawer_memory principle
           to leave room for the 提),
       (d) 提 (rising) tail from the bottom of the 竖 up-and-right,
           thick→thin, ~25° above horizontal.

Revision: pass-1 strokes were too heavy and the 提 tail too pronounced.
GT lines are thin/wiry — using thinner radii throughout, shorter 提.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(30, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Stroke 1: 点 (dot) — a right-facing teardrop at top-left --------
# GT: small comma-like stroke, top-left of frame.
line_dabs(x0=95, y0=55, x1=120, y1=82, r0=1.2, r1=4.5)
dab(121, 83, 4.5)


# --- Stroke 2: 横折提 -----------------------------------------------
# Layout: sits below the 点, occupies mid-left of frame.
# Thinner uniform width (~3.5 px radius) matching GT weight.
# Beat 1 (横): from ~(65, 138) to ~(150, 128) — slight up-tilt.
# Corner (顿 shoulder) at ~(150, 128), small dab.
# Beat 2 (竖): descends from ~(150, 128) to ~(140, 225) with slight
#   left lean (so 提 has room).
# Beat 3 (提): short, from ~(140, 225) rising to ~(190, 205),
#   thick→thin, ~-22° above horizontal.

# Beat 1: 横 — thin, near-uniform
line_dabs(x0=65, y0=138, x1=150, y1=128, r0=3.5, r1=4.2)

# Shoulder dab (顿) at corner
dab(150, 128, 5)

# Beat 2: 竖 — thin, near-uniform, slight left lean
line_dabs(x0=150, y0=128, x1=140, y1=225, r0=4.2, r1=3.8)

# Small joining dab where 提 attaches
dab(140, 225, 4.5)

# Beat 3: 提 — short, thick→thin, rising
line_dabs(x0=140, y0=225, x1=192, y1=205, r0=4.0, r1=1.0)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_035_讠/01_讠.png"
)
