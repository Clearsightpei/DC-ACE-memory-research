"""Render 乡 (xiang) to a 300x300 PNG using PIL.

乡 has 3 similar strokes stacked diagonally top-right to bottom-left:
  1) top 撇折 — small: diagonal-down-left then a short flick down-right
  2) middle 撇折 — medium, offset down-right of #1
  3) bottom 撇折 — largest, longest sweep, with a curling hook tail
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(points, width=5):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill="black", width=width)
    for p in points:
        r = width // 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


# Stroke 1 — top small 撇折
# starts upper-right (~170,55), sweeps down-left curved, then hooks
# down-right (the "折" part) ending around lower-right.
s1 = [
    (172, 55),
    (162, 68),
    (150, 88),
    (140, 108),
    (135, 122),
    (145, 128),
    (160, 130),
    (172, 128),
    (178, 135),
]
stroke(s1, width=4)

# Stroke 2 — middle 撇折, larger, shifted down-right
s2 = [
    (198, 115),
    (185, 132),
    (168, 155),
    (150, 178),
    (140, 192),
    (155, 198),
    (172, 198),
    (186, 194),
    (192, 202),
]
stroke(s2, width=5)

# Stroke 3 — bottom largest 撇折 with pronounced curling hook
s3_main = [
    (222, 172),
    (208, 192),
    (188, 218),
    (162, 244),
    (132, 262),
    (100, 272),
    (75, 273),
]
stroke(s3_main, width=6)
# hook curl at end going up-right
s3_hook = [
    (75, 273),
    (68, 265),
    (72, 255),
    (85, 252),
]
stroke(s3_hook, width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0091_乡/01_乡.png")
print("saved")
