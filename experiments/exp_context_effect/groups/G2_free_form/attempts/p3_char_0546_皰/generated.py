"""
Render 皰 (pao4) at 300x300, black ink on white.

Structure: 皮 (left) + 包 (right)
  皮 (5 strokes): top 横+短撇, long 撇 sweep, 又 middle, 捺 bottom
  包 (5 strokes): top 撇, 横折钩 wrap enclosing 巳 inside

Revision 2: fix inner 巳 (was floating rectangle, wrong position);
clean up 皮 又-piece topology.
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


# ============ LEFT: 皮 (x range ~15..135) ============

# 1) top 横 — starting a little indented, going right
h1 = bez((45, 78), (65, 76), (85, 75), (108, 78), n=50)
stroke(h1, (5, 6))

# 2) short right-turn flick at top-right (part of 横撇 or 横钩)
flick1 = bez((108, 78), (112, 85), (114, 95), (114, 105), n=25)
stroke(flick1, (6, 4))
dab(108, 79, 4)

# 3) long 撇 — starts inside the top 横 at ~x=68, sweeps down-left
pie = bez((70, 82), (58, 130), (42, 180), (18, 245), n=90)
stroke(pie, (10, 4))

# 4) 又 interior: horizontal top of 又 (crossing the 撇)
h2 = bez((60, 130), (80, 128), (100, 128), (120, 130), n=40)
stroke(h2, (5, 5))

# 5) 又's left leg (小撇) from top-right of 又 sweeping down-left
leg1 = bez((105, 130), (95, 155), (80, 180), (58, 210), n=60)
stroke(leg1, (7, 3))

# 6) 又's 捺 — the big bottom-right sweep
na = bez((92, 145), (110, 180), (128, 210), (148, 240), n=80)
stroke(na, (4, 12))
foot = bez((148, 240), (154, 241), (160, 240), (164, 238), n=15)
stroke(foot, (12, 3))


# ============ RIGHT: 包 (x range ~135..280) ============

# 1) top 撇 — sweeps down-left
pie2 = bez((190, 55), (178, 78), (170, 95), (162, 112), n=50)
stroke(pie2, (10, 3))

# 2) 横折钩 wrap
wrap_h = bez((162, 112), (195, 108), (225, 108), (252, 112), n=60)
stroke(wrap_h, (6, 7))
dab(252, 114, 5)
wrap_v = bez((252, 112), (254, 155), (250, 200), (238, 240), n=70)
stroke(wrap_v, (8, 8))
# hook flick UP-and-LEFT
hook = bez((238, 240), (228, 236), (218, 230), (206, 224), n=30)
stroke(hook, (8, 3))

# 3) inner 巳 — top 横折 (forms upper box of 巳)
inner_top = bez((180, 145), (200, 143), (218, 143), (232, 145), n=45)
stroke(inner_top, (5, 5))
dab(232, 146, 4)
# right side going down to mid
inner_right = bez((232, 145), (232, 160), (232, 175), (232, 185), n=30)
stroke(inner_right, (5, 5))

# 4) middle 横 (closing top box of 巳) at y~185
inner_mid = bez((180, 185), (200, 185), (218, 185), (232, 185), n=40)
stroke(inner_mid, (5, 5))

# 5) 竖弯 — left vertical starts at top of 巳, comes down and curves right
left_v = bez((180, 145), (180, 175), (180, 200), (185, 215), n=50)
stroke(left_v, (5, 5))
# curve out to the right at bottom
curve_out = bez((185, 215), (195, 220), (208, 220), (220, 218), n=40)
stroke(curve_out, (5, 5))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0546_皰/01_皰.png")
