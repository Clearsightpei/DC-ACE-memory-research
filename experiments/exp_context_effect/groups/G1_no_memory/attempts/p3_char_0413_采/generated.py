from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def line(pts, w=LW):
    d.line(pts, fill=INK, width=w)

# 采 = 爫 (top claw, 4 strokes) + 木 (bottom tree, 4 strokes)

# --- Top 爫 (claw radical) — 4 short strokes, top-heavy ---
# Stroke 1: left short 撇 (down-left)
line([(105, 65), (90, 100)], w=LW)
# Stroke 2: middle-left short down 丨
line([(130, 78), (128, 108)], w=LW)
# Stroke 3: middle-right short down 丨
line([(165, 78), (168, 108)], w=LW)
# Stroke 4: right short 撇 (down-left, mirrored to close the claw)
line([(205, 65), (195, 108)], w=LW)
# Top connecting horizontal (part of 爫 visual - light stroke across top)
line([(100, 70), (200, 62)], w=LW)

# --- Middle horizontal (top of 木) ---
line([(50, 160), (250, 152)], w=LW)

# --- Vertical (through center down) ---
line([(150, 125), (152, 275)], w=LW)

# --- Left falling 撇 ---
line([(148, 170), (60, 265)], w=LW)

# --- Right falling 捺 ---
line([(155, 170), (245, 262)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_采.png")
img.save(out)
print("wrote", out)
