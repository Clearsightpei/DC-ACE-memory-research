"""G1 draw 疭 — 疒 radical (top+left frame) + 从 inside."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 疒 radical ---
# 1. top-left short dot (slanting)
stroke([(78, 55), (90, 78)], width=4)
# 2. top horizontal (long, extending right, slight tilt up)
stroke([(90, 90), (220, 78)], width=4)
# 3. long sweeping left-down curve (piě) from just below top-horizontal start
stroke([(92, 92), (80, 140), (65, 200), (55, 255)], width=4)
# 4. two inner-left dots (biǎn dou)
stroke([(102, 118), (95, 138)], width=4)   # upper small dot
stroke([(115, 135), (108, 158)], width=4)  # lower small dot

# --- 从 (inside, lower-right area) ---
# left 人
stroke([(130, 130), (115, 200), (100, 265)], width=4)  # piě sweep
stroke([(128, 180), (155, 265)], width=4)              # nà
# right 人
stroke([(195, 125), (180, 195), (165, 265)], width=4)  # piě sweep
stroke([(195, 180), (255, 275)], width=4)              # nà

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0454_疭/01_疭.png")
print("done")
