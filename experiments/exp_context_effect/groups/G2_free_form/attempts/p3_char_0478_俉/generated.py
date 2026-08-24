"""
Render 俉 (wu3) at 300x300, black ink on white.

Structure: 亻 (left) + 吾 (right). 吾 = 五 (top) + 口 (bottom).

Applies calligraphic-weight 4-move per memory_index TIER-0 F:
- teardrop tapers on 撇/点
- shoulder dabs at 折 joints
- bezier curves for 撇 sweeps
- (no hooks in 俉, so hook flick rule N/A)
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
    """Draw a variable-width stroke via overlapping circles."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(x, y, r=5.5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =====================================================
# 亻 (left, narrow) — occupies x ~35-95, y ~55-260
# =====================================================
# 撇: from upper-right, curves down and left
pie = bez((92, 55), (78, 110), (62, 155), (38, 195), n=70)
stroke(pie, (10, 4))

# 竖: from mid-撇 down straight
shu = bez((78, 118), (78, 170), (78, 220), (78, 265), n=60)
stroke(shu, (7, 7))

# =====================================================
# 吾 right side — occupies x ~110-275, y ~55-275
# 五 (top): rough y ~55-175
# 口 (bottom): rough y ~185-275
# =====================================================

# --- 五 (top half) — y ~60-180 ---
# 1. Top short 横
h_top = bez((155, 68), (180, 66), (210, 66), (238, 70), n=40)
stroke(h_top, (6, 7))

# 2. 竖 (slanted, longer, dropping from top-mid down-left)
v_top = bez((190, 72), (183, 100), (176, 130), (168, 160), n=50)
stroke(v_top, (7, 5))

# 3. 横折 — mid horizontal, folds down (right side of 五's box)
mid_h = bez((150, 128), (180, 126), (215, 126), (240, 130), n=50)
stroke(mid_h, (6, 6))
dab(240, 130, r=4.5)
mid_v = bez((240, 130), (240, 148), (240, 165), (240, 180), n=40)
stroke(mid_v, (6, 6))

# 4. Bottom 横 (long, closes 五)
h_bot = bez((122, 180), (165, 178), (215, 178), (258, 182), n=60)
stroke(h_bot, (7, 8))

# --- 口 (bottom) — smaller, y ~200-268 ---
# left 竖
kou_l = bez((150, 205), (150, 225), (150, 248), (150, 268), n=40)
stroke(kou_l, (6, 6))
# top 横折 (top horizontal + right vertical)
kou_top = bez((150, 205), (180, 203), (215, 203), (245, 207), n=50)
stroke(kou_top, (6, 6))
dab(245, 207, r=4.5)
kou_r = bez((245, 207), (245, 228), (245, 250), (243, 268), n=40)
stroke(kou_r, (6, 5))
# bottom 横 (closes)
kou_bot = bez((150, 268), (185, 266), (215, 266), (245, 268), n=50)
stroke(kou_bot, (6, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0478_俉/01_俉.png")
