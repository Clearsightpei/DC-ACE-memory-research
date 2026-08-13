"""Render 皅 (pa) — 白 (left) + 巴 (right). Left-right compound.

Layout: left component 白 slightly narrower; right 巴 similar width.
Vertical centers roughly aligned; 巴 has a bottom sweep 竖弯钩 that
extends slightly below 白.

Reference: p3_char_0359_的 generated.py (白 pattern reused, scaled).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p0, p1, width=5):
    d.line([p0, p1], fill=BLACK, width=width)


def poly(points, width=5):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=width)


# ---------- LEFT: 白 (cell x: 35..130, y: 60..235) ----------
# 1) 撇 — short diagonal down-left from top-right of box
poly([(105, 65), (88, 82), (72, 105)], width=5)

# 2) 竖 — left vertical of box
line((72, 105), (72, 228), width=6)

# 3) 横折 (top + right) — top horizontal then right vertical
poly([(72, 105), (128, 105), (128, 228)], width=6)

# 4) 横 middle — inside horizontal
line((78, 160), (122, 160), width=5)

# 5) 横 bottom — close the box
line((74, 226), (128, 226), width=5)


# ---------- RIGHT: 巴 (cell x: 155..265, y: 60..255) ----------
# 巴 has 4 strokes:
# 1) 竖 (left vertical)
# 2) 横折 (top + right vertical)
# 3) 横 (middle horizontal)
# 4) 竖弯钩 (bottom: closes the box then sweeps right and flicks up)

# 1) 竖 — left vertical
line((165, 70), (165, 235), width=6)

# 2) 横折 — top horizontal + right vertical (right side descends further)
poly([(165, 70), (245, 70), (245, 175)], width=6)

# 3) 横 middle — inside horizontal
line((165, 145), (245, 145), width=5)

# 4) 竖弯钩 — from lower-left box, go down, then curve right, then flick up
poly([
    (165, 200), (165, 235),      # continue down (below 横)
    (175, 250), (200, 255),      # curve into horizontal bottom
    (235, 253), (255, 245),      # sweep right along bottom
    (260, 230),                  # transition into hook
], width=6)
# hook flick UP-and-slightly-LEFT
poly([(260, 230), (256, 215), (252, 205)], width=6)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0460_皅/01_皅.png")
print("saved")
