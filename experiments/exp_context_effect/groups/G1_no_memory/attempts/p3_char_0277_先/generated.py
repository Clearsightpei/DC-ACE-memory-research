"""Render 先 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")

# 先 — 6 strokes
# Top component (like 生 top): short pie, short horizontal, vertical crossing, longer horizontal
# Bottom component: 儿 (pie + vertical-curving-hook)

# 1) Short pie at top-left of upper component
line([(148, 55), (128, 82)])

# 2) Short horizontal (top of upper block)
line([(115, 82), (172, 78)])

# 3) Short vertical crossing through both horizontals
line([(150, 70), (150, 138)])

# 4) Longer middle horizontal
line([(65, 140), (235, 134)])

# 5) Long pie (left-falling) descending to lower-left
line([(135, 140), (115, 175), (90, 215), (60, 258)])

# 6) 竖弯钩 (vertical-curving-hook) on the right
line([(180, 140), (180, 210), (188, 245), (220, 260), (245, 248), (250, 232)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0277_先/01_先.png")
print("Saved.")
