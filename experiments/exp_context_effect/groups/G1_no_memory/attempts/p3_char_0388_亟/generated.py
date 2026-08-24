from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLK = (0, 0, 0)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=BLK, width=w)

# Top horizontal stroke (一)
line([(45, 60), (255, 55)], w=LW)

# Middle row: 口 (mouth) on left, 又 on right, connected by short curve on top
# --- 口 (small mouth, left) ---
line([(65, 115), (130, 113)])   # top
line([(67, 113), (73, 185)])    # left
line([(128, 113), (124, 180)])  # right
line([(73, 185), (124, 180)])   # bottom

# --- Right side: horizontal-turn top piece (like 又's top hook) ---
line([(135, 108), (240, 112)])  # top horizontal going right
line([(240, 112), (232, 140)])  # short turn down

# --- 又 body ---
# horizontal middle stroke
line([(150, 145), (245, 148)])
# piě (falling left) from upper right down to lower left
line([(215, 118), (155, 210)], w=LW)
# nà (falling right) from mid going down-right
line([(185, 155), (255, 215)], w=LW)

# Bottom horizontal stroke (一) - full width
line([(30, 260), (275, 258)], w=LW+1)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0388_亟/01_亟.png")
