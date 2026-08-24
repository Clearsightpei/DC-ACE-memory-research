"""
Render 己 (radical, 3 strokes) at 300x300, white bg, black ink, PIL brush-dabs.

Structure of 己:
  Stroke 1: 横折 — short 横 rightward, then 折 down (blunt end, no hook)
  Stroke 2: 横 — starts on left, meets stroke 1's vertical end at the right
  Stroke 3: 竖弯钩 — starts at stroke 1's top-left corner region (shares
            start with stroke 1's start), drops down, curves right into a
            rightward-running horizontal, ending in a blunt press (no hook
            in this GT — modern rendering).

Actually, looking at the GT more carefully, the standard MMH form of 己:
  1) 横折: top horizontal + fold down to mid-height
  2) 横: middle horizontal from left, meets stroke 1's fold end
  3) 竖弯钩: from the LEFT side (start of stroke 1), drops straight down,
            arcs into rightward horizontal, ends with blunt press.

But the top-left of stroke 3 shares the start of stroke 1 (both begin at
same left anchor). Standalone rendering — use bigger canvas fills, smaller
顿-dabs at endpoints (per standalone discipline).
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


def quad_bezier(p0, p1, p2, r0, r1, steps=300):
    x0, y0 = p0
    xc, yc = p1
    x1, y1 = p2
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * xc + t ** 2 * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * yc + t ** 2 * y1
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# --- Layout anchors (standalone scale) ---
# Top-left of stroke 1
TL = (85, 82)
# Fold point (end of stroke 1's 横, start of the vertical drop of stroke 1)
FOLD1 = (205, 76)
# End of stroke 1's 竖 drop (about mid-height)
END1 = (200, 148)

# Middle horizontal (stroke 2) — extends slightly past FOLD1's vertical
MID_LEFT = (90, 148)
MID_RIGHT = (215, 148)

# Stroke 3: 竖弯钩-like — starts slightly BELOW and LEFT of stroke 1's TL
# (small visual gap so the top-left corner reads as "open")
S3_START = (88, 92)
S3_VERT_END = (82, 208)  # end of the vertical drop before arc
ARC_R = 38
# After arc from S3_VERT_END sweeping into rightward horizontal
S3_ARC_END = (S3_VERT_END[0] + ARC_R, S3_VERT_END[1] + ARC_R)  # (120, 246)
S3_H_END = (240, 246)


# --- Stroke 1: 横折 ---
# 横 with slight up-tilt: TL -> FOLD1
r_body = 5.5
# Start 顿 dab (small for standalone)
dab(TL[0], TL[1], r_body + 1.5)
line_taper(TL, FOLD1, r_body, r_body + 0.5, steps=260)
# Shoulder dab at FOLD1
dab(FOLD1[0], FOLD1[1], r_body + 2.5)
# 竖 drop, straight-ish, slight lean left
line_taper(FOLD1, END1, r_body + 0.5, r_body, steps=180)
# Blunt terminal press
dab(END1[0], END1[1], r_body + 1.2)


# --- Stroke 2: 横 middle ---
# Slight up-tilt, small 顿 both ends
dab(MID_LEFT[0], MID_LEFT[1], r_body + 1.5)
line_taper(MID_LEFT, MID_RIGHT, r_body, r_body + 0.5, steps=240)
dab(MID_RIGHT[0], MID_RIGHT[1], r_body + 1.5)


# --- Stroke 3: 竖弯钩 (no visible hook — blunt end) ---
# 顿 dab at start (shared with stroke 1's start visually)
dab(S3_START[0], S3_START[1], r_body + 1.5)
# Straight vertical descent
line_taper(S3_START, S3_VERT_END, r_body, r_body, steps=260)
# Tangent-continuous quarter arc: descending vertical -> rightward horizontal
# Using KEY PRIMITIVE from memory
cx, cy = S3_VERT_END[0], S3_VERT_END[1]
x0, y0 = S3_VERT_END
R = ARC_R
arc_steps = 120
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r_body)
# arc ends at (x0 + R, y0 + R) = S3_ARC_END
# Continue rightward as 横
line_taper(S3_ARC_END, S3_H_END, r_body, r_body + 0.8, steps=240)
# Blunt terminal press (no hook flick — GT shows blunt end)
dab(S3_H_END[0], S3_H_END[1], r_body + 1.8)


out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_053_己/01_己.png"
img.save(out_path)
print(f"Saved {out_path}")
