"""Render 门 (mén, gate) — 3 strokes:
1) 点 (left dot / short diagonal at top-left)
2) 竖 (left vertical, straight down)
3) 横折钩 (top horizontal → sharp fold down → bottom hook to the left)

Free-form G2 approach: PIL, brush-dab along sampled polylines/beziers.
Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(p0, p1, r=6, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    dist = (dx * dx + dy * dy) ** 0.5
    if steps is None:
        steps = max(2, int(dist))
    for i in range(steps + 1):
        t = i / steps
        dab(x0 + t * dx, y0 + t * dy, r)


def stroke_bezier(p0, p1, p2, r=6, steps=80):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        dab(x, y, r)


# --- stroke 1: 点 (left short diagonal above the vertical) ---
# small stroke slanting down-left, sits above where the 竖 starts
stroke_line((100, 55), (78, 88), r=6)

# --- stroke 2: 竖 (left vertical) ---
# starts below the dot, goes straight down to near the bottom
stroke_line((92, 100), (92, 268), r=7)

# --- stroke 3: 横折钩 (top horizontal → fold down right wall → hook left) ---
# horizontal top-lid, starts roughly at column of the dot and extends right
stroke_line((130, 72), (240, 72), r=7)
# vertical right wall, extends a bit below the left 竖 so the hook lives lower
stroke_line((240, 72), (240, 262), r=7)
# hook: pronounced flick up-and-to-the-left at the bottom of the right wall
stroke_bezier((240, 262), (228, 278), (192, 272), r=7)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0063_门/01_门.png"
)
