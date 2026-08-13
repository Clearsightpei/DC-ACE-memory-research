"""
Render 盃 (bei1, cup) at 300x300, black ink on white.

Structural read from GT:
  Top (upper half): 不 —
    - long 横 (top horizontal)
    - central 竖 dropping down from just under horizontal
    - 撇 sweeping down-left from horizontal
    - 点 dot down-right
  Bottom (lower half): 皿 (vessel base) —
    - left 竖 (vertical stroke on left of the bowl)
    - 竖折 forming the right side + bowl bottom
    - two inner short verticals
    - long 横 base (wider than the bowl above it)

Applies the calligraphic-weight 4-move:
  1. Teardrop taper on 撇 / 捺 / 点.
  2. Shoulder dab at 折 joints.
  3. Bezier for curved sweeps.
  4. Hook flicks (none in 盃 — 皿 has no hook).
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

# ===== TOP: 不 (occupies y ~ 30..145) =====
# 1) top horizontal (long, slightly rising then a small down-tilt on the right)
top_h = bez((55, 55), (110, 48), (185, 48), (240, 58), n=60)
stroke(top_h, (6, 6))

# 2) central 竖 dropping from just under the horizontal down to ~145
center_v = bez((150, 60), (150, 95), (150, 120), (150, 148), n=40)
stroke(center_v, (7, 7))

# 3) 撇 sweeping down-left from the crossing
pie = bez((148, 70), (130, 95), (105, 120), (78, 145), n=60)
stroke(pie, (8, 3))

# 4) 点 dot to the right (short taper down-right)
dot = bez((175, 85), (195, 100), (212, 115), (225, 128), n=40)
stroke(dot, (3, 9))

# ===== BOTTOM: 皿 (occupies y ~ 160..275) =====
# outer left 竖
left_v = bez((78, 175), (76, 205), (76, 235), (78, 260), n=40)
stroke(left_v, (7, 7))

# 竖折: right vertical + bottom-right corner + bowl bottom line
right_v = bez((222, 175), (222, 205), (222, 235), (222, 258), n=40)
stroke(right_v, (7, 7))
# shoulder dab at bottom-right corner where the fold would be if drawn continuous
dab(78, 260, 4.5)
dab(222, 258, 4.5)

# bowl bottom horizontal (connects the two verticals, inside the base line)
bowl_bottom = bez((80, 258), (140, 258), (185, 258), (222, 258), n=50)
stroke(bowl_bottom, (6, 6))

# inner short vertical 1 (left-of-center)
inner_v1 = bez((120, 185), (120, 210), (120, 235), (120, 258), n=40)
stroke(inner_v1, (6, 6))

# inner short vertical 2 (right-of-center)
inner_v2 = bez((180, 185), (180, 210), (180, 235), (180, 258), n=40)
stroke(inner_v2, (6, 6))

# top rim of 皿 (short horizontal touching top of the outer verticals)
top_rim = bez((80, 178), (140, 176), (185, 176), (222, 178), n=40)
stroke(top_rim, (5, 5))

# base long 横 (wider than the bowl, sits at the bottom)
base = bez((45, 280), (110, 275), (195, 275), (255, 282), n=60)
stroke(base, (7, 7))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0466_盃/01_盃.png")
