"""
Render 盏 (zhan3, "cup/lamp") at 300x300, black ink on white.

Structural read from GT (top 戋 + bottom 皿):
  戋 (5 strokes):
    1. 横       — top diagonal 一
    2. 提/横    — shorter 一 below
    3. 撇       — sweeps down-left from mid-top
    4. 斜钩     — big diagonal down-right with UP-LEFT hook
    5. 点       — small dot inside the hook cradle
  皿 (5 strokes):
    top 横, left 竖, two inner 竖, right 竖, wide bottom 横

TIER-0: bezier sweeps, teardrop tapers, shoulder dabs,
UP-and-LEFT hook flick. Components MUST touch — 斜钩 tail
overlaps 皿 top 横.
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

def dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---------- Top: 戋 (rows y~35..205) ----------
# Stroke 1: top 横 — rising slightly to the right
h1 = bez((80, 60), (125, 55), (170, 50), (215, 45), n=50)
stroke(h1, (5, 7))

# Stroke 2: middle short 横 — under h1, in the body
h2 = bez((95, 115), (130, 112), (170, 112), (200, 115), n=50)
stroke(h2, (5, 6))

# Stroke 3: 撇 — from upper mid-body, sweeps down-left, thins at tail
pie1 = bez((145, 60), (128, 100), (108, 135), (78, 170), n=70)
stroke(pie1, (9, 3))

# Stroke 4: 斜钩 — big diagonal from upper-right down-right,
# tail sits over 皿 top; then UP-and-LEFT hook flick
xg_main = bez((190, 55), (215, 100), (240, 150), (250, 195), n=90)
stroke(xg_main, (7, 10))
# shoulder dab at hook joint
dab(250, 195, r=7)
# hook flick up-and-left
hook = bez((250, 195), (240, 188), (228, 180), (215, 170), n=30)
stroke(hook, (10, 3))

# Stroke 5: small 点 — nestled inside the 斜钩 cradle (upper right)
pt = bez((215, 78), (222, 88), (228, 96), (232, 105), n=25)
stroke(pt, (3, 7))

# ---------- Bottom: 皿 (rows y~200..280) ----------
# Top 横 of 皿 — overlaps 斜钩 tail (components touch)
b_top = bez((70, 210), (130, 207), (190, 207), (240, 210), n=60)
stroke(b_top, (6, 8))

# Left wall 竖 (short slant inward slightly)
lw = bez((85, 210), (84, 230), (83, 250), (82, 268), n=40)
stroke(lw, (7, 7))

# Inner left 竖
il = bez((130, 215), (129, 233), (128, 250), (127, 267), n=40)
stroke(il, (5, 5))

# Inner right 竖
ir = bez((175, 215), (176, 233), (177, 250), (178, 267), n=40)
stroke(ir, (5, 5))

# Right wall 竖
rw = bez((225, 210), (226, 230), (227, 250), (228, 268), n=40)
stroke(rw, (7, 7))

# Bottom 横 — widest stroke, base of 皿
b_bot = bez((55, 278), (130, 275), (200, 275), (265, 278), n=70)
stroke(b_bot, (7, 10))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0552_盏/01_盏.png")
