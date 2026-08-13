"""G1 render of 疱 (bao4) - 疒 radical + 包 inside/right."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width)

# ==== 疒 radical (left) ====
# 1) top dot (short slash, upper-left) - 点
line([(110, 55), (125, 72)], width=4)

# 2) top horizontal (short) - 横
line([(85, 95), (180, 90)], width=4)

# 3) long left-falling stroke (撇) - from near top-right of horizontal, sweeps down-left
pieces = [(135, 95), (120, 130), (100, 175), (75, 230), (60, 255)]
for i in range(len(pieces)-1):
    line([pieces[i], pieces[i+1]], width=4)

# 4) two short slashes inside 疒 (on the left interior)
line([(95, 130), (115, 145)], width=4)   # upper 点
line([(80, 170), (105, 185)], width=4)   # lower 点

# ==== 包 (right) ====
# 5) 勹 top slash (short 撇) - top-left corner of 包
line([(175, 100), (165, 118)], width=4)

# 6) 勹 body: horizontal top going right, curve down right side, hook at bottom
line([(165, 118), (235, 118)], width=4)  # top horizontal
# right curve down
curve_pts = [(235, 118), (238, 160), (232, 205), (215, 245)]
for i in range(len(curve_pts)-1):
    line([curve_pts[i], curve_pts[i+1]], width=4)
# hook to left at bottom (勹 hook goes left-up)
line([(215, 245), (195, 240)], width=4)

# ==== 巳 inside 包 ====
# small horizontal top
line([(175, 150), (215, 150)], width=4)
# right side down
line([(215, 150), (215, 190)], width=4)
# bottom back to left
line([(215, 190), (180, 190)], width=4)
# left vertical connecting to tail (curves down and left)
line([(180, 150), (180, 200)], width=4)
line([(180, 200), (195, 215)], width=4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0518_疱/01_疱.png")
print("saved")
