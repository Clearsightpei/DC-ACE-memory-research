"""
Render 疹 (zhen3) at 300x300, black ink on white.

SIGNATURE CHECK (疒 frozen-cohort row, memory_index TIER-0 G):
  疒 = 5 strokes:
    (1) 点 top-left of 一
    (2) 横 short across top
    (3) LONG curved 撇 from right end of 横 down to bottom-left (identity-carrying, MUST dominate)
    (4) inner 点 below 横, right of 撇
    (5) 提 rising short flick BELOW the inner 点
  Body 㐱 sits TUCKED inside canopy, top-right region.
  㐱 = 人 (top: small 撇+捺) + 彡 (three parallel down-left flicks).

Components-must-touch (TIER-0 H): 㐱 sits INSIDE the 撇 sweep, not to
its right in a detached column.
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

# ============ 疒 CANOPY ============

# (1) 点 top: small down-right teardrop, top-left region
dot1 = bez((105, 40), (110, 48), (115, 55), (118, 62), n=25)
stroke(dot1, (4, 9))

# (2) 横: short horizontal, starting from right of dot area, going right
h_top = bez((120, 75), (155, 72), (195, 72), (225, 76), n=50)
stroke(h_top, (7, 6))
# shoulder dab at right end for the 折-like turn into 撇
d.ellipse((219, 70, 233, 84), fill="black")

# (3) LONG 撇: from right-end of 横, sweeping down-left to bottom-left corner
# identity-carrying stroke, must dominate
pie_long = bez((225, 78), (170, 130), (110, 200), (55, 275), n=100)
stroke(pie_long, (11, 4))

# (4) inner 点: small dot below 横 on the left interior (under top area)
dot_inner = bez((100, 115), (105, 122), (110, 128), (113, 135), n=25)
stroke(dot_inner, (4, 8))

# (5) 提: rising short flick below the inner 点, angled up-right
ti = bez((80, 175), (100, 168), (118, 162), (135, 155), n=40)
stroke(ti, (8, 3))

# ============ 㐱 INNER BODY (tucked inside canopy, right side) ============

# 人 top: small 撇 + 捺 meeting at apex around (185, 115)
# 撇 (smaller, doesn't intrude far left)
ren_pie = bez((190, 108), (180, 130), (170, 150), (160, 170), n=50)
stroke(ren_pie, (7, 3))
# 捺
ren_na = bez((193, 112), (213, 140), (233, 165), (255, 185), n=60)
stroke(ren_na, (4, 10))
# foot flare
foot = bez((255, 185), (260, 187), (265, 188), (270, 189), n=15)
stroke(foot, (10, 3))

# 彡: three parallel down-left short flicks under the 人 (right region)
# top flick
f1 = bez((215, 180), (205, 195), (195, 208), (183, 222), n=40)
stroke(f1, (6, 3))
# middle flick
f2 = bez((230, 205), (218, 220), (205, 232), (190, 248), n=40)
stroke(f2, (6, 3))
# bottom flick (longest, most curved)
f3 = bez((245, 230), (225, 248), (205, 262), (183, 278), n=45)
stroke(f3, (7, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0526_疹/01_疹.png")
print("wrote PNG")
