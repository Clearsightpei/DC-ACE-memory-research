"""
Render 起 at 300x300, black on white.

# SIGNATURE CHECK: 己 (component in upper-right) — three strokes
#   1) 横折 (horiz top + vertical drop on right)
#   2) 横 (middle horizontal to right wall)
#   3) 竖弯钩 (left vertical, then sweep right, then UP-LEFT flick)
#   Distinguish 己 from 已/巳: opening at TOP-LEFT of the box (the
#   middle 横 does NOT reach the left wall — it starts inside).

Structure:
  LEFT/CENTER: 走 compressed on the left. 土 (3 strokes) on top,
    then short 横 + 撇 + long sweeping 捺 (goes UNDER 己).
  UPPER-RIGHT: 己 (3 strokes).
Components MUST touch (TIER-0 H): the 走's 捺 sweeps under and past 己.
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


def line_stroke(p0, p1, widths, n=40):
    pts = bez(p0,
              (p0[0] + (p1[0]-p0[0])/3, p0[1] + (p1[1]-p0[1])/3),
              (p0[0] + 2*(p1[0]-p0[0])/3, p0[1] + 2*(p1[1]-p0[1])/3),
              p1, n=n)
    stroke(pts, widths)


def shoulder(cx, cy, r=6):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ============ LEFT/CENTER: 走 (7 strokes) ============
# 土 on top
# 1) short 横 (top of 土)
line_stroke((55, 62), (118, 62), (6, 6))
# 2) 竖 (of 土)
line_stroke((88, 50), (88, 118), (7, 7))
# 3) longer 横 (bottom of 土)
line_stroke((38, 120), (145, 122), (7, 7))

# lower 走 half (4 strokes: 横 竖 撇 捺):
# 4) short 横 (middle) — sits just below 土
line_stroke((55, 160), (128, 158), (6, 6))
# 5) short 竖 — dropping from center of the mid 横
line_stroke((90, 158), (90, 188), (6, 6))
# 6) 撇 — from the crossing, sweeping down-left, tapering
pie = bez((90, 182), (72, 210), (55, 232), (25, 258), n=70)
stroke(pie, (10, 3))
# 7) 捺 — long sweeping under-stroke; from the crossing sweeping
#    down and RIGHT, flattening to a foot flare (passes UNDER 己).
na = bez((92, 186), (145, 230), (205, 258), (258, 262), n=90)
stroke(na, (5, 14))
# foot flare
foot = bez((258, 262), (266, 262), (273, 260), (280, 257), n=25)
stroke(foot, (14, 4))

# ============ UPPER-RIGHT: 己 (3 strokes) ============
# 1) 横折 — horizontal top then vertical drop (shoulder at corner)
line_stroke((175, 70), (258, 68), (6, 6))
shoulder(258, 70, r=4)
line_stroke((258, 70), (258, 112), (6, 6))
# 2) middle 横 (does NOT touch left wall — 己 opens top-left)
line_stroke((190, 112), (258, 112), (6, 6))
# 3) 竖弯钩 — left vertical down, curve right, UP-LEFT hook flick
sv = bez((190, 112), (188, 140), (200, 165), (250, 175), n=70)
stroke(sv, (7, 7))
# hook flick UP-and-LEFT
hook = bez((250, 175), (252, 168), (250, 160), (244, 152), n=25)
stroke(hook, (7, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0505_起/01_起.png")
