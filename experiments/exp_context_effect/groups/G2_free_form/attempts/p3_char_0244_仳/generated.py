"""
Target: 仳 = 亻 (left) + 比 (right)
比 = 匕 + 匕 (D. rule: apply 匕 sibling row TWICE, once per 匕)

# SIGNATURE CHECK (匕, applied to BOTH sub-glyphs of 比):
# 匕: top stroke is a 撇 (upper-right→lower-left);
#     terminal hook flicks UP-and-LEFT (~-105° to -115°)
# Right 匕: 撇 goes UR->LL, 竖弯钩 flick UP-LEFT
# Left 匕 in 比: written as 横+竖(bent hook) — flick UP-LEFT
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=6):
    d.line(points, fill=BLACK, width=width, joint="curve")


# --- 亻 (left, x ~ 40..110) ---
# 撇: apex upper-right, sweeps down-left more diagonally
stroke([(100, 55), (85, 100), (65, 145), (45, 180)], width=7)
# 竖: from apex straight down, slightly shorter than 撇 tail
stroke([(88, 105), (88, 260)], width=7)

# --- 比 (right, x ~ 130..270) ---
# Left half of 比 (looks like small mirrored 匕 without prominent hook):
#   - short 横 attached to top of vertical, extending RIGHT (not crossing)
#   - vertical goes straight down; slight up-left tick at bottom
stroke([(140, 110), (180, 108)], width=7)   # 横 to the right of vertical top
stroke([(140, 110), (140, 250), (148, 258), (135, 253)], width=7)  # 竖 + small flick

# Right half of 比 (匕: 撇 top + 竖弯钩 with flick UP-LEFT)
# 撇 from upper-right down-left, crossing near mid-height
stroke([(245, 80), (225, 135), (210, 180), (195, 225)], width=7)
# 竖弯钩: comes down from where 撇 crosses, curves right along bottom, flicks UP-LEFT
stroke(
    [(215, 135), (215, 225), (230, 250), (260, 250), (270, 240), (258, 228)],
    width=7,
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0244_仳/01_仳.png"
)
print("saved")
