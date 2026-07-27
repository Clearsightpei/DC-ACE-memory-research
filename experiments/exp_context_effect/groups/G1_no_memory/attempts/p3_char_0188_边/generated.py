"""Render 边 (biān) to 300x300 PNG using PIL.

边 = 辶 (walking radical, wrapping bottom-left) + 力 (right upper area).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 力 component (right upper area) ---
# Top short slash (丿-like) above the top bar
line([(150, 55), (175, 90)], width=5)

# Horizontal + vertical-with-hook (横折钩 top of 力)
line([(160, 95), (230, 92)], width=6)
line([(230, 92), (225, 195), (205, 208)], width=5)

# 力's left slash (长撇) from inside the top bar down-left
line([(180, 105), (140, 210)], width=6)

# --- 辶 walking radical (left side + bottom sweep) ---
# Top dot of 辶 (small stroke upper-left)
line([(78, 105), (95, 128)], width=5)

# Middle horizontal-fold of 辶 — small angled curve
line([(65, 155), (100, 160)], width=5)
line([(100, 160), (78, 200), (95, 218)], width=5)

# Bottom long sweeping stroke (平捺) — starts lower-left, curves along bottom, sweeps up-right
line([(50, 235), (85, 258), (150, 262), (215, 255), (265, 235)], width=7)

out = os.path.join(os.path.dirname(__file__), "01_边.png")
img.save(out)
print(f"wrote {out}")
