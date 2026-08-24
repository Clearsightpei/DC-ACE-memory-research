"""
行 (xíng) — 6 strokes, left-right compound.
Left component 彳 (double-person radical):
  1. 撇 (short, top)   - top-left flick down-left
  2. 撇 (mid)          - a bit lower/longer, down-left
  3. 竖 (long vertical) - down the middle-left
Right component 亍:
  4. 横 (short top)
  5. 横 (longer middle)
  6. 竖钩 (long vertical with tiny hook flick UP-LEFT at bottom)

Hook flick rule (from memory_index TIER-0-B): 竖钩 flicks UP-and-LEFT.
Left/right proportion ~ 45/55, left compressed vertically & narrow.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")

# ---------- LEFT: 彳 ----------
# 1. Upper 撇 - short flick from top starting slightly right, going down-left
stroke([(105, 70), (95, 90), (78, 108)], width=7)

# 2. Middle 撇 - starts to the right of the first, longer sweep down-left
stroke([(120, 110), (100, 135), (72, 160)], width=8)

# 3. 竖 - vertical drop from around midpoint of second pie, straight down
stroke([(112, 145), (110, 240)], width=9)

# ---------- RIGHT: 亍 ----------
# 4. Upper short 横 (slightly rising)
stroke([(165, 105), (225, 95)], width=7)

# 5. Middle longer 横
stroke([(150, 155), (270, 150)], width=8)

# 6. Long 竖钩 - vertical then small hook flick up-left
stroke([(215, 130), (215, 250)], width=9)
# hook flick: from (215,250) up-and-left
stroke([(215, 250), (200, 240)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0237_行/01_行.png")
