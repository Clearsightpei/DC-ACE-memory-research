"""
p3_char_0052_亡 — G2 free-form drawer.

亡 has 3 strokes:
  1) 点 (small down-right dot at top-center)
  2) 横 (top-lid horizontal, spans wide, slight up-tilt)
  3) 竖折 (vertical down on the left, then turn horizontal to the right)

Following form_catalog:
- 横 as top-lid over hanging body: MEDIUM (~140-160 px), y ~ 70-90.
- 点 above lid: a short down-right flick.
- 竖折: left wall + bottom horizontal, forming an L; the bottom
  横 extends rightward to about the top-lid's right end (or a bit shorter).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(p0, p1, w_start, w_end, steps=40):
    """Variable-width line drawn as overlapping filled circles."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w_start + (w_end - w_start) * t) / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def brush_poly(points, widths, steps_per_seg=30):
    """Piecewise variable-width along a polyline."""
    for i in range(len(points) - 1):
        brush_line(points[i], points[i + 1], widths[i], widths[i + 1], steps_per_seg)


# ---- Stroke 1: 点 (small dot) at top center-right, tilts down-left slightly
# GT shows a small diagonal flick going from upper-right toward lower-left.
brush_line((172, 68), (158, 92), w_start=4, w_end=11)

# ---- Stroke 2: 横 (top-lid) — medium, slight upward tilt, does NOT
# reach as far right as the bottom 横 in GT.
brush_poly(
    points=[(55, 128), (140, 122), (225, 118)],
    widths=[9, 10, 12],
    steps_per_seg=40,
)
# small 顿 press at right end
draw.ellipse((218, 112, 232, 126), fill=BLACK)

# ---- Stroke 3: 竖折 (L-shape) — vertical down on the left, then a long
# horizontal sweeping RIGHT and extending past the top 横's right end.
# Start slightly detached from top-lid (small gap at top-left corner
# matches GT feel), vertical descends, then bottom sweeps wide.
# Vertical portion:
brush_poly(
    points=[(72, 138), (73, 200), (75, 238)],
    widths=[11, 11, 12],
    steps_per_seg=30,
)
# Corner turn:
brush_line((75, 238), (95, 243), 12, 12, steps=15)
# Horizontal portion sweeping right — extends beyond the top-lid's right end:
brush_poly(
    points=[(95, 243), (170, 240), (255, 236)],
    widths=[12, 11, 10],
    steps_per_seg=40,
)
# small terminal press at right end
draw.ellipse((248, 230, 262, 242), fill=BLACK)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0052_亡/01_亡.png"
)
print("wrote 01_亡.png")
