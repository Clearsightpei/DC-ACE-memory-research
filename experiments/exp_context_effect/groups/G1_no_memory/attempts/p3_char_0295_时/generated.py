"""G1 render for 时 (character, phase 3)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(a, b, w=LW):
    d.line([a, b], fill="black", width=w)

# ---- Left component: 日 (small, upper-left) ----
# Box roughly x:60-115, y:80-200
L, R = 60, 118
T, B = 80, 205
MID = (T + B) // 2

# left vertical
line((L, T), (L, B))
# top horizontal
line((L, T), (R, T))
# right vertical (slight lean out)
line((R, T + 2), (R + 2, B))
# middle horizontal
line((L, MID), (R + 1, MID))
# bottom horizontal
line((L, B), (R + 2, B))

# ---- Right component: 寸 ----
# 横 (top horizontal)
line((150, 105), (270, 100))
# 竖钩 (vertical with hook at bottom) — starts near top of 横 middle-right
line((215, 80), (213, 240))
# small hook to left
line((213, 240), (200, 232))
# 点 (dot) — short diagonal stroke on the left of 竖
line((175, 165), (195, 180))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0295_时/01_时.png")
