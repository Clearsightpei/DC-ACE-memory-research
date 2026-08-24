"""
Render 侖 (lún) to a 300x300 PNG.

Structure:
- Top: 亼 hat (撇 + 捺 meeting at apex)
- Middle: 一 horizontal below the hat
- Bottom: 冊-like frame: left 竖, right 横折钩, two internal 竖 with a horizontal.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def stroke(pts, width=6):
    d.line(pts, fill=INK, width=width, joint="curve")

# --- Top 亼 hat (tall triangle) ---
# Apex at (150, 35). Left 撇 sweeps down-left; right 捺 flares down-right.
stroke([(150, 35), (85, 130)], width=7)    # 撇 (left long diagonal)
stroke([(150, 40), (215, 128)], width=7)   # 捺 (right diagonal)

# --- Middle horizontal 一 (bar under the hat) ---
stroke([(70, 150), (230, 150)], width=6)

# --- Bottom 冊 frame ---
# Left vertical (short 竖 slightly slanting outward at bottom)
stroke([(80, 155), (74, 265)], width=6)
# Right vertical (横折钩: comes from top bar, goes down, hooks up-left)
stroke([(226, 155), (232, 258)], width=6)
# Hook flick up-and-left (per memory: terminal always flicks up-left ~-105 to -120°)
stroke([(232, 258), (218, 246)], width=6)

# Internal middle horizontal (crossbar inside frame)
stroke([(85, 210), (228, 210)], width=6)

# Two internal verticals descending from top bar down through mid bar
# to below the bottom of side verticals (冊 style: verticals stick down)
stroke([(125, 155), (125, 275)], width=6)
stroke([(178, 155), (178, 275)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0428_侖/01_侖.png")
