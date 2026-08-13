"""
Render 值 (zhi2) at 300x300, black ink on white.

Structural read from GT:
  Left: 亻 — 撇 from top-center-left sweeping down-left, then 竖 down.
        亻 竖 must touch/reach into right component's territory (TIER-0 H).
  Right: 直 — top short 横, 竖 through 十, 目 box (2 vert + 4 horiz),
         bottom 一 extending under the box.

# SIGNATURE CHECK (亻 as component, per TIER-0 D):
# - 撇 sweeps down-left from a start ABOVE where the 竖 begins.
# - 竖 is straight, no hook, terminates as suspended vertical.
# - 亻 竖 touches or overlaps the right component's leftmost stroke.

Uses bez() + stroke() teardrop-taper pattern per TIER-0 F.
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


# ============== LEFT: 亻 ==============
# 撇 — starts high, sweeps down-left with taper, curved bow
pie = bez((85, 55), (75, 100), (60, 135), (40, 175), n=70)
stroke(pie, (10, 4))

# 竖 — vertical from mid-upper down (starts inside the 撇 body)
# extended to reach body-bottom per GT
shu = bez((78, 88), (82, 150), (86, 215), (90, 265), n=60)
stroke(shu, (7, 7))

# ============== RIGHT: 直 ==============
# top short 横 (top of 十) — extends to overlap left-vert of 目
h_top = bez((120, 68), (170, 63), (215, 63), (255, 68), n=40)
stroke(h_top, (6, 6))

# 竖 through 十 into 目 (straight vertical, integrated)
shu2 = bez((190, 55), (190, 100), (190, 155), (190, 210), n=60)
stroke(shu2, (6, 6))

# 目 box — LEFT vertical
left_v = bez((140, 100), (140, 145), (140, 185), (140, 220), n=60)
stroke(left_v, (6, 6))

# 目 box — RIGHT vertical with slight bend at top (横折)
# horizontal-top of 目 first
h_box_top = bez((140, 100), (185, 100), (225, 100), (245, 103), n=40)
stroke(h_box_top, (6, 6))
# shoulder dab at top-right corner
shoulder(245, 103, r=5)
# right vertical descending
right_v = bez((245, 103), (245, 145), (245, 185), (245, 220), n=60)
stroke(right_v, (6, 6))

# middle horizontal 1 (upper of the two internal)
h_mid1 = bez((145, 145), (180, 144), (215, 144), (240, 145), n=40)
stroke(h_mid1, (5, 5))

# middle horizontal 2 (lower of the two internal)
h_mid2 = bez((145, 185), (180, 184), (215, 184), (240, 185), n=40)
stroke(h_mid2, (5, 5))

# bottom horizontal closing 目
h_box_bot = bez((140, 220), (180, 220), (215, 220), (245, 220), n=40)
stroke(h_box_bot, (5, 5))

# bottom 一 — extending underline (wider than 目 box)
h_under = bez((100, 250), (150, 248), (210, 248), (265, 252), n=50)
stroke(h_under, (7, 7))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0533_值/01_值.png")
