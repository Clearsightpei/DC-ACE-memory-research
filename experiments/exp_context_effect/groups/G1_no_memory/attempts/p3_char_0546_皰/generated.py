"""G1 attempt for 皰 (pao) — left: 皮 (5 strokes), right: 包 (5 strokes)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ============ LEFT: 皮 (x ~ 35..140) ============
# 1) Top short 横 (little horizontal at top)
stroke([(70, 80), (110, 78)], width=4)
# 2) Long left 撇 (long falling left curve from top-right area)
stroke([(105, 78), (95, 105), (80, 145), (60, 200), (40, 245)], width=4)
# 3) 横折 — horizontal then turn down (upper mid part of 皮)
stroke([(80, 115), (135, 110), (135, 155)], width=4)
# 4) 竖 (short vertical inside, forming 又 top left)
stroke([(95, 130), (90, 175)], width=4)
# 5) 捺 (right-falling from mid to lower-right)
stroke([(95, 165), (120, 200), (150, 245)], width=4)

# ============ RIGHT: 包 (x ~ 160..280) ============
# 6) Top 撇 (short slash)
stroke([(210, 65), (185, 105)], width=4)
# 7) 横折钩 — horizontal then long curve down and hook left
stroke([(185, 105), (255, 100), (265, 115), (260, 210), (245, 245), (205, 258), (180, 248)], width=4)
# 8) Top horizontal of 巳
stroke([(200, 140), (240, 140)], width=4)
# 9) Middle horizontal + left vertical of 巳 (as one 横折)
stroke([(200, 140), (200, 190), (240, 190)], width=4)
# 10) 竖弯钩 tail
stroke([(240, 140), (240, 200), (250, 220), (270, 220)], width=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0546_皰/01_皰.png")
print("done")
