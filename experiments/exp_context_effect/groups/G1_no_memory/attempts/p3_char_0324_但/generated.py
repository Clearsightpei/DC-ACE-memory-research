"""Render 但 (dan4) — 7 strokes: 亻 (2) + 旦 (5)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

LW = 6

def line(pts, width=LW):
    draw.line(pts, fill="black", width=width, joint="curve")

# ---- 亻 (left radical: person, 2 strokes) ----
# Stroke 1: 撇 (falling-left diagonal)
line([(90, 60), (45, 190)], width=LW)

# Stroke 2: 竖 (vertical) dropping from the belly of the 撇
line([(72, 140), (78, 270)], width=LW)

# ---- 旦 (right component: 日 + 一, 5 strokes) ----
# Right side occupies roughly x=125..255
# 日 on top: 4 strokes
# S1: 竖 (left vertical of 日)
line([(135, 90), (135, 195)], width=LW)
# S2: 横折 (top + right vertical) — top horizontal then turn down
line([(135, 90), (235, 90), (235, 195)], width=LW)
# S3: 横 (middle horizontal inside 日)
line([(140, 145), (230, 145)], width=LW)
# S4: 横 (bottom of 日, closing)
line([(135, 195), (235, 195)], width=LW)
# S5: 一 (long bottom horizontal — base of 旦)
line([(110, 250), (270, 250)], width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0324_但/01_但.png")
