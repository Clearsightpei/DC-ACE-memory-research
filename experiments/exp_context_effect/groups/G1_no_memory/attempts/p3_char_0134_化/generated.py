"""Render 化 (huà) at 300x300 using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"

def polyline(points, w=6):
    draw.line(points, fill=INK, width=w)

# ------ Left radical 亻 (person radical) ------
# Stroke 1: 撇 (slant) from upper-right down-left
polyline([(105, 60), (90, 100), (72, 140), (55, 185)], w=6)

# Stroke 2: 竖 (vertical) from top-mid downward
polyline([(105, 105), (105, 250)], w=6)

# ------ Right component 匕 ------
# Stroke 3: 撇 short slant upper right, crosses through where the vertical/curve will be
polyline([(200, 75), (185, 110), (165, 150), (150, 175)], w=6)

# Stroke 4: 竖弯钩 - vertical down, curve right along bottom, small hook up
polyline([
    (175, 115),
    (172, 160),
    (172, 200),
    (178, 230),
    (200, 250),
    (235, 255),
    (260, 250),
    (263, 235),
    (260, 220),
], w=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0134_化/01_化.png")
print("saved 01_化.png")
