"""
Render 带 (dai4) at 300x300, black ink on white.

Structure from GT:
  Top:    廿-like — 3 short verticals crossed by a long horizontal,
          with the horizontal's endpoints tucking down (short hook feet).
  Middle: 冖 covering — horizontal with a short left descender and a
          right 折 shoulder.
  Bottom: 巾 — box (left 竖 + right 横折) with a long 竖钩 through the
          middle, hook flick UP-and-LEFT (TIER-0 rule B).

Applies TIER-0 F (calligraphic 4-move): teardrop taper, shoulder dabs
at 折, bezier for curved sweeps, correct hook flick.
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


# === TOP: 廿 (three verticals + long horizontal) ===
# left short vertical
v1 = bez((90, 45), (92, 65), (94, 85), (95, 100), n=30)
stroke(v1, (6, 6))
# middle short vertical
v2 = bez((150, 40), (150, 60), (150, 80), (150, 100), n=30)
stroke(v2, (6, 6))
# right short vertical (slight slant)
v3 = bez((210, 45), (211, 65), (213, 85), (215, 100), n=30)
stroke(v3, (6, 6))

# long horizontal crossing them all, slightly rising and then hooking down at the right end
h_top = bez((55, 100), (110, 96), (180, 96), (245, 102), n=70)
stroke(h_top, (7, 7))
# right-end tuck-down foot (small)
right_foot = bez((245, 102), (248, 108), (250, 115), (250, 122), n=20)
stroke(right_foot, (7, 3))

# === MIDDLE: 冖 covering ===
# left short descender (点/短撇)
left_desc = bez((70, 130), (68, 145), (66, 158), (62, 170), n=30)
stroke(left_desc, (7, 3))

# top horizontal of 冖
h_mid = bez((85, 145), (140, 143), (190, 143), (235, 146), n=60)
stroke(h_mid, (6, 6))
# shoulder dab at the 折 corner
dab(235, 146, 4.5)
# right 折 descender (short vertical dropping from right end of h_mid)
r_desc = bez((235, 146), (236, 160), (238, 175), (240, 188), n=30)
stroke(r_desc, (7, 5))

# === BOTTOM: 巾 box + center 竖钩 ===
# left 竖 of box
box_l = bez((100, 155), (100, 190), (100, 225), (100, 260), n=40)
stroke(box_l, (7, 7))

# right 横折钩 top-horizontal
box_top = bez((100, 165), (140, 163), (180, 163), (218, 166), n=40)
stroke(box_top, (6, 6))
# shoulder dab
dab(218, 166, 5)
# right 竖 down
box_r = bez((218, 166), (220, 200), (222, 230), (222, 258), n=40)
stroke(box_r, (7, 6))
# hook at bottom-right, UP-and-LEFT
box_hook = bez((222, 258), (216, 256), (210, 252), (204, 246), n=20)
stroke(box_hook, (7, 3))

# center 竖 through 巾, long, extends below the box with hook
cen = bez((155, 148), (155, 200), (155, 240), (155, 278), n=60)
stroke(cen, (8, 7))
# hook flick UP-and-LEFT
cen_hook = bez((155, 278), (149, 274), (143, 268), (137, 261), n=20)
stroke(cen_hook, (8, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0459_带/01_带.png")
