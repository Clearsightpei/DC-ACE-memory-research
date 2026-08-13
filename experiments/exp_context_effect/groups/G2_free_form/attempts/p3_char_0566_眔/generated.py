"""
Render 眔 at 300x300, black ink on white.

Structural read from GT:
  Top:    罒 (net radical) — outer box with two inner verticals.
          Strokes: left 竖, 横折 (top-and-right), inner 竖 x2, bottom 横.
  Bottom: 氺-like — short horizontal, central 竖(钩), left 撇, right 捺.
          Hook flick UP-and-LEFT per TIER-0 rule B.
Apply calligraphic-weight 4-move: bezier curves, teardrop taper,
shoulder dab at 折 corner. Components TOUCH (罒 bottom line == body top).
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

# --- 罒 top ---
# Left 竖: (75,50) → (75,140)
left_v = bez((80, 50), (80, 80), (80, 110), (78, 140), n=40)
stroke(left_v, (6, 7))

# 横折: top horizontal (80,50)→(225,50), then vertical (225,50)→(225,140)
top_h = bez((78, 52), (120, 48), (170, 46), (225, 50), n=50)
stroke(top_h, (7, 7))
dab(224, 52, 5)  # shoulder dab at 折 corner
right_v = bez((225, 50), (226, 82), (226, 112), (225, 140), n=40)
stroke(right_v, (7, 6))

# Inner left 竖: (128,60) → (128,138)
inner_l = bez((128, 62), (128, 90), (128, 115), (128, 138), n=40)
stroke(inner_l, (5, 5))

# Inner right 竖: (175,60) → (175,138)
inner_r = bez((175, 62), (175, 90), (175, 115), (175, 138), n=40)
stroke(inner_r, (5, 5))

# Bottom 横: (75,140) → (225,140) — closes the net
bot_h = bez((76, 140), (120, 142), (170, 142), (226, 140), n=50)
stroke(bot_h, (6, 7))

# --- 氺-like bottom (touching 罒 at y~140) ---

# Short top horizontal of bottom (like the 一 of 水)
top_bar = bez((115, 155), (140, 153), (170, 153), (195, 156), n=40)
stroke(top_bar, (5, 6))

# Central 竖 with slight hook (spine of water)
spine = bez((152, 158), (152, 200), (152, 240), (150, 270), n=60)
stroke(spine, (7, 7))
# Hook flick UP-and-LEFT
hook = bez((150, 270), (145, 265), (139, 258), (132, 250), n=25)
stroke(hook, (7, 3))

# Left 撇 — long, from upper-mid inside 罒-region, sweeping down-left
left_pie = bez((140, 170), (115, 200), (90, 235), (55, 280), n=70)
stroke(left_pie, (7, 3))

# Right 捺 — long, from upper-mid, sweeping down-right with foot flare
right_na = bez((165, 170), (190, 205), (215, 240), (245, 275), n=70)
stroke(right_na, (4, 11))
foot = bez((245, 275), (250, 277), (255, 278), (260, 278), n=15)
stroke(foot, (11, 4))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0566_眔/01_眔.png")
