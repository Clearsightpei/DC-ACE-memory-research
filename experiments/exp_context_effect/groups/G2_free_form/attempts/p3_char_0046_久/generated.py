"""Render 久 to a 300x300 PNG.

Structure (3 strokes):
1) Short 撇 near top-center (small tick sloping down-left).
2) 横撇 body: short horizontal shoulder starting mid-upper, turning
   into a long left-sweeping 撇 down to lower-left.
3) 捺: right-leg starting from mid-body, sweeping down-right ending
   in a flat pressed tail at lower-right.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush(points, widths):
    """Draw a variable-width polyline by dabbing circles.
    points: list of (x,y). widths: matching list of radii.
    """
    # densify
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


# --- Stroke 1: short 撇 near top-center ---
# from upper-right small point sloping down-left, thin
brush(
    [(140, 50), (130, 65), (118, 85)],
    [2.5, 3.0, 3.8],
)

# --- Stroke 2: 横撇 body ---
# Short horizontal shoulder then long sweeping 撇 down to lower-left.
horiz = [(95, 108), (120, 103), (150, 100), (170, 108)]
horiz_w = [3.5, 4.0, 4.0, 4.8]
brush(horiz, horiz_w)

# sweeping 撇 after shoulder — extend to lower-left corner
pie = [
    (170, 108),
    (158, 140),
    (135, 175),
    (105, 210),
    (75, 240),
    (45, 262),
    (30, 273),
]
pie_w = [4.8, 5.0, 5.2, 5.0, 4.5, 3.5, 2.2]
brush(pie, pie_w)

# --- Stroke 3: 捺 (right leg) ---
# Starts thin from mid-body, sweeps down-right ending in a pressed
# flat tail extending toward the lower-right area.
na = [
    (130, 178),
    (155, 200),
    (185, 225),
    (215, 250),
    (245, 268),
    (268, 273),
    (282, 272),
]
na_w = [2.5, 3.5, 4.5, 5.5, 6.5, 5.5, 2.8]
brush(na, na_w)

out = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0046_久/01_久.png"
)
img.save(out)
print("saved", out)
