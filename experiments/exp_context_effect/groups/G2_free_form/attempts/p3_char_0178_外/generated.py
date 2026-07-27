"""
外 (wai) — 5 strokes, left-right composition.
Left: 夕 (3 strokes: 撇, 横折钩, 点-inside)
Right: 卜 (2 strokes: long 竖, 点)

Layout: 夕 in left ~40% of canvas (x ~40-140), 卜 in right ~40% (x ~170-260).
卜's 竖 dominates vertically — longest stroke, tall & straight.
夕 is smaller, sits in upper-left area.

Renderer: PIL brush-dabs (per drawer_memory technique reference).
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def bezier(p0, p1, p2, r_start, r_end, n=80, dun_r=None):
    """Quadratic Bezier with tapering brush-dabs. Optional 顿 dab at start."""
    if dun_r is not None:
        dab(p0[0], p0[1], dun_r)
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)

def line_taper(p0, p1, r_start, r_end, n=80, dun_r=None):
    if dun_r is not None:
        dab(p0[0], p0[1], dun_r)
    for i in range(n + 1):
        t = i / n
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)

# ============ LEFT: 夕 ============
# Stroke 1: 撇 (top flick), starts upper area, throws down-left
# Start ~(115, 55), end ~(55, 155). Steep-ish, slight bow.
bezier((115, 55), (100, 95), (55, 155),
       r_start=4.5, r_end=1.5, dun_r=5)

# Stroke 2: 横折钩 (the 夕 body: short 横 → shoulder → curved 撇 tail with hook flick)
# Short 横 from ~(90, 80) to ~(150, 78) — a bit shorter, sits below the top 撇
line_taper((90, 80), (150, 78), r_start=3.5, r_end=3.5, dun_r=4)
# Shoulder dab
dab(150, 80, 4)
# 折 tail: curves down-left, ends around (70, 220). Belly on right side.
bezier((150, 80), (135, 160), (70, 220),
       r_start=4, r_end=2)
# Hook flick at bottom: UP-and-LEFT per TIER-0 hook rule (~-105°)
hx0, hy0 = 70, 220
angle = math.radians(-110)
hx1 = hx0 + 18 * math.cos(angle)
hy1 = hy0 + 18 * math.sin(angle)
line_taper((hx0, hy0), (hx1, hy1), r_start=2.5, r_end=1.2)

# Stroke 3: 点 (small dot inside the 夕 body, roughly middle-lower)
# Short thick-to-thin flick going down-right
line_taper((95, 145), (118, 165), r_start=2, r_end=3.5, dun_r=2)

# ============ RIGHT: 卜 ============
# Stroke 4: 竖 (long vertical) — dominant tall stroke
# From ~(200, 45) to ~(200, 265). Nearly straight, slight taper at bottom.
line_taper((200, 45), (200, 265), r_start=4.5, r_end=3, dun_r=5)

# Stroke 5: 点 (small dot to the right of the 竖, upper-middle area)
# Short flick going down-right from cross-point
line_taper((205, 130), (240, 160), r_start=2.5, r_end=4, dun_r=2.5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0178_外/01_外.png")
print("saved 01_外.png")
