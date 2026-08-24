# generated.py — p3_char_0136_比 (bǐ, "compare") — revision 1
# 4 strokes:
#   Left component (匕-like): 1) short 撇 (top) 2) 竖提 (down + upward tick)
#   Right component (匕):     3) 撇 (crosses across) 4) 竖弯钩
# Uniform thin lines per P12 (MMH GT rendering). Larger, taller layout.

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


# ---- LEFT COMPONENT (x-range ~55..145) ----
# Stroke 1: short 撇 at top (drops down-left, small)
line((115, 95), (75, 130))

# Stroke 2: 竖提 — vertical down from near top-right of shu, then upward tick
# Vertical shaft
line((80, 105), (80, 225))
# 提 tick at bottom, going up-right
line((80, 225), (145, 195))

# ---- RIGHT COMPONENT (x-range ~155..245) ----
# Stroke 3: 撇 — starts upper, sweeps down-left across the shu (crosses it)
line((215, 100), (158, 180))

# Stroke 4: 竖弯钩 — vertical down, curves right along bottom, hook up
# Vertical shaft
line((180, 115), (180, 215))
# Smooth curve from bottom of shaft along to the right
polyline([(180, 215), (188, 230), (205, 238), (230, 235), (245, 220)])
# Hook (small upward tick at right end)
line((245, 220), (245, 200))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0136_比/01_比.png")
