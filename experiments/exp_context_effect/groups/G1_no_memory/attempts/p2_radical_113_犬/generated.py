"""G1 render for p2_radical_113_犬 (radical, 4 strokes).

犬 = 大 (horizontal + left-falling 撇 + right-falling 捺) + a 点 in
the upper-right corner. Rendered with PIL to a 300x300 PNG.

Stroke order (standard):
  1. 横 (heng)  — horizontal, upper-middle
  2. 撇 (pie)   — left-falling from top-center diagonal
  3. 捺 (na)    — right-falling from crossing point
  4. 点 (dian)  — dot at upper-right
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=7):
    """Draw a variable-width tapered stroke by segments."""
    if len(pts) < 2:
        return
    # Uniform width for clarity; PIL doesn't do easy width taper.
    d.line(pts, fill="black", width=width, joint="curve")
    # Round endpoints
    r = width / 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- 1. 横 (horizontal) ----
# Shorter than my first attempt: from ~x=70 to x=195, slight up-tilt.
heng = [(70, 138), (198, 128)]
stroke(heng, width=6)

# ---- 2. 撇 (left-falling pie) ----
# Starts near top-center just above heng, sweeps down-left, curving.
pie = [
    (155, 72),
    (146, 108),
    (132, 148),
    (112, 190),
    (85, 230),
    (55, 268),
]
stroke(pie, width=7)

# ---- 3. 捺 (right-falling na) ----
# Starts at the crossing of heng & pie, sweeps down-right; thickens.
na_pts = [
    (140, 140),
    (162, 162),
    (188, 190),
    (218, 222),
    (250, 253),
    (275, 273),
]
for i in range(len(na_pts) - 1):
    w = 5 + int(i * 1.3)
    d.line([na_pts[i], na_pts[i + 1]], fill="black", width=w, joint="curve")
# Tail flick to the right
d.line([na_pts[-1], (285, 268)], fill="black", width=4)

# ---- 4. 点 (dot at upper-right) ----
# Short down-right dash above the na, higher and more separated
# from the heng than the first attempt.
dot = [(205, 82), (232, 102)]
stroke(dot, width=6)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_113_犬/01_犬.png"
)
