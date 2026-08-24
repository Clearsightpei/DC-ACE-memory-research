"""Render 畈 (tian + fan) at 300x300."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

# ============ LEFT: 田 (tian) ============
left, right = 45, 130
top, bottom = 115, 210

d.line([(left, top), (right, top)], fill="black", width=LW)
d.line([(right, top), (right, bottom)], fill="black", width=LW)
d.line([(left, top), (left, bottom)], fill="black", width=LW)
d.line([(left, bottom), (right, bottom)], fill="black", width=LW)
midx = (left + right) // 2
midy = (top + bottom) // 2
d.line([(midx, top), (midx, bottom)], fill="black", width=LW)
d.line([(left, midy), (right, midy)], fill="black", width=LW)

# ============ RIGHT: 反 (fan) ============
# Stroke 1: top flick — small horizontal at upper-right
d.line([(200, 95), (255, 80)], fill="black", width=LW)

# Stroke 2: 撇 (piě) — long diagonal from upper right down to lower left
# Starts near top of the flick, sweeps down and left
d.line([(200, 95), (150, 250)], fill="black", width=LW)

# Stroke 3: interior 横 (short horizontal) crossing the piě
d.line([(178, 165), (250, 155)], fill="black", width=LW)

# Stroke 4: 捺 (na) — big sweeping stroke from interior down-right
d.line([(200, 165), (275, 250)], fill="black", width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0430_畈/01_畈.png")
