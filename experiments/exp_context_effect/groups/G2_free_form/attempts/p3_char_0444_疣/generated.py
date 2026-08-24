"""
Render 疣 (you2) at 300x300, black ink on white.

Structural read from GT:
  疒 radical (top+left wrap):
    - 点 at top-center (small dot slanting down-right)
    - 横 short horizontal starting from top-center going right
    - 撇 long sweeping stroke from top-center down-left to bottom-left
    - two short 点 dots stacked on the inside-left of the 疒 curve
  尤 inside (right-lower):
    - 横 short horizontal at upper-right (slight left-to-right)
    - 撇 sweeping down-left from that horizontal
    - 竖弯钩 rising from the 撇 midpoint, going down then curving right, hook UP-and-LEFT at tail
    - 点 at upper-right corner

Apply the calligraphic 4-move: teardrop taper, shoulder dab at 折,
bezier for curves, hook flick UP-and-LEFT.
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

# ==== 疒 radical ====

# 点 at top-center (small down-right slanting dot)
top_dot = bez((115, 40), (120, 46), (125, 52), (130, 58), n=25)
stroke(top_dot, (3, 8))

# 横 short horizontal at the top of 疒, running right from ~ (115, 65) to (200, 70)
# shoulder dab at the right end where it will implicitly turn
heng = bez((115, 68), (140, 66), (170, 66), (200, 70), n=50)
stroke(heng, (7, 6))
dab(200, 70, 4.5)  # shoulder dab at right end

# 撇 long sweep from top-center down-left (a bit less extreme)
pie = bez((118, 68), (95, 130), (65, 190), (30, 275), n=100)
stroke(pie, (10, 3))

# two 点 dots inside the 疒 curve (to the right of the 撇, in the interior)
# upper dot: small down-right dot
dot1 = bez((92, 115), (97, 122), (101, 128), (105, 133), n=20)
stroke(dot1, (3, 7))
# lower dot: small down-right dot
dot2 = bez((78, 158), (83, 165), (88, 171), (92, 176), n=20)
stroke(dot2, (3, 7))

# ==== 尤 inside (right/lower) ====

# 横 upper (slightly slanting up), from (145, 110) to (240, 105)
you_heng = bez((145, 112), (175, 108), (210, 107), (245, 108), n=50)
stroke(you_heng, (6, 6))

# 撇 sweeping down-left from the 横 mid-left, ending at lower-left of the 尤 area
you_pie = bez((165, 105), (155, 150), (145, 195), (135, 240), n=80)
stroke(you_pie, (9, 3))

# 竖弯钩: starts from the 撇 upper area (~180,120), goes down then curves right, hook UP-LEFT
# Segment 1: down from (185, 120) to (185, 220)
sg_down = bez((185, 125), (188, 165), (188, 200), (188, 225), n=60)
stroke(sg_down, (7, 7))
# shoulder dab at the arc's start
dab(188, 225, 5)
# Segment 2: arc curving right to (255, 260)
sg_arc = bez((188, 230), (200, 258), (225, 268), (255, 262), n=60)
stroke(sg_arc, (7, 6))
# hook flick UP-and-LEFT at (255, 262)
hook = bez((255, 262), (255, 252), (252, 244), (248, 236), n=25)
stroke(hook, (6, 2))

# 点 at upper-right corner of 尤 (small down-right dot around 250, 80)
you_dot = bez((248, 78), (253, 85), (258, 91), (262, 96), n=20)
stroke(you_dot, (3, 7))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0444_疣/01_疣.png")
