"""Render 去 (5 strokes) at 300x300, white bg, black ink.

Structure:
  Top 土: short horizontal, vertical stroke, longer horizontal
  Bottom 厶: 撇折 (down-left then turn right/up), 点 on the right
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
THICK = 5

def line(pts, width=THICK):
    d.line(pts, fill=INK, width=width, joint="curve")

# --- Top 土 ---
# Short upper horizontal (slightly slanted up like GT)
line([(115, 70), (195, 62)])
# Vertical stroke through it
line([(150, 45), (150, 130)])
# Longer middle horizontal
line([(85, 128), (215, 122)])

# --- Middle long horizontal (the wide base of 去) ---
line([(55, 190), (255, 185)], width=6)

# --- Bottom 厶 ---
# 撇折: slanting down-left from around center, then turning right (折)
line([(145, 200), (115, 250), (165, 262)])   # 撇 down-left then 折 right
# 点 / small 捺 on the right, angling down-right
line([(170, 230), (200, 275)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0166_去/01_去.png")
print("wrote 01_去.png")
