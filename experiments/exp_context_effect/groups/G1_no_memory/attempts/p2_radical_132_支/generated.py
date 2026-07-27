"""Render 支 (radical 132, 4 strokes) at 300x300 using PIL.

Canonical stroke breakdown for 支 (4 strokes):
  1. 横 — top short horizontal
  2. 竖 — short vertical descending from center of top horizontal down
         to (through) the long horizontal
  3. 横 — long horizontal (main crossbar)
  4. 又 shape (the bottom radical, treated as a single unit here but
     visually two brush strokes):
       4a. 横撇 — short horizontal then a long 撇 sweep down-left
       4b. 捺 — thickening sweep down-right

Compared to first pass: enlarged the 又, moved the top-bar up-tilted
like GT, widened the main horizontal, moved intersection of 又 lower.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p0, p1, width=6):
    d.line([p0, p1], fill=BLACK, width=width)


def tapered_curve(pts, w_start=8, w_end=3):
    n = len(pts) - 1
    for i in range(n):
        t = i / max(1, n - 1)
        w = int(round(w_start + (w_end - w_start) * t))
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=max(2, w))


# ---- Stroke 1: short top horizontal, slightly slanting up-right ----
line((130, 65), (175, 60), width=6)

# ---- Stroke 2: short vertical (small tick) dropping from top-bar center
#      down to just above the long horizontal ----
line((152, 55), (150, 110), width=6)

# ---- Stroke 3: long horizontal (main crossbar) — wide, centered ----
line((55, 118), (245, 115), width=7)

# ---- Stroke 4a: 横撇 — short horizontal, then long sweep down-left ----
# Short horizontal top of 又
line((115, 158), (185, 158), width=6)
# 撇 sweep down-left, tapering
pie_pts = [
    (185, 158),
    (172, 180),
    (155, 205),
    (130, 235),
    (95, 260),
    (65, 275),
]
tapered_curve(pie_pts, w_start=7, w_end=3)

# ---- Stroke 4b: 捺 — starts where 横撇 begins its downward slope,
# sweeps down-right, thickening near end ----
na_pts = [
    (150, 175),
    (170, 200),
    (195, 225),
    (220, 250),
    (245, 268),
    (260, 275),
]
tapered_curve(na_pts, w_start=4, w_end=10)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_132_支/01_支.png"
img.save(out)
print(f"Wrote {out}")
