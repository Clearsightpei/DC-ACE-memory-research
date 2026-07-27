"""G1 render: 有 (revised)"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 3

# 有 = 一横 + 一撇 (crossing) + 月 sitting under the right portion.

# Stroke 1: 横 - long top horizontal, slight downward slope right-to-left
d.line([(55, 95), (250, 85)], fill=INK, width=LW)

# Stroke 2: 撇 - starts high above horizontal, sweeps down-left to bottom
d.line([(155, 60), (60, 265)], fill=INK, width=LW)

# 月 sits under the right side of the 横, starting around x=130
# Stroke 3: left vertical of 月 (short 竖 that leans slightly)
d.line([(130, 110), (128, 245)], fill=INK, width=LW)

# Stroke 4: 横折钩 of 月 - top horizontal then long vertical with hook at end
d.line([(130, 110), (225, 115)], fill=INK, width=LW)   # top
d.line([(225, 115), (215, 260)], fill=INK, width=LW)   # right vertical
d.line([(215, 260), (198, 258)], fill=INK, width=LW)   # small hook

# Stroke 5: upper inner 横
d.line([(135, 160), (218, 162)], fill=INK, width=LW)

# Stroke 6: lower inner 横
d.line([(133, 205), (216, 208)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0221_有/01_有.png")
