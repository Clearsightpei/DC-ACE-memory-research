"""刂 (2画 radical) — left short 竖, right 竖钩. PIL brush-dabs, 300x300."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def straight(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# LEFT stroke: short 竖 (roughly middle-height, upper-left of radical body).
# Radical 刂 sits on the right side of a character; when isolated, we still
# place it centered but keep the compositional look — left short 竖 sits
# higher than the right 竖钩's bottom and does NOT extend as far down.
lx = 120
straight(lx, 100, lx, 200, 5, 5)
# subtle 顿 at start and end
dab(lx, 100, 6)
dab(lx, 200, 6)

# RIGHT stroke: 竖钩 — straight 竖 from top, longer than the left, ending in
# an up-and-left hook flick from the bottom.
rx = 190
ry0 = 70
ry1 = 235
straight(rx, ry0, rx, ry1, 5.5, 5.5)
dab(rx, ry0, 7)  # 顿 at top
# hook flick from (rx, ry1) going up-and-left ~ -145°, cleaner taper
import math
flick_len = 28
angle = math.radians(-145)  # image coords: negative y is up
fx = rx + flick_len * math.cos(angle)
fy = ry1 + flick_len * math.sin(angle)
# joining dab at the corner, then taper thin start->thin tip so the hook
# is a delicate flick, not an arrowhead
dab(rx, ry1, 6)  # joining dab hides seam between 竖 and hook
steps = 200
for i in range(steps + 1):
    t = i / steps
    x = rx + (fx - rx) * t
    y = ry1 + (fy - ry1) * t
    r = 5.0 + (1.0 - 5.0) * t
    dab(x, y, r)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_016_刂/01_刂.png")
