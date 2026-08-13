from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=5):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# 侖 = 人 (roof) over 一 (short horizontal) over 冊-like grid
# Top: 人 (roof-like apex)
# Left diagonal of 人
stroke([(150, 40), (85, 100)], width=6)
# Right diagonal of 人
stroke([(150, 40), (220, 100)], width=6)

# Short horizontal under the roof (the '一' of 亼)
stroke([(100, 115), (205, 115)], width=6)

# Inner box below (like 冊 / 侖's lower component)
# Top horizontal of inner box
stroke([(80, 155), (225, 155)], width=6)
# Left vertical
stroke([(80, 155), (80, 260)], width=6)
# Right vertical (curving into a hook)
stroke([(225, 155), (225, 250), (215, 260)], width=6)
# Middle vertical dividing the box
stroke([(152, 155), (152, 260)], width=6)
# Bottom horizontal
stroke([(80, 260), (225, 260)], width=6)

# Two small inner horizontals in each cell
stroke([(80, 205), (152, 205)], width=5)
stroke([(152, 205), (225, 205)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0428_侖/01_侖.png")
