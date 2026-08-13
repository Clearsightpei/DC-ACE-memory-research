# generated.py — p3_char_0383_些 (xiē, "some") — 8 strokes
# Structure: 此 (top) over 二 (bottom).
#   此 = 止 (top-left) + 匕 (top-right)
#   二 = short 横 + long 横
# Uniform thin lines per P12 (MMH GT style).
# Inline fresh; using bi_char.py's 匕 recipe as a shape reference for
# the top-right component, and er.py's spacing as a reference for 二.

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


# ============================================================
# TOP: 此 (occupies y ~50..160, full width)
# ============================================================

# ---- 止 (top-left, x ~40..135) ----
# Stroke 1: 竖 — vertical on left side of 止
line((70, 60), (70, 155))
# Stroke 2: 短横 — short horizontal from vertical rightward
line((70, 120), (115, 118))
# Stroke 3: 短竖 — short vertical rising above the middle-horizontal
line((110, 90), (110, 120))
# Stroke 4: 长横 — bottom horizontal (base of 止)
line((45, 155), (140, 155))

# ---- 匕 (top-right, x ~150..250) ----
# Stroke 5: 撇 — short drop from upper-right, down-left
line((215, 65), (170, 110))
# Stroke 6: 竖弯钩 — vertical down, curve right, hook up
# Vertical shaft
line((185, 80), (185, 135))
# Curve along bottom to the right
polyline([(185, 135), (195, 150), (215, 158), (240, 155), (252, 140)])
# Hook (upward tick at right end)
line((252, 140), (252, 122))

# ============================================================
# BOTTOM: 二 (y ~200..260, centered horizontally)
# ============================================================

# Stroke 7: 短横 (upper, shorter)
line((115, 195), (185, 195))

# Stroke 8: 长横 (lower, longer)
line((40, 250), (260, 250))


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0383_些/01_些.png")
