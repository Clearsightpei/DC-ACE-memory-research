"""Render 治 (govern/manage) as 300x300 PNG.
Structure: 氵 (three-drops water) left + 台 right; 台 = 厶 + 口.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=w)

# --- Left: 氵 water radical (three drops) ---
# top dot (short diagonal, down-left)
polyline([(80, 85), (95, 108)])
# middle dot (short diagonal, down-left, further left)
polyline([(55, 130), (75, 150)])
# bottom rising 提 stroke (up-right)
polyline([(60, 235), (100, 200)])

# --- Right: 台 ---
# 厶 (top): 撇 (down-left) + 折 (down-right then hook back) + 点 inside
# left down-slant
polyline([(180, 70), (150, 115)])
# right stroke: horizontal-ish then bent down
polyline([(180, 70), (220, 108), (185, 130)])
# small dot/hook inside 厶
polyline([(170, 125), (195, 130)])

# --- 口 (bottom rectangle, slightly narrower) ---
lx, rx, ty, by = 160, 235, 165, 235
# left vertical
polyline([(lx, ty), (lx, by)])
# top + right (横折)
polyline([(lx, ty), (rx, ty), (rx, by)])
# bottom horizontal
polyline([(lx, by), (rx, by)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0405_治/01_治.png")
