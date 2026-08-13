from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# 佽 = 亻 (left, person radical) + 次 (right)

# --- 亻 (left person radical) ---
# 撇 (top slant)
stroke([(70, 55), (45, 165)], width=5)
# 竖 (vertical), starts around mid of the slash
stroke([(60, 130), (60, 265)], width=5)

# --- 冫 (two-dot ice) on left of 欠 ---
# top dot (short slash)
stroke([(115, 85), (128, 105)], width=5)
# bottom dot (tick going up-right)
stroke([(115, 155), (130, 140)], width=5)

# --- 欠 (right portion) ---
# 撇 top short - top-left descending
stroke([(180, 55), (160, 90)], width=5)
# 橫折 - horizontal turning down (top of 欠 head)
stroke([(160, 82), (220, 82), (215, 118)], width=5)
# small 撇 inside/below 欠 head
stroke([(190, 118), (170, 148)], width=5)
# 撇 long - left-sweeping bottom of 欠
stroke([(200, 130), (135, 265)], width=5)
# 捺 - right-sweeping bottom
stroke([(175, 175), (265, 270)], width=5)

img.save(os.path.join(os.path.dirname(__file__), "01_佽.png"))
