"""
Render 疱 (pao4 — pimple/blister) at 300x300, black ink on white.

Decomposition: 疒 (canopy) + 包 (wrap+巳) tucked into the canopy's
bottom-right per TIER-0 H (components must touch, body inside canopy)
and frozen_cohort 疒 row (5-stroke 疒, NOT 广).

# SIGNATURE CHECK (frozen_cohort 疒):
#   疒 = 5 strokes: (1) top-left 点, (2) 横 spanning canopy width,
#   (3) LONG curved 撇 from right end of 横 sweeping bottom-left
#   (identity-carrying, dominates), (4) inner 点 below 横 right of 撇,
#   (5) 提 rising flick BELOW inner 点. Body 包 tucked UNDER the 撇.
# TIER-0 F: teardrop taper on 撇/捺/点, bezier for curves, hook UP-LEFT.
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

# ============ 疒 canopy (5 strokes) ============
# (1) top-left 点 — teardrop, small
p1 = bez((70, 45), (78, 55), (85, 63), (92, 72), n=25)
stroke(p1, (3, 8))

# (2) 横 — long horizontal from left side across to right of canopy
h_top = bez((55, 90), (120, 86), (180, 86), (235, 92), n=50)
stroke(h_top, (6, 6))

# (3) LONG curved 撇 — from right end of 横 sweeping down-left to bottom-left
# identity-carrying: dominates the character
pie = bez((230, 92), (185, 155), (120, 210), (45, 275), n=90)
stroke(pie, (11, 4))

# (4) inner 点 — below 横, right of 撇 sweep
inner_dot = bez((85, 120), (92, 130), (98, 140), (103, 150), n=25)
stroke(inner_dot, (3, 7))

# (5) 提 — rising flick BELOW the inner 点
ti = bez((70, 168), (90, 162), (110, 156), (128, 150), n=30)
stroke(ti, (8, 3))

# ============ 包 body — tucked inside canopy, bottom-right ============
# 包 = 撇 + 横折钩 (wrap) + 巳 inside (横 + 竖弯 or similar)
# Positioned so wrap touches / overlaps with 疒's 撇 sweep.

# (a) 包's top 撇 — short angled flick, sits above the wrap
bao_pie = bez((165, 118), (158, 135), (150, 148), (140, 160), n=40)
stroke(bao_pie, (8, 3))

# (b) 横折钩: 横 top → 竖 down → hook UP-LEFT
# 横 segment
h_wrap = bez((150, 145), (185, 143), (215, 143), (240, 148), n=40)
stroke(h_wrap, (6, 6))
# shoulder dab at the top-right corner (折 joint)
d.ellipse((240 - 5, 148 - 5, 240 + 5, 148 + 5), fill="black")
# 竖 segment down
v_wrap = bez((240, 148), (240, 190), (240, 230), (238, 265), n=50)
stroke(v_wrap, (6, 6))
# hook flick UP-and-LEFT (frozen_cohort + TIER-0 B)
hook = bez((238, 265), (228, 258), (218, 250), (208, 242), n=25)
stroke(hook, (7, 3))

# (c) inside 巳 — 横折 opening from left, going right then folding down
in_h = bez((175, 180), (200, 178), (218, 179), (228, 183), n=30)
stroke(in_h, (5, 5))
# shoulder dab at 折 joint
d.ellipse((228 - 4, 183 - 4, 228 + 4, 183 + 4), fill="black")
# short 竖 going down from the fold
in_v = bez((228, 183), (227, 195), (226, 205), (226, 214), n=30)
stroke(in_v, (5, 5))

# (d) inside 竖弯 base — starts from left below 横, sweeps down and curves right
# forms the characteristic 巳 tail
in_base_v = bez((175, 180), (173, 200), (175, 215), (183, 224), n=45)
stroke(in_base_v, (6, 6))
in_base_h = bez((183, 224), (200, 227), (215, 226), (228, 220), n=40)
stroke(in_base_h, (6, 5))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0518_疱/01_疱.png")
