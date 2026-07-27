"""Render 用 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# 用: 5 strokes
# Frame roughly: left x ~ 90, right x ~ 210, top y ~ 60, bottom y ~ 260
# Inner middle vertical at x ~ 150

# Stroke 1: 丿 left slant — starts near top of left side, sweeps down-left
d.line([(105, 65), (75, 265)], fill=BLACK, width=LW)

# Stroke 2: 横折钩 — top horizontal then down the right side, ending with a small hook
# Top horizontal from left-frame-top to right
d.line([(105, 65), (215, 75)], fill=BLACK, width=LW)
# Right vertical down
d.line([(215, 75), (210, 260)], fill=BLACK, width=LW)
# Small hook at bottom (going left-up slightly)
d.line([(210, 260), (192, 250)], fill=BLACK, width=LW)

# Stroke 3: top inner horizontal (upper crossbar)
d.line([(95, 130), (212, 135)], fill=BLACK, width=LW)

# Stroke 4: middle inner horizontal (lower crossbar)
d.line([(90, 195), (211, 198)], fill=BLACK, width=LW)

# Stroke 5: middle vertical — from top down through both crossbars to bottom
d.line([(150, 75), (150, 260)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0168_用/01_用.png")
print("saved")
