"""
Render 癸 (gui3) at 300x300 — revised.
癸 = 癶 (top) + 天-ish bottom. 9 strokes.

Revision notes vs pass 1:
  - crossbar 一 was too long/dominant, making body look like a ring.
    Shortened + the 撇/捺 legs now originate ABOVE the crossbar
    and pierce through it (matches GT).
  - top 癶 needs stronger left/right separation.
  - use taper + Bezier per v7.5 4-move.
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


# ============= TOP: 癶 (roughly y=35..140) =============
# LEFT half: big 竖撇 starting upper-mid-left, sweeping down-left with belly
left_pie = bez((115, 45), (108, 85), (85, 115), (48, 150), n=70)
stroke(left_pie, (11, 4))
# small companion 点 to the right of the top of left stem
dot1 = bez((128, 78), (135, 88), (141, 98), (144, 106), n=25)
stroke(dot1, (4, 8))

# RIGHT half: short 撇 upper on the right
right_pie_top = bez((188, 55), (183, 72), (178, 88), (170, 105), n=30)
stroke(right_pie_top, (7, 3))
# little 提/short horizontal cap
short_cap = bez((195, 75), (208, 72), (218, 72), (225, 75), n=25)
stroke(short_cap, (4, 4))
# RIGHT main 捺 sweeping wide down-right (dominant right diagonal)
right_na = bez((175, 65), (200, 100), (230, 130), (262, 155), n=80)
stroke(right_na, (5, 13))
tail1 = bez((262, 155), (268, 157), (273, 158), (277, 158), n=15)
stroke(tail1, (13, 3))

# ============= MIDDLE: short 一 crossbar (shorter than pass 1) =============
h_mid = bez((85, 165), (140, 162), (200, 162), (240, 168), n=50)
stroke(h_mid, (6, 6))

# ============= BOTTOM: 撇 + 捺 legs (originate above crossbar, pierce through) =============
# left leg 撇 — starts above crossbar near center, sweeps down-left through it
bot_pie = bez((148, 145), (128, 190), (100, 230), (65, 275), n=80)
stroke(bot_pie, (10, 4))

# right leg 捺 — starts above crossbar near center, sweeps down-right
bot_na = bez((152, 150), (180, 195), (210, 235), (245, 275), n=80)
stroke(bot_na, (5, 12))
bot_tail = bez((245, 275), (252, 277), (257, 278), (261, 278), n=15)
stroke(bot_tail, (12, 3))

# small final 点 hanging near center-right below crossbar
last_dot = bez((168, 210), (176, 225), (183, 240), (188, 250), n=25)
stroke(last_dot, (4, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0458_癸/01_癸.png")
