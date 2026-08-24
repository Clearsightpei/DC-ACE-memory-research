"""
Render 七 to a 300x300 PNG using PIL brush-dabs.

Decomposition (per form_catalog sibling-pair table and drawer_memory
hook family):
  Stroke 1: 横 — a clearly tilted 横 (left→right, up-slope ~10-12°),
            spans most of canvas width. Left end LOW, right end HIGH.
  Stroke 2: 竖弯钩 — starts ABOVE the 横, descends with a slight
            leftward lean (mild 撇 posture), crosses the 横, continues
            down, then arcs (弯, no shoulder) into a rightward
            horizontal along the lower canvas, ending with a short
            up-flick 钩.

Silhouette family: square-ish, ~70% x-extent, ~65% y-extent.
Center of mass: centered / slightly-lower (the 竖弯钩 body dominates).

Sibling check (匕 vs 七): the top stroke IS a 横 (left→right,
low-to-high), NOT a 撇 that would slant downward.
"""

import math
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def uniform_line(x0, y0, x1, y1, r, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 1: 横 (top). Clear up-tilt (~11°).
# Left LOW (~y=145), right HIGH (~y=108). Length ~200 px.
# ---------------------------------------------------------------
H_X0, H_Y0 = 45, 148
H_X1, H_Y1 = 245, 108
R_H = 6

# 顿 press at start
dab(H_X0, H_Y0, R_H + 2)
# body (slight ramp)
taper_line(H_X0, H_Y0, H_X1, H_Y1, R_H, R_H + 1, steps=350)
# terminal blunt press at end
dab(H_X1, H_Y1, R_H + 2)


# ---------------------------------------------------------------
# Stroke 2: 竖弯钩.
#   Beat A: near-vertical descent (slight leftward lean), starting
#           ABOVE the 横 so it clearly crosses through it.
#   Beat B: smooth quarter-arc (弯, no shoulder dab).
#   Beat C: short rightward horizontal running along the bottom.
#   Beat D: 钩 flick UP from the horizontal's right end (short).
# ---------------------------------------------------------------

R_V = 7  # main body radius of 竖弯钩

# --- Beat A: near-vertical descent (slight leftward lean) ---
VA_X0, VA_Y0 = 158, 75      # top: well above the 横
VA_X1, VA_Y1 = 122, 210     # bottom of descent, arc entry
dab(VA_X0, VA_Y0, R_V + 2)  # 顿 start
uniform_line(VA_X0, VA_Y0, VA_X1, VA_Y1, R_V, steps=350)

# --- Beat B: tangent-continuous quarter-arc (弯) ---
R_ARC = 32
ax0, ay0 = VA_X1, VA_Y1
arc_steps = 120
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = ax0 + R_ARC * (1 - math.cos(t * math.pi / 2))
    y = ay0 + R_ARC * math.sin(t * math.pi / 2)
    dab(x, y, R_V)
arc_end_x = ax0 + R_ARC   # = 154
arc_end_y = ay0 + R_ARC   # = 242

# --- Beat C: rightward horizontal along the bottom ---
HC_X0, HC_Y0 = arc_end_x, arc_end_y
HC_X1, HC_Y1 = 250, arc_end_y - 4   # very slight up-tilt over the run
uniform_line(HC_X0, HC_Y0, HC_X1, HC_Y1, R_V, steps=250)

# --- Beat D: 钩 flick, short UP from horizontal's end ---
HOOK_LEN = 25
HOOK_ANGLE_DEG = -100   # in image coords: -90 is straight up
ang = math.radians(HOOK_ANGLE_DEG)
HK_X0, HK_Y0 = HC_X1, HC_Y1
HK_X1 = HK_X0 + HOOK_LEN * math.cos(ang)
HK_Y1 = HK_Y0 + HOOK_LEN * math.sin(ang)
dab(HK_X0, HK_Y0, R_V)
taper_line(HK_X0, HK_Y0, HK_X1, HK_Y1, R_V, 1.5, steps=200)


img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0027_七/01_七.png"
)
