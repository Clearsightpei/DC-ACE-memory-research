"""
G1 render of 匸 (radical, 2 strokes conceptually — top横 + 竖折 shape).
Looking at GT: top horizontal (slight downward tilt right, then up), then a
竖折 forming the left vertical + bottom horizontal (open-right bracket).
Uses PIL for a clean 300x300 render.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 8  # stroke thickness

# Approximate anchors from GT observation:
# Top横: from (~60, 95) to (~225, 90) — slight upward tilt right (in image coords, y smaller = higher)
# Actually GT shows top slightly wavy but essentially horizontal spanning
# 竖折 (stroke 2): starts at top-left, goes down to bottom, then right along bottom.
#   Left vertical: (~72, 95) down to (~72, 235)
#   Bottom horizontal: (~72, 235) to (~230, 232)

def stroke(pts, width=LW):
    draw.line(pts, fill=INK, width=width, joint="curve")
    # round caps by drawing circles at endpoints
    for (x, y) in [pts[0], pts[-1]]:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)

# Stroke 1: top 横 (slight arc — barely visible tilt)
top_horiz = [(58, 98), (100, 92), (160, 90), (225, 92)]
stroke(top_horiz)

# Stroke 2: 竖折 — left vertical down then bottom horizontal right
# Left vertical
left_vert = [(72, 98), (72, 165), (72, 235)]
stroke(left_vert)
# Bottom horizontal (continuation)
bot_horiz = [(72, 235), (140, 234), (200, 232), (232, 232)]
stroke(bot_horiz)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_034_匸/01_匸.png")
print("saved 01_匸.png")
