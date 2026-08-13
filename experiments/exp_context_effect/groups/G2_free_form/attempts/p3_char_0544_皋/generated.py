"""
Render 皋 (gao1, marsh) at 300x300, black ink on white.

Structural read from GT:
  Top:    白 — small 丿 top-left, rectangle box (left竖, top横折, right竖),
          inner mid 横, bottom-closing 横. Centered high.
  Middle: 大-like arms — a small 丿 on left, small 丶 on right, flanking
          a central vertical. (This is 皋's middle part.)
  Lower:  a long wide 横 spanning most of canvas width.
  Bottom: a long 竖 (十's vertical) descending through the wide 横
          down to near the baseline.

Apply v7.5 4-move: taper via stroke(widths), Bezier for curved sweeps,
hook flick n/a (皋 has no hook), shoulder dab at 白's top-right 折.
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


def dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# === TOP: 白 (centered, ~y=35..120, ~x=110..190) ===

# 1. small 丿 above top-left of the box
pie_top = bez((138, 35), (132, 42), (127, 50), (122, 58), n=30)
stroke(pie_top, (5, 2))

# 2. left 竖 of the box
left_v = bez((115, 55), (115, 78), (115, 100), (115, 118), n=40)
stroke(left_v, (5, 5))

# 3. top 横 + right 折 (竖) — one stroke: horizontal then turn down
top_h = bez((115, 55), (140, 55), (170, 55), (190, 55), n=40)
stroke(top_h, (5, 5))
dab(190, 55, r=4)  # shoulder dab at 折
right_v = bez((190, 55), (190, 78), (190, 100), (190, 118), n=40)
stroke(right_v, (5, 5))

# 4. inner middle 横
mid_h = bez((117, 85), (140, 85), (170, 85), (188, 85), n=40)
stroke(mid_h, (4, 4))

# 5. bottom-closing 横
bot_h = bez((115, 118), (140, 118), (170, 118), (190, 118), n=40)
stroke(bot_h, (5, 5))


# === MIDDLE: 大-like arms with central vertical stem (~y=130..185) ===

# central vertical stem (continues into the 十 below)
stem_upper = bez((152, 130), (152, 150), (152, 170), (152, 190), n=40)
stroke(stem_upper, (5, 6))

# left arm — small 丿 flicking down-left
left_arm = bez((152, 138), (130, 160), (105, 185), (80, 210), n=60)
stroke(left_arm, (8, 2))

# right arm — small 丶/short 捺 flicking down-right
right_arm = bez((152, 138), (175, 160), (200, 185), (225, 210), n=60)
stroke(right_arm, (2, 9))


# === LOWER: long wide 横 (~y=205) ===
long_h = bez((45, 205), (110, 203), (190, 203), (258, 205), n=80)
stroke(long_h, (6, 6))


# === BOTTOM: long 竖 (十 vertical) descending to baseline ===
long_v = bez((152, 190), (152, 225), (152, 255), (152, 282), n=60)
stroke(long_v, (7, 7))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0544_皋/01_皋.png")
