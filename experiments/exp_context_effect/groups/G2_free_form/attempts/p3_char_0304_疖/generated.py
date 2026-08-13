"""Render 疖 (jiē — a boil/furuncle) at 300x300 black on white.

Composition: 疒 (illness radical, outer) + 卩 (inner bottom-right).

Reused PASSed precedents:
  - 疒 skeleton from p3_char_0171_疒 (B6 PASS) — 5 strokes.
  - 卩 skeleton from p2_radical_023_卩 (B1 PASS) — 2 strokes.
  Total: 7 strokes.

Placement per GT:
  疒 fills the left+top frame (top 点 near center-top, 横 spanning
  ~x=95..255, two inner 点/提 on the left, long curved 撇 descending
  to bottom-left). 卩 sits inside the RIGHT half, under the 横,
  mid-height: vertical spine around x~175, loop bulging further right.
"""
import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_line(pts, width_start=8, width_end=8):
    if len(pts) < 2:
        return
    n_seg = len(pts) - 1
    for si in range(n_seg):
        x0, y0 = pts[si]
        x1, y1 = pts[si + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for t in range(steps + 1):
            u = t / steps
            gu = (si + u) / n_seg
            w = width_start * (1 - gu) + width_end * gu
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            r = w / 2
            dab(x, y, r)


def line_dabs(p0, p1, r0, r1):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    steps = max(int(dist * 3), 20)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=280):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * x0 + 2 * omt * t * xc + t * t * x2
        y = omt * omt * y0 + 2 * omt * t * yc + t * t * y2
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# =====================================================================
# 疒 outer radical (5 strokes)
# =====================================================================

# Stroke 1: top 点 above the 横, right-of-center
dab_line([(140, 40), (160, 68)], width_start=4, width_end=8)

# Stroke 2: long 横 across the top
dab_line([(88, 92), (150, 88), (255, 95)], width_start=6, width_end=6)

# Stroke 3: upper inner 点 (short slanted flick, inside upper-left)
dab_line([(50, 128), (72, 146)], width_start=4, width_end=8)

# Stroke 4: lower inner 提 (slanted flick rising to the right)
dab_line([(38, 190), (70, 172)], width_start=8, width_end=4)

# Stroke 5: long curved 撇 from horizontal's left end down-left
curve = [
    (90, 92),
    (86, 138),
    (82, 182),
    (72, 222),
    (55, 260),
    (38, 278),
]
dab_line(curve, width_start=9, width_end=5)


# =====================================================================
# 卩 inner-right component (2 strokes) — scaled ~65% and offset right
# =====================================================================

# Stroke 6: 竖 (vertical spine on the LEFT of 卩)
r_shu = 4.5
shu_top = (168, 115)
shu_bot = (168, 268)
dab(shu_top[0], shu_top[1], r_shu + 1)
line_dabs(shu_top, shu_bot, r_shu, r_shu)
dab(shu_bot[0], shu_bot[1], r_shu + 1)

# Stroke 7: 横折钩 forming the small loop upper-right of 卩
r_main = 4.5

# 横 top
heng_start = (176, 112)
heng_end = (238, 105)
dab(heng_start[0], heng_start[1], r_main + 1.5)
line_dabs(heng_start, heng_end, r_main, r_main + 0.5)

# shoulder 顿
shoulder = (240, 105)
dab(shoulder[0], shoulder[1], r_main + 2.0)

# curved 竖 (belly on the right) tucking back to the left
b_p0 = (240, 108)
b_p1 = (258, 155)
b_p2 = (210, 195)
bezier_dabs(b_p0, b_p1, b_p2, r_main + 0.5, r_main)

dab(b_p2[0], b_p2[1], r_main + 1.2)

# Hook flick UP-and-LEFT into the character body
hook_end = (188, 178)
steps = 60
for i in range(steps + 1):
    t = i / steps
    x = b_p2[0] + (hook_end[0] - b_p2[0]) * t
    y = b_p2[1] + (hook_end[1] - b_p2[1]) * t
    r = (r_main + 0.5) + (1.2 - (r_main + 0.5)) * t
    dab(x, y, r)


out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0304_疖/01_疖.png"
img.save(out)
print("saved", out)
