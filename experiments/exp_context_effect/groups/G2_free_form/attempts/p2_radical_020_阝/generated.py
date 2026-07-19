"""
Render 阝 (radical, 2画) to 300x300 PNG.

阝 is the "左耳旁 / 右耳旁" ear radical (officially 2 strokes):

Stroke 1: 横撇弯钩 (heng-pie-wan-gou) — the "ear" at the top.
  In standard MMH rendering this reads as a distinctive DOUBLE-LOBED
  squiggle, not a plain half-circle "P":
    a) small 横 top going right
    b) 折 shoulder, then down-and-left (small 撇-ish inward tuck)
    c) then out to the right forming the lower lobe (belly right)
    d) curl back leftward and slightly upward — the 弯钩 tail
  Visually reminiscent of a small "3" or "ε" laid on its back.

Stroke 2: 竖 — long vertical descending from the joint at the bottom
  of the ear, ending in a blunt press.

Uses PIL brush-dab technique per drawer_memory.md.

Revision 1: added the double-lobe zigzag character of the ear.
"""

from PIL import Image, ImageDraw
import math
import os

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


# ---------- STROKE 1: 横撇弯钩 (ear, double-lobed) ----------
# All coordinates image-coords (y grows DOWN).
#
# Path plan:
#   P0 (110, 88)  — 顿笔 start of small 横
#   P1 (160, 82)  — top-right corner, 折 shoulder press
#   P2 (135, 118) — inward tuck (top of the ear's inner bay, first lobe base)
#   P3 (175, 135) — bulge back out to the right (belly of second lobe)
#   P4 (118, 158) — end at the joint with 竖 (hooks back inward)
#
# Rendered as: line P0->P1 (小 横), then Bezier P1->P2 via ctrl (170,105),
# then Bezier P2->P3 via ctrl (170,125), then Bezier P3->P4 via ctrl (170,158).

# (a) small 横 top of the ear
line_dabs(110, 88, 160, 82, 5.5, 5.5, steps=140)
dab(110, 88, 7)     # 顿笔 start
dab(160, 82, 7.5)   # 折 shoulder press

# (b) first curve: from corner down-and-left to inner tuck
bezier_dabs(
    p0=(160, 82),
    p1=(170, 105),
    p2=(135, 118),
    r0=5.5, r1=5.0,
    steps=160,
)

# (c) second curve: from inner tuck out-and-down forming lower lobe belly
bezier_dabs(
    p0=(135, 118),
    p1=(178, 128),
    p2=(170, 148),
    r0=5.0, r1=5.0,
    steps=160,
)

# (d) closing curve: from lower-lobe belly back leftward and down to joint
bezier_dabs(
    p0=(170, 148),
    p1=(150, 162),
    p2=(118, 158),
    r0=5.0, r1=4.5,
    steps=160,
)

# small terminal flick (the 钩 nub of 横撇弯钩) — a tiny leftward taper
line_dabs(118, 158, 108, 155, 4.5, 2.0, steps=60)

# joining dab at the joint where 竖 will begin
dab(118, 158, 6.5)


# ---------- STROKE 2: 竖 (long vertical) ----------
# From joint (118, 158) straight down to (118, 262).
# Uniform width, blunt press at both ends.
line_dabs(118, 158, 118, 262, 5.5, 5.5, steps=340)
dab(118, 158, 7.5)   # start press (loaded beginning)
dab(118, 262, 6.5)   # end blunt press


out_path = os.path.join(os.path.dirname(__file__), "01_阝.png")
img.save(out_path)
print(f"Wrote {out_path}")
