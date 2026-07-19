"""G1 render of radical 飞 (3-stroke radical form)."""
import os
from PIL import Image, ImageDraw

SIZE = 300
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_飞.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = "black"
W = 5  # stroke width


def smooth_polyline(pts, width=W):
    # draw a polyline with rounded joins by using line + circle at each vertex
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=width)
    for p in pts:
        r = width / 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=INK)


# --- Stroke 1: 横折弯钩 (the big enclosing stroke)
# Long near-horizontal top (slightly rising to the right), sharp turn down,
# gentle curve down-left, terminating in a small upward hook at bottom-right.
s1 = [
    (50, 158),   # start far left
    (85, 152),
    (120, 148),
    (150, 145),
    (170, 143),
    (182, 148),  # turn point
    (188, 158),
    (190, 175),
    (188, 195),  # curve begins
    (182, 215),
    (172, 235),
    (162, 250),
    (156, 258),  # bottom of curve
    (162, 262),  # hook up
    (172, 260),
    (178, 254),
]
smooth_polyline(s1, W)

# --- Stroke 2: 撇 (short pie) — a curving diagonal inside the enclosure,
# from upper area sweeping down-left.
s2 = [
    (215, 170),
    (208, 185),
    (200, 200),
    (192, 218),
    (183, 235),
    (175, 250),
]
smooth_polyline(s2, W)

# --- Stroke 3: small 点/tick at the top of s2 — a short slanted mark
# pointing down-right from just above stroke 2's start.
s3 = [
    (210, 168),
    (220, 178),
    (228, 188),
]
smooth_polyline(s3, W)

img.save(OUT)
print(f"wrote {OUT}")
