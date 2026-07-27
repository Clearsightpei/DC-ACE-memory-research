"""
Retry 2 of 己 (radical, 3 strokes).

Prior retry_1 failure diagnosis (from errata + curator vision):
  - Middle 横 started at x=105 but visually STILL read as touching the
    left wall -> glyph read as 已 not 己. Signature bit failed.
  - Bottom 竖弯钩 hook flick was small / hard to see.

Sibling bit (from form_catalog.md, HARD RULE per memory_index):
  己 vs 已 vs 巳:
    己 = middle 横 FLOATS (visible ~15+ px gap from left wall)
    已 = middle 横 TOUCHES left wall midway
    巳 = middle 横 TOUCHES at top

Fixes here:
  * Push middle-横 left endpoint significantly right (x=118) vs left
    wall at x=72 -> visible ~45 px whitespace gap.
  * Make the left wall thinner-looking / not too bulky at the y-band
    of the middle bar so the gap is unambiguous.
  * Terminal 竖弯钩 hook: longer (~45 px) at angle -115° with clear
    taper so the up-and-left flick is visually decisive.
  * Bottom horizontal sweep extends CLEARLY past the top-right x
    (top ends x=210, bottom sweep out to x=250).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r0, r1, steps=300):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Layout anchors ---
r_body = 5.0

# Stroke 1: 横折 (top-lid)
S1_TL = (72, 82)       # top-left corner (also stroke 3 start)
S1_TR = (210, 78)      # top-right corner (fold shoulder)
S1_BR = (208, 148)     # end of the vertical drop (blunt)

# Stroke 2: 横 middle — FLOATING with big visible gap from left wall
S2_LEFT = (135, 152)   # ~63 px right of left wall at x=72 -> obvious gap
S2_RIGHT = (208, 152)  # meets near where stroke 1's vertical ends

# Stroke 3: 竖弯钩 (bottom sweep)
S3_TOP = (72, 88)                       # shared with S1_TL (below start dab)
S3_VBOT = (72, 220)                     # bottom of vertical (straight down)
ARC_R = 32
S3_ARC_END = (S3_VBOT[0] + ARC_R, S3_VBOT[1] + ARC_R)  # (104, 252)
S3_HEND = (250, 252)                    # sweeps CLEARLY past S1_TR's x=210

# Hook flick: up-and-left, longer & clearly visible
HOOK_LEN = 55
HOOK_ANGLE_DEG = -120
hx = S3_HEND[0] + HOOK_LEN * math.cos(math.radians(HOOK_ANGLE_DEG))
hy = S3_HEND[1] + HOOK_LEN * math.sin(math.radians(HOOK_ANGLE_DEG))
S3_HOOK_TIP = (hx, hy)


# --- Stroke 1: 横折 (top) ---
dab(S1_TL[0], S1_TL[1], r_body + 1.5)                 # start 顿
line_taper(S1_TL, S1_TR, r_body, r_body + 0.5, steps=260)
dab(S1_TR[0], S1_TR[1], r_body + 2.0)                 # 折 shoulder
line_taper(S1_TR, S1_BR, r_body + 0.5, r_body, steps=200)
dab(S1_BR[0], S1_BR[1], r_body + 1.0)                 # blunt end


# --- Stroke 2: 横 middle (floating with big gap) ---
dab(S2_LEFT[0], S2_LEFT[1], r_body + 1.2)
line_taper(S2_LEFT, S2_RIGHT, r_body, r_body + 0.4, steps=220)
dab(S2_RIGHT[0], S2_RIGHT[1], r_body + 1.2)


# --- Stroke 3: 竖弯钩 ---
dab(S3_TOP[0], S3_TOP[1], r_body + 1.2)
# Vertical descent
line_taper(S3_TOP, S3_VBOT, r_body, r_body, steps=280)
# Tangent-continuous quarter arc: vertical -> horizontal (bottom-right sweep)
cx0, cy0 = S3_VBOT
R = ARC_R
arc_steps = 140
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = cx0 + R * (1 - math.cos(t * math.pi / 2))
    y = cy0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)
# Horizontal sweep past top-right edge
line_taper(S3_ARC_END, S3_HEND, r_body, r_body + 0.4, steps=260)
# Join dab at hook base — segment-radius only (no r+2, per memory)
dab(S3_HEND[0], S3_HEND[1], r_body)
# Hook flick: up-and-left, tapering to sharp point
line_taper(S3_HEND, S3_HOOK_TIP, r_body, 1.0, steps=110)


out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_053_己__retry_2/01_己.png"
img.save(out_path)
print(f"Saved {out_path}")
