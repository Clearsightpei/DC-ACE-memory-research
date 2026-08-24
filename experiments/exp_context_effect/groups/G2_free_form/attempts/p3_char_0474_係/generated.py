"""
Render 係 (xi4) at 300x300, black ink on white.

Structure:
  Left: 亻 (single-person radical) — 撇 sweeping down-left, 竖 vertical
  Right: 系 — top short 丿 dab, then folded/curled body (like 幺 with
         upper 折), then bottom 小-like three feet (撇/竖/捺-dots).

Apply TIER-0 F: bezier sweeps, teardrop taper, hook flick UP-LEFT.
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


# ============== 亻 (left radical) ==============
# 撇 — from ~upper-center-left down to lower-left, bowed
pie1 = bez((85, 55), (78, 105), (65, 150), (48, 200), n=80)
stroke(pie1, (10, 5))

# 竖 — from the mid of the 撇 straight down
shu1 = bez((78, 118), (78, 170), (78, 220), (78, 268), n=60)
stroke(shu1, (9, 8))

# ============== 系 (right) ==============
# Top small 丿 (short slanting flick, top-right area)
top_pie = bez((175, 40), (170, 55), (160, 68), (145, 82), n=40)
stroke(top_pie, (9, 3))

# Upper 折 body — like a horizontal-fold then a small hook loop.
# Draw a compact 幺-like shape: horizontal top, then dropping curve.
# Segment 1: horizontal top (小横)
h_top = bez((150, 90), (175, 88), (205, 88), (230, 92), n=40)
stroke(h_top, (6, 6))

# Segment 2: 折 down-and-in from right end
fold1 = bez((228, 92), (230, 100), (222, 115), (210, 128), n=40)
stroke(fold1, (7, 6))

# Segment 3: little loop / bowl (幺 upper coil)
loop1 = bez((210, 128), (195, 138), (185, 148), (180, 158), n=40)
stroke(loop1, (6, 5))

# Segment 4: small 折 curl closing the coil rightward
loop2 = bez((180, 158), (195, 165), (215, 168), (230, 165), n=40)
stroke(loop2, (5, 6))

# Middle: another small horizontal like the "waist" of 系
h_mid = bez((160, 190), (185, 188), (215, 188), (235, 192), n=40)
stroke(h_mid, (5, 5))

# ============== bottom 小 (three feet under 系) ==============
# Left dab (撇 flick)
left_foot = bez((165, 210), (155, 230), (148, 250), (140, 270), n=40)
stroke(left_foot, (7, 3))

# Center vertical short (竖) — the "leg" under the coil
mid_foot = bez((195, 208), (195, 235), (195, 258), (195, 275), n=40)
stroke(mid_foot, (6, 6))
# hook flick UP-LEFT
mid_hook = bez((195, 275), (190, 270), (184, 264), (178, 258), n=20)
stroke(mid_hook, (6, 3))

# Right dab (捺-dot)
right_foot = bez((225, 215), (238, 235), (250, 255), (260, 272), n=40)
stroke(right_foot, (4, 8))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0474_係/01_係.png")
