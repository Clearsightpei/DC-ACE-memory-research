"""G1 render for 伦 (lún). Left: 亻. Right: 仑 = 人 roof + ㄙ (angle with hook)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

def line(pts, width=LW):
    d.line(pts, fill="black", width=width)

def curve(pts, width=LW):
    # simple polyline approximation for gentle curves
    d.line(pts, fill="black", width=width, joint="curve")

# --- Left: 亻 (person radical) ---
# 撇 (pie): from upper-right to lower-left, slight arc
curve([(95, 55), (88, 100), (75, 160), (55, 220)], width=LW)
# 竖 (vertical): starts at mid of pie stroke, straight down
line([(90, 120), (90, 270)], width=LW)

# --- Right: 仑 ---
# Top 人 roof
# Left slant (撇): from apex down-left
curve([(190, 45), (175, 80), (150, 120), (125, 150)], width=LW)
# Right slant (捺): from apex down-right, ending with a slight flare
curve([(190, 45), (210, 85), (235, 130), (255, 155)], width=LW)

# Bottom ㄙ: horizontal top + vertical/slant left + bottom hook right
# Horizontal top of ㄙ
line([(155, 175), (235, 175)], width=LW)
# Left side: slants down-left slightly then curves
curve([(155, 175), (150, 210), (155, 245), (170, 265)], width=LW)
# Bottom hook: from bottom of left slant across to right, then hook up
line([(170, 265), (240, 265)], width=LW)
line([(240, 265), (245, 240)], width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_伦.png"))
print("Saved 01_伦.png")
