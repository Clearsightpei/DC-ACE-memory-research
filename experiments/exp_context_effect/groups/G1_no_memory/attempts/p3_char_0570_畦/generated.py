from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
T = 4  # stroke thickness

def line(x1, y1, x2, y2, w=T):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

# ============ LEFT: 田 (tian - field) ============
# Positioned in left third, slightly upper-mid
L, R = 40, 130     # left/right edges of 田
TP, BT = 70, 210   # top/bottom edges of 田
# Outer box
line(L, TP, R, TP)          # top
line(L, TP, L, BT)          # left
line(R, TP, R, BT)          # right
line(L, BT, R, BT)          # bottom
# Inner cross
midX = (L + R) // 2
midY = (TP + BT) // 2
line(midX, TP, midX, BT)    # vertical middle
line(L, midY, R, midY)      # horizontal middle

# ============ RIGHT: 圭 (gui - two 土 stacked) ============
# Upper 土
u_top_y = 60
u_mid_y = 115
u_bot_y = 145
u_v_x = 210
u_top_L, u_top_R = 175, 245
u_mid_L, u_mid_R = 185, 235
u_bot_L, u_bot_R = 160, 260

# Upper 土: horizontal top (short), vertical, horizontal middle (shorter), horizontal bottom (longest)
line(u_top_L, u_top_y, u_top_R, u_top_y)      # top short horizontal
line(u_v_x, u_top_y, u_v_x, u_bot_y)          # vertical
line(u_mid_L, u_mid_y, u_mid_R, u_mid_y)      # mid short horizontal
line(u_bot_L, u_bot_y, u_bot_R, u_bot_y)      # bottom long horizontal

# Lower 土
l_top_y = 175
l_mid_y = 220
l_bot_y = 260
l_v_x = 210
l_top_L, l_top_R = 180, 245
l_mid_L, l_mid_R = 190, 235
l_bot_L, l_bot_R = 150, 275

line(l_top_L, l_top_y, l_top_R, l_top_y)      # top short horizontal
line(l_v_x, l_top_y, l_v_x, l_bot_y)          # vertical
line(l_mid_L, l_mid_y, l_mid_R, l_mid_y)      # mid short horizontal
line(l_bot_L, l_bot_y, l_bot_R, l_bot_y)      # bottom long horizontal

out = os.path.join(os.path.dirname(__file__), "01_畦.png")
img.save(out)
print("wrote", out)
