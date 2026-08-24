"""
Render 疭 at 300x300, black ink on white.

Structural read from GT:
  疒 (sickness radical, top+left wrap):
    - short 点 top-left
    - 横 (short horizontal, upper)
    - long 撇 sweeping from top-right of the horizontal down to bottom-left
    - two small inside strokes: upper 点 and lower 提 (rising short)
  从 (inside/right of 疒):
    - left 人-component: 撇 + right-side compressed 点/dot
    - right 人: full 撇 + 捺

Apply 4-move calligraphic weight recipe (TIER-0 F):
  - teardrop taper on all 撇/捺/点
  - shoulder dab on 折 joints
  - bezier for curved sweeps
  - hook flicks UP-and-LEFT (n/a here — no hooks in 疭)
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
    """Variable-width stroke via overlapping circles."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============== 疒 wrapper ==============

# 1) top 点 — small teardrop, tilted down-right
top_dot = bez((78, 45), (82, 52), (86, 58), (92, 65), n=25)
stroke(top_dot, (3, 8))

# 2) 横 — short horizontal, upper area, going right from ~ x=70 to x=175
heng = bez((70, 78), (100, 76), (140, 76), (175, 80), n=40)
stroke(heng, (7, 6))

# shoulder dab at the right end (before the 撇 turns down — actually 疒 has
# the 撇 starting from near the right end of the 横; add a dab at joint)
r = 5
d.ellipse((175 - r, 80 - r, 175 + r, 80 + r), fill="black")

# 3) long 撇 — from the right end of 横 sweeping down-left to bottom
pie_long = bez((175, 78), (140, 130), (100, 190), (55, 275), n=90)
stroke(pie_long, (10, 3))

# 4) inside upper 点 (inside 疒, upper) — small dot leaning down-right
in_dot = bez((92, 115), (97, 122), (102, 128), (108, 135), n=25)
stroke(in_dot, (3, 8))

# 5) inside lower 提 — short rising stroke (thick to thin), going up-right
ti = bez((85, 175), (100, 168), (115, 162), (135, 155), n=35)
stroke(ti, (8, 3))

# ============== 从 (two 人 inside right area) ==============
# Position: below 横 (y > 100), right of 疒's 撇. Two people side-by-side.

# --- left 人 ---
# 撇 — apex near (155, 130), sweeps down-left
left_pie = bez((155, 130), (140, 170), (130, 205), (115, 245), n=70)
stroke(left_pie, (8, 3))
# right side: compressed 捺 becomes 点 (dot)
left_dot = bez((158, 145), (170, 175), (180, 200), (188, 225), n=45)
stroke(left_dot, (3, 9))

# --- right 人 ---
# 撇 — apex near (225, 120), sweeps down-left
right_pie = bez((225, 120), (208, 165), (195, 210), (180, 260), n=80)
stroke(right_pie, (9, 3))
# 捺 — from apex, sweeps down-right with S-curve and foot flare
right_na = bez((228, 135), (245, 180), (258, 220), (275, 265), n=80)
stroke(right_na, (4, 12))
# foot flare on 捺
foot = bez((275, 265), (280, 267), (285, 268), (290, 269), n=20)
stroke(foot, (12, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0454_疭/01_疭.png")
