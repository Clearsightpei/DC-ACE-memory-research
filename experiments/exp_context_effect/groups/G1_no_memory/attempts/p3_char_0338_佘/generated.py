from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

def poly(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# 佘 = 人 (top) + 一 + 示-like bottom
# apex near top-center
apex = (150, 40)

# 人 top: left-falling (撇) and right-falling (捺)
# left stroke: apex down-left, sweeping
poly([apex, (120, 80), (85, 130), (55, 165)], w=6)
# right stroke: apex down-right, sweeping wider (捺)
poly([(155, 45), (185, 90), (225, 135), (255, 165)], w=6)

# small horizontal (一) under the 人 roof, mid area
line((100, 155), (200, 155), w=5)

# vertical stroke (竖) going down center
poly([(150, 165), (150, 260)], w=5)
# small hook at bottom of vertical (optional)
# line((150, 260), (140, 255), w=5)

# left small stroke (撇) near bottom - starts near vertical mid-bottom, goes down-left
poly([(148, 210), (120, 245), (100, 265)], w=5)

# right small stroke (点/捺) - from near vertical, goes down-right
poly([(152, 215), (180, 245), (200, 265)], w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佘.png"))
print("saved")
