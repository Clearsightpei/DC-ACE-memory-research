"""Render 贝 (radical, 4 strokes simplified) at 300x300."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 4

def line(p1, p2, width=LW):
    draw.line([p1, p2], fill=INK, width=width)

# Box roughly spanning x=100..190, y=60..205 (taller upper portion)
# Stroke 1: 竖 (left vertical of the box)
line((105, 60), (105, 210))

# Stroke 2: 横折 - horizontal top then down the right side
line((105, 60), (190, 60))
line((190, 60), (190, 215))

# Middle horizontal inside the box
line((105, 145), (190, 145))

# Stroke 3: 撇 - left leg going down and to the left from bottom-left area
line((105, 210), (75, 265))

# Stroke 4: 点 - right leg going down-right from bottom-right area
line((175, 210), (220, 265))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_085_贝/01_贝.png")
