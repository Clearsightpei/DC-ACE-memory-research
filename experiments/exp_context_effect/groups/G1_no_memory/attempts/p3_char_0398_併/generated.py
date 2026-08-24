"""Render 併 as a 300x300 PNG. G1 no-memory attempt."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ==== 亻 radical (person radical, left side) ====
# 撇 (falling left): from upper area down-left
stroke([(85, 70), (78, 130), (55, 220)], width=6)
# 竖 (vertical): drops from mid-撇 down
stroke([(88, 140), (90, 240)], width=6)

# ==== 幵 / 并 right side ====
# Two short 撇 at top (dots/short falling strokes)
stroke([(155, 65), (145, 95)], width=5)
stroke([(225, 65), (215, 95)], width=5)

# Upper horizontal (short)
stroke([(140, 130), (245, 125)], width=5)

# Lower horizontal (long)
stroke([(120, 175), (270, 170)], width=5)

# Left vertical of right component
stroke([(170, 110), (165, 245)], width=6)

# Right vertical of right component (slight lean)
stroke([(235, 110), (245, 250)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0398_併/01_併.png")
print("saved")
