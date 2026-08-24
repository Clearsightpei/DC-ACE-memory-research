"""
Render 俛 (fu3/mian3) at 300x300, black ink on white.

Structural read from GT:
  Left:  亻 (person radical) — 撇 (small pie at top) + long 竖 (vertical)
  Right: 免 — top pie + 横折钩 forming the top of a small box,
             left 竖, middle 一, then 儿 legs (撇 + 竖弯钩).
             The 竖弯钩 hooks UP-and-LEFT per TIER-0 rule B.

TIER-0 apply:
  - Components touch: the 亻 竖 sits close to the 免 left edge so
    strokes nearly overlap.
  - Taper on every 撇/捺/点 via stroke(pts, (w0, w1)).
  - Bezier for every curved sweep.
  - Hook flick UP-and-LEFT on the 竖弯钩 of 儿.
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

# =====================================================================
# 亻 radical, left side (columns ~55..95)
# =====================================================================
# 撇: small pie at top, curves down-left slightly
pie = bez((90, 60), (84, 85), (74, 110), (60, 130), n=60)
stroke(pie, (9, 4))

# 竖: long vertical from just under the pie's start; ends near 免 baseline
shu = bez((90, 100), (88, 160), (87, 210), (87, 245), n=60)
stroke(shu, (8, 8))

# =====================================================================
# 免, right side (columns ~110..260)
# =====================================================================
# 1) top 撇 (small flick, meets the top-left corner of the box)
top_pie = bez((160, 42), (150, 55), (142, 65), (135, 75), n=40)
stroke(top_pie, (8, 3))

# 2) 横折钩 top box:
#    horizontal from just under the pie's end to right,
#    then a fold down (this is actually a 横折 forming the top+right of the small hat/box)
box_top = bez((135, 75), (170, 72), (205, 72), (235, 75), n=50)
stroke(box_top, (6, 6))
shoulder(235, 75)
box_right = bez((235, 75), (233, 95), (231, 115), (230, 130), n=40)
stroke(box_right, (6, 6))

# 3) 竖 left side of box, starting from where 横 begins
box_left = bez((135, 75), (135, 100), (135, 120), (135, 135), n=40)
stroke(box_left, (6, 6))

# 4) 一 middle horizontal (the mouth 口 middle bar)
mid_h = bez((138, 105), (170, 103), (200, 103), (228, 105), n=40)
stroke(mid_h, (5, 5))

# 5) 一 bottom of the box (closes 口)
box_bot = bez((138, 135), (170, 133), (200, 133), (230, 133), n=40)
stroke(box_bot, (6, 6))

# =====================================================================
# 儿 bottom legs of 免
# =====================================================================
# 6) 撇: left leg, curves down-left
left_leg = bez((155, 145), (140, 180), (125, 215), (110, 255), n=60)
stroke(left_leg, (8, 3))

# 7) 竖弯钩: right leg — starts vertical, curves right across the bottom,
#    ends with a hook flick UP-and-LEFT
sv_down = bez((200, 145), (200, 175), (200, 205), (205, 230), n=50)
stroke(sv_down, (7, 7))
# curve rightwards
sv_arc = bez((205, 230), (215, 250), (235, 258), (255, 258), n=50)
stroke(sv_arc, (7, 7))
# hook flick UP-and-LEFT (~ -110°)
hook = bez((255, 258), (253, 248), (249, 236), (243, 224), n=30)
stroke(hook, (7, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0494_俛/01_俛.png")
