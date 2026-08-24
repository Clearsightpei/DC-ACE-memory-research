"""Render 痃 (a hernia/illness) at 300x300 — 疒 wrapper (left) + 玄 (right).

Composition:
  - 疒 (5 strokes, left-top-wrap): top 点 + short 一 + inner 冫(点+提) +
    long 撇. Adapted from proven p3_char_0376_疚 template but 一 shortened
    so it does not merge with 玄's 亠 horizontal.
  - 玄 (5 strokes, right-inside-wedge): 亠 (点+一) on top, then 幺 (two
    撇折 loops) + final 丶.

Rev 2: shortened 疒 一 (was overlapping 玄 一 -> merged into one line);
made 幺's 撇折 curls smoother (curved not angular).
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


# ============ 疒 wrapper (left) ============

# Stroke 1: top 点 (slanted dot above the horizontal)
brush([(95, 35), (113, 62)], [2.5, 4.5])

# Stroke 2: 一 top horizontal — SHORT so it does not merge with 玄 一
brush([(55, 82), (100, 80), (135, 84)], [3.0, 3.0, 3.5])

# Stroke 3: upper inner 点 (冫 upper, inside the wedge)
brush([(38, 108), (60, 128)], [2.5, 4.5])

# Stroke 4: lower inner 提 (冫 lower, rising to the right)
brush([(32, 168), (66, 152)], [4.5, 2.5])

# Stroke 5: long 撇 (descender from horizontal's left, curving down-left)
brush(
    [(55, 82), (54, 125), (50, 168), (40, 215), (28, 258), (18, 282)],
    [4.5, 4.2, 4.0, 3.7, 3.2, 2.0],
)

# ============ 玄 (right side) ============

# Stroke 1: 丶 top dot (crown of 亠), placed above 一
brush([(190, 40), (206, 60)], [2.0, 4.5])

# Stroke 2: 一 horizontal (亠 bar), higher than 疒 一 to stay distinct
brush([(150, 78), (215, 74), (280, 82)], [3.0, 3.2, 4.0])

# Stroke 3: first 撇折 (upper ㄥ loop) — 撇 down-left, then curved right
brush(
    [(195, 100), (180, 118), (168, 138), (175, 144)],
    [2.5, 3.2, 3.6, 3.6],
)
brush(
    [(175, 144), (200, 148), (225, 148), (240, 144)],
    [3.6, 3.6, 3.2, 2.5],
)

# Stroke 4: second 撇折 (lower ㄥ loop) — larger, below the first
brush(
    [(185, 165), (168, 190), (152, 215), (160, 222)],
    [2.5, 3.3, 3.8, 3.8],
)
brush(
    [(160, 222), (200, 228), (240, 228), (258, 222)],
    [3.8, 3.8, 3.4, 2.6],
)

# Stroke 5: final 丶 (right-side closing dot)
brush([(255, 240), (275, 262)], [2.0, 4.5])


out = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0534_痃/01_痃.png"
)
img.save(out)
print("saved", out)
