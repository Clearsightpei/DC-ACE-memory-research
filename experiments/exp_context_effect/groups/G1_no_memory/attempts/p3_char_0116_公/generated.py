"""Render 公 (gōng) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5

def stroke(points, width=LW):
    draw.line(points, fill=INK, width=width, joint="curve")

# 公 has 4 strokes:
# top 八 (piě + 捺), then 厶 below (撇折 + 点)
# GT proportions: 八 wide across upper half, 厶 sits centered in lower half

# --- Stroke 1: 撇 (piě) — top-left --- from upper-center-right down to lower-left
s1 = [(160, 75), (140, 105), (115, 140), (85, 175), (60, 205)]
stroke(s1, width=6)

# --- Stroke 2: 捺 (nà) — top-right --- from upper-center down to lower-right, longer
s2 = [(165, 70), (185, 100), (210, 130), (235, 155), (255, 175)]
stroke(s2, width=6)

# --- Stroke 3: 撇折 (厶 left part) --- short piě then折 rightward, centered lower
# left tip
s3 = [(130, 175), (120, 200), (115, 225), (135, 240), (170, 245)]
stroke(s3, width=6)

# --- Stroke 4: 点 (closing dot on right of 厶) ---
s4 = [(170, 220), (185, 240), (175, 255)]
stroke(s4, width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0116_公/01_公.png")
print("saved")
