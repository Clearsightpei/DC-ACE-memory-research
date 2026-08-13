"""
Render 爱 (ai4) at 300x300, black ink on white.

Simplified 爱 decomposition (10 strokes):
  Top 爫 (claw):  ノ + three short 丶/vertical dashes (4 strokes)
  Middle 冖:      horizontal cover with a small drop at right end
                  plus an under-horizontal (the base of 爫 becomes 冖-top)
  Bottom 友-like: 一 (short horiz mid), 撇 (long sweep down-left),
                  又 (横撇 + 捺 crossing bottom-right)

Applying TIER-0 F: teardrop taper for 撇/捺, bezier for curves,
components must touch (H rule).
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


# ============ Top 爫 (4 strokes) ============
# leftmost ノ short slash
s1 = bez((100, 45), (96, 55), (92, 62), (88, 70), n=30)
stroke(s1, (7, 3))

# three short vertical/near-vertical descending dashes
s2 = bez((130, 45), (131, 55), (132, 62), (133, 72), n=30)
stroke(s2, (6, 4))

s3 = bez((165, 45), (167, 55), (170, 62), (173, 72), n=30)
stroke(s3, (6, 4))

s4 = bez((200, 50), (205, 60), (210, 68), (215, 78), n=30)
stroke(s4, (5, 8))  # rightmost gets a bit heavier like a 点

# ============ Long horizontal (top of 冖) ============
h_top = bez((70, 100), (130, 96), (190, 96), (230, 100), n=60)
stroke(h_top, (6, 6))

# ============ 冖 cover: right-end drop ============
# small vertical drop at right end of the top horizontal (the 冖 fold)
drop = bez((230, 100), (232, 115), (233, 130), (232, 145), n=30)
stroke(drop, (6, 5))

# left-side small dot/hat of 冖
left_hat = bez((70, 100), (68, 108), (67, 115), (67, 122), n=25)
stroke(left_hat, (6, 4))

# ============ Middle horizontal (inside 冖) ============
h_mid = bez((90, 155), (140, 152), (185, 152), (220, 155), n=50)
stroke(h_mid, (6, 6))

# ============ Big 撇 sweep from mid-upper-right down to bottom-left ============
pie_big = bez((175, 145), (150, 190), (110, 230), (65, 270), n=90)
stroke(pie_big, (10, 4))

# ============ 又 at bottom-right ============
# 横撇: horizontal segment then folds down-left
heng_pie_h = bez((115, 205), (150, 203), (185, 203), (215, 205), n=40)
stroke(heng_pie_h, (6, 6))
# shoulder dab at fold
d.ellipse((208, 199, 222, 213), fill="black")
# 撇 part
heng_pie_p = bez((215, 205), (200, 225), (180, 245), (155, 275), n=50)
stroke(heng_pie_p, (8, 3))

# 捺: from crossing near mid-bottom, sweeps down-right with foot
na = bez((175, 225), (200, 245), (225, 260), (255, 275), n=60)
stroke(na, (4, 12))
# foot flare
foot = bez((255, 275), (262, 275), (268, 275), (272, 274), n=20)
stroke(foot, (12, 4))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0541_爱/01_爱.png")
