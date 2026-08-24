"""
过 = 辶 (walking radical, bottom-left wrap) + 寸 (right upper)
Layout: 寸 sits upper-right; 辶 wraps under-left with long 平捺 base.
Reference: form_catalog + hook rules — 竖钩 flicks UP-and-LEFT.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=8):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # round caps
    for (x, y) in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

def brush_curve(pts, widths):
    # sample lines between successive points with tapered width
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i+1]
        w = int((widths[i] + widths[i+1]) / 2)
        d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)
    for (x, y), w in zip(pts, widths):
        r = w // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# ============= 寸 (right upper part) =============
# 寸 has: 横 (top horizontal), 竖钩 (vertical hook), 点 (dot)

# 1. Top dot of 辶 (小点 upper-left of char, above the 横折折撇)
# Small dot around (100, 60)
brush_curve([(105, 55), (115, 72)], [4, 9])

# 2. 寸's 横 (horizontal): from about (130, 95) to (255, 90) -- long horizontal on right
stroke([(135, 95), (260, 92)], width=8)

# 3. 寸's 竖钩: vertical from around (200, 80) down to (200, 200), then hook up-left
# Vertical portion
stroke([(205, 78), (203, 195)], width=9)
# Hook flick UP-and-LEFT
stroke([(203, 195), (185, 180)], width=8)

# 4. 寸's 点 (dot on left side, crossing the vertical): around (170, 150) going down-right
brush_curve([(160, 135), (185, 158)], [4, 10])

# ============= 辶 (walking radical) =============
# 5. 横折折撇 (turning stroke): compact z-form on the left, smoother than before
# Start with small horizontal
stroke([(65, 130), (105, 138)], width=8)
# Diagonal down-left (long stroke)
stroke([(105, 138), (60, 195)], width=8)
# Small horizontal turn at bottom of z
stroke([(60, 195), (105, 205)], width=8)

# 6. 平捺 (flat 捺, long sweeping base): starts where the 撇 ends and sweeps right
# Connect from ~(105, 205), dip down and sweep out to lower-right corner
pts = []
widths = []
N = 30
for i in range(N + 1):
    t = i / N
    # start (55, 215) -> end (285, 245), passing through a dip
    x = 55 + t * 230
    # gentle dip: start high, drop, rise slightly
    y = 215 + math.sin(math.pi * t) * 18 + t * 15
    pts.append((x, y))
    if t < 0.15:
        w = 5 + int(t / 0.15 * 7)
    elif t < 0.75:
        w = 13
    else:
        # taper for the outgoing flick
        w = int(13 - (t - 0.75) / 0.25 * 9)
    widths.append(max(3, w))
brush_curve(pts, widths)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0239_过/01_过.png")
print("saved")
