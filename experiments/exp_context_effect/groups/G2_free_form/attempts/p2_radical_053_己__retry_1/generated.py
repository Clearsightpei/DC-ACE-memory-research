"""
Retry 1 of 己 (radical, 3 strokes).

Prior failure diagnosis (from errata):
  - Read as boxy 巳: bottom lacked sweeping 竖弯钩 tail extending right
  - Middle 横 touched left wall (that's a 已, not 己)
  - No terminal hook flick up-and-left

Fixes here:
  Stroke 1 (横折): top 横 rightward then fold down (short vertical drop
      ending at mid-height, blunt). Establishes top-right corner at ~x=210.
  Stroke 2 (横): middle horizontal, FLOATING — starts several px OFF the
      left vertical (a visible gap), extends right to meet stroke 1's
      fold-vertical end.
  Stroke 3 (竖弯钩): starts at stroke 1's top-left (top-left corner),
      drops straight DOWN as 竖, then arcs into a rightward 弯, and the
      horizontal extends PAST the top-right edge (past x=210, out to
      about x=245), then a small terminal HOOK flick up-and-slightly-
      left (~30-40 px, angled about -100° to -110°).
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
r_body = 5.5

# Stroke 1: 横折
S1_TL = (78, 82)        # top-left corner (shared start with stroke 3)
S1_TR = (210, 78)       # top-right corner (fold shoulder)
S1_BR = (205, 150)      # end of vertical drop (blunt, mid-height)

# Stroke 2: 横 middle — FLOATING, doesn't touch left wall
S2_LEFT = (105, 150)    # gap of ~25 px from left vertical (which is at x≈78)
S2_RIGHT = (200, 150)   # meets near where stroke 1's vertical ends

# Stroke 3: 竖弯钩
S3_TOP = (78, 88)                    # just below S1_TL (shared corner)
S3_VBOT = (72, 215)                  # bottom of vertical (slight lean left)
ARC_R = 34
S3_ARC_END = (S3_VBOT[0] + ARC_R, S3_VBOT[1] + ARC_R)  # (106, 249)
S3_HEND = (245, 249)                 # extends RIGHT past S1_TR's x=210
# Hook flick from S3_HEND: up and slightly LEFT
HOOK_LEN = 38
HOOK_ANGLE_DEG = -108  # -100° to -110°: up and slightly left
hx = S3_HEND[0] + HOOK_LEN * math.cos(math.radians(HOOK_ANGLE_DEG))
hy = S3_HEND[1] + HOOK_LEN * math.sin(math.radians(HOOK_ANGLE_DEG))
S3_HOOK_TIP = (hx, hy)


# --- Stroke 1: 横折 (top) ---
dab(S1_TL[0], S1_TL[1], r_body + 1.5)                 # start 顿
line_taper(S1_TL, S1_TR, r_body, r_body + 0.5, steps=260)
dab(S1_TR[0], S1_TR[1], r_body + 2.0)                 # 折 shoulder
line_taper(S1_TR, S1_BR, r_body + 0.5, r_body, steps=200)
dab(S1_BR[0], S1_BR[1], r_body + 1.0)                 # blunt end


# --- Stroke 2: 横 middle (floating) ---
dab(S2_LEFT[0], S2_LEFT[1], r_body + 1.2)
line_taper(S2_LEFT, S2_RIGHT, r_body, r_body + 0.4, steps=220)
dab(S2_RIGHT[0], S2_RIGHT[1], r_body + 1.2)


# --- Stroke 3: 竖弯钩 ---
# Start dab
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
# Join dab at hook base — segment radius only (per memory: no r+2 at hook joints)
dab(S3_HEND[0], S3_HEND[1], r_body)
# Hook flick: up-and-slightly-left, tapering from r_body to sharp point
line_taper(S3_HEND, S3_HOOK_TIP, r_body, 1.2, steps=90)


out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_053_己__retry_1/01_己.png"
img.save(out_path)
print(f"Saved {out_path}")
