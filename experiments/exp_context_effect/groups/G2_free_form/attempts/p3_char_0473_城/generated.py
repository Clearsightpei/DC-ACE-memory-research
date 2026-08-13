"""
Render 城 (cheng2) at 300x300, black ink on white.

SIGNATURE CHECK (component 土):
  BOTTOM 横 LONGER than top ~1.5x, distinguishes 土 from 士.

FROZEN-RADICAL ALARM (戈 family, TIER-0 G):
  right component 成 contains 斜钩 (戈-style long arc).
  斜钩: quadratic-like bezier from upper-left area sweeping DOWN
        and RIGHT to lower-right, then hook flick UP-and-LEFT.
  Top 丶 dot must sit above the 横 crossbar with ~5 px overlap.

Structural read from GT:
  Left  (土):
    - short top 横 (upper) around y=120
    - central 竖 through both 横
    - long bottom 横 around y=195 (~1.5x the top 横)
  Right (成):
    - short top 一 (a hook/short横) around y=95
    - 撇 sweeping from upper area down-left to mid-bottom
    - the big 斜钩: from top-left of 成 sweeping down-right, hook UP-LEFT
    - interior small 撇
    - top-right 丶 dot
Apply 4-move recipe: bezier curves, tapered widths, shoulder dabs, UP-LEFT hook.
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

def dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ============================================================
# LEFT COMPONENT: 土  (~ x range 30-125)
# ============================================================
# top short 横 (short)
h_top = bez((45, 122), (65, 120), (90, 120), (105, 123), n=40)
stroke(h_top, (5, 6))

# central 竖 through the two horizontals
v = bez((78, 105), (78, 145), (78, 180), (78, 200), n=50)
stroke(v, (7, 7))

# bottom LONG 横 (~1.5x top)
h_bot = bez((30, 200), (60, 197), (100, 197), (128, 200), n=50)
stroke(h_bot, (6, 7))

# ============================================================
# RIGHT COMPONENT: 成  (~ x range 130-285)
# ============================================================

# 1. Top-left short 一 (the little top horizontal of 成)
h_top_r = bez((150, 100), (165, 98), (180, 98), (195, 100), n=40)
stroke(h_top_r, (5, 6))

# 2. 撇 (from just under the top 一, sweeping down-left)
pie = bez((165, 90), (155, 130), (140, 175), (128, 230), n=80)
stroke(pie, (9, 4))

# 3. 横 short crossbar mid-body (part of the 成 skeleton, ~y=140)
h_mid = bez((140, 148), (170, 145), (200, 145), (225, 148), n=50)
stroke(h_mid, (5, 6))
# shoulder dab at right end of 横 where it joins the 斜钩 start
dab(225, 148, r=6)

# 4. BIG 斜钩 (戈-family): starts high near the top-一, sweeps in a long
#    shallow arc DOWN and to the RIGHT reaching lower-right corner,
#    then hook flick UP-and-LEFT (~-115°).
xg = bez((170, 105), (200, 165), (235, 220), (270, 270), n=100)
stroke(xg, (8, 9))
# hook flick UP-and-LEFT (into the character body)
hook = bez((270, 270), (260, 262), (248, 253), (235, 245), n=30)
stroke(hook, (9, 3))
# shoulder dab at start joint
dab(170, 105, r=6)

# 5. Interior small 撇 (inside the 成 bowl, from crossbar sweeping down-left)
pie2 = bez((215, 150), (200, 180), (185, 210), (170, 240), n=60)
stroke(pie2, (7, 3))

# 6. Top-right 丶 dot (sits above the 斜钩 arc, upper-right area)
dot = bez((255, 95), (260, 103), (263, 110), (265, 118), n=25)
stroke(dot, (3, 9))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0473_城/01_城.png")
