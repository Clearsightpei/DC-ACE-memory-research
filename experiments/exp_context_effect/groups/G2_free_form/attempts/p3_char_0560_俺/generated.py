"""
Render 俺 (an3) at 300x300, black ink on white.

Structural read from GT:
  Left:  亻 radical (short 撇 + medium 竖 ending mid-body ~y=205).
  Right: 奄 = 大 top canopy + 日 small box (middle) + 乚 竖弯钩 bottom sweep.
    - 大 = 横 + 撇 + 捺
    - 日 (small) tucked under the canopy apex
    - 乚 starts left of 日, drops, arcs right, flicks UP-LEFT

Revision 1 fixes:
  - 亻 竖 shortened (was too long — extended past body).
  - 日 narrowed and lifted (was too wide, overlapping 亻).
  - 乚 vertical begins further left so its arc wraps under 日.
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


def dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 亻 radical (left column) ---
# 撇 short pie
pie_ren = bez((80, 70), (73, 100), (65, 125), (55, 150), n=60)
stroke(pie_ren, (9, 4))
# 竖 medium length — end mid-body so it touches the right component's belt
shu_ren = bez((78, 105), (78, 150), (78, 190), (78, 220), n=60)
stroke(shu_ren, (7, 7))

# --- 奄 right component ---
# TOP: 大 (横 + 撇 + 捺) — apex centered on right block
# 横
h_da = bez((115, 70), (155, 66), (200, 66), (245, 70), n=40)
stroke(h_da, (6, 6))
# 撇 of 大
pie_da = bez((180, 58), (162, 90), (140, 115), (115, 138), n=60)
stroke(pie_da, (9, 3))
# 捺 of 大
na_da = bez((180, 70), (200, 100), (225, 122), (250, 140), n=60)
stroke(na_da, (4, 11))
foot = bez((250, 140), (256, 142), (261, 143), (265, 143), n=20)
stroke(foot, (11, 3))

# MIDDLE: 日 small box (~x 145..220, y 148..195)
lv = bez((145, 150), (145, 170), (145, 185), (145, 195), n=30)
stroke(lv, (6, 6))
th = bez((145, 150), (175, 148), (200, 148), (220, 150), n=40)
stroke(th, (6, 6))
dab(220, 150, 4)
rv = bez((220, 150), (220, 170), (220, 185), (220, 195), n=30)
stroke(rv, (6, 6))
mh = bez((147, 173), (175, 172), (200, 172), (218, 173), n=30)
stroke(mh, (5, 5))
bh = bez((145, 195), (175, 195), (200, 195), (220, 195), n=30)
stroke(bh, (6, 6))

# BOTTOM: 乚 竖弯钩 — vertical begins slightly left of the 日,
# drops down, curves right beneath, flick UP-LEFT at end.
sw_v = bez((125, 200), (125, 225), (128, 250), (135, 270), n=50)
stroke(sw_v, (7, 6))
sw_arc = bez((135, 270), (160, 282), (200, 285), (240, 278), n=60)
stroke(sw_arc, (6, 6))
hook = bez((240, 278), (244, 270), (242, 260), (235, 253), n=25)
stroke(hook, (6, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0560_俺/01_俺.png")
