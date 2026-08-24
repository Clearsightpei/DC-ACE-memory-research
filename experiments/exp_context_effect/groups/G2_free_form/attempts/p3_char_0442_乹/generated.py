"""
Render 乹 (qian2, variant of 乾) at 300x300 black-on-white.

Structural read from GT:
  Left half (~x 35–170): 龺-like stack —
    row1 (~y 40–65):  short 横 + 竖 (十-top)
    row2 (~y 70–140): 日 box (two 横 + two 竖)
    row3 (~y 150–265): 十 lower — a long 横 across the whole left half,
                        a 竖 through it, plus small side 撇/捺 legs.
  Right half (~x 180–275): big 乚 (竖弯钩) —
    竖 from top-right down, curves right at bottom, hook flicks UP-LEFT.

Applies TIER-0 rule B (hook UP-and-LEFT) and calligraphic-weight taper.
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


# ---------- LEFT HALF: 龺 ----------

# Row 1 — top 十
# short 横 at top
h_top = bez((60, 50), (95, 48), (135, 48), (165, 52), n=40)
stroke(h_top, (5, 6))
# 竖 through top down into 日 area
v_top = bez((110, 40), (110, 55), (110, 65), (110, 72), n=30)
stroke(v_top, (6, 6))

# Row 2 — 日 box (approx x 55..160, y 72..140)
# top 横 of 日
h2_top = bez((60, 76), (100, 74), (140, 74), (160, 78), n=40)
stroke(h2_top, (6, 6))
# middle 横 of 日
h2_mid = bez((60, 108), (100, 106), (140, 106), (160, 108), n=40)
stroke(h2_mid, (5, 5))
# bottom 横 of 日
h2_bot = bez((60, 138), (100, 136), (140, 136), (162, 140), n=40)
stroke(h2_bot, (6, 6))
# left 竖
v2_left = bez((62, 76), (60, 100), (60, 120), (62, 140), n=40)
stroke(v2_left, (6, 6))
# right 竖 (with slight折 at top corner shoulder)
dab(160, 78, 4)
v2_right = bez((160, 78), (160, 100), (160, 120), (160, 140), n=40)
stroke(v2_right, (6, 6))

# Row 3 — bottom 十 with legs
# long 横 across left half
h_bot = bez((45, 175), (95, 173), (150, 173), (185, 178), n=50)
stroke(h_bot, (6, 7))
# 竖 down through middle
v_bot = bez((115, 155), (115, 195), (115, 235), (115, 268), n=50)
stroke(v_bot, (7, 6))
# small 撇 leg to the left of the 竖 (from row3 area)
leg_l = bez((85, 195), (75, 220), (65, 245), (52, 270), n=40)
stroke(leg_l, (6, 3))
# small 捺 leg to the right of the 竖
leg_r = bez((150, 200), (160, 225), (170, 245), (180, 260), n=40)
stroke(leg_r, (3, 7))


# ---------- RIGHT HALF: 乚 (竖弯钩) ----------
# Vertical portion descending on the right
v_right = bez((205, 45), (207, 100), (209, 160), (210, 210), n=60)
stroke(v_right, (7, 8))

# Sweep bottom curve to the right
sweep = bez((210, 210), (215, 245), (235, 268), (270, 268), n=60)
stroke(sweep, (8, 9))

# Hook flick UP-and-LEFT at end
hook = bez((270, 268), (270, 258), (267, 246), (260, 232), n=30)
stroke(hook, (9, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0442_乹/01_乹.png")
