"""
p3_char_0564_倀 — 亻 (left) + 長 (right, traditional).
Applying calligraphic-weight 4-move (TIER-0 F): tapers on 撇/捺,
bez curves for 撇/捺, hook flick UP-and-LEFT.

Components MUST touch (TIER-0 H): 亻 竖 must sit adjacent to /
touching 長's left edge, not floating in a detached column.

長 structure (8 strokes traditional):
  1. 横 (top short-mid horizontal)
  2. 竖 (vertical descending from top-right of top-横)
  3. 横 (upper interior)
  4. 横 (mid interior)
  5. 横 (longer bottom-of-top-stack, extends right)
  6. 撇 (descends from mid-left, sweeps down-left)
  7. 竖提 (short vertical + tick) — inside body
  8. 捺 (long sweep from mid down-right past bottom)
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


# ==================== 亻 (left radical) ====================
# 撇 — head near x=75 y=50, sweeps down-left to x=40 y=175 (bowed)
pie = bez((78, 50), (72, 90), (60, 130), (38, 180), n=70)
stroke(pie, (9, 3))

# 竖 — vertical drop, top touches 撇 body at ~x=70 y=105
shu = bez((72, 108), (72, 155), (72, 210), (72, 255), n=60)
stroke(shu, (6, 6))
# shoulder dab at top of 竖
d.ellipse((67, 104, 78, 115), fill="black")


# ==================== 長 (right) ====================
# ----- top stack (4 horizontals + vertical) -----
# Stroke 1: top 横 — from x=115 y=65 to x=225 y=62
h1 = bez((115, 68), (150, 65), (195, 63), (230, 62), n=40)
stroke(h1, (5, 5))

# Stroke 2: 竖 — descends from right end of top 横, down to y=175
shu2 = bez((150, 68), (150, 100), (150, 130), (150, 165), n=50)
stroke(shu2, (6, 6))

# Stroke 3: 横 (upper interior short) — x=150 to x=220 at y=100
h2 = bez((155, 100), (180, 99), (200, 99), (218, 100), n=40)
stroke(h2, (5, 5))

# Stroke 4: 横 (mid interior short) — x=150 to x=220 at y=135
h3 = bez((155, 133), (180, 132), (200, 132), (218, 133), n=40)
stroke(h3, (5, 5))

# Stroke 5: 横 (bottom of top-stack, extends further right and left) — long horizontal
h4 = bez((112, 168), (150, 166), (200, 166), (250, 167), n=50)
stroke(h4, (6, 6))

# ----- bottom (撇, 竖提, 捺 forming 衣-like base) -----
# Stroke 6: 撇 — from x=145 y=168 down-left to x=100 y=270 (bowed, taper)
pie2 = bez((148, 172), (135, 200), (120, 235), (98, 275), n=70)
stroke(pie2, (7, 3))

# Stroke 7: short 竖提 inside — small vertical from x=165 y=180 to x=165 y=225, tick up-right
sg = bez((168, 180), (168, 200), (168, 220), (168, 232), n=40)
stroke(sg, (5, 5))
# tick (提) up-right
tick = bez((168, 232), (185, 225), (200, 218), (215, 210), n=25)
stroke(tick, (5, 2))

# Stroke 8: 捺 — from ~x=170 y=180 sweeping down-right to x=270 y=270 (thick-tail sweep)
na = bez((172, 178), (200, 210), (230, 240), (268, 270), n=80)
stroke(na, (4, 12))
# foot flare at end of 捺
foot = bez((268, 270), (275, 272), (280, 272), (283, 272), n=20)
stroke(foot, (12, 3))


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0564_倀/01_倀.png"
)
print("saved")
