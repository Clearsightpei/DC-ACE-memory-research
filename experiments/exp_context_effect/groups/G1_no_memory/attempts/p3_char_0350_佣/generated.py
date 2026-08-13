"""Render 佣 (yong) to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 佣 = 亻 (left person radical) + 用 (right)

# --- 亻 radical (left) ---
# Slanted top stroke (piě), starts high near top
stroke([(85, 55), (50, 145)], width=5)
# Vertical stroke, tall
stroke([(78, 115), (78, 260)], width=5)

# --- 用 (right side) ---
# Short piě at top-left of 用
stroke([(155, 55), (135, 95)], width=5)
# Top + right side with hook (横折钩)
stroke([(135, 90), (240, 85), (240, 260), (228, 268)], width=5)
# Left vertical
stroke([(135, 90), (135, 255)], width=5)
# Middle vertical extending below
stroke([(188, 88), (188, 278)], width=5)
# Upper inner horizontal
stroke([(135, 150), (240, 148)], width=5)
# Lower inner horizontal
stroke([(135, 205), (240, 203)], width=5)
# Bottom horizontal (closes frame)
stroke([(135, 255), (240, 255)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佣.png"))
print("saved")
