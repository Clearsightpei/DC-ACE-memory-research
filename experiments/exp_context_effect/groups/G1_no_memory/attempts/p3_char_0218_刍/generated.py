"""Render 刍 (chu) - 5 strokes.
Structure:
  1. Top small pie 丿 (upper left small diagonal)
  2. Upper wrap: heng-zhe 横折 forming top of 勹-like enclosure
  3. Short heng 横 inside the upper enclosure
  4. Lower heng-zhe 横折 forming bottom enclosure top
  5. Bottom long heng 横 extending to right (base stroke)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # line width


def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")


def curve(pts, width=LW):
    # smooth polyline
    d.line(pts, fill=BLACK, width=width, joint="curve")


# ---- Stroke 1: small top-left pie (short diagonal going down-left)
line([(140, 55), (128, 78)], width=LW)

# ---- Stroke 2: upper enclosure - heng then zhe going down-left (like part of 勹)
# horizontal top, turn, diagonal down-left
curve([(112, 92), (175, 88), (180, 92), (170, 130), (110, 148)], width=LW)

# ---- Stroke 3: small horizontal inside the upper enclosure
line([(128, 128), (162, 125)], width=LW)

# ---- Stroke 4: middle horizontal (top of lower enclosure) + turn down forming right hook
curve([(105, 178), (185, 172), (195, 178), (188, 218)], width=LW)

# ---- Stroke 5: bottom long horizontal extending well to the right
line([(90, 240), (215, 235)], width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0218_刍/01_刍.png")
print("saved")
