"""Render 的 (de) — 白 (left) + 勺 (right).

Layout: two-part, left component 白 slightly narrower, right 勺 slightly
wider with the enclosing hook stroke. Both share vertical center line.
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


# ---------- LEFT: 白 (roughly cell x: 40..135, y: 55..245) ----------
# 白 has 5 strokes: 撇 (top diagonal), 竖 (left of box), 横折 (top+right of box),
# 横 (middle), 横 (bottom close).

# 1) 撇 — short diagonal down-left from top-right of box
poly([(112, 60), (95, 78), (78, 100)], width=5)

# 2) 竖 — left vertical of box
line((78, 100), (78, 235), width=6)

# 3) 横折 (top + right) — top horizontal then right vertical
poly([(78, 100), (135, 100), (135, 235)], width=6)

# 4) 横 middle — inside horizontal
line((85, 160), (128, 160), width=5)

# 5) 横 bottom — close the box
line((80, 233), (135, 233), width=5)


# ---------- RIGHT: 勺 (roughly cell x: 150..265, y: 55..265) ----------
# 勺 has 3 strokes: 撇 (long diagonal from upper-right going down-left),
# 横折钩 (top+right+hook enclosing), 点 (dot inside).

# 1) 撇 — long sweeping diagonal starting from top going down-left
poly([(200, 60), (185, 105), (170, 160), (155, 220)], width=6)

# 2) 横折钩 — top horizontal starts near top of 撇, folds down along right,
# curves under, hook flicks UP-and-LEFT into the interior.
poly([
    (200, 78), (250, 82),        # top horizontal (slight rise)
    (258, 92), (260, 140),       # shoulder + right descending
    (256, 190), (240, 230),      # curve inward at bottom-right
    (210, 250),                  # bottom of bowl
    (185, 240),                  # bottom-left of bowl
], width=6)
# hook flick UP-and-LEFT from the bottom-left of bowl
poly([(185, 240), (180, 225), (178, 215)], width=6)

# 3) 点 — small vertical-ish dot inside the enclosure (upper-middle)
poly([(215, 155), (220, 175), (222, 195)], width=7)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0359_的/01_的.png")
print("saved")
