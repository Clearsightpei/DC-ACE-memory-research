"""Render 俛 = 亻 (person radical, left) + 免 (right).

免 structure:
  - top: 丿 (short slanted pie) forming the top of 刀
  - 横折钩-like frame enclosing 口
  - 一 inside
  - 儿 at bottom (curved left leg + right vertical with hook 竖弯钩)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---------------- 亻 (left, person radical) ----------------
# Top pie (撇), slanting down-left
stroke([(85, 70), (55, 130)], width=6)
# Vertical (竖) — long, hanging down
stroke([(70, 105), (70, 250)], width=6)

# ---------------- 免 (right) ----------------
# Top pie (丿) — short, slanted
stroke([(165, 60), (145, 90)], width=5)
# Top-left short horizontal joining pie
stroke([(145, 90), (170, 88)], width=5)
# Top horizontal + right vertical (横折) forming top of frame
stroke([(155, 100), (225, 100), (225, 155)], width=5)
# Left vertical of 口 (short)
stroke([(155, 100), (155, 155)], width=5)
# Bottom horizontal of 口
stroke([(155, 155), (225, 155)], width=5)
# 一 inside the 口 (the horizontal in middle of 免)
stroke([(150, 178), (230, 178)], width=5)

# ---------------- 儿 (bottom of 免) ----------------
# Left leg — curving pie going down-left
stroke([(170, 178), (155, 220), (135, 260)], width=6)
# Right leg — 竖弯钩: down, curve right, hook up-right
stroke([(215, 178), (215, 235), (240, 260), (270, 250)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0494_俛/01_俛.png")
