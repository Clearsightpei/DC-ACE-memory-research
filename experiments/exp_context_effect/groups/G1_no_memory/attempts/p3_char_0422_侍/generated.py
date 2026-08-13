from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# 侍 = 亻 (left) + 寺 (right)

# ---- 亻 (left radical: person) ----
# 撇 (falling diagonal from top)
stroke([(95, 70), (90, 105), (75, 150), (55, 215)], width=6)
# 竖 (vertical starting at joint on 撇)
stroke([(88, 125), (88, 245)], width=6)

# ---- 寺 (right side) ----
# 土 component
# short 横 top
stroke([(155, 85), (230, 83)], width=6)
# 竖 vertical through top horizontals
stroke([(190, 65), (192, 150)], width=6)
# longer 横 middle
stroke([(135, 125), (255, 123)], width=6)

# 寸 component
# long 横
stroke([(125, 170), (265, 168)], width=6)
# 竖钩 vertical with small hook
stroke([(200, 150), (200, 265), (185, 268)], width=6)
# 点 (dot to the right of the vertical, mid-lower)
stroke([(225, 200), (245, 218)], width=8)

out = os.path.join(os.path.dirname(__file__), "01_侍.png")
img.save(out)
print("saved", out)
