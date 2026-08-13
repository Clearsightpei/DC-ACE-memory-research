"""
Render 俅 (qiu2) at 300x300, black ink on white.

Structural read from GT:
  Left  1/3: 亻 (single-person radical)
         - 撇 at top-left (short pie), starts at ~x=70,y=60
         - long 竖 straight down from upper-mid, ends near bottom
  Right 2/3: 求
         - top: small 点/tick + short horizontal near top
         - 竖钩 down center (with UP-LEFT hook flick)
         - 点 upper left of vertical
         - long 撇 sweeping down-left from mid-upper
         - long 捺 sweeping down-right from mid
         - small 点 lower right
Applies TIER-0-F: teardrop taper via stroke(), bezier for curves,
hook flicks UP-and-LEFT.
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


# =========== LEFT: 亻 ===========
# 撇 — short pie at top of 亻
pie = bez((85, 55), (75, 90), (65, 120), (55, 155), n=60)
stroke(pie, (10, 4))

# 竖 — long vertical, starts near top-middle of 亻 (right of pie tail)
ren_v = bez((85, 90), (85, 160), (85, 220), (85, 275), n=60)
stroke(ren_v, (8, 8))


# =========== RIGHT: 求 ===========
# 1) 横 — top horizontal (spans width of 求)
h_top = bez((155, 85), (185, 80), (220, 80), (255, 85), n=50)
stroke(h_top, (7, 6))

# 2) small tick at top-right of the 横 (upward-right point)
top_tick = bez((250, 82), (256, 76), (260, 70), (264, 64), n=20)
stroke(top_tick, (6, 3))

# 3) 竖钩 — vertical hook down the center of right side
zg = bez((205, 90), (205, 150), (205, 210), (205, 252), n=60)
stroke(zg, (8, 7))
# hook flick UP-and-LEFT (into character body)
hook = bez((205, 252), (199, 246), (192, 238), (184, 230), n=30)
stroke(hook, (7, 3))

# 4) 点 — upper-left dot of 求
p_upper_left = bez((165, 115), (160, 122), (156, 130), (152, 138), n=30)
stroke(p_upper_left, (4, 8))

# 5) 撇 — long sweeping pie from upper-right area down to lower-left
long_pie = bez((222, 128), (198, 172), (168, 212), (135, 260), n=80)
stroke(long_pie, (10, 3))

# 6) 捺 — long sweeping na from mid down to lower-right
na = bez((215, 152), (232, 188), (250, 218), (270, 250), n=80)
stroke(na, (4, 12))
# small foot flare
na_foot = bez((270, 250), (275, 252), (280, 253), (283, 254), n=15)
stroke(na_foot, (12, 3))

# 7) small 点 — lower-right dot of 求 (small, below/right of hook end)
p_lower_right = bez((240, 200), (247, 210), (252, 220), (255, 228), n=25)
stroke(p_lower_right, (4, 8))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0476_俅/01_俅.png")
