"""G1 render of 便 (biàn) — 亻 + 更."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 亻 (person radical, left) ---
# 撇 (left-falling stroke)
line([(95, 55), (55, 210)], width=6)
# 竖 (vertical, from mid of 撇)
line([(78, 130), (76, 260)], width=6)

# --- 更 (right side) ---
# top horizontal of 更 (一)
line([(115, 75), (255, 75)], width=6)

# 日/曰 box: left vertical
line([(140, 75), (140, 175)], width=6)
# right vertical
line([(240, 80), (238, 175)], width=6)
# middle horizontal (inside box)
line([(140, 128), (238, 128)], width=5)
# bottom of box
line([(140, 175), (240, 175)], width=6)

# lower horizontal of 更 (crosses full width)
line([(105, 210), (260, 210)], width=6)

# central vertical descending through the box+horizontal
line([(188, 128), (188, 235)], width=6)

# 撇 sweeping down-left from lower center
line([(188, 210), (120, 275)], width=6)
# 捺 sweeping down-right from lower center
line([(188, 210), (270, 275)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0469_便/01_便.png")
