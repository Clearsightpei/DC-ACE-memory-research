"""
p3_char_0489_指 — 扌 (left) + 旨 (right)

# SIGNATURE CHECK:
# 指 has 9 strokes total:
#   Left 扌 (3): 短横 tilted up, 长竖钩 (hook flicks UP-LEFT), 提 rising
#   Right 旨 (6): top 匕 = 撇 + 竖弯钩; bottom 日 = 竖 + 横折 + 中横 + 底横
# TIER-0 rule B: 竖钩 flick UP-and-slightly-LEFT (~-100 to -110°)
# TIER-0 rule H: components must TOUCH — 扌 竖 should slightly overlap
#   with 旨's 日 rectangle boundary. 匕's 竖弯钩 forms the roof of 日.
# v7.5 four-move: taper on 撇/提, shoulder dab at 折 corners, bezier for
#   sweeping strokes, UP-LEFT hook flick.
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


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ============================================================
# LEFT: 扌  (x ~ 30..115, y ~ 70..270)
# ============================================================

# 1. 短横 — short horizontal tilted slightly up-right
h_top = bez((35, 115), (55, 112), (85, 108), (110, 103), n=40)
stroke(h_top, (7, 6))

# 2. 长竖钩 — long vertical starting above 短横, hook flicks UP-LEFT
v_main = bez((78, 78), (78, 150), (78, 220), (78, 258), n=60)
stroke(v_main, (8, 8))
# hook flick UP-and-LEFT
hook = bez((78, 258), (72, 254), (65, 248), (55, 240), n=25)
stroke(hook, (8, 3))
dab(78, 258, 4)  # rounded corner at hook base

# 3. 提 — rising stroke from lower-left crossing the 竖
ti = bez((28, 215), (55, 205), (85, 192), (115, 178), n=40)
stroke(ti, (9, 3))  # thick to thin


# ============================================================
# RIGHT: 旨  (x ~ 130..270, y ~ 55..270)
# Top: 匕 (~y 55..155), Bottom: 日 (~y 155..270)
# ============================================================

# ---- 匕 top ----
# 4. 撇 — starts at top-right (touching vertical), sweeps down-left
pie = bez((222, 80), (205, 100), (185, 118), (158, 138), n=40)
stroke(pie, (9, 4))

# 5. 竖弯钩 — starts high-right, drops down then bends right, UP-LEFT hook.
#    In 旨 the 匕 bottom forms the roof of 日.
v_bi = bez((222, 82), (222, 105), (222, 130), (222, 148), n=40)
stroke(v_bi, (8, 7))
# shoulder dab at corner
dab(222, 148, 6)
# horizontal sweep (bottom of 匕 = top of 日 roof)
h_bi = bez((222, 152), (210, 152), (180, 152), (155, 152), n=40)
stroke(h_bi, (8, 7))
# hook UP-LEFT at end
hbi = bez((155, 152), (152, 147), (150, 142), (148, 137), n=20)
stroke(hbi, (7, 3))

# ---- 日 bottom (rectangle with middle horizontal) ----
# 6. 竖 (left vertical of 日)
v_left = bez((158, 158), (158, 195), (158, 235), (158, 268), n=40)
stroke(v_left, (7, 7))

# 7. 横折 (top-right corner + right vertical of 日)
h_top_ri = bez((158, 160), (185, 160), (215, 160), (245, 160), n=40)
stroke(h_top_ri, (7, 7))
dab(245, 160, 6)  # shoulder dab at 折 corner
v_right = bez((245, 160), (245, 200), (245, 240), (245, 268), n=40)
stroke(v_right, (7, 7))

# 8. 中横 (middle horizontal inside 日)
mid_h = bez((160, 215), (185, 214), (220, 214), (243, 214), n=40)
stroke(mid_h, (6, 6))

# 9. 底横 (bottom horizontal closes 日)
bot_h = bez((158, 268), (185, 268), (218, 268), (245, 268), n=40)
stroke(bot_h, (7, 7))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0489_指/01_指.png")
