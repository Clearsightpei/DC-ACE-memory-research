"""
Render 真 (zhen1) at 300x300, black ink on white.

Structural read from GT (10 strokes):
  Top:    十 — one short horizontal + one vertical (the vertical passes
          down and becomes/aligns with the top of the 目 box).
  Middle: 目-like box — 竖 (left), 横折 (top+right), three inner 横s,
          and one bottom 横 to close.
  Under:  one long 横 spanning almost the full width.
  Bottom: 八 — a left 撇/dot and a right 点.

Applies the 4-move calligraphic-weight recipe: variable-width
strokes, shoulder dab at 折 corner, no uniform width=6 polylines.
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


# --- Top 十 ---
# short horizontal
h_top = bez((112, 46), (135, 44), (170, 44), (192, 47), n=40)
stroke(h_top, (6, 6))
# vertical (crosses horizontal, continues down toward box top)
v_top = bez((150, 26), (150, 55), (150, 78), (150, 95), n=40)
stroke(v_top, (7, 7))

# --- 目 box ---
# Coordinates
BL, BR = 92, 214
BT, BB = 78, 190

# Left vertical (竖)
left_v = bez((BL, BT), (BL, BT + 40), (BL, BT + 80), (BL, BB), n=50)
stroke(left_v, (7, 7))

# 横折: top horizontal + right vertical (one stroke, with shoulder dab)
top_h = bez((BL - 5, BT), (BL + 40, BT - 2), (BR - 40, BT - 2), (BR, BT), n=50)
stroke(top_h, (7, 7))
# shoulder dab at the corner
dab(BR, BT, 4.5)
right_v = bez((BR, BT), (BR, BT + 40), (BR, BT + 80), (BR, BB), n=50)
stroke(right_v, (7, 7))

# Three inner horizontals
h_in1 = bez((BL + 8, 110), (BL + 40, 109), (BR - 40, 109), (BR - 8, 111), n=40)
stroke(h_in1, (5, 5))
h_in2 = bez((BL + 8, 138), (BL + 40, 137), (BR - 40, 137), (BR - 8, 139), n=40)
stroke(h_in2, (5, 5))
h_in3 = bez((BL + 8, 165), (BL + 40, 164), (BR - 40, 164), (BR - 8, 166), n=40)
stroke(h_in3, (5, 5))

# Bottom close of the box (a 横)
bot_h = bez((BL - 4, BB), (BL + 40, BB - 1), (BR - 40, BB - 1), (BR + 4, BB), n=50)
stroke(bot_h, (7, 7))

# --- Long 横 underneath (spans wider than the box) ---
long_h = bez((44, 216), (110, 213), (200, 213), (260, 217), n=70)
stroke(long_h, (7, 9))

# --- 八 bottom ---
# left 撇/dot — sweeps down-left
left_dot = bez((132, 236), (122, 250), (110, 262), (96, 274), n=40)
stroke(left_dot, (7, 3))
# right 点 — thick teardrop pointing down-right
right_dot = bez((190, 236), (200, 250), (211, 262), (222, 273), n=40)
stroke(right_dot, (4, 9))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0517_真/01_真.png")
