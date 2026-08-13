"""Render 苦 (bitter) at 300x300, white bg, black ink.
Structure: 艹 (grass radical) on top + 古 (gu) below.
古 = 十 above 口.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill="black", width=w)

# --- 艹 (grass radical) top — compact, sits above 古 ---
# Long horizontal bar for 艹
line((55, 75), (245, 70), w=6)
# Left vertical (slight left-lean top)
line((90, 45), (85, 115))
# Right vertical (slight right-lean top)
line((210, 45), (215, 118))

# --- 古 below ---
# 十: horizontal (long, spanning wide) — the main long crossbar of 苦
line((20, 145), (280, 142), w=6)
# 十 vertical — extends from just below top of 古 down toward 口
line((150, 118), (150, 200))

# 口 (mouth) — box at bottom
line((108, 200), (108, 270))          # left vertical
line((108, 200), (200, 203))          # top horizontal
line((200, 203), (198, 270))          # right vertical
line((108, 270), (200, 270))          # bottom horizontal

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_苦.png"))
print("saved")
