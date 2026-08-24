"""G1 render of 运 (yun) — 云 (upper-right) + 辶 (walking radical). Revised."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 云 component (upper-right region) ---
# top short 点 (dot slash) above the 二
stroke([(140, 55), (160, 72)], width=7)
# upper horizontal of 二 (shorter)
stroke([(145, 85), (215, 82)], width=7)
# lower horizontal of 二 (longer, slight dip)
stroke([(120, 115), (235, 110)], width=7)
# 厶 : single connected 撇折点 shape
stroke([(160, 135), (135, 175), (185, 180), (215, 165)], width=7)

# --- 辶 component (wraps left + bottom) ---
# top 点 (small dot slash) at upper-left
stroke([(70, 90), (85, 105)], width=8)
# 横折折撇: continuous zigzag under the dot
stroke([(60, 135), (95, 140), (70, 175), (105, 190)], width=7)
# long 平捺 sweeping across the bottom
stroke([(50, 225), (150, 260), (275, 225)], width=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0329_运/01_运.png")
