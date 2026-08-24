"""
Render 美 (mei3) at 300x300, black ink on white.

Structural read from GT (9 strokes):
  Top:    丷 — left 点 slanting down-left, right 撇/点 slanting down-right.
  Upper:  三 — three horizontals of increasing width.
  Middle: 丨 — vertical crossing all three horizontals (王-pattern together).
  Belt:   一 — long widest horizontal (top of the 大 below).
  Bottom: 大 — long 撇 down-left + long 捺 down-right, radiating from the belt.

Applied TIER-0 F (calligraphic 4-move):
  1. Teardrop taper on 点/撇/捺.
  2. Bezier for curved sweeps (撇, 捺).
  3. Uniform-ish widths only for 横 (short 三 horizontals).
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

# --- 丷 top (splayed outward, larger) ---
# left 点: slanting down-LEFT (thin -> thick)
left_dot = bez((135, 25), (125, 38), (113, 52), (98, 68), n=30)
stroke(left_dot, (3, 9))
# right 点/撇: slanting down-RIGHT (thin -> thick)
right_dot = bez((170, 25), (183, 40), (195, 55), (208, 70), n=30)
stroke(right_dot, (3, 9))

# --- 三 (three horizontals) ---
# top horizontal (short)
h1 = bez((115, 82), (140, 80), (170, 80), (190, 84), n=40)
stroke(h1, (6, 6))
# middle horizontal (medium)
h2 = bez((105, 120), (135, 118), (170, 118), (200, 122), n=40)
stroke(h2, (6, 6))
# lower horizontal (a bit longer)
h3 = bez((95, 158), (135, 156), (175, 156), (210, 160), n=40)
stroke(h3, (6, 6))

# --- 丨 vertical through the three horizontals ---
vt = bez((150, 70), (150, 105), (150, 140), (150, 170), n=40)
stroke(vt, (7, 7))

# --- 一 belt (long widest horizontal, top of 大) ---
belt = bez((50, 200), (110, 197), (190, 197), (250, 202), n=60)
stroke(belt, (7, 7))

# --- 大 bottom (撇 + 捺 radiating from ~(150, 200)) ---
# 撇: sweep down-left, thick -> thin
pie = bez((150, 205), (128, 230), (95, 258), (55, 285), n=80)
stroke(pie, (11, 4))
# 捺: S-curve sweep down-right, thin -> thick, with foot flare
na = bez((150, 205), (175, 235), (215, 260), (250, 280), n=80)
stroke(na, (5, 13))
foot = bez((250, 280), (258, 282), (265, 284), (270, 285), n=20)
stroke(foot, (13, 4))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0449_美/01_美.png")
