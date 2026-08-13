"""
Render 疽 (ju1) at 300x300, black ink on white.

# SIGNATURE CHECK: 疒 canopy = 5 STROKES (not 广 = 3). Missing 点 + 提
# pair is the #1 fail mode per frozen_cohort.md (7x in B12).
# Components MUST touch (TIER-0 H): 且 must be tucked INSIDE the 撇 sweep,
# with left 竖 overlapping the canopy interior, not detached under it.
#
# Structure (frozen_cohort 疒 row):
#   S1: 点 top-left (small dot above the 一)
#   S2: 横 long top spanning canopy width
#   S3: LONG curved 撇 from right end of 横 down to bottom-left (identity)
#   S4: inner 点 below 横, left of 撇-body (short down-right)
#   S5: 提 short rising flick BELOW inner 点
# 且 inside (5 strokes):
#   竖 (left), 横折 (top+right vertical), mid横, mid横, bottom横 (extends)
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


def shoulder(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============= 疒 canopy =============
# S1: 点 top-left — small down-right dot above the horizontal
s1 = bez((72, 42), (78, 52), (84, 62), (90, 72), n=30)
stroke(s1, (3, 8))

# S2: 横 long top — spans the canopy width, thin flat rise
s2 = bez((55, 82), (110, 80), (170, 80), (215, 84), n=60)
stroke(s2, (6, 6))

# S3: LONG curved 撇 — from just LEFT of right end of 横, curves down-left
# to bottom-left. Identity-carrying, must dominate.
s3 = bez((150, 82), (120, 130), (85, 185), (32, 265), n=100)
stroke(s3, (11, 4))

# S4: inner 点 — small dot below 横, left interior of canopy (down-right)
s4 = bez((62, 108), (68, 118), (74, 128), (80, 138), n=30)
stroke(s4, (3, 7))

# S5: 提 — short rising flick BELOW inner 点 (up-and-right)
s5 = bez((52, 168), (65, 162), (78, 155), (92, 148), n=30)
stroke(s5, (7, 3))

# ============= 且 inside canopy (right-lower area, tucked under 撇) =============
# Layout: rectangle-like frame with 2 internal horizontals and an extending
# bottom base. Position so left 竖 sits inside the canopy, right 竖 at ~230.
LEFT_X = 118
RIGHT_X = 232
TOP_Y = 108
BOT_Y = 258

# Left 竖: vertical down
sL = bez((LEFT_X, TOP_Y), (LEFT_X, TOP_Y + 45),
         (LEFT_X, TOP_Y + 100), (LEFT_X, BOT_Y), n=60)
stroke(sL, (6, 6))

# 横折: top horizontal + right vertical as one folded stroke
top_h = bez((LEFT_X, TOP_Y), (LEFT_X + 35, TOP_Y - 2),
            (RIGHT_X - 35, TOP_Y - 2), (RIGHT_X, TOP_Y), n=60)
stroke(top_h, (6, 6))
shoulder(RIGHT_X, TOP_Y, r=5)  # shoulder dab at 折 joint
right_v = bez((RIGHT_X, TOP_Y), (RIGHT_X, TOP_Y + 45),
              (RIGHT_X, TOP_Y + 100), (RIGHT_X, BOT_Y), n=60)
stroke(right_v, (7, 7))

# Mid 横 1
mid1_y = TOP_Y + 50
m1 = bez((LEFT_X, mid1_y), (LEFT_X + 35, mid1_y - 1),
         (RIGHT_X - 35, mid1_y - 1), (RIGHT_X, mid1_y), n=50)
stroke(m1, (5, 5))

# Mid 横 2
mid2_y = TOP_Y + 100
m2 = bez((LEFT_X, mid2_y), (LEFT_X + 35, mid2_y - 1),
         (RIGHT_X - 35, mid2_y - 1), (RIGHT_X, mid2_y), n=50)
stroke(m2, (5, 5))

# Bottom 横 — extends slightly beyond both verticals
bot = bez((LEFT_X - 8, BOT_Y), (LEFT_X + 40, BOT_Y - 2),
          (RIGHT_X - 40, BOT_Y - 2), (RIGHT_X + 8, BOT_Y), n=60)
stroke(bot, (6, 7))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0528_疽/01_疽.png")
