"""Render 实 (shi2) — 8 strokes: 宀 (3) + 丷 (2) + 大 (3)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 宀 radical (roof) ---
# 1. Top dot 丶
stroke([(148, 30), (156, 48)], width=6)
# 2. Left dot 丶 of 宀
stroke([(92, 65), (78, 82)], width=6)
# 3. Horizontal-hook 横钩 of 宀
stroke([(80, 88), (120, 82), (170, 80), (215, 84), (222, 92), (216, 104)], width=5)

# --- 丷 (two dots above 大) ---
# 4. Left dot 丿-like tick
stroke([(115, 115), (105, 135)], width=5)
# 5. Right dot 丶-like tick
stroke([(185, 115), (198, 135)], width=5)

# --- 大 body ---
# 6. Long horizontal 一
stroke([(50, 175), (110, 170), (185, 168), (250, 172)], width=6)
# 7. 撇 (left-falling)
stroke([(150, 145), (135, 175), (110, 215), (80, 250), (55, 275)], width=6)
# 8. 捺 (right-falling)
stroke([(160, 175), (185, 210), (215, 245), (240, 275)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0393_实/01_实.png")
