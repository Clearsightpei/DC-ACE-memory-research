"""G1 drawer: 失 (character)"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 6

def line(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# Stroke 1: short 撇 tick at top (upper-left of the top piece of 失)
line([(150, 70), (128, 100)])

# Stroke 2: short top horizontal
line([(128, 100), (200, 95)])

# Stroke 3: long main 撇 (left-falling) — begins upper-right, sweeps to lower-left
line([(185, 60), (170, 120), (145, 175), (105, 230), (60, 270)])

# Stroke 4: main middle horizontal (longer than top one)
line([(70, 165), (235, 158)])

# Stroke 5: 捺 (right-falling) — from middle crossing point, down-right to lower-right corner
line([(160, 165), (195, 210), (230, 245), (260, 275)])

out = os.path.join(os.path.dirname(__file__), "01_失.png")
img.save(out)
print("wrote", out)
