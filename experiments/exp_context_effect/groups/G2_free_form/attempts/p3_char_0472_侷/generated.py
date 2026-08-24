"""
Render 侷 (jú, cramped) at 300x300, black ink on white.

Structural read from GT:
  Left: 亻 (人-radical) — one bowed 撇 + one 竖, tall column on the left third.
  Right: 局 — 尸 on top (横 + 横折 + long 撇), then a small 一 mid-line, then
         a 横折钩 enclosure with 口 inside near the bottom.

TIER-0 F applied: teardrop taper on 撇/捺, shoulder dab at 折 joints,
bezier for curves, UP-and-LEFT hook flick.
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


def shoulder(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =============================================================
# LEFT: 亻 (person radical)
# =============================================================
# 撇 — starts high, sweeps down-left, tapered
pie_left = bez((75, 55), (65, 100), (50, 145), (30, 190), n=70)
stroke(pie_left, (10, 3))

# 竖 — long vertical from just below 撇 start
shu_left = bez((78, 105), (78, 155), (78, 200), (78, 250), n=50)
stroke(shu_left, (8, 8))

# =============================================================
# RIGHT: 局 (top 尸, mid line, bottom 横折钩 + 口)
# =============================================================

# --- 尸 top ---
# top 横 (horizontal)
h_top = bez((130, 65), (170, 63), (210, 63), (245, 65), n=40)
stroke(h_top, (6, 6))
# 折 down (right side of 尸): 竖 going down
shoulder(245, 65, r=4)
zhe_r = bez((245, 65), (245, 90), (245, 105), (245, 115), n=30)
stroke(zhe_r, (7, 7))

# 撇 long — from left corner of 尸 sweeping down-left to about y=245
pie_long = bez((132, 65), (125, 130), (115, 180), (95, 250), n=80)
stroke(pie_long, (9, 4))

# --- middle short 横 (the 一 inside 尸-body, above 口) ---
h_mid = bez((135, 130), (180, 128), (215, 128), (235, 130), n=40)
stroke(h_mid, (6, 6))

# =============================================================
# 横折钩 enclosure (the outer wrap for the bottom 口)
# =============================================================
# Actually in 局 the 横折钩 wraps down from the right, forming the bottom
# right corner and the hook.
# top-right corner already dabbed; we run a 竖 from ~(255, 128) down
# to ~(255, 250) with hook up-left.
shoulder(255, 128, r=5)
zhe_hook_v = bez((255, 130), (255, 175), (255, 220), (253, 255), n=60)
stroke(zhe_hook_v, (7, 7))
# hook flick UP-and-LEFT
hook = bez((253, 255), (245, 250), (238, 244), (230, 238), n=25)
stroke(hook, (7, 3))

# --- bottom 口 inside ---
# left 竖
k_left = bez((155, 180), (155, 210), (155, 235), (155, 255), n=40)
stroke(k_left, (6, 6))
# top 横 + 折 down (single 横折 forming top-right of 口)
k_top = bez((155, 180), (185, 178), (215, 178), (235, 180), n=40)
stroke(k_top, (6, 6))
shoulder(235, 180, r=4)
k_right = bez((235, 180), (235, 210), (235, 235), (235, 255), n=40)
stroke(k_right, (6, 6))
# bottom 横 closing 口
k_bot = bez((155, 255), (185, 253), (215, 253), (235, 255), n=40)
stroke(k_bot, (6, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0472_侷/01_侷.png")
