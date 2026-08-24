"""
亦 (yì) — 6 strokes: 点, 横, 撇, 竖, 竖钩, 点
Not in sibling checklist. Layout:
- Top: small dot centered slightly right of middle
- Long horizontal below the dot
- Below horizontal: left 撇 slanting down-left, short 竖 near center-left,
  竖钩 near center-right (bottom curves up-left as hook), right 点 far right.
Ink: black on white, 300x300.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=6):
    d.line(points, fill="black", width=width, joint="curve")
    # rounded caps
    r = width / 2
    for x, y in [points[0], points[-1]]:
        d.ellipse([x-r, y-r, x+r, y+r], fill="black")

# 1. Top dot (点) — small diagonal dab, slightly right of center
# Position: around (155, 70) going down-right
def dot(cx, cy, dx, dy, w=7):
    # taper: start narrow, end wide
    steps = 8
    for i in range(steps):
        t = i / (steps - 1)
        x = cx + dx * t
        y = cy + dy * t
        rr = w * (0.4 + 0.6 * t)
        d.ellipse([x-rr, y-rr, x+rr, y+rr], fill="black")

# Stroke 1: top 点 (going down-right, slender)
dot(148, 55, 18, 18, w=4.5)

# Stroke 2: long 横 (horizontal), slight rise, curves down at right (hook-tail)
# From ~(55, 110) to ~(245, 110), slight upward arc
horiz = []
import math
for i in range(31):
    t = i / 30
    x = 55 + t * 190
    y = 110 - 6 * math.sin(math.pi * t) * 0.5 - 2*t  # slight bow
    horiz.append((x, y))
stroke(horiz, width=6)

# Stroke 3: 撇 (left down-slanting), from ~(105, 130) curving to ~(70, 240)
pie = []
for i in range(31):
    t = i / 30
    # curve leftward as it descends
    x = 105 - 35 * t - 8 * math.sin(math.pi * t)
    y = 130 + 110 * t
    pie.append((x, y))
stroke(pie, width=6)

# Stroke 4: short 竖 (vertical) center-left, from ~(135, 140) to (135, 210)
stroke([(140, 140), (138, 220)], width=6)

# Stroke 5: 竖钩 (vertical with hook at bottom), center-right
# Descends nearly straight, then hook flicks up-and-left
sk = [(180, 138)]
for i in range(1, 22):
    t = i / 21
    x = 180 - 1 * t
    y = 138 + 105 * t
    sk.append((x, y))
# hook: sharp flick up-and-left
for i in range(1, 10):
    t = i / 9
    x = 179 - 20 * t
    y = 243 - 14 * t
    sk.append((x, y))
stroke(sk, width=6)

# Stroke 6: right 点 (going down-right), on the far right, slender
dot(228, 150, 18, 25, w=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0238_亦/01_亦.png")
print("saved")
