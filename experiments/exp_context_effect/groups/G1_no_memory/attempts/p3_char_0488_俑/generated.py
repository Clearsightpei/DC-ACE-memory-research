"""G1 draw 俑 (yǒng) — person radical 亻 + 甬"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- Left: 亻 (person radical) ---
# 撇 (slanted top stroke)
line([(85, 75), (55, 200)], width=6)
# 竖 (long vertical)
line([(78, 130), (78, 275)], width=6)

# --- Right: 甬 ---
# Top hat (龴-like)
# small left tick
line([(175, 65), (185, 80)], width=5)
# top horizontal
line([(140, 100), (235, 95)], width=5)
# right hook down from end of horizontal
line([(235, 95), (240, 115)], width=5)

# 用 body: top horizontal bar
line([(140, 130), (240, 130)], width=5)
# left vertical
line([(140, 130), (145, 280)], width=6)
# right vertical with slight hook at bottom
line([(240, 130), (240, 275)], width=6)
line([(240, 275), (230, 285)], width=6)
# middle spine — extends UP into hat and DOWN past bottom
line([(188, 80), (190, 295)], width=6)
# two inner horizontal bars
line([(145, 178), (240, 178)], width=5)
line([(147, 225), (240, 225)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0488_俑/01_俑.png")
print("saved")
