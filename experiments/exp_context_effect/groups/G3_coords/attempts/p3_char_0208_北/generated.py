# generated.py - p3_char_0208_北 (bei, "north")
# 5 strokes: left 丬-like (横+竖+提), right 匕 (撇+竖弯钩).
# Structure adapted from bi_char.py (bank #162) with left top-stroke
# swapped from 撇 to a short heng-slash and an added stroke to match
# the 5-stroke MMH decomposition. Uniform thin lines per P12.
from PIL import Image, ImageDraw

CANVAS = 300
W = 5

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# ---- LEFT COMPONENT (x-range ~55..145) — 3 strokes ----
# Stroke 1: 横 (short, top area, meets the shu near its top; slight slant)
line((55, 120), (108, 128))

# Stroke 2: 竖 (vertical shaft, meets top heng at its right end)
line((108, 105), (108, 230))

# Stroke 3: 提 (tick at bottom-left, going up-right toward mid)
line((60, 240), (135, 205))

# ---- RIGHT COMPONENT (x-range ~150..250) — 2 strokes (匕) ----
# Stroke 4: 撇 — sweeps from upper-right down-left across the shu
line((225, 105), (155, 190))

# Stroke 5: 竖弯钩 — vertical down, curves right along bottom, hook up
line((190, 130), (190, 215))
polyline([(190, 215), (200, 232), (220, 240), (240, 235), (250, 220)])
line((250, 220), (250, 195))

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0208_北/01_北.png"
)
