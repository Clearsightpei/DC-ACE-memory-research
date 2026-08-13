"""
伾 = 亻 (person radical, left) + 丕 (right)
丕 = 一 (top short-medium) + 丿 (slanting) + 丨 (vertical) + 丶 (dot/short) + 一 (bottom long)

Left 亻: 撇 from top going down-left, then 竖 straight down (compressed left, taller).
Right 丕: top horizontal, then middle group (丿, 丨, dot), bottom long horizontal.

Composition: left ~35% of width, right ~65%.
Bottom horizontal of 丕 is the longest single stroke, extends near full right width.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=6):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# --- Left: 亻 (person radical) ---
# 撇: slants from top going down-left; top point at (100,65)
stroke([(100, 65), (92, 105), (78, 150), (55, 215)], width=6)
# 竖: starts from the 撇 body (around y=115) and goes straight down
stroke([(90, 115), (92, 265)], width=6)

# --- Right: 丕 ---
# Top 一 (medium-long horizontal, slight upward tilt to right)
stroke([(140, 90), (260, 80)], width=6)

# Middle: 丿 (short slant, sits just below top-一 on left side of 丕)
stroke([(185, 105), (168, 145), (152, 195)], width=6)

# Middle: 丨 (vertical, center of 丕)
stroke([(212, 108), (215, 225)], width=6)

# 丶 dot on right (short slanted stroke)
stroke([(238, 150), (262, 162)], width=6)

# Bottom 一 (long horizontal — longest stroke of the character)
stroke([(130, 258), (288, 248)], width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0320_伾/01_伾.png")
