from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 4

def line(pts, w=W):
    d.line(pts, fill="black", width=w, joint="curve")

# 度 — 广 (yǎn) radical wrapping 廿-like + 又 at bottom

# 广 radical:
# 1) small dot at top
line([(148, 30), (158, 55)], W)
# 2) top horizontal (slight upward tilt to right)
line([(90, 78), (215, 68)], W)
# 3) long left-falling piě (from left end of horizontal down to lower-left corner)
line([(100, 78), (85, 130), (65, 190), (40, 265)], W)

# Interior: 廿-style with horizontal cross-bar extending past on right
# upper horizontal
line([(105, 130), (215, 125)], W)
# left inner vertical
line([(125, 130), (123, 180)], W)
# right inner vertical
line([(195, 125), (197, 180)], W)
# lower long horizontal (extends past right side)
line([(100, 180), (250, 175)], W)

# Bottom 又 (starts roughly under interior)
# 横撇 (horizontal turning into piě): short horizontal then piě sweeping down-left
line([(115, 210), (200, 205)], W)          # horizontal top of 又
line([(200, 205), (180, 225), (110, 285)], W)  # piě sweeping down-left
# 捺 (nà): diagonal from upper-middle down to lower-right
line([(150, 220), (200, 260), (255, 285)], W)

out_path = os.path.join(os.path.dirname(__file__), "01_度.png")
img.save(out_path)
print("wrote", out_path)
