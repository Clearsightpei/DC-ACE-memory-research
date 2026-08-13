"""
Render 战 (zhan4) at 300x300, black ink on white.

# SIGNATURE CHECK (戈 frozen radical, tier-0 G):
#   戈 = 横 + 斜钩 + 撇 + 丶(top-right dot)
#   斜钩: quadratic-Bezier arc from top-right-region, curves down-then-right,
#         hook flick UP-and-LEFT (~-115 deg) at terminal
#   Top 丶 sits ABOVE the 横 crossbar with ~5 px overlap; do NOT detach
#   Short 撇 crosses the 横 from upper-right to lower-left-of-hook

Structure: left 占 + right 戈 (left-right compound, ~40/60 split).
  Left 占  = 卜 (竖+点) on top, 口 (竖+横折+横) on bottom.
  Right 戈 = 一 (横) + 斜钩 (with UP-LEFT hook flick) + 短撇 + 丶(top dot).

Applies calligraphic 4-move: teardrop taper on 撇/点, shoulder dabs at
折 joints, bezier for curved sweeps, UP-and-LEFT hook flick.
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

# ===================== LEFT: 占 (occupies ~x=30..135) =====================
# 卜 top: 竖 + 点 (short dot to RIGHT of vertical, NOT a full crossing 横)
# 竖 (vertical) — center of 卜
zhu_bu = bez((80, 45), (80, 70), (80, 95), (80, 125), n=40)
stroke(zhu_bu, (8, 8))

# 点 of 卜 — SHORT dot/tick on the RIGHT of the 竖, near its middle,
# angled slightly down-right (teardrop). Do NOT cross the vertical.
dot_bu = bez((85, 85), (95, 88), (105, 92), (115, 97), n=25)
stroke(dot_bu, (3, 8))

# 口 (bottom box) — squat, approx (40, 150) to (130, 215)
# left 竖
left_v = bez((45, 150), (45, 175), (45, 200), (45, 215), n=40)
stroke(left_v, (7, 7))
# top 横 + right 竖 as single 横折 stroke
hor_top = bez((45, 150), (70, 148), (100, 148), (128, 150), n=40)
stroke(hor_top, (6, 6))
dab(128, 150, 5)
right_v = bez((128, 150), (128, 175), (128, 200), (128, 215), n=40)
stroke(right_v, (7, 7))
# bottom 横 (closes the box)
bot_h = bez((45, 215), (70, 213), (100, 213), (128, 215), n=40)
stroke(bot_h, (6, 6))

# ===================== RIGHT: 戈 (occupies ~x=150..285) =====================
# 一 (horizontal crossbar) — spans across the 戈, slight upward slant
ge_h = bez((150, 130), (185, 127), (225, 126), (275, 128), n=50)
stroke(ge_h, (6, 6))

# 斜钩 (main diagonal sweep with hook)
# starts top (small vertical stub above 横), sweeps down-right in an arc,
# terminates near bottom-right; then hook UP-and-LEFT.
# small vertical stub before the arc (attaches near top-center of 戈)
stub = bez((210, 90), (210, 105), (210, 118), (210, 128), n=25)
stroke(stub, (7, 7))
# main斜钩 arc: from ~(210, 128) sweep down-right to bottom-right corner
xie_gou = bez((210, 128), (225, 175), (250, 220), (278, 260), n=80)
stroke(xie_gou, (8, 6))
# hook flick — UP-and-LEFT (~-115 deg) into the character body
hook = bez((278, 260), (275, 250), (270, 240), (262, 232), n=25)
stroke(hook, (7, 3))

# 短撇 (short pie) — crosses the 横 from upper-right to lower-left, thin tail
duan_pie = bez((235, 105), (222, 130), (208, 155), (188, 178), n=50)
stroke(duan_pie, (7, 3))

# 丶 (top-right dot) — bigger teardrop sitting above the 横 crossbar,
# top-right area of 戈, ~5 px overlap with 横 (do NOT detach)
top_dot = bez((255, 85), (260, 95), (264, 105), (268, 125), n=30)
stroke(top_dot, (4, 10))

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0475_战/01_战.png"
img.save(out)
print(f"Saved: {out}")
