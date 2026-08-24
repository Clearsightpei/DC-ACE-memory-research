# BANK_DEVIATION
# skipped: yue.py
# reason: yue.py is a full-canvas 月; in 能 the 月 sits in the bottom-left
#   quadrant at ~40% width — extreme compression would misplace the hook;
#   inlining a compact bottom-left 月 keeps the hook proportions correct.
# fresh_component: yue_for_neng_BL (compact bottom-left 月)

# 能 (neng) — 10 strokes
# Layout (300x300):
#   TOP-LEFT:  厶 (small)          TOP-RIGHT: 匕 (small)
#   BOT-LEFT:  月 (compact)         BOT-RIGHT: 匕 (compact)

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), (255, 255, 255))
D = ImageDraw.Draw(img)


def taper_line(D, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def taper_bezier(D, p0, p1, p2, w0, w1, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


# =========================================
# TOP-LEFT: 厶 (approx x 30..115, y 45..115)
# Two strokes: 撇折 (pie then heng) + 点
# =========================================
# 撇折: pie down-left from (85,50) to (45,105), then heng-ish to (105,110)
taper_bezier(D, (85, 50), (55, 85), (48, 108), w0=7, w1=6)
taper_line(D, (48, 108), (108, 112), w0=6, w1=8, steps=18)
# small 点 at top-right of 厶
taper_bezier(D, (90, 78), (100, 88), (108, 100), w0=3, w1=8)

# =========================================
# TOP-RIGHT: 匕 (approx x 160..270, y 40..125)
# Two strokes: 撇 (upper-left) + 竖弯钩
# =========================================
# 撇 slanting from top-right down-left
taper_bezier(D, (215, 50), (200, 75), (175, 105), w0=7, w1=3)
# 竖弯钩: short vertical then curve right + hook up
taper_line(D, (200, 65), (200, 105), w0=6, w1=7, steps=14)
# curve to right
taper_bezier(D, (200, 105), (215, 125), (255, 122), w0=7, w1=8)
# hook up
taper_line(D, (255, 122), (255, 108), w0=8, w1=3, steps=8)

# =========================================
# BOT-LEFT: 月 (approx x 30..135, y 130..275)
# 撇 + 横折钩 + 2 interior 横
# =========================================
BL_XL, BL_XR = 55, 128
BL_YT, BL_YB = 140, 275

# 撇 (nearly vertical scoop, tapered)
taper_bezier(D, (BL_XL + 5, BL_YT),
             (BL_XL, BL_YT + (BL_YB - BL_YT) * 0.7),
             (30, BL_YB), w0=9, w1=2, steps=48)
# top nub
D.ellipse([BL_XL + 5 - 6, BL_YT - 4, BL_XL + 5 + 4, BL_YT + 6], fill=(0, 0, 0))

# 横 top of frame (top-left corner to top-right)
taper_line(D, (BL_XL + 5, BL_YT), (BL_XR, BL_YT), w0=8, w1=8, steps=18)
# corner nub
D.ellipse([BL_XR - 5, BL_YT - 5, BL_XR + 5, BL_YT + 5], fill=(0, 0, 0))

# 竖 right side down
taper_line(D, (BL_XR, BL_YT), (BL_XR, BL_YB - 8), w0=8, w1=8, steps=26)

# hook (short, up-left)
taper_line(D, (BL_XR, BL_YB - 8), (BL_XR - 14, BL_YB - 22), w0=8, w1=2, steps=10)
D.ellipse([BL_XR - 5, BL_YB - 13, BL_XR + 5, BL_YB - 3], fill=(0, 0, 0))

# interior 横 x2
YI1 = BL_YT + int((BL_YB - BL_YT) * 0.35)
YI2 = BL_YT + int((BL_YB - BL_YT) * 0.65)
taper_line(D, (BL_XL + 8, YI1), (BL_XR - 8, YI1), w0=4, w1=5, steps=14)
taper_line(D, (BL_XL - 2, YI2), (BL_XR - 8, YI2), w0=4, w1=5, steps=14)

# =========================================
# BOT-RIGHT: 匕 (approx x 155..275, y 140..275)
# 撇 + 竖弯钩 (larger than top one)
# =========================================
# 撇 from upper-right down-left, tapered
taper_bezier(D, (230, 148), (210, 195), (170, 240), w0=9, w1=3, steps=40)
# 竖弯钩
taper_line(D, (208, 170), (208, 240), w0=8, w1=9, steps=22)
# curve to right
taper_bezier(D, (208, 240), (230, 268), (272, 262), w0=9, w1=10, steps=32)
# hook up
taper_line(D, (272, 262), (272, 235), w0=10, w1=3, steps=12)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0499_能/01_能.png")
print("saved")
