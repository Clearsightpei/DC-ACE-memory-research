"""Render 外 (outside) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

LW = 5


def curve(points, w=LW):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill="black", width=w)


# ---------- LEFT: 夕 ----------
# Stroke 1: short 撇 at top — starts upper mid-left, falls left
curve([(85, 85), (70, 105), (58, 125)])

# Stroke 2: 横折撇 — horizontal top, sharp turn, then long diagonal down-left
curve([
    (65, 115), (110, 110),                   # short horizontal
    (115, 125),                               # turn
    (108, 145), (90, 175), (65, 215), (40, 265)  # long diagonal falling
])

# Stroke 3: 点 inside 夕 (short diagonal from left rim to middle)
curve([(70, 165), (100, 180)])

# ---------- RIGHT: 卜 ----------
# Stroke 4: long vertical 竖
curve([(200, 55), (200, 165), (200, 245), (202, 280)])

# Stroke 5: 点 — short right-slanting off the vertical, upper-middle
curve([(200, 145), (225, 155), (245, 170)])

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p3_char_0178_外/01_外.png"
)
print("saved")
