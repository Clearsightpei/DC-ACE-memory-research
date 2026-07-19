"""G1 Drawer — p1_stroke_01_横
Renders a horizontal stroke (横) as a 300x300 PNG, white bg, black ink.
Uses PIL to avoid turtle display dependencies.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Horizontal stroke 横: from left to right, roughly centered vertically.
# Slight thickness variation is characteristic of 横 (starts firm, tapers slightly,
# ends with a small 顿笔). We approximate with a solid horizontal bar with
# subtle end caps.
x0, x1 = 50, 250
y_center = 150
thickness = 14

# Main body — slight upward slope typical of 横 in kaishu (very subtle)
# Draw as a filled polygon with slightly heavier ends.
left_top = (x0, y_center - thickness // 2)
left_bot = (x0, y_center + thickness // 2)
right_top = (x1, y_center - thickness // 2 - 1)  # subtle taper up
right_bot = (x1 + 6, y_center + thickness // 2 + 3)  # 顿笔 at end

draw.polygon(
    [left_top, right_top, right_bot, left_bot],
    fill="black",
)

# Small 起笔 (starting dot) on the left
draw.ellipse(
    [x0 - 4, y_center - thickness // 2 - 2, x0 + 6, y_center + thickness // 2 + 2],
    fill="black",
)

# Small 顿笔 (ending press) on the right
draw.ellipse(
    [x1 - 4, y_center - thickness // 2, x1 + 10, y_center + thickness // 2 + 5],
    fill="black",
)

out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_01_横/01_横.png"
)
img.save(out_path)
print(f"Saved {out_path} size={img.size}")
