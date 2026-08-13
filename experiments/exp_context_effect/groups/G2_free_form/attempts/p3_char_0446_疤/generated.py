"""
Render 疤 (bā, scar) at 300x300, black ink on white.

疤 = 疒 (illness canopy, 5 strokes) + 巴 (bā, 4 strokes)  — 9 strokes total.

疒 structure (canopy over top-left):
  1. 点         — small dot upper (a bit right of top-left)
  2. 横         — short horizontal across the top
  3. 撇         — long sweep from top down to lower-left
  4. 点         — short dot inside canopy, left
  5. 提         — short upward flick inside canopy, left below point 4

巴 structure (sits in bottom-right, tucked inside canopy):
  6. 横折       — top-and-right-side (goes right then turns down)
  7. 竖         — left down
  8. 横         — middle crossbar (touches both sides)
  9. 竖弯钩     — sweep down then right then hook UP-LEFT

Hook direction (per TIER-0 rule B): 竖弯钩 terminal flicks UP-and-LEFT.
Weight moves (per TIER-0 rule F): teardrop taper on 撇/点; Bezier for
sweeps; shoulder dabs at 折 joints.
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


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ================= 疒 canopy =================

# 1) 点 — top dot (upper-center-left of the canopy)
p1 = bez((95, 30), (98, 38), (102, 46), (108, 54), n=25)
stroke(p1, (3, 7))

# 2) 横 — short horizontal across the top of the canopy
h_top = bez((108, 58), (150, 55), (200, 55), (235, 58), n=40)
stroke(h_top, (5, 5))
# shoulder dab where 横 will connect to 撇's top (visual continuity)
dab(108, 58, 4)

# 3) 撇 — long left-down sweep, starts near the 横's left end,
#         curves down to lower-left. Teardrop taper (thick to thin).
pie = bez((108, 58), (95, 130), (75, 195), (40, 265), n=90)
stroke(pie, (11, 4))

# 4) 点 — inside dot, upper (small down-right dot) — well left of 巴
p_in1 = bez((78, 105), (83, 115), (88, 124), (93, 133), n=25)
stroke(p_in1, (3, 8))

# 5) 提 — inside upward flick (short, goes up-right) — below the dot
ti = bez((60, 175), (75, 168), (88, 162), (100, 158), n=30)
stroke(ti, (9, 3))

# ================= 巴 (sits tucked in bottom-right) =================
# Bounding box for 巴 approx: x 130–245, y 140–275 (tucked inside canopy)

# 6) 横折 — top horizontal + right vertical (one stroke)
hz_h = bez((132, 145), (165, 143), (215, 143), (240, 147), n=50)
stroke(hz_h, (6, 6))
dab(240, 147, 8)  # shoulder dab at 折 corner
hz_v = bez((240, 147), (241, 175), (241, 205), (240, 232), n=40)
stroke(hz_v, (6, 6))

# 7) 竖 — left vertical of 巴
sh_v = bez((134, 147), (133, 178), (132, 210), (132, 240), n=50)
stroke(sh_v, (6, 6))

# 8) 横 — middle crossbar of 巴
mid_h = bez((132, 190), (170, 188), (210, 188), (240, 190), n=40)
stroke(mid_h, (5, 5))

# 9) 竖弯钩 — bottom sweep from left corner down, right, hook UP-LEFT
seg = bez((132, 240), (137, 265), (185, 275), (240, 268), n=70)
stroke(seg, (7, 7))
# hook flick UP-and-LEFT at the right terminus
hook = bez((240, 268), (242, 258), (236, 248), (226, 240), n=25)
stroke(hook, (7, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0446_疤/01_疤.png")
