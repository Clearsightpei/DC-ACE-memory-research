"""
佰 = 亻 (left) + 百 (right)
百 = 一 (top horizontal) + 白 (short 丿 + rectangle with two internal horizontals)
Left-right composition, 亻 narrow left, 百 wider right.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 亻 (left radical), narrow column left ~x=50-95 ----
# 撇 (top slanted stroke): start upper-right, go down-left
stroke([(95, 90), (60, 175)], width=7)
# 竖 (vertical): from top of 撇 area, straight down
stroke([(80, 130), (80, 265)], width=7)

# ---- 百 (right), roughly x=115-265, y=70-270 ----
# Top: short 丿 (small slant on top center)
stroke([(180, 65), (165, 95)], width=6)
# Top horizontal 一 (long)
stroke([(120, 100), (260, 100)], width=7)
# 白 rectangle:
# Left vertical of rectangle (starts a bit below the 一)
stroke([(140, 115), (140, 265)], width=7)
# Top horizontal of rectangle (kind of the "shoulder" 横折): from ~x150 to right, then down
stroke([(150, 130), (250, 130)], width=6)
stroke([(250, 130), (250, 265)], width=7)
# Bottom horizontal of rectangle
stroke([(140, 265), (250, 265)], width=7)
# Middle horizontal (making it 日-like)
stroke([(150, 195), (245, 195)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0394_佰/01_佰.png")
