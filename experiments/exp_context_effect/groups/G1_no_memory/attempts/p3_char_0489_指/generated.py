"""G1 render of 指 (finger) — hand-shaped left radical 扌 + 旨 right."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")

# ---------- Left radical 扌 (shou3-pang) ----------
# Horizontal stroke (short, slanted up-right)
line([(35, 105), (110, 95)], w=LW)
# Vertical hook stroke
line([(75, 65), (75, 245)], w=LW)
line([(75, 245), (92, 235)], w=LW)
# Rising stroke (提) from lower-left going up-right
line([(38, 195), (110, 165)], w=LW)

# ---------- Right side 旨 (top: 匕-like spoon; bottom: 日) ----------
# 匕 top: short slanted stroke (piě)
line([(150, 80), (180, 65)], w=LW)
# 匕 vertical then turning right and up (hook)
line([(165, 60), (165, 125)], w=LW)
line([(165, 125), (225, 125)], w=LW)
line([(225, 125), (225, 100)], w=LW)  # small up-hook

# Bottom component 日 (rectangle with middle horizontal)
# Left vertical
line([(160, 155), (160, 265)], w=LW)
# Top horizontal
line([(160, 155), (245, 155)], w=LW)
# Right vertical
line([(245, 155), (245, 265)], w=LW)
# Middle horizontal
line([(160, 208), (245, 208)], w=LW)
# Bottom horizontal
line([(160, 265), (245, 265)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0489_指/01_指.png")
