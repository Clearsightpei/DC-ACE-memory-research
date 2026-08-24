"""
Render 疸 (dan3, jaundice) at 300x300, black ink on white.

Composition: 疒 (canopy, 5 strokes) + 旦 (day, 5 strokes) = 10 strokes.

Frozen-cohort 疒 recipe (from frozen_cohort.md):
  (1) 点 top-left of 一
  (2) 横 long top spanning radical width
  (3) LONG curved 撇 from right end of 横 to bottom-left (dominant)
  (4) inner 点 below 横 right of 撇
  (5) 提 rising short flick BELOW the inner 点

TIER-0 H rule: 旦 must be tucked INSIDE the canopy's 撇 sweep, touching.

# SIGNATURE CHECK: 疒 = 5 strokes (NOT 3 as 广). Inner 点+提 pair mandatory.
Calligraphic-weight moves applied: bez arcs, teardrop taper, shoulder dab.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def shoulder_dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============ 疒 canopy (5 strokes) ============

# (1) 点 top-left dot
p1 = bez((62, 42), (68, 52), (72, 62), (76, 72), n=25)
stroke(p1, (3, 8))

# (2) 横 top spanning radical width — starts just right of the 点
h_top = bez((78, 78), (130, 76), (185, 76), (225, 80), n=50)
stroke(h_top, (5, 6))
shoulder_dab(225, 80, r=6)  # shoulder for the 撇 that starts here

# (3) LONG dominant 撇 from right end of 横 curving fast down-left
pie = bez((225, 80), (140, 135), (80, 195), (35, 268), n=100)
stroke(pie, (11, 4))

# (4) inner 点 below 横, right of 撇 (small dab)
inner_dot = bez((93, 108), (98, 116), (102, 122), (105, 130), n=20)
stroke(inner_dot, (3, 8))

# (5) 提 rising flick BELOW the inner 点 (goes up-right)
ti = bez((72, 152), (92, 145), (110, 140), (128, 137), n=30)
stroke(ti, (8, 3))


# ============ 旦 body (5 strokes) — tucked inside canopy, bottom-right ============
# 日 box: 竖 left, 横折 top+right, 横 middle, 横 bottom
# Shifted right so it sits INSIDE the canopy, not crossed by 撇

BX0, BX1 = 140, 235   # box left/right
BY0, BY1 = 130, 225   # box top/bottom

# left 竖 of 日
zh = bez((BX0, BY0), (BX0, 158), (BX0, 195), (BX0, BY1), n=50)
stroke(zh, (7, 7))

# 横折: top 横 then turn to right 竖
h_top2 = bez((BX0, BY0), (170, BY0 - 2), (205, BY0 - 2), (BX1, BY0 + 2), n=50)
stroke(h_top2, (5, 6))
shoulder_dab(BX1, BY0 + 2, r=6)
zr = bez((BX1, BY0 + 2), (BX1, 158), (BX1, 195), (BX1, BY1), n=50)
stroke(zr, (7, 7))

# middle 横 (日's crossbar)
h_mid = bez((BX0 + 2, 178), (170, 176), (205, 176), (BX1 - 2, 178), n=40)
stroke(h_mid, (5, 5))

# bottom 横 closing the box
h_bot = bez((BX0 + 2, BY1), (170, BY1 - 1), (205, BY1 - 1), (BX1 - 2, BY1), n=40)
stroke(h_bot, (5, 5))

# 一 base line of 旦 — spanning across the bottom, extending under the canopy
h_base = bez((70, 262), (140, 260), (210, 260), (265, 264), n=60)
stroke(h_base, (5, 7))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0524_疸/01_疸.png")
