"""
代 (dài) = 亻 (left) + 弋 (right). 5 strokes total.
Left 亻: 撇 (top-left slanting flick) + 竖 (long vertical).
Right 弋: 横 (short flat rising) + 斜钩 (long diagonal with UP-LEFT hook)
         + 点 (small dot near top).

# SIGNATURE CHECK (hook family — 斜钩):
# The 斜钩 terminal MUST flick UP-and-LEFT (~-110°..-120°),
# never DOWN. This was the #1 root cause of B4/B5 fails.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(pts, steps=80):
    n = len(pts) - 1
    from math import comb
    out = []
    for i in range(steps + 1):
        t = i / steps
        x = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][0] for k in range(n + 1))
        y = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][1] for k in range(n + 1))
        out.append((x, y))
    return out

def stroke(pts, widths):
    """Draw a variable-width stroke via bezier + circle dabs."""
    curve = bezier(pts, steps=100)
    n = len(curve)
    for i, (x, y) in enumerate(curve):
        t = i / (n - 1)
        # interpolate width
        idx = t * (len(widths) - 1)
        lo = int(idx); hi = min(lo + 1, len(widths) - 1)
        frac = idx - lo
        w = widths[lo] * (1 - frac) + widths[hi] * frac
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---- Left component 亻 ----
# 撇: from around (100, 70) curving down-left to (60, 165)
stroke([(105, 62), (95, 105), (75, 145), (55, 175)], widths=[8, 8, 6, 3])
# 竖: from around (105, 92) straight down to (105, 260)
stroke([(102, 92), (103, 175), (104, 258)], widths=[7, 8, 7])

# ---- Right component 弋 ----
# 横: short flat rising stroke, top-right area
stroke([(150, 100), (185, 92), (225, 88)], widths=[6, 8, 7])
# 斜钩: long diagonal from around (170, 105) sweeping down-right,
#       then hook flicks UP-and-LEFT at terminal near (245, 250)
stroke([(165, 108), (185, 155), (220, 210), (250, 250)], widths=[8, 8, 9, 10])
# Hook flick UP-and-LEFT from (250, 250)
stroke([(250, 250), (245, 240), (238, 232)], widths=[9, 7, 4])
# 点: small dot upper-right, above/near start of 斜钩
stroke([(210, 65), (222, 72), (232, 80)], widths=[4, 7, 8])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0192_代/01_代.png")
