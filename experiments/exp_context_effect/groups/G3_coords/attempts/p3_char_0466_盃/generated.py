# BANK_DEVIATION
# skipped: bu_char.py, min_dish.py
# reason: 盃 is 不-over-皿 top/bottom stack — both bank primitives are
#   sized/positioned for full-canvas solo renders; need vertical compression
#   and repositioning of both components so 不 fits the top ~45% and 皿 the
#   bottom ~50% of the 300x300 canvas.
# fresh_component: bu_top_compressed_for_stack, min_bottom_compressed_for_stack

"""盃 (bēi, "cup") — 不 over 皿, 9 strokes total (4 + 5).
Inline PIL fresh render adapted from bu_char + min_dish geometry,
compressed vertically for top-bottom stack composition.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6


def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)


def bezier_taper(x0, y0, x1, y1, w_head, w_tail, bow_perp=-6.0, n=60):
    """Tapered quadratic bezier from (x0,y0) to (x1,y1) with perpendicular bow.
    Coords are pixel-space (y down)."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = (x0 + x1) / 2.0 + perp_x * bow_perp
    my = (y0 + y1) / 2.0 + perp_y * bow_perp
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (bx, by)], fill=INK, width=wi)
            r = w / 2.0
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=INK)
        prev = (bx, by)


# ============================================================
# TOP: 不 (compressed into y ~ 30..145)
# heng at top, pie down-left from heng center, shu descending
# from heng center, dian on the right
# ============================================================

# Stroke 1: 横 (heng) — top horizontal, wide
line((45, 60), (255, 55), w=6)

# Stroke 2: 丿 (pie) — from just left of center on heng, sweeping down-left
bezier_taper(150, 62, 60, 145, w_head=7.0, w_tail=2.5, bow_perp=-6.0)

# Stroke 3: 丨 (shu) — short vertical from heng center downward
line((155, 62), (162, 140), w=6)

# Stroke 4: 丶 (dian) — right dot, sweeping down-right
bezier_taper(180, 80, 225, 135, w_head=3.0, w_tail=8.0)


# ============================================================
# BOTTOM: 皿 (compressed into y ~ 160..275)
# 3 inner verticals + 横折 top-right corner + long base heng
# ============================================================

# Left vertical (slanted inward at bottom)
line((70, 175), (78, 260), w=6)

# First inner short vertical
line((120, 182), (122, 260), w=6)

# Second inner short vertical
line((170, 182), (170, 260), w=6)

# 横折 top-right corner (short top horizontal, then right wall down)
line((105, 175), (225, 175), w=6)
line((225, 175), (218, 260), w=6)

# Long bottom horizontal (extends beyond box)
line((35, 275), (270, 273), w=7)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0466_盃/01_盃.png")
print("saved")
