"""
Render 阝 (radical, 2画) to 300x300 PNG. Retry #1.

Prior attempt failure: ear was drawn as double-humped "3" with the 竖
disconnected. GT shows a clean P-shape ear (single closed lobe) with
the 竖 continuing DOWN from the ear's bottom-left joint.

阝 has 2 strokes officially:
  Stroke 1: 横撇弯钩 — starts with a small 横, folds down and forms
    a closed round-ish lobe (belly on the RIGHT) that closes back
    at the vertical axis. Think of a capital "P" bowl.
  Stroke 2: 竖 — long vertical from the top of the ear joint,
    passing through the ear-closure point, extending well below.

The GT's ear looks like a bumpy P-lobe (belly right), and the 竖 is
one continuous vertical.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = max(40, int(math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# Spine (vertical axis) for the ear at x ≈ 118
SPINE_X = 118
EAR_TOP_Y = 78
EAR_BOTTOM_Y = 168

# ---------- STROKE 1: 横撇弯钩 (ear as a single P-lobe) ----------
# a) small 横: from spine top going right
line_dabs(SPINE_X, EAR_TOP_Y, SPINE_X + 42, EAR_TOP_Y - 4, 6, 6, steps=140)
dab(SPINE_X, EAR_TOP_Y, 7)              # 顿笔 start
dab(SPINE_X + 42, EAR_TOP_Y - 4, 7.5)   # 折 shoulder

# b) P-lobe: from shoulder curve out-and-down (belly on the right)
# Control the right belly around x=178, then curl back to spine at bottom
# First half of arc: down-right to rightmost belly
bezier_dabs(
    p0=(SPINE_X + 42, EAR_TOP_Y - 4),
    p1=(SPINE_X + 78, EAR_TOP_Y + 22),
    p2=(SPINE_X + 68, EAR_TOP_Y + 55),
    r0=6.0, r1=5.5,
    steps=200,
)
# Second half of arc: from belly back to spine at ear-bottom
bezier_dabs(
    p0=(SPINE_X + 68, EAR_TOP_Y + 55),
    p1=(SPINE_X + 50, EAR_TOP_Y + 82),
    p2=(SPINE_X, EAR_BOTTOM_Y - 78),
    r0=5.5, r1=5.5,
    steps=200,
)
# Small hook flick UP-and-LEFT (canonical 钩 direction)
bezier_dabs(
    p0=(SPINE_X, EAR_BOTTOM_Y - 78),
    p1=(SPINE_X - 4, EAR_BOTTOM_Y - 82),
    p2=(SPINE_X - 10, EAR_BOTTOM_Y - 88),
    r0=5.5, r1=3.5,
    steps=80,
)

# ---------- STROKE 2: 竖 (long vertical) ----------
# From ear-top joint straight down through the ear-closure and past
line_dabs(SPINE_X, EAR_TOP_Y + 2, SPINE_X, 258, 7, 7.5, steps=400)
dab(SPINE_X, EAR_TOP_Y + 2, 7.5)   # top 顿笔
dab(SPINE_X, 258, 8)               # bottom press (blunt)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_020_阝__retry_1/01_阝.png"
img.save(out_path)
print(f"Saved: {out_path}")
