"""
Render 拿 (ná) at 300x300, black ink on white.

Structural read from GT:
  Top: 合 = 人-apex (撇+捺) + 一 (short horizontal) + 口 (small box)
  Bottom: 手 = short 撇 + horizontal(s) + long crossbar 一 + 竖钩 (UP-LEFT flick)

Applies TIER-0 F (4-move): bezier curves, teardrop tapers, hook up-left.
Components-touch rule H: 口 sits tucked under the 人 apex; 手 body starts
just below 口.
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

# ---------- Top: 合 ----------
# 人 apex — 撇 (top-center down-left), thin at tail
pie_top = bez((150, 20), (135, 55), (100, 90), (45, 130), n=80)
stroke(pie_top, (12, 4))

# 人 apex — 捺 (top-center down-right, thick at tail with foot)
na_top = bez((150, 30), (180, 70), (215, 105), (255, 130), n=80)
stroke(na_top, (5, 13))
foot_top = bez((255, 130), (261, 132), (267, 134), (271, 135), n=20)
stroke(foot_top, (13, 4))

# 一 (short horizontal under the apex, forming 合's middle band)
h_mid = bez((78, 138), (130, 136), (170, 136), (222, 140), n=40)
stroke(h_mid, (6, 6))

# 口 (small box tucked under the 一)
# top of 口 is the 一 line above, but 口 has its own top short horizontal + verticals + bottom
# left vertical (short)
lv = bez((108, 148), (108, 170), (108, 185), (108, 195), n=30)
stroke(lv, (6, 6))
# right vertical (short, ends with slight foot right)
rv = bez((196, 148), (196, 170), (196, 185), (196, 195), n=30)
stroke(rv, (6, 6))
# bottom of 口 (横)
h_box_bot = bez((108, 193), (145, 193), (170, 193), (196, 193), n=30)
stroke(h_box_bot, (6, 6))
# top-left short cap of 口 (small overlap to make box read)
h_box_top = bez((108, 148), (140, 147), (170, 147), (196, 148), n=30)
stroke(h_box_top, (5, 5))

# ---------- Bottom: 手 ----------
# short 撇 (upper-left flick at top of 手)
pie_hand = bez((160, 200), (145, 210), (130, 218), (110, 225), n=40)
stroke(pie_hand, (7, 3))

# 一 (upper short horizontal of 手)
h1 = bez((115, 224), (150, 222), (185, 222), (215, 226), n=40)
stroke(h1, (6, 6))

# 一 (middle horizontal — the wide crossbar of 手)
h2 = bez((55, 253), (130, 251), (180, 251), (245, 255), n=60)
stroke(h2, (7, 7))

# 竖钩 (center vertical through the crossbars, ends with UP-LEFT hook)
sg = bez((152, 205), (152, 245), (152, 275), (152, 288), n=60)
stroke(sg, (8, 8))
# shoulder dab at hook base
d.ellipse((152 - 5.5, 288 - 5.5, 152 + 5.5, 288 + 5.5), fill="black")
# hook flick UP-and-LEFT (TIER-0 rule B)
hook = bez((152, 288), (146, 282), (140, 275), (132, 268), n=25)
stroke(hook, (8, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0559_拿/01_拿.png")
