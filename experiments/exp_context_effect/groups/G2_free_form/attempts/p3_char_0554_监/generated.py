"""
Render 监 (jian1) at 300x300, black ink on white.

Structural read of 监:
  Top-left:  small 臣-like block (left 竖 + open box facing right)
  Top-right: small 卜 shape (vertical + dot)
  Middle:   short 一 tucked under the top block, spanning center
  Bottom:  皿 (dish radical) — 4 verticals + wide 一 base
Components must touch across the horizontal seam (per TIER-0 rule H).
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


def shoulder(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ===== TOP-LEFT: 臣-like block (compressed) =====
# left 竖 (tall vertical)
stroke(bez((70, 45), (70, 80), (70, 115), (70, 150), n=40), (6, 6))
# top 横 going right from the 竖 top
stroke(bez((70, 47), (95, 47), (120, 47), (140, 48), n=40), (6, 5))
shoulder(140, 48, 4)
# right 竖 (short, drops to mid)
stroke(bez((140, 48), (140, 75), (140, 100), (140, 115), n=40), (5, 5))
# inner short horizontal (middle bar)
stroke(bez((90, 90), (105, 90), (120, 90), (135, 90), n=30), (5, 5))
# bottom horizontal closing the box
stroke(bez((70, 148), (95, 148), (120, 148), (145, 150), n=40), (6, 6))

# ===== TOP-RIGHT: small 卜-like mark =====
# vertical
stroke(bez((205, 55), (205, 90), (205, 120), (205, 145), n=40), (6, 5))
# right dot/short 捺
stroke(bez((205, 95), (220, 100), (230, 108), (240, 118), n=30), (4, 8))

# ===== MIDDLE 一 (short bar joining under top) =====
stroke(bez((85, 170), (135, 168), (185, 168), (225, 170), n=50), (7, 6))

# ===== BOTTOM: 皿 =====
# left 竖 (leans slightly out) — stops at base line
stroke(bez((60, 195), (58, 215), (55, 235), (54, 253), n=40), (7, 7))
# inner 竖 #1 — stops at base line
stroke(bez((110, 210), (110, 225), (110, 240), (110, 253), n=40), (6, 6))
# inner 竖 #2 — stops at base line
stroke(bez((160, 210), (160, 225), (160, 240), (160, 253), n=40), (6, 6))
# right 竖折 — vertical then flick right → base
stroke(bez((215, 195), (218, 215), (222, 235), (225, 253), n=40), (7, 7))
# base 一 — long horizontal seat, wider than verticals
stroke(bez((30, 258), (100, 260), (200, 260), (275, 262), n=80), (9, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0554_监/01_监.png")
