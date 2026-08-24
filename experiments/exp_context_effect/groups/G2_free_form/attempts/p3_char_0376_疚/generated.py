"""Render 疚 (guilt) at 300x300 — 疒 wrapper + 久 inside.

Composition (per GT):
  - 疒 (5 strokes) wraps top-left: top dot, long 横, two inner-left dots,
    long 撇 descending to lower-left.
  - 久 (3 strokes) sits inside the wrapper, upper-right area, with its
    捺 sweeping to the lower-right below the 疒 hook.

Reuses proven brush/dab patterns from p3_char_0171_疒 + p3_char_0046_久.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush(points, widths):
    dense_pts = []
    dense_w = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for s in range(steps):
            t = s / steps
            dense_pts.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
            dense_w.append(w0 + (w1 - w0) * t)
    dense_pts.append(points[-1])
    dense_w.append(widths[-1])
    for (x, y), r in zip(dense_pts, dense_w):
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============ 疒 wrapper ============

# Stroke 1: top 点 (slanted dot, sits above the horizontal, upper-mid)
brush([(140, 40), (158, 68)], [2.5, 4.5])

# Stroke 2: long 横 (top horizontal bar)
brush([(90, 90), (155, 88), (240, 95)], [3.0, 3.0, 3.5])

# Stroke 3: upper inner 点 (冫-style upper, on the left interior)
brush([(55, 120), (78, 140)], [2.5, 4.5])

# Stroke 4: lower inner 提 (冫-style lower, rising to the right)
brush([(45, 180), (78, 165)], [4.5, 2.5])

# Stroke 5: long 撇 (descender from horizontal's left, curving down-left)
brush(
    [(90, 90), (88, 130), (85, 170), (78, 210), (62, 250), (48, 275)],
    [4.5, 4.2, 4.0, 3.7, 3.2, 2.0],
)

# ============ 久 inside (upper-right / mid area) ============

# Stroke 1: short 撇 near top (small tick sloping down-left)
brush(
    [(180, 105), (172, 118), (162, 135)],
    [2.0, 2.5, 3.0],
)

# Stroke 2: 横撇 body — short shoulder then long sweep down-left
brush(
    [(140, 150), (170, 145), (195, 148)],
    [3.0, 3.5, 4.0],
)
brush(
    [(195, 148), (180, 175), (155, 205), (125, 235), (105, 258)],
    [4.0, 4.2, 4.0, 3.4, 2.2],
)

# Stroke 3: 捺 (right leg) — starts from mid-body, sweeps to lower-right
brush(
    [(160, 190), (185, 215), (215, 245), (245, 265), (268, 273), (282, 272)],
    [2.5, 3.8, 5.0, 5.8, 5.0, 2.5],
)

out = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0376_疚/01_疚.png"
)
img.save(out)
print("saved", out)
