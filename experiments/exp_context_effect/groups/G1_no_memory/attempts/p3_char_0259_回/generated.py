"""G1 render: 回 (character). Outer box + inner box."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7

# Outer box (roughly centered, occupies most of canvas)
ox1, oy1 = 55, 55
ox2, oy2 = 245, 245

# Outer left vertical
d.line([(ox1, oy1), (ox1, oy2)], fill=INK, width=LW)
# Outer top horizontal + right vertical (single 横折)
d.line([(ox1, oy1), (ox2, oy1)], fill=INK, width=LW)
d.line([(ox2, oy1), (ox2, oy2)], fill=INK, width=LW)
# Outer bottom horizontal (closing stroke)
d.line([(ox1, oy2), (ox2, oy2)], fill=INK, width=LW)

# Inner box (口), centered inside
ix1, iy1 = 115, 115
ix2, iy2 = 195, 195

# Inner left vertical
d.line([(ix1, iy1), (ix1, iy2)], fill=INK, width=LW)
# Inner top + right (横折)
d.line([(ix1, iy1), (ix2, iy1)], fill=INK, width=LW)
d.line([(ix2, iy1), (ix2, iy2)], fill=INK, width=LW)
# Inner bottom
d.line([(ix1, iy2), (ix2, iy2)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0259_回/01_回.png")
print("saved")
