"""
Render 畢 (bi4) at 300x300, black ink on white.

Structural read from GT:
  Top:    small 田 (rice-paddy) centered upper — 5 strokes:
          left 竖, top 横折 (top+right), inner 横, inner 竖, bottom 横.
  Middle: horizontals below 田 with short vertical continuations
          (like 卄-ish structure).
  Long 横: a wide horizontal near lower-middle spanning almost full width.
  Center 竖: long vertical descending to near the bottom.

Applies TIER-0 F (calligraphic 4-move): bezier for any curved sweep,
teardrop taper at 撇 tails, shoulder-dab at 折 corners.
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


def line(p0, p1, w=6):
    stroke(bez(p0, ((p0[0]+p1[0])/2, (p0[1]+p1[1])/2),
               ((p0[0]+p1[0])/2, (p0[1]+p1[1])/2), p1, n=40), (w, w))


def shoulder(x, y, r=4.5):
    d.ellipse((x-r, y-r, x+r, y+r), fill="black")


# ============================================================
# TOP: 田 (small, upper-center) — box ~ x[110..195], y[50..118]
# ============================================================
BL, BR = 110, 195
BT, BB = 50, 118
CX = (BL + BR) // 2  # 152
CY_MID = (BT + BB) // 2  # 84

# 1) left 竖
line((BL, BT), (BL, BB), w=6)
# 2) top 横折 (top 横 + right 竖)
line((BL, BT), (BR, BT), w=6)
shoulder(BR, BT)
line((BR, BT), (BR, BB), w=6)
# 3) inner 横 (mid horizontal inside)
line((BL, CY_MID), (BR, CY_MID), w=5)
# 4) inner 竖 (mid vertical inside) — this will be extended by the long center 竖 below
line((CX, BT), (CX, BB), w=5)
# 5) bottom 横 (close the box)
line((BL, BB), (BR, BB), w=6)


# ============================================================
# BELOW 田: two horizontals with short vertical continuations
# ============================================================
# upper crossbar (below 田)
h_upper_left = 100
h_upper_right = 210
line((h_upper_left, 150), (h_upper_right, 150), w=6)

# two short verticals descending from that crossbar
line((132, 150), (132, 200), w=5)
line((178, 150), (178, 200), w=5)

# lower crossbar
line((100, 200), (210, 200), w=6)


# ============================================================
# WIDE 横: the long horizontal near the bottom
# ============================================================
long_h = bez((45, 230), (110, 227), (200, 227), (260, 232), n=80)
stroke(long_h, (7, 7))


# ============================================================
# CENTER 竖: the long vertical extending through everything
#           (from near top of 田 down to near bottom)
# ============================================================
center_v = bez((CX, 42), (CX, 130), (CX, 210), (CX, 285), n=80)
stroke(center_v, (7, 7))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0512_畢/01_畢.png")
