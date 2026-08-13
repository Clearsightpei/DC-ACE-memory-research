"""G1 render of 设 (shè) - revised.
Left: 讠 (2 strokes) - dot on top + 横折提 combined
Right: 殳 (5 strokes) = top 几-like (3 strokes) + bottom 又 (2 strokes)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left radical 讠 ----
# 1) 点 (dot)
line([(52, 78), (68, 95)], width=6)
# 2) 横折提 - short horizontal, turn down-left, then rising tick
line([(50, 130), (85, 138)], width=4)      # short horizontal
line([(85, 138), (55, 178)], width=4)      # turn down-left
line([(50, 195), (90, 180)], width=4)      # rising tick (提)

# ---- Right top: 几-like part of 殳 ----
# 1) small 撇 on top-left
line([(135, 68), (118, 100)], width=5)
# 2) 横折 (long top horizontal turning down on right)
line([(140, 82), (232, 82)], width=4)      # horizontal
line([(232, 82), (232, 118)], width=4)     # down turn
# 3) closing tick / connecting横
line([(155, 128), (232, 118)], width=4)

# ---- Right bottom: 又 ----
# 1) 横撇 - horizontal that turns into long falling-left
line([(130, 158), (215, 158)], width=4)    # short horizontal
line([(215, 158), (125, 250)], width=5)    # long 撇 down-left
# 2) 捺 - long sweeping falling-right
line([(165, 175), (275, 265)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0281_设/01_设.png")
print("saved")
