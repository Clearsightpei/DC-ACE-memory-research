"""G1 render for 俏 — 亻 + 肖."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 亻 (person radical, left)
# piě starting from top, curving down-left
stroke([(85, 70), (75, 115), (55, 170), (35, 220)], width=5)
# vertical shù dropping from mid of piě
stroke([(72, 130), (72, 255)], width=5)

# 肖 top: 小-like three strokes
# left short piě
stroke([(150, 65), (135, 100)], width=5)
# center vertical
stroke([(180, 55), (180, 100)], width=5)
# right short nà
stroke([(210, 65), (225, 100)], width=5)

# 月-like lower box
# left vertical (slight piě)
stroke([(145, 110), (140, 265)], width=5)
# top horizontal
stroke([(145, 110), (230, 115)], width=5)
# right vertical with hook
stroke([(230, 115), (228, 260), (218, 273)], width=5)
# middle horizontal bar
stroke([(150, 165), (228, 168)], width=5)
# lower horizontal bar
stroke([(150, 215), (228, 218)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0484_俏/01_俏.png")
