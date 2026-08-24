"""
Render 济 (ji4) at 300x300, black ink on white.

Structural read from GT:
  Left:  氵 (three-dots water) — top dot, mid dot, bottom 提 (rising tick)
  Right: 齐
    - top: 亠 (small dot + long horizontal)
    - middle: 撇 + 捺 inverted V under the horizontal
    - bottom: two verticals (撇 on left, 竖 on right)

4-move calligraphy: taper via widths, bezier for curves, shoulder dab n/a here,
hook flick n/a (齐 has no hook — bottom is a 撇 and a 竖).
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

# ============ 氵 (left, three-dots water) ============
# Top dot (small, points down-right)
d1 = bez((55, 75), (62, 82), (68, 90), (72, 98), n=30)
stroke(d1, (3, 9))

# Middle dot (a bit lower and slightly right, similar shape)
d2 = bez((45, 130), (52, 138), (58, 146), (62, 154), n=30)
stroke(d2, (3, 9))

# Bottom 提 (rising tick — starts low-left, sweeps up-right)
tii = bez((50, 210), (65, 200), (82, 190), (100, 178), n=40)
stroke(tii, (10, 2))

# ============ 齐 (right) ============
# --- 亠 top ---
# small dot (top, slight left of center of 齐)
top_dot = bez((165, 45), (172, 52), (178, 60), (182, 68), n=30)
stroke(top_dot, (3, 9))

# long horizontal (spans most of right side)
h_top = bez((115, 92), (155, 88), (215, 88), (265, 92), n=60)
stroke(h_top, (7, 7))

# --- 撇 + 捺 inverted V ---
# 撇: starts near center-top under horizontal, sweeps down-left
pie = bez((185, 100), (165, 135), (140, 165), (110, 195), n=70)
stroke(pie, (10, 4))

# 捺: starts near same apex, sweeps down-right with belly and foot flare
na = bez((190, 100), (215, 140), (240, 170), (265, 195), n=70)
stroke(na, (5, 12))
foot = bez((265, 195), (270, 197), (274, 199), (278, 200), n=20)
stroke(foot, (12, 3))

# --- bottom two verticals ---
# left 撇 (short, curves down-left slightly)
left_v = bez((160, 200), (155, 225), (148, 250), (138, 275), n=50)
stroke(left_v, (8, 4))

# right 竖 (straight-ish vertical, slightly right of center)
right_v = bez((220, 200), (220, 230), (220, 255), (220, 278), n=50)
stroke(right_v, (7, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0481_济/01_济.png")
