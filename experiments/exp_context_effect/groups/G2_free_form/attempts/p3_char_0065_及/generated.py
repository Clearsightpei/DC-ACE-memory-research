"""Render 及 to a 300x300 PNG using PIL.

Decomposition (3 strokes):
  1. 撇 (long): starts upper-mid (joins the top 横 of stroke 2),
     sweeps down-left with a curve to lower-left. Body diagonal.
  2. 横折折撇: short 横 across the top, shoulder drops diagonally,
     short mid segment folds back, then a 撇 flick down-left ending
     inside the body. Signature multi-fold of 及.
  3. 捺 (long, sweeping): starts thin near the mid of stroke 2's
     inner flick, sweeps down-right ALMOST HORIZONTALLY to a broad
     flat foot at the baseline far right. Crosses the first 撇.

Revision v2: softened the multi-fold (less boxy), flattened the 捺
into a more horizontal sweep with a longer flat terminal at the
baseline, made the inner 撇 flick more visible, tightened the
top-横 join with stroke 1.
"""

from math import hypot
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=7):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for (x, y) in pts:
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def taper_stroke(pts, w_start=4, w_end=10, samples=50):
    seglens = [hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
               for i in range(len(pts) - 1)]
    total = sum(seglens)
    if total == 0:
        return
    step = total / samples
    acc = 0.0
    seg_i = 0
    seg_used = 0.0
    prev_pt = pts[0]
    for s in range(1, samples + 1):
        target = s * step
        while seg_i < len(seglens) and acc + (seglens[seg_i] - seg_used) < target:
            acc += seglens[seg_i] - seg_used
            seg_i += 1
            seg_used = 0.0
        if seg_i >= len(seglens):
            x, y = pts[-1]
            w = w_end
        else:
            remain = target - acc
            frac = (seg_used + remain) / seglens[seg_i] if seglens[seg_i] > 0 else 0
            x = pts[seg_i][0] + (pts[seg_i + 1][0] - pts[seg_i][0]) * frac
            y = pts[seg_i][1] + (pts[seg_i + 1][1] - pts[seg_i][1]) * frac
            seg_used += remain
            t = s / samples
            w = w_start + (w_end - w_start) * t
        d.line([prev_pt, (x, y)], fill=BLACK, width=max(2, int(round(w))))
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)
        prev_pt = (x, y)


# --------- Stroke 1: long 撇 (body diagonal) ----------
# Starts where top 横 ends (upper-mid), curves down-left to lower-left.
p撇 = [(150, 85), (135, 115), (115, 150), (90, 190), (68, 225), (52, 255)]
taper_stroke(p撇, w_start=8, w_end=3, samples=60)

# --------- Stroke 2: 横折折撇 (top multi-fold) ----------
# Top 横: from (145, 82) rightward to (215, 78) — joins stroke 1 start.
# Fold 1 (shoulder + diagonal drop): to (218, 112)
# Fold 2 (short back-in-and-down): to (188, 138)
# 撇 tail (long down-left into body): to (135, 200)
p2 = [
    (150, 85),   # left end (joins stroke 1)
    (175, 82),
    (200, 80),
    (218, 80),   # top-right corner
    (222, 100),
    (218, 118),  # shoulder / first fold
    (205, 128),
    (188, 138),  # second fold apex
    (172, 158),
    (155, 180),
    (138, 200),  # 撇 tail end
]
# Draw with mild taper (endings thin)
taper_stroke(p2, w_start=6, w_end=4, samples=90)
# Boost the mid section width a touch by re-drawing the corner arcs
stroke(p2[:5], width=7)

# --------- Stroke 3: long sweeping 捺 ----------
# Starts thin near stroke 2's fold-2 area, sweeps down-right, crosses
# stroke 1's 撇 near mid, ends in broad flat foot at baseline.
p捺 = [
    (155, 165),
    (175, 195),
    (200, 220),
    (230, 240),
    (255, 250),
    (275, 253),
]
taper_stroke(p捺, w_start=3, w_end=11, samples=70)
# Extend the flat terminal foot rightward
d.ellipse((268, 247, 285, 262), fill=BLACK)
# Draw the flat baseline foot as a short horizontal wedge
for i, w in enumerate([11, 11, 10, 9, 7, 5]):
    x = 275 + i * 3
    d.ellipse((x - w / 2, 254 - w / 2, x + w / 2, 254 + w / 2), fill=BLACK)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
         "groups/G2_free_form/attempts/p3_char_0065_及/01_及.png")
print("wrote 01_及.png (rev2)")
