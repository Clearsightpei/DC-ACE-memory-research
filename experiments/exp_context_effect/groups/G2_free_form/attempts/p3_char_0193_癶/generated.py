"""癶 (p3_char_0193) — 5 strokes.

MMH decomposition (5 strokes): 撇, 点, 撇, 撇, 捺.
Silhouette: symmetric V-like shape opening downward, with small
top ticks on each half. Two long diagonal sweeps dominate.

Revision: simplified right half; removed spurious ticks; cleaner
symmetry between left (short 撇 + long 撇) and right (short 撇 +
long 捺).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")
    for x, y in pts:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


def bezier(p0, p1, p2, n=50):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


# ================ LEFT HALF ================
# Stroke 1: short 撇 flick at upper-left (small down-left tick)
short_pie_left = bezier((120, 85), (108, 100), (90, 115), n=25)
stroke(short_pie_left, width=8)

# Stroke 2 (点): tiny dot just below/right of short-pie start
d.ellipse([124, 100, 138, 118], fill="black")

# Stroke 3: long 撇 sweeping from upper-center-left down to lower-left
long_pie_left = bezier((140, 95), (100, 175), (55, 250), n=60)
stroke(long_pie_left, width=9)

# ================ RIGHT HALF ================
# Stroke 4: short 撇 at upper-right (mirror of left short pie)
short_pie_right = bezier((190, 85), (178, 105), (162, 125), n=25)
stroke(short_pie_right, width=8)

# Stroke 5: long 捺 sweeping from upper-center-right down to lower-right
na = bezier((175, 105), (215, 180), (258, 250), n=60)
stroke(na, width=10)

# small terminal thickening for 捺 tail
d.ellipse([250, 245, 268, 258], fill="black")

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0193_癶/01_癶.png"
)
