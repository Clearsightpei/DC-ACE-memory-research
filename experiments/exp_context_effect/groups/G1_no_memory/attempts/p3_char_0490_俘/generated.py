"""Render 俘 (captive) to 300x300 PNG."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left radical 亻 (person) ----
# 撇 - slash from upper-right to lower-left
stroke([(80, 80), (55, 145)], width=5)
# 竖 - vertical descending stroke
stroke([(72, 130), (72, 245)], width=5)

# ---- Right side 孚 ----
# Top 爫 (three small drops)
stroke([(135, 80), (128, 100)], width=4)   # left slash
stroke([(160, 78), (163, 100)], width=4)   # middle
stroke([(195, 80), (188, 100)], width=4)   # right slash
# Horizontal covering stroke
stroke([(115, 118), (225, 112)], width=5)

# ---- Bottom 子 (child) ----
# Top curved stroke of 子 - horizontal-turn (横折)
stroke([(145, 150), (210, 148), (195, 175)], width=5)
# Vertical hook (竖钩): comes down through center, hooks left
stroke([(178, 148), (178, 275), (158, 268)], width=5)
# Long horizontal 一 through middle
stroke([(110, 208), (245, 202)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0490_俘/01_俘.png")
print("saved")
