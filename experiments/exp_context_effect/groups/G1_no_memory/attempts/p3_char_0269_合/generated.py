"""Render 合 (hé) — 6 strokes: 人 top (撇+捺), 一 middle, 口 bottom (竖+横折+横)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- Top 人 ---
# 撇 (left-falling): from top-center-ish down-left
stroke([(150, 40), (135, 70), (115, 105), (85, 145), (55, 175)], width=6)
# 捺 (right-falling): from top-center down-right, ends flatter
stroke([(150, 40), (170, 75), (195, 115), (225, 150), (250, 170)], width=6)

# --- Middle 一 (horizontal inside the 人 roof) ---
stroke([(105, 155), (200, 158)], width=5)

# --- Bottom 口 ---
# left vertical 竖
stroke([(105, 190), (105, 260)], width=5)
# top+right 横折 (top horizontal then down)
stroke([(105, 190), (205, 188), (205, 258)], width=5)
# bottom 横
stroke([(107, 260), (207, 258)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0269_合/01_合.png")
