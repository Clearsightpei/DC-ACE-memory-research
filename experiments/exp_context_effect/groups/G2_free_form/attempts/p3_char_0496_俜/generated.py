"""
Render 俜 (ping1) at 300x300, black ink on white.

Structural read from GT:
  Left:  亻 (person radical) — 撇 (top-down-left sweep) + 竖 to about
         y=270, staying near the vertical center of the 甹 body.
  Right: 甹 = 由-like top box + long horizontal + 竖弯钩 sweeping right.

TIER-0 F 4-move: teardrop taper on 撇/点, shoulder dabs at 折 joints,
bezier for curved sweeps, hook flicks UP-and-LEFT.

Components MUST touch (TIER-0 H): 亻 竖 close to 甹's left edge, and
the top box connects to the lower horizontal via the middle 竖.
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


# ---------------- 亻 (left radical) ----------------
# 撇: from upper area, curving down-left, thick-to-thin
pie = bez((85, 55), (78, 100), (68, 145), (45, 195), n=80)
stroke(pie, (10, 4))

# 竖: from the belly of the 撇, straight down to ~y=265
shu_l = bez((80, 105), (80, 160), (80, 210), (80, 265), n=60)
stroke(shu_l, (8, 8))


# ---------------- 甹 (right component) ----------------
# --- top: 由-like box, sitting a bit higher ---
box_top = 45
box_bot = 130
box_l = 135
box_r = 250

# 竖 (left side of box)
stroke(bez((box_l, box_top), (box_l, box_top+30), (box_l, box_bot-30), (box_l, box_bot), n=40), (7, 7))

# 横 top + 折 corner + 竖 right side
stroke(bez((box_l, box_top), (170, box_top-2), (215, box_top-2), (box_r, box_top), n=40), (6, 7))
dab(box_r, box_top, 5)
stroke(bez((box_r, box_top), (box_r, box_top+30), (box_r, box_bot-30), (box_r, box_bot), n=40), (7, 6))

# middle horizontal (inside the box)
mid_y = (box_top + box_bot) // 2
stroke(bez((box_l, mid_y), (170, mid_y), (215, mid_y), (box_r, mid_y), n=40), (6, 6))

# center vertical inside box — extends down BELOW box to meet lower horizontal
cx = (box_l + box_r) // 2  # ~192
stroke(bez((cx, box_top), (cx, mid_y), (cx, box_bot), (cx, box_bot+20), n=40), (6, 6))

# bottom horizontal of box (closing it)
stroke(bez((box_l, box_bot), (170, box_bot), (215, box_bot), (box_r, box_bot), n=40), (6, 6))

# --- bottom of 甹: long horizontal + 竖折折钩 that sweeps right ---
# long horizontal (spans wider than the box, close to it)
lh_y = 165
stroke(bez((110, lh_y), (160, lh_y-2), (215, lh_y-2), (265, lh_y), n=60), (7, 7))

# vertical from left-of-center down
shu_r_x = 150
shu_r_bot = 245
stroke(bez((shu_r_x, lh_y), (shu_r_x, lh_y+30), (shu_r_x, shu_r_bot-20), (shu_r_x, shu_r_bot), n=50), (7, 7))
dab(shu_r_x, shu_r_bot, 5)

# curved sweep (竖弯) from bottom of 竖 rightward
sweep = bez((shu_r_x, shu_r_bot), (shu_r_x+20, shu_r_bot+15),
            (shu_r_x+60, shu_r_bot+18), (shu_r_x+95, shu_r_bot+5), n=60)
stroke(sweep, (7, 7))

# hook: UP-and-LEFT flick at the tail
tail_x, tail_y = shu_r_x + 95, shu_r_bot + 5
hook = bez((tail_x, tail_y), (tail_x-2, tail_y-12),
           (tail_x-6, tail_y-22), (tail_x-12, tail_y-30), n=30)
stroke(hook, (7, 3))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0496_俜/01_俜.png")
