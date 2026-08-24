"""Render 八 (radical, 2画) to a 300x300 PNG.

Left stroke: 撇 (piě) — starts near upper middle, curves down and to the left,
tapering slightly.
Right stroke: 捺 (nà) — starts just right of the piě's top, sweeps down-right,
broadening toward the tail.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(points, widths):
    """Draw a variable-width stroke by connecting circles along a polyline.

    points: list of (x, y)
    widths: list of widths matching points (linear interp between them)
    """
    # densify
    n_seg = 60
    dense_pts = []
    dense_w = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for t in range(n_seg + 1):
            u = t / n_seg
            dense_pts.append((x0 + (x1 - x0) * u, y0 + (y1 - y0) * u))
            dense_w.append(w0 + (w1 - w0) * u)
    for (x, y), w in zip(dense_pts, dense_w):
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# Left 撇 — short, starts around (120, 105), curves down-left to (70, 220).
# Ends mid-lower zone. GT shows it noticeably shorter than the right stroke,
# with a slight rightward-concave curve (bowing right).
pie_pts = [
    (120, 105),
    (110, 140),
    (98, 170),
    (85, 195),
    (70, 220),
]
pie_widths = [9, 8, 8, 7, 4]
stroke(pie_pts, pie_widths)

# Right 捺 — longer and dominant. Starts higher and slightly right of piě's top,
# with a clear gap between the two stroke starts. Sweeps down-right and
# broadens toward the tail.
na_pts = [
    (155, 80),
    (180, 130),
    (205, 175),
    (225, 210),
    (245, 240),
]
na_widths = [6, 9, 11, 12, 8]
stroke(na_pts, na_widths)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_009_八/01_八.png"
)
