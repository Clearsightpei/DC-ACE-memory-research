"""
Render 得 (de2) at 300x300, black ink on white.

Structural read from GT:
  Left: 彳 (short 撇 + short 撇 + long 竖) — narrow column, x ~25-90.
  Right (stacked):
    - 日 (small rectangle): top-right block, ~y 40-110.
    - 一 (long horizontal): full width of right side, ~y 140.
    - 寸 (bottom): 横 + 竖钩(UP-LEFT flick) + 丶.
  Components TOUCH: 彳 竖 abuts left edge of right column;
  日 bottom feeds into 一; 一 sits on top of 寸.
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


# === 彳 (left, x ~25-95) ===
# Upper 撇 (short pie)
pie1 = bez((78, 50), (68, 65), (58, 78), (48, 90), n=40)
stroke(pie1, (7, 3))

# Lower 撇 (short pie, starts where upper ended, sweeps further)
pie2 = bez((72, 95), (58, 115), (46, 135), (32, 155), n=50)
stroke(pie2, (8, 3))

# Long 竖 (starting from second 撇's upper joint)
sh = bez((68, 100), (68, 160), (68, 210), (68, 255), n=60)
stroke(sh, (7, 6))

# === 日 (small rectangle, top-right; x ~115-185, y ~45-110) ===
# Left 竖
r_left = bez((118, 48), (118, 78), (118, 95), (118, 112), n=40)
stroke(r_left, (7, 6))

# Top 横折: 横 + shoulder + 竖
top_h = bez((118, 48), (145, 46), (170, 46), (188, 48), n=40)
stroke(top_h, (5, 6))
shoulder(188, 48, r=4.5)  # shoulder dab at 折
r_right = bez((188, 48), (188, 78), (188, 95), (188, 112), n=40)
stroke(r_right, (6, 6))

# Middle short 横 inside 日
mid_h = bez((120, 80), (145, 80), (170, 80), (186, 80), n=30)
stroke(mid_h, (5, 5))

# Bottom 横 closing 日
bot_h = bez((118, 112), (145, 112), (170, 112), (188, 112), n=30)
stroke(bot_h, (5, 5))

# === 一 (long horizontal, spans right column, ~y 142) ===
h_long = bez((100, 142), (160, 140), (220, 140), (275, 143), n=60)
stroke(h_long, (5, 7))

# === 寸 (bottom-right) ===
# 横 (寸's top horizontal)
cun_h = bez((108, 195), (160, 193), (215, 193), (265, 196), n=50)
stroke(cun_h, (5, 7))

# 竖钩: starts above 横 crossing it, comes straight down, hooks UP-LEFT
cun_v = bez((185, 160), (185, 200), (185, 240), (185, 268), n=60)
stroke(cun_v, (7, 7))
# Hook flick UP-and-LEFT (TIER-0 rule B)
hook = bez((185, 268), (178, 262), (170, 255), (160, 248), n=30)
stroke(hook, (7, 2))

# 丶 (small dot on right of 竖, angled down-right)
dot = bez((205, 218), (215, 228), (222, 236), (228, 242), n=25)
stroke(dot, (3, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0569_得/01_得.png")
