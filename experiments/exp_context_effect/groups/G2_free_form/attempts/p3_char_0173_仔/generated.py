"""
Render 仔 (p3_char_0173_仔) at 300x300 with PIL.

Composition: 亻 (left, ~35% width) + 子 (right, ~55% width).

# SIGNATURE CHECK (子, sibling-risk):
#   子 = full 横 crossing 竖钩. Not partial tick (孑/孓).
#   Hook flicks UP-and-LEFT at bottom (per TIER-0 B).

亻 (left, compressed to left ~x=45..115):
  1. 撇: from (105, 50) sweeping down-left to (55, 175).
  2. 竖: from (100, 105) straight drop to (100, 245).

子 (right, ~x=125..270):
  3. 横撇 (head): 横 from (135, 80) to (250, 70), shoulder turn,
     撇 down-left to (155, 145).
  4. 弯钩 (spine): from (205, 95) descending, curving, hook up-left.
  5. 横 (long cross-bar): from (125, 175) to (275, 173), crossing spine.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=7):
    d.line(points, fill=BLACK, width=width, joint="curve")
    for (x, y) in (points[0], points[-1]):
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK)


# ---------- 亻 (left radical) ----------
# Stroke 1: 撇 (steep down-left)
pie = [(108, 55), (98, 90), (85, 125), (68, 160), (52, 185)]
stroke(pie, width=7)
dab(108, 55, 4)

# Stroke 2: 竖 (vertical drop from mid-撇)
shu = [(100, 108), (100, 160), (100, 210), (100, 250)]
stroke(shu, width=7)
dab(100, 108, 4)


# ---------- 子 (right side) ----------
# Stroke 3: 横撇 (head) — 横 then shoulder, then 撇 down-left
horiz_start = (138, 82)
shoulder = (248, 72)
pie_end = (158, 148)
stroke([horiz_start, shoulder], width=7)
dab(shoulder[0], shoulder[1], 6)  # shoulder 顿
stroke([shoulder, (220, 100), (190, 122), pie_end], width=7)
dab(horiz_start[0], horiz_start[1], 4)

# Stroke 4: 弯钩 (spine, ends with UP-LEFT hook)
spine = [
    (205, 98),
    (203, 130),
    (203, 165),
    (205, 200),
    (200, 230),
    (185, 248),   # bottom of curve
    (160, 245),   # hook flick UP-LEFT
    (145, 232),
]
stroke(spine, width=8)
dab(205, 98, 5)

# Stroke 5: long 横 crossbar
hbar = [(128, 178), (200, 176), (275, 174)]
stroke(hbar, width=7)
dab(128, 178, 4)
dab(275, 174, 5)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0173_仔/01_仔.png"
)
