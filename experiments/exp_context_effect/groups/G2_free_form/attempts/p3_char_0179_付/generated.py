"""
付 (fù) — 亻 (LEFT, tall-narrow ~40% width) + 寸 (十 with dot)
5 strokes total:
  1. 撇 (亻 top): short down-left flick, starts ~x=100 y=90, ends ~x=60 y=170
  2. 竖 (亻 right leg): long vertical, ~x=95 y=95 to x=95 y=260
  3. 横 (寸 top): horizontal bar across right side, x=145..255 y=140
  4. 竖钩 (寸 middle vertical with hook): x=200 y=115 to y=250, tiny hook up-left
  5. 点 (寸 dot on right): small teardrop at ~(220, 180)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# 1. 亻 撇 — short down-left
stroke([(110, 85), (95, 120), (75, 155), (55, 180)], width=7)

# 2. 亻 竖 — long vertical
stroke([(100, 115), (100, 175), (100, 235), (100, 275)], width=8)

# 3. 寸 横 — top horizontal (centered around 竖钩 at x~200; extends slightly more right)
stroke([(145, 145), (185, 143), (225, 143), (260, 145)], width=7)

# 4. 寸 竖钩 — vertical with hook flicking up-left at bottom
stroke([(205, 118), (205, 175), (205, 235), (205, 260)], width=8)
# hook: flick UP-and-LEFT (per TIER-0 rule: never DOWN)
stroke([(205, 260), (190, 252), (178, 243)], width=7)

# 5. 寸 点 — dot on right side of 竖钩, mid-height
stroke([(225, 175), (240, 195)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0179_付/01_付.png")
