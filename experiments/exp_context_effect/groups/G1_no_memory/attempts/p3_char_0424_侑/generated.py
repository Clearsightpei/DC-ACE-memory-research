"""Render 侑 (yòu) — 亻 + 有 — to a 300x300 PNG."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w)

# ---- Left radical 亻 ----
# 撇 from top-right down to lower-left
line([(95, 60), (55, 190)], w=LW)
# 竖 - starts at midpoint of the 撇 and goes straight down
line([(80, 130), (80, 260)], w=LW)

# ---- Right component 有 ----
# 丿 - long slanting stroke starting upper, going down-left through the horizontal
line([(200, 60), (140, 200)], w=LW)
# 一 - horizontal that intersects the 丿
line([(150, 105), (265, 105)], w=LW)

# 月 box (positioned below)
# left vertical (curves slightly)
line([(150, 145), (150, 260)], w=LW)
# top horizontal
line([(150, 145), (245, 145)], w=LW)
# right vertical with hook
line([(245, 145), (245, 255)], w=LW)
line([(245, 255), (230, 262)], w=LW)
# two inner horizontals
line([(155, 185), (240, 185)], w=LW)
line([(155, 220), (240, 220)], w=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0424_侑/01_侑.png")
print("saved")
