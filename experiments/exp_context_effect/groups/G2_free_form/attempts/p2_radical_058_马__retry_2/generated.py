"""
p2_radical_058_马 (3画) — G2 retry_2.

Prior-fail analysis (from errata.md line 526-536):
- retry_1 body was too cramped: middle 折 segments ~20px each, character
  read as narrow rectangle with a tail.
- Fix per errata: middle-body height ~130 px (was ~80); each 折 segment
  ~40 px minimum. 竖折折钩 = 3 body beats + hook.

Structure (3 strokes, MMH-standard):
  1. 横折  — top edge of upper box (top 横) then 折 into short right 竖.
  2. 竖折折钩 — starting at top-left, goes DOWN (left wall of top box),
     folds RIGHT (bottom of top box / middle 横), folds DOWN (long
     descending 竖), ends with hook flicking UP-LEFT.
  3. 一 (long 横) — bottom horizontal spanning wide, passing through
     the terminal region of stroke 2 (not floating disconnected).

Layout tall — top box occupies upper ~30% of body; descending body
takes middle ~40%; bottom 横 sits at ~y=250, spans wide. Body is
TALL not cramped.
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    L = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(L * 2.5), 8)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ----------------------------------------------------------------------
# LAYOUT — Tall body per errata fix
# ----------------------------------------------------------------------
# Top box: upper region roughly y=55..100 (height ~45 px)
# Middle 横 (bottom of top box): y ~100
# Descending 竖: y=100 → y=225 (~125 px descent — the "body height" fix)
# Hook flick tip: up-and-left from bottom
# Final 一: y ~ 250, spanning x=45 to x=270 (wide)
# ----------------------------------------------------------------------

# Stroke 1 (横折) beats
S1_TL = (85, 68)     # top-left of top box (start of top 横)
S1_TR = (210, 58)    # top-right corner (slight up-tilt on top 横)
S1_BR = (218, 105)   # bottom-right of top box (end of short right 竖)

# Stroke 2 (竖折折钩) beats — TALL body, wider descending 竖
S2_TL   = (88, 72)    # start (just under S1_TL — left wall top)
S2_BL   = (92, 110)   # bottom-left of top box (end of left 竖)
S2_MR   = (205, 113)  # right end of middle 横 (bottom of top box, wide)
S2_BOT  = (180, 232)  # bottom of descending 竖 (deep, slight leftward drift)
S2_HKTIP = (120, 205) # hook flick tip up-and-left (long flick)

# Stroke 3 (一) — long bottom horizontal
H_L = (45, 253)
H_R = (270, 248)

R = 5.5
R_SH = R + 2.5      # shoulder emphasis at 折 corners

# ----------------------------------------------------------------------
# Stroke 1: 横折  (top 横 + short right 竖)
# ----------------------------------------------------------------------
dab(S1_TL[0], S1_TL[1], R + 1.5)                          # 顿-start
line_dabs(S1_TL[0], S1_TL[1], S1_TR[0], S1_TR[1], R, R + 0.5)
dab(S1_TR[0], S1_TR[1], R_SH)                             # shoulder at 折
line_dabs(S1_TR[0], S1_TR[1], S1_BR[0], S1_BR[1], R, R)
dab(S1_BR[0], S1_BR[1], R + 1)                            # terminal press

# ----------------------------------------------------------------------
# Stroke 2: 竖折折钩 — three body beats + hook flick
# beat A: 竖  S2_TL → S2_BL          (left wall of top box)
# beat B: 横  S2_BL → S2_MR          (middle 横, bottom of top box)
# beat C: 竖  S2_MR → S2_BOT         (long descending 竖 — TALL body)
# flick :     S2_BOT → S2_HKTIP      (hook up-and-left)
# ----------------------------------------------------------------------
dab(S2_TL[0], S2_TL[1], R + 1.5)                          # 顿-start
# beat A — left wall of top box (~33 px)
line_dabs(S2_TL[0], S2_TL[1], S2_BL[0], S2_BL[1], R, R)
dab(S2_BL[0], S2_BL[1], R_SH)                             # shoulder at 折
# beat B — middle 横 (bottom of top box, ~93 px wide)
line_dabs(S2_BL[0], S2_BL[1], S2_MR[0], S2_MR[1], R, R)
dab(S2_MR[0], S2_MR[1], R_SH)                             # shoulder at 折
# beat C — long descending 竖 (~117 px — the fix)
line_dabs(S2_MR[0], S2_MR[1], S2_BOT[0], S2_BOT[1], R, R)
# hook flick — sharp tapered up-and-left
line_dabs(S2_BOT[0], S2_BOT[1], S2_HKTIP[0], S2_HKTIP[1], R + 0.5, 1.2, steps=90)

# ----------------------------------------------------------------------
# Stroke 3: long 一 — bottom horizontal, spans wide, near hook terminus
# ----------------------------------------------------------------------
dab(H_L[0], H_L[1], R + 2)
line_dabs(H_L[0], H_L[1], H_R[0], H_R[1], R, R + 0.5)
dab(H_R[0], H_R[1], R + 2)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_058_马__retry_2/01_马.png"
)
