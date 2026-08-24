# generated.py — p3_char_0244_仳 (pǐ, "match/mate") — G3
# 仳 = 亻 (left radical, 2 strokes) + 比 (right, 4 strokes)
# 6 strokes total. Uniform thin lines per P12 (MMH GT rendering).
# Layout: 亻 in left ~30% of width, 比 compressed into right ~65%.

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


# ---- LEFT: 亻 (person radical) ----
# Stroke 1: 撇 sweeping down-left from upper-right
line((80, 75), (45, 195))
# Stroke 2: 竖 vertical shaft on right side of the pie
line((72, 135), (72, 255))

# ---- RIGHT: 比 (compressed into right side ~110..275) ----
# Left component of 比 (匕-like):
# Stroke 3: short 撇 at top
line((165, 105), (128, 140))
# Stroke 4: 竖提 — vertical down, then upward tick
line((135, 118), (135, 235))
line((135, 235), (200, 210))

# Right component of 比 (匕):
# Stroke 5: 撇 — starts upper, sweeps down-left across the shu
line((235, 110), (172, 205))
# Stroke 6: 竖弯钩 — vertical down, curves right, hook up
line((200, 130), (200, 230))
polyline([(200, 230), (210, 248), (230, 258), (258, 255), (275, 238)])
line((275, 238), (275, 215))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0244_仳/01_仳.png")
