"""G1 render of 起 — 走 radical (left/bottom) + 己 (upper right)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width)

# =========== 走 radical ===========
# 土 portion (upper-left)
# short top horizontal
line([(95, 60), (160, 60)], 4)
# vertical of 土
line([(128, 55), (128, 125)], 4)
# middle wide horizontal
line([(70, 100), (170, 95)], 4)
# lower slanted stroke (走's 撇 to left)
line([(128, 125), (65, 195)], 4)
# small right-tick off the pie
line([(90, 165), (135, 170)], 4)

# 走's 捺 (long sweep from mid-left curving down-right to bottom-right corner)
# Simulate curve with segments
sweep = [(60, 205), (100, 220), (150, 235), (200, 250), (250, 262), (285, 270)]
for i in range(len(sweep)-1):
    line([sweep[i], sweep[i+1]], 5)

# =========== 己 (upper right) ===========
# 横折 (horizontal then down)
line([(185, 80), (250, 80)], 4)
line([(250, 80), (250, 135)], 4)
# middle horizontal
line([(190, 135), (250, 135)], 4)
# 竖弯钩 base
line([(190, 135), (190, 185)], 4)
line([(190, 185), (265, 185)], 4)
# hook up
line([(265, 185), (265, 165)], 4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0505_起/01_起.png")
print("saved")
