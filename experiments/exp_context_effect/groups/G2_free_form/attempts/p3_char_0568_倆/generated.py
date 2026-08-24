"""
Render 倆 (liǎ) at 300x300, black ink on white.
Compound: 亻 (left) + 兩 (right).

# SIGNATURE CHECK:
# - 亻: 撇 (top-right to bottom-left) + 竖 starting mid-撇, straight down.
#   Components MUST TOUCH (H rule): 亻竖 tucks under 兩 top horizontal.
# - 兩: 一 (top wide 横) + 冂 (left 竖 + 横折钩 with UP-LEFT hook flick)
#   + two 入 shapes inside (从-like pair).
# - Hook flick on 横折钩 = UP-and-LEFT (~-110°) INTO body (TIER-0 B).
# Apply calligraphic-weight 4-move: taper, shoulder dab, bezier, hook flick.
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


def shoulder(x, y, r=5.5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ==== 亻 (left, x ~ 40..95) ====
# 撇: top-center-left, sweep down-left, thin at tail
pie_ren = bez((90, 65), (80, 105), (65, 135), (45, 175), n=70)
stroke(pie_ren, (10, 4))

# 竖: straight vertical starting from mid-撇
sh_ren = bez((78, 100), (78, 155), (78, 210), (78, 255), n=60)
stroke(sh_ren, (7, 7))


# ==== 兩 (right, x ~ 110..275) ====
# Top 一: wide horizontal
h_top = bez((115, 80), (170, 78), (230, 78), (275, 82), n=60)
stroke(h_top, (7, 7))

# Left 竖 of 冂 (starts just under the 一)
sh_left = bez((132, 95), (132, 150), (132, 210), (132, 260), n=60)
stroke(sh_left, (7, 6))

# 横折钩 (top horizontal + right vertical with UP-LEFT hook)
# top horizontal a bit lower than 一
h_zh = bez((132, 110), (185, 108), (240, 108), (268, 112), n=60)
stroke(h_zh, (6, 7))
# shoulder dab at fold
shoulder(268, 112, r=5.5)
# right vertical down
sh_right = bez((268, 112), (268, 170), (268, 220), (265, 258), n=60)
stroke(sh_right, (7, 7))
# hook flick UP-and-LEFT into body
hook = bez((265, 258), (258, 254), (250, 248), (243, 240), n=25)
stroke(hook, (7, 3))

# ==== Inside 兩: two 入-like elements ====
# Left 入
l_pie = bez((175, 140), (170, 175), (163, 210), (155, 245), n=55)
stroke(l_pie, (7, 3))
l_na = bez((175, 140), (183, 175), (192, 210), (200, 245), n=55)
stroke(l_na, (3, 7))

# Right 入
r_pie = bez((230, 140), (225, 175), (218, 210), (210, 245), n=55)
stroke(r_pie, (7, 3))
r_na = bez((230, 140), (238, 175), (247, 210), (255, 245), n=55)
stroke(r_na, (3, 7))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0568_倆/01_倆.png")
