"""
Render 通 (tong1) at 300x300, black ink on white.

Structural read from GT (通 = 甬 upper-right + 辶 wrapping bottom-left):

  甬 (upper-right, x ~ 105..245, y ~ 30..245):
    - 丶 (small point) top
    - 横折 short — small horn top-right (the 龴 top of 甬)
    - 用 body: left 竖, top-right 横折钩 (right vertical hooks up-left),
      middle 竖 piercing through top opening,
      two inner 横 cross-bars.

  辶 (radical, wraps bottom-left):
    - 丶 top-left point
    - 横折折撇 shepherd-hook (short 横 then 折 down then 撇 down-left)
    - 平捺 long bottom sweep, ends with a foot flare up-right
       (this stroke passes UNDER 甬, so 甬 sits on top of it — components touch)

Applies the 4-move calligraphic recipe (TIER-0 F):
  - variable-width tapered strokes for 撇/捺/点
  - shoulder dabs at 折 joints
  - Bezier for curved sweeps
  - hook flick UP-and-LEFT
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

# ============ 甬 (upper-right block) ============
# 1) 丶 top point (tiny slanted dot)
dot_top = bez((148, 35), (152, 40), (156, 46), (160, 52), n=20)
stroke(dot_top, (4, 8))

# 2) short 横折 horn top-right (龴 hook shape): tiny 横 then 折 tick down
horn_h = bez((160, 55), (180, 55), (200, 55), (215, 55), n=30)
stroke(horn_h, (7, 7))
dab(215, 55, 5)  # shoulder dab
horn_v = bez((215, 55), (213, 62), (211, 68), (209, 75), n=20)
stroke(horn_v, (7, 5))

# ============ 用 body (rectangle with piercing middle) ============
LX = 130     # left vertical x
RX = 232     # right vertical x
TY = 78      # top of the rectangle
BY = 238     # bottom (right) of the rectangle

# 3) left 竖 (long vertical, straight)
left_v = bez((LX, TY), (LX, TY + 55), (LX, TY + 110), (LX, BY + 6), n=60)
stroke(left_v, (8, 7))

# 4) top 横 spanning LX..RX
top_h = bez((LX, TY), (LX + 30, TY - 1), (RX - 30, TY - 1), (RX, TY), n=50)
stroke(top_h, (7, 7))
dab(RX, TY, 5)  # shoulder dab at 横折

# 5) right 竖钩: down from (RX, TY) to bottom, then hook UP-and-LEFT
right_v = bez((RX, TY), (RX, TY + 55), (RX, TY + 110), (RX, BY), n=60)
stroke(right_v, (7, 7))
hook = bez((RX, BY), (RX - 5, BY - 5), (RX - 12, BY - 10), (RX - 20, BY - 16), n=25)
stroke(hook, (7, 3))

# 6) middle 竖 piercing through the top (starts above top, goes to bottom)
MX = (LX + RX) // 2
mid_v = bez((MX, 58), (MX, 110), (MX, 180), (MX, BY + 8), n=70)
stroke(mid_v, (7, 6))

# 7) inner upper 横
inner_h1 = bez((LX + 4, 128), (MX - 10, 127), (MX + 10, 127), (RX - 4, 128), n=40)
stroke(inner_h1, (6, 6))

# 8) inner lower 横
inner_h2 = bez((LX + 4, 180), (MX - 10, 179), (MX + 10, 179), (RX - 4, 180), n=40)
stroke(inner_h2, (6, 6))

# ============ 辶 radical (wraps bottom-left) ============
# 9) 丶 top-left point of 辶
dot_ra = bez((60, 55), (64, 62), (68, 70), (72, 78), n=20)
stroke(dot_ra, (4, 9))

# 10) 横折折撇 shepherd hook: small 横 tick, then down, then 撇 down-left
sh_h = bez((52, 108), (65, 106), (78, 106), (92, 108), n=30)
stroke(sh_h, (6, 6))
dab(92, 108, 5)  # shoulder dab
sh_v = bez((92, 108), (91, 118), (89, 128), (86, 138), n=25)
stroke(sh_v, (6, 6))
dab(86, 138, 5)  # shoulder dab
sh_pie = bez((86, 138), (75, 155), (62, 175), (48, 198), n=50)
stroke(sh_pie, (8, 3))

# 11) 平捺 long bottom sweep (starts upper-left, curves down and right, foot flare)
# This must pass UNDER 甬 body so 用's bottom touches it.
pn = bez((40, 210), (100, 258), (180, 268), (240, 252), n=80)
stroke(pn, (5, 12))
# foot flare at end (up-right)
foot = bez((240, 252), (252, 248), (262, 243), (270, 238), n=25)
stroke(foot, (12, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0513_通/01_通.png")
