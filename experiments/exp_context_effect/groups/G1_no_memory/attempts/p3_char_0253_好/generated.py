"""Render 好 (nǚ + zǐ) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width)

# --- Left component: 女 (nǚ, 3 strokes) ---
# Stroke 1: 撇点 — down-left, then a "dot" back down-right
line([(95, 80), (55, 170)], width=5)          # 撇 down-left
line([(55, 170), (100, 200)], width=5)        # 点 down-right (forms X bottom-left leg)

# Stroke 2: 撇 — long diagonal from upper-right down to lower-left, crossing stroke 1
line([(125, 100), (30, 240)], width=5)

# Stroke 3: 横 — horizontal bar across the middle
line([(20, 180), (145, 170)], width=5)

# --- Right component: 子 (zǐ, 3 strokes) ---
# Stroke 1: 横撇 — flat then sharp down-left tail
line([(160, 100), (240, 95)], width=5)        # 横
line([(240, 95), (195, 145)], width=5)        # 撇 (down-left tail)

# Stroke 2: 竖钩 — long vertical with small hook left at bottom
line([(210, 110), (220, 260)], width=5)       # vertical spine
line([(220, 260), (200, 250)], width=5)       # hook left

# Stroke 3: 横 — horizontal crossbar through middle of 子
line([(160, 185), (275, 180)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0253_好/01_好.png")
print("saved")
