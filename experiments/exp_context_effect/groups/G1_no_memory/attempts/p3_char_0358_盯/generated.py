from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# ---- Left: 目 (a tall rectangle with three internal horizontal bars) ----
# Bounding box: x 45-115, y 70-240
left_x, right_x = 45, 115
top_y, bot_y = 70, 240

# Stroke 1: left vertical
line(left_x, top_y, left_x, bot_y)
# Stroke 2: top horizontal + right vertical (横折)
line(left_x, top_y, right_x, top_y)
line(right_x, top_y, right_x, bot_y)
# Stroke 3: upper inner horizontal
line(left_x + 4, top_y + 55, right_x - 4, top_y + 55)
# Stroke 4: middle inner horizontal
line(left_x + 4, top_y + 108, right_x - 4, top_y + 108)
# Stroke 5: bottom horizontal (closing)
line(left_x, bot_y, right_x, bot_y)

# ---- Right: 丁 ----
# Long horizontal across the right side, then vertical hook
# Horizontal starts a bit left of 目's right edge (crosses over slightly)
h_left, h_right = 130, 285
h_y = 82
line(h_left, h_y, h_right, h_y)

# Vertical hook: comes down from about mid-horizontal, ending with a small left hook
v_x = 225
v_top = h_y
v_bot = 245
line(v_x, v_top, v_x, v_bot)
# small hook to left at bottom
line(v_x, v_bot, v_x - 20, v_bot - 6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_盯.png"))
print("saved")
