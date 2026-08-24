from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# 佐 = 亻(person radical) + 左
# Left side: 亻 (person radical) — occupies left ~1/3
# Stroke 1: 撇 (left-falling) from top down-left
stroke([(95, 55), (60, 200)], width=5)
# Stroke 2: 竖 (vertical) starting from mid of 撇, going straight down
stroke([(85, 130), (85, 260)], width=5)

# Right side: 左 — occupies right ~2/3
# Stroke 1: 横 (short top horizontal) - slightly tilted
stroke([(140, 90), (240, 78)], width=5)
# Stroke 2: 撇 (long left-falling from top) through the horizontal
stroke([(180, 60), (145, 260)], width=5)
# Stroke 3: 工 top horizontal (short)
stroke([(155, 175), (230, 172)], width=5)
# Stroke 4: 工 vertical
stroke([(195, 175), (195, 240)], width=5)
# Stroke 5: 工 bottom horizontal (longer)
stroke([(140, 245), (260, 243)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0332_佐/01_佐.png")
