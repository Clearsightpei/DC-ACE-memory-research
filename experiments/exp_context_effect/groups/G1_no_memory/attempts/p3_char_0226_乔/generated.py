"""G1 render of 乔 (p3_char_0226) at 300x300."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# 乔 — 6 strokes: 丿, 一, 丿, 一, 丿, 亅
# Top piece 夭: short 丿 + long 一 + long 丿
# Bottom piece: short 一 + 丿 (left leg) + 亅 (right leg with hook)

# 1) top short 丿 — steeper slant down-left
line([(160, 55), (120, 90)], 7)

# 2) long 一 across upper — slight upward slope to right
line([(70, 105), (235, 95)], 7)

# 3) long 丿 — from just under right end of horizontal, sweeps down-left
line([(185, 108), (55, 230)], 7)

# 4) short 一 in middle — cuts across the 丿
line([(100, 155), (220, 150)], 6)

# 5) left leg 丿 — starts at middle-left of 4, curves down-left
line([(148, 158), (135, 210), (115, 260)], 6)

# 6) right leg 亅 — vertical then hook left at bottom
line([(180, 158), (180, 250)], 6)
line([(180, 250), (165, 258)], 6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_乔.png"))
print("wrote", os.path.join(out_dir, "01_乔.png"))
