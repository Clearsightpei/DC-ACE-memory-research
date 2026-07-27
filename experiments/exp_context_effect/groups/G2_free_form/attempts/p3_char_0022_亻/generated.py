"""
Render 亻 (person radical, left-position) to a 300x300 PNG.

Composition (per form_catalog.md):
  - 撇 as left-position radical component: starts x~155 y~65,
    steep (~70deg), throws down-left to ~x=95 y=170, thick->thin.
  - 竖 as vertical drop: starts where the 撇 body is at ~x=155 y=100
    (near the top of the pie), descends straight down to y=250.
    No hook. Uniform width, slight top 顿 dab.
Silhouette family: tall-narrow (x-extent ~40%, y-extent ~85%).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    """Draw a variable-width stroke by dabbing circles along the path.

    points: list of (x, y).
    widths: list of radii the same length as points.
    Segments are subdivided so consecutive dabs overlap.
    """
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse(
                (x - r, y - r, x + r, y + r),
                fill="black",
            )


# ---- 撇 (pie) -- steep left-position flick ----
# Slight rightward bow on the body. Thick at head, thin at tail.
# Longer + more curved to match GT's graceful sweep.
pie_points = [
    (170, 55),   # head (upper-right, slight curl feel)
    (165, 80),
    (155, 110),
    (140, 140),
    (120, 170),
    (95, 195),   # tail (thin, points down-left)
]
pie_widths = [5.5, 5.5, 5.0, 4.5, 3.5, 1.8]
brush_stroke(pie_points, pie_widths)

# Tiny hook-back at the head to mimic GT's little curl at the top
head_curl = [(170, 55), (176, 62), (172, 72)]
head_widths = [5.5, 4.0, 2.5]
brush_stroke(head_curl, head_widths)


# ---- 竖 (vertical) -- right-side straight drop ----
# Starts where the 撇 body passes near x=152, descends straight.
shu_points = [
    (155, 115),  # top -- meets pie body
    (155, 160),
    (155, 210),
    (155, 255),  # bottom (blunt terminal)
]
shu_widths = [5.5, 5.5, 5.5, 5.0]
brush_stroke(shu_points, shu_widths)

# Small top 顿 dab for the 竖 (subtle, not a lump)
d.ellipse((151, 112, 160, 121), fill="black")


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0022_亻/01_亻.png"
)
