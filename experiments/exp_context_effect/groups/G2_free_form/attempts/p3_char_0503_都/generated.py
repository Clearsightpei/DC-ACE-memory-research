"""
Render 都 (dū) — 10 strokes. Left-right compound:
  Left: 者 (老字头 top + 日 bottom) — takes ~60% of width.
  Right: 阝 (右耳旁) — takes ~40%, tucked so it touches 者.

TIER-0 checks consulted:
- 者 is NOT a sibling-risk target; 阝 is not either.
- Hook rule (B): 阝's 横撇弯钩 flicks UP-and-LEFT into the body.
- Rule H (components must touch): 者's right edge overlaps with 阝's
  left extent by ~5-10px. 者's 日 sits under the 撇 tail on left.
- Rule F (calligraphic 4-move): using bez + variable-width stroke().

Structure adapted from prior PASS attempts:
  p3_char_0373_者/generated.py (者 alone)
  p2_radical_020_阝/generated.py (阝 alone)
"""
from PIL import Image, ImageDraw
import math, os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=80):
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


def line_str(p0, p1, w, n=None):
    if n is None:
        n = int(max(30, math.hypot(p1[0]-p0[0], p1[1]-p0[1]) * 2))
    pts = [(p0[0] + (p1[0]-p0[0])*i/n, p0[1] + (p1[1]-p0[1])*i/n) for i in range(n+1)]
    stroke(pts, w)


# ============ LEFT: 者 (compressed to left ~60%) ============
# Top: 老字头
# S1: short 横 near top
line_str((45, 55), (135, 52), (7, 7))

# S2: 竖 through it — short, only pokes above/below 横 slightly
line_str((90, 40), (90, 108), (7, 7))

# S3: long slanting 横 (spans wide, extends into right side to touch 阝)
line_str((15, 118), (195, 112), (8, 8))

# S4: long 撇 sweeping from upper-right down to lower-left
pie = bez((155, 68), (130, 130), (85, 195), (25, 275), n=100)
stroke(pie, (9, 4))

# Bottom: 日 (positioned under 老字头, slightly right of center-left)
LX, RX = 75, 160
TY, BY = 170, 258

# S5: 竖 (left of 日)
line_str((LX, TY), (LX, BY), (7, 7))

# S6: 横折 (top + right side of 日) — corner needs a shoulder dab
line_str((LX, TY), (RX, TY), (7, 7))
d.ellipse((RX-5, TY-5, RX+5, TY+5), fill="black")  # shoulder dab
line_str((RX, TY), (RX, BY), (7, 7))

# S7: middle 横 of 日
line_str((LX + 4, 214), (RX - 4, 214), (5, 5))

# S8: bottom 横 of 日
line_str((LX, BY), (RX, BY), (7, 7))


# ============ RIGHT: 阝 (右耳旁, taller, ear on top) ============
# Ear is smaller and higher; 竖 is long, extends full height for right 耳.
# Positioned so its 竖 sits around x=225, ear around x=190-260.
# Overlap with 者: 者's 横 (S3) extends to x=200, 阝's ear starts near x=195 -> touching.

# Stroke 9: 横撇弯钩 (the "ear" — a "3" or "ε" laid on its back)
# small 横 at top
line_str((195, 82), (245, 78), (6, 6))
d.ellipse((243-5, 78-5, 243+5, 78+5), fill="black")  # 折 shoulder

# first curve: from corner down-and-left to inner tuck
bezier_pts = bez((245, 78), (258, 105), (215, 122), (208, 118), n=80)
# above bez signature is p0,p1,p2,p3 cubic — do it right
c1 = bez((245, 78), (258, 100), (245, 125), (215, 128), n=80)
stroke(c1, (6, 5))

# second curve: form lower lobe belly
c2 = bez((215, 128), (260, 138), (255, 165), (205, 168), n=80)
stroke(c2, (5, 5))

# terminal 钩 flick UP-and-LEFT (into character body)
hook = bez((205, 168), (200, 162), (196, 155), (190, 150), n=40)
stroke(hook, (5, 2))

# Stroke 10: 竖 (long vertical for 右耳, extends further down than left ear)
# from joint area (~215, 128) straight down to ~215, 285.
line_str((215, 128), (215, 288), (7, 7))
d.ellipse((215-5, 128-5, 215+5, 128+5), fill="black")  # loaded start


out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0503_都/01_都.png"
img.save(out_path)
print(f"saved {out_path}")
