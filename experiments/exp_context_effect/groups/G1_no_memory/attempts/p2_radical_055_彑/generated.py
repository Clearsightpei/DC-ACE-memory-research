"""G1 render of 彑 (3-stroke radical)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5

# Stroke 1: short slanted stroke at top (like a small ノ), upper area
d.line([(170, 80), (150, 115)], fill=INK, width=LW)

# Stroke 2: the middle zigzag — top horizontal, down right side, bottom horizontal,
# and a tail extending down-right past the body
d.line([
    (110, 120),   # upper-left of the body
    (195, 125),   # top horizontal
    (190, 165),   # right side down
    (115, 170),   # bottom horizontal (back left)
    (205, 215),   # tail extending down to the right past body
], fill=INK, width=LW, joint="curve")

# Stroke 3: long horizontal stroke at bottom (slight tilt like GT)
d.line([(45, 250), (255, 245)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_055_彑/01_彑.png")
