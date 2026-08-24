"""
Render 造 (zao4) at 300x300, black ink on white.

Structural read from GT (造 = 告 upper-right + 辶 wrapping bottom-left):

  告 (upper-right, x ~ 110..245, y ~ 30..240):
    - 丿 short pie at top (小撇 leaning left)
    - 短横 first horizontal (short)
    - 长横 second horizontal (longer, wider than first)
    - 竖 vertical piercing through the two 横 (牛-head shape)
    - 口 (mouth rectangle) at bottom: 竖, 横折, 横 (3 strokes)

  辶 (radical, wraps bottom-left):
    - 丶 top-left point
    - 横折折撇 shepherd-hook (short 横 then 折 down then 撇 down-left)
    - 平捺 long bottom sweep, ends with a foot flare up-right
      (this stroke passes UNDER 告 so 告 sits ON it — components touch)

Applies the 4-move calligraphic recipe (TIER-0 F):
  - variable-width tapered strokes for 撇/捺/点
  - shoulder dabs at 折 joints
  - Bezier for curved sweeps
  - hook flick UP-and-LEFT (none here — no 钩 in 造)

Total strokes: 3 (辶) + 7 (告) = 10.
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

# ============ 告 (upper-right block) ============
# 1) 丿 short pie at top (leaning down-left)
pie = bez((172, 32), (166, 44), (158, 58), (148, 72), n=30)
stroke(pie, (5, 9))

# 2) 短横 first horizontal (short, upper)
h1 = bez((150, 82), (170, 80), (200, 80), (220, 82), n=40)
stroke(h1, (7, 7))

# 3) 长横 second horizontal (longer, wider)
h2 = bez((130, 122), (165, 120), (215, 120), (245, 122), n=50)
stroke(h2, (7, 8))

# 4) 竖 vertical piercing through both 横 (牛-head style)
MX = 182
v_mid = bez((MX, 62), (MX, 100), (MX, 130), (MX, 165), n=50)
stroke(v_mid, (8, 8))

# 5) 口 rectangle at bottom: left 竖
KX_L = 145
KX_R = 232
KY_T = 175
KY_B = 232

k_left = bez((KX_L, KY_T), (KX_L, KY_T + 20), (KX_L, KY_T + 40), (KX_L, KY_B), n=40)
stroke(k_left, (7, 7))

# 6) 口 横折 (top 横 + right 竖)
k_top = bez((KX_L, KY_T), (KX_L + 25, KY_T - 1), (KX_R - 25, KY_T - 1), (KX_R, KY_T), n=45)
stroke(k_top, (7, 7))
dab(KX_R, KY_T, 5)  # shoulder dab
k_right = bez((KX_R, KY_T), (KX_R, KY_T + 20), (KX_R, KY_T + 40), (KX_R, KY_B), n=40)
stroke(k_right, (7, 6))

# 7) 口 bottom 横
k_bot = bez((KX_L, KY_B), (KX_L + 25, KY_B + 1), (KX_R - 25, KY_B + 1), (KX_R, KY_B), n=45)
stroke(k_bot, (7, 7))

# ============ 辶 radical (wraps bottom-left) ============
# 8) 丶 top-left point of 辶
dot_ra = bez((62, 55), (66, 63), (70, 72), (74, 80), n=20)
stroke(dot_ra, (4, 9))

# 9) 横折折撇 shepherd hook: small 横 tick, then down, then 撇 down-left
sh_h = bez((54, 112), (68, 110), (82, 110), (96, 112), n=30)
stroke(sh_h, (6, 6))
dab(96, 112, 5)  # shoulder dab
sh_v = bez((96, 112), (94, 122), (92, 132), (89, 143), n=25)
stroke(sh_v, (6, 6))
dab(89, 143, 5)  # shoulder dab
sh_pie = bez((89, 143), (78, 162), (63, 185), (48, 210), n=50)
stroke(sh_pie, (8, 3))

# 10) 平捺 long bottom sweep (starts upper-left, curves down and right, foot flare)
pn = bez((40, 222), (100, 268), (180, 278), (240, 262), n=80)
stroke(pn, (5, 12))
# foot flare at end (up-right)
foot = bez((240, 262), (252, 258), (262, 253), (272, 248), n=25)
stroke(foot, (12, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0527_造/01_造.png")
