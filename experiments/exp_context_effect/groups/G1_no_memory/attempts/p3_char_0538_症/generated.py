"""G1 render of 症 (illness) — 疒 radical containing 正."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, width=5):
    d.line([(x1, y1), (x2, y2)], fill="black", width=width)

# --- 疒 radical (sickness) ---
# 1. top small dot (点) — above the horizontal
line(115, 55, 130, 70, width=5)

# 2. horizontal top stroke (横)
line(80, 90, 220, 90, width=5)

# 3. long left-falling stroke (撇) — starts at left end of horizontal, curves down-left
line(85, 90, 40, 275, width=5)

# 4. two dots inside the radical (upper-left area, right of the pie)
# upper-left small dot
line(75, 125, 90, 140, width=5)
# lower-left small dot (below the upper)
line(70, 160, 85, 175, width=5)

# --- 正 (correct) inside the radical, lower-right ---
# top horizontal
line(120, 155, 230, 155, width=5)
# left short vertical
line(145, 155, 145, 210, width=5)
# middle short horizontal
line(145, 195, 205, 195, width=5)
# center main vertical
line(170, 155, 170, 255, width=5)
# bottom long horizontal
line(105, 255, 250, 255, width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0538_症/01_症.png")
