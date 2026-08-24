"""
Render 能 (neng2) at 300x300, black ink on white.

Structural read from GT — 4 quadrants, roughly:
  UL (~x 30-135, y 45-125):   厶 (small — 撇折 + 点)
  BL (~x 30-140, y 135-275):  月 (tall — 撇 + 横折钩 + two horizontals)
  UR (~x 155-275, y 55-135):  匕 (撇 + 竖弯钩, small)
  BR (~x 155-275, y 145-275): 匕 (撇 + 竖弯钩, tall — hook flicks UP-LEFT)

COMPONENTS MUST TOUCH (tier-0 rule H): left column body ~140,
right column body starts ~155, minimal gap; UL/BL vertical stack
sits within left column; UR/BR sit within right column.

Sibling-row for 匕 (tier-0 D): 匕's 竖弯钩 crosses the 撇 above the
midpoint of 撇; hook flicks UP-and-LEFT into the character body.
Applied TWICE — once per 匕.

Calligraphic 4-move (tier-0 F): bez helpers, variable-width tapers,
shoulder dabs at 折 joints, hook flick per rule B.
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


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============ UL: 厶 (small, upper-left) ============
# stroke 1: 撇折 — starts upper-right of 厶, sweeps down-left, then flat right
pie_ul = bez((100, 55), (85, 78), (65, 100), (48, 118), n=60)
stroke(pie_ul, (7, 4))
zhe_ul = bez((48, 118), (70, 118), (95, 118), (120, 120), n=40)
stroke(zhe_ul, (5, 5))
dab(48, 118, 4)  # shoulder dab at fold
# stroke 2: 点 at upper part of the curve
pt_ul = bez((115, 95), (122, 100), (128, 108), (128, 118), n=25)
stroke(pt_ul, (4, 8))


# ============ UR: 匕 (upper-right, small) ============
# stroke 1: 撇 — from top going down-left, slight curve
pie_ur = bez((215, 55), (200, 80), (180, 100), (162, 115), n=60)
stroke(pie_ur, (8, 4))
# stroke 2: 竖弯钩 — starts a bit above center of 撇, down, arc right, hook UP-LEFT
sw_ur_v = bez((200, 78), (198, 100), (198, 120), (205, 130), n=40)
stroke(sw_ur_v, (7, 7))
sw_ur_h = bez((205, 130), (225, 132), (250, 130), (272, 122), n=40)
stroke(sw_ur_h, (7, 7))
# hook flick UP-and-LEFT
hook_ur = bez((272, 122), (268, 112), (263, 102), (258, 92), n=25)
stroke(hook_ur, (7, 3))


# ============ BL: 月 (bottom-left, tall) ============
# stroke 1: 撇 — left side, from upper-right of 月, sweeps down-left
pie_bl = bez((85, 145), (75, 175), (60, 220), (40, 268), n=70)
stroke(pie_bl, (9, 5))
# stroke 2: 横折钩 — top: horizontal, corner, down long, hook UP-LEFT
h_bl = bez((85, 145), (105, 143), (125, 143), (140, 145), n=40)
stroke(h_bl, (6, 7))
dab(140, 148, 5)  # shoulder dab at fold
v_bl = bez((140, 148), (140, 190), (140, 235), (140, 268), n=50)
stroke(v_bl, (7, 7))
hook_bl = bez((140, 268), (132, 262), (124, 256), (118, 250), n=25)
stroke(hook_bl, (7, 3))
# two inner horizontals (short)
ih1 = bez((70, 190), (90, 189), (115, 189), (135, 190), n=35)
stroke(ih1, (5, 5))
ih2 = bez((60, 230), (85, 229), (115, 229), (137, 230), n=35)
stroke(ih2, (5, 5))


# ============ BR: 匕 (bottom-right, tall) ============
# stroke 1: 撇 — from top going down-left
pie_br = bez((220, 148), (205, 180), (185, 215), (162, 245), n=70)
stroke(pie_br, (9, 4))
# stroke 2: 竖弯钩 — down long, arc right, hook UP-LEFT
sw_br_v = bez((205, 175), (203, 210), (203, 240), (210, 258), n=50)
stroke(sw_br_v, (8, 8))
sw_br_h = bez((210, 258), (230, 262), (255, 258), (275, 248), n=40)
stroke(sw_br_h, (8, 8))
# hook flick UP-and-LEFT
hook_br = bez((275, 248), (270, 235), (264, 222), (258, 210), n=30)
stroke(hook_br, (8, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0499_能/01_能.png")
