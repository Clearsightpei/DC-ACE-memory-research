"""Render 保 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts):
    d.line(pts, fill="black", width=LW)

# 保 = 亻 (left) + 呆 (right: 口 on top of 木)

# --- 亻 (person radical, left) ---
# ノ (piě): from upper-right down to lower-left, short
line([(85, 75), (55, 135)])
# 丨 vertical: starts where ノ meets, goes down long
line([(70, 110), (70, 240)])

# --- 口 (mouth box, upper right) ---
# left vertical
line([(135, 80), (135, 135)])
# top horizontal + right vertical (in a turn)
line([(135, 80), (225, 82)])
line([(225, 82), (225, 135)])
# bottom horizontal
line([(135, 135), (225, 135)])

# --- 木 (below 口) ---
# horizontal 一 (wider than 口)
line([(105, 160), (250, 162)])
# vertical 丨 (trunk from just below 口 down to bottom)
line([(175, 135), (175, 265)])
# 撇 (left descending)
line([(175, 175), (110, 255)])
# 捺 (right descending)
line([(175, 175), (245, 255)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0479_保/01_保.png")
print("saved")
