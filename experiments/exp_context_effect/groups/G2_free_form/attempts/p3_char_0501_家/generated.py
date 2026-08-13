"""
Render 家 (jia1) at 300x300, black ink on white.

Structural read from GT (10 strokes):
  Top: 宀 canopy (3 strokes)
    1. 点 top center
    2. 点/短竖 top-left descending
    3. 横钩 long horizontal with UP-LEFT hook at right end
  Bottom: 豕 (7 strokes)
    4. 短横 short horizontal under canopy center
    5. 撇 (long sweeping) from upper-left area down to lower-left
    6. 弯钩/short 撇 in middle
    7. 撇 (interior)
    8. 撇 (interior)
    9. 撇 (interior lower)
    10. 捺 sweeping down-right, foot-flared

TIER-0 applied:
  - Canopy body must TOUCH: 豕 tucked inside 宀's sweep, no vertical gap.
  - Hook flicks UP-and-LEFT (rule B).
  - All 撇/捺 use bezier + tapered stroke helper (rule F).
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


# ===================== 宀 canopy (top) =====================
# 1. 点 top center (small teardrop, sits ABOVE the horizontal)
dot_top = bez((148, 28), (150, 36), (152, 46), (154, 58), n=25)
stroke(dot_top, (3, 10))

# 2. 短竖/点 left shoulder of canopy — tucked at the LEFT END of horizontal,
#    descending down-left as a short tick.
left_tick = bez((72, 72), (74, 82), (78, 92), (82, 102), n=25)
stroke(left_tick, (4, 9))

# 3. 横钩 — long horizontal across, then hook UP-LEFT at right end
h_body = bez((72, 78), (130, 76), (190, 76), (240, 84), n=70)
stroke(h_body, (8, 9))
# hook flick DOWN-LEFT at right end (canopy hook goes down into body)
hook = bez((240, 84), (238, 96), (234, 108), (228, 118), n=25)
stroke(hook, (9, 3))

# ===================== 豕 (bottom) =====================
# 4. 短横 short horizontal near the top of 豕, just below canopy
h_short = bez((115, 128), (145, 126), (175, 126), (200, 130), n=40)
stroke(h_short, (6, 6))

# 5. 长撇 — the big sweeping 撇 starting near the horizontal's left,
#    sweeping down-left to lower-left corner
big_pie = bez((150, 130), (130, 175), (100, 220), (55, 270), n=90)
stroke(big_pie, (10, 3))

# 6. 弯钩 spine — from the horizontal center-right, curving down-left slightly,
#    ending with UP-LEFT flick
spine = bez((175, 138), (175, 175), (170, 215), (162, 250), n=60)
stroke(spine, (7, 6))
# hook flick UP-and-LEFT at bottom
spine_hook = bez((162, 250), (158, 245), (154, 240), (150, 234), n=15)
stroke(spine_hook, (6, 2))

# 7. inner 撇 upper — short slanted stroke branching off spine
inner_pie1 = bez((165, 165), (150, 178), (135, 192), (118, 205), n=35)
stroke(inner_pie1, (5, 3))

# 8. inner 撇 middle — another short curve inside body
inner_pie2 = bez((170, 195), (155, 210), (138, 225), (120, 240), n=35)
stroke(inner_pie2, (5, 3))

# 9. inner 撇 lower — final small 撇 near bottom
inner_pie3 = bez((155, 225), (140, 245), (125, 260), (108, 275), n=40)
stroke(inner_pie3, (5, 3))

# 10. 捺 — sweeping down-right from upper right area, with foot flare
na_main = bez((190, 155), (215, 195), (240, 235), (265, 275), n=80)
stroke(na_main, (5, 13))
# foot flare
foot = bez((265, 275), (270, 277), (275, 278), (278, 279), n=15)
stroke(foot, (13, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0501_家/01_家.png")
