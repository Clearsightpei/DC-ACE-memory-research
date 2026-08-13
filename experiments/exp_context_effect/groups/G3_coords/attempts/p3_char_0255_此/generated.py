# generated.py — p3_char_0255_此 (cǐ, "this")
# 6 strokes: 止 (left, 4 strokes) + 匕 (right, 2 strokes)
# Uniform thin lines per P12 (MMH GT rendering). Modeled after bi_char.py.

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


# ---- LEFT COMPONENT 止 (x-range ~45..145) ----
# Stroke 1: 竖 — short vertical top-left
line((72, 105), (72, 225))
# Stroke 2: 横 — short horizontal crossbar (upper mid)
line((72, 160), (120, 155))
# Stroke 3: 竖 — main vertical (goes down from crossbar area)
line((115, 130), (115, 220))
# Stroke 4: 横提 — long baseline with slight upward tick to the right
line((45, 230), (150, 215))

# ---- RIGHT COMPONENT 匕 (x-range ~155..250) ----
# Stroke 5: 撇 — from upper right sweeping down-left, crosses the shu
line((220, 100), (160, 190))

# Stroke 6: 竖弯钩 — vertical, curve right along bottom, hook up
# Vertical shaft
line((180, 120), (180, 220))
# Curve along bottom to the right
polyline([(180, 220), (190, 235), (208, 243), (232, 240), (248, 225)])
# Hook (small upward tick at right end)
line((248, 225), (248, 205))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0255_此/01_此.png")
