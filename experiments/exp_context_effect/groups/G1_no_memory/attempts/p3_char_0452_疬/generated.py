"""Render 疬 (illness radical 疒 + 力) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

def curve(points, w=LW):
    d.line(points, fill="black", width=w, joint="curve")

# ============ 疒 radical ============
# Stroke 1: top-right tick (short diagonal)
line(140, 55, 160, 70)

# Stroke 2: top horizontal (long)
line(75, 95, 240, 92)

# Stroke 3: left piě — sweeps down-left from just under horizontal
curve([(105, 95), (85, 150), (65, 210), (50, 270)])

# Stroke 4: upper dot on 冫 (inside, to the right of piě)
line(75, 135, 90, 148)

# Stroke 5: lower dot on 冫
line(60, 175, 78, 188)

# ============ 力 (nested inside 疒 lower-right) ============
# Horizontal-fold-hook: top horizontal + right vertical fold + inward hook at bottom
curve([(140, 140), (225, 138), (223, 175), (215, 225), (200, 260), (185, 265)])

# 力 piě: from top-mid, sweeping down-left
curve([(160, 145), (145, 200), (130, 250), (115, 275)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0452_疬/01_疬.png")
print("saved")
