"""Render 処 to a 300x300 PNG."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 処 layout:
# 夂 component: sits in upper-left, its 捺 sweeps down through center
# 几 component (几-like enclosure): big arching stroke around the right/bottom

# --- 夂 (top-left) ---
# stroke 1: short 撇 (top diagonal, upper-left)
stroke([(95, 75), (75, 100)], width=5)

# stroke 2: 横撇 - short horizontal turning into a 撇 going down-left
stroke([(95, 90), (135, 95), (110, 130), (85, 165)], width=5)

# stroke 3: 捺 - starts near where 横撇 turns, sweeps down and to the right
stroke([(110, 120), (145, 160), (180, 210), (215, 250)], width=6)

# --- 几-like enclosing shape (right side) ---
# stroke 4: left 撇 of 几 (short, from upper area down to lower-left)
stroke([(140, 130), (125, 175), (105, 240)], width=5)

# stroke 5: 横折弯钩 - top horizontal from mid to right, then curves down along right edge, ends with small upward hook
stroke([(140, 130), (200, 128), (245, 140), (255, 200), (260, 250), (245, 265)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0213_処/01_処.png")
