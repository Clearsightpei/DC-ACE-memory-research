"""
Render 疫 (yi4) at 300x300, black ink on white.

Structural read from GT:
  疒 radical (wraps top+left):
    - 点   : small dot at top-center (slightly right of centerline)
    - 横   : long horizontal, slopes slightly up to the right, from
             upper-left to well past the horizontal center
    - 撇   : long enclosing 撇 sweeping from top-right down to the
             bottom-left corner (big curved back of 疒)
    - 冫   : two short interior tick strokes on the left side
             (upper tick and lower tick, both flick down-left)
  又 (sits inside, bottom-right of 疒):
    - 横撇 : short horizontal turning at shoulder into a down-left 撇
    - 捺   : long S-curve stroke sweeping from junction down-right,
             flaring at the foot

Applies TIER-0 F 4-move: Bezier curves everywhere, teardrop tapers,
shoulder dab at 横撇 corner, no straight-line strokes.
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
    """Draw variable-width stroke via overlapping circles."""
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


# --- 疒 radical ---

# 点 top dot: small teardrop sloping down-right
dot_top = bez((150, 30), (155, 36), (160, 44), (164, 52), n=25)
stroke(dot_top, (3, 7))

# 横 top horizontal: from left of center, sweeping slightly up-right,
# long, ends about 3/4 across the canvas
heng = bez((105, 68), (150, 62), (200, 58), (238, 55), n=60)
stroke(heng, (6, 6))

# 撇 long enclosing sweep: begins near right end of 横 (the 折
# shoulder), curves down and left, ending at bottom-left corner
# with a soft taper.
pie_big = bez((238, 62), (200, 130), (140, 200), (58, 280), n=100)
stroke(pie_big, (10, 4))
# shoulder dab where 横 meets big 撇
dab(238, 60, 6)

# 冫 (two interior ticks on left side of 疒)
# upper tick: short down-left flick
tick1 = bez((118, 118), (110, 128), (102, 138), (95, 148), n=25)
stroke(tick1, (7, 3))

# lower tick: short down-left flick, larger and lower
tick2 = bez((100, 170), (92, 182), (85, 195), (78, 208), n=25)
stroke(tick2, (7, 3))

# --- 又 inside, sits in the bottom-right pocket of 疒 ---

# 横撇 : short horizontal then turn into down-left 撇
# horizontal segment
h_top = bez((138, 128), (165, 126), (190, 128), (210, 132), n=40)
stroke(h_top, (5, 5))
# shoulder dab at fold
dab(210, 132, 6)
# down-left 撇 sweeping into the middle
pie_you = bez((210, 132), (185, 175), (155, 210), (128, 245), n=70)
stroke(pie_you, (9, 3))

# 捺 : S-curve from junction near top of 又 sweeping down-right,
# ending with a flared foot near bottom-right
na_main = bez((172, 152), (195, 195), (225, 230), (252, 258), n=80)
stroke(na_main, (4, 12))
# foot flare
foot = bez((252, 258), (258, 262), (262, 266), (266, 268), n=15)
stroke(foot, (12, 4))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0450_疫/01_疫.png")
