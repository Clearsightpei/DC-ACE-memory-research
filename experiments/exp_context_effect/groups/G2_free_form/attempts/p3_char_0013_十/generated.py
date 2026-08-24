"""Render 十 (ten) — two strokes: 横 crossing 竖.

Rendered against clean GT (prior GT was corrupted with overlaid strokes).

GT observations (clean version):
- 横 sits slightly above vertical middle (~y=150), spans ~x=50..250,
  very slight upward tilt to the right, small brush flares at both ends.
- 竖 runs from ~y=60 (short protrusion above 横) down to ~y=275
  (longer descent below), centered ~x=150. Straight, uniform-ish
  width, small 顿 dab at top, blunt at bottom.
- Silhouette: a plus/cross with vertical dominant, horizontal in the
  upper-middle band. Vertical > horizontal in visual weight.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke_taper(pts, w_start, w_end):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = w_start * (1 - t) + w_end * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def sample_line(p0, p1, n=200):
    return [
        (p0[0] + (p1[0] - p0[0]) * i / n, p0[1] + (p1[1] - p0[1]) * i / n)
        for i in range(n + 1)
    ]


# ---- Stroke 1: 横 (horizontal, upper-middle) ----
h_start = (52, 156)   # left, slightly lower
h_end   = (248, 148)  # right, slightly higher — subtle upward tilt
h_pts = sample_line(h_start, h_end, n=220)
stroke_taper(h_pts, w_start=4.8, w_end=5.2)
# End flares
draw.ellipse([h_start[0] - 5, h_start[1] - 4, h_start[0] + 5, h_start[1] + 5],
             fill="black")
draw.ellipse([h_end[0] - 5, h_end[1] - 5, h_end[0] + 6, h_end[1] + 6],
             fill="black")

# ---- Stroke 2: 竖 (vertical, through-going axis) ----
v_start = (152, 62)
v_end   = (150, 275)
v_pts = sample_line(v_start, v_end, n=240)
stroke_taper(v_pts, w_start=5.0, w_end=5.2)
# 顿 dab at top
draw.ellipse([v_start[0] - 5, v_start[1] - 3, v_start[0] + 6, v_start[1] + 6],
             fill="black")
# Blunt bottom
draw.ellipse([v_end[0] - 5, v_end[1] - 5, v_end[0] + 5, v_end[1] + 5],
             fill="black")


img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0013_十/01_十.png"
)
print("wrote 01_十.png")
