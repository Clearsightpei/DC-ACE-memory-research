"""
甲 — 5 strokes:
  1. 竖 (left wall of box)
  2. 横折 (top + right wall)
  3. 横 (internal cross-bar, mid)
  4. 横 (bottom of box)
  5. 竖 (long central axis, extending WAY below the box — hanging drop)

Form catalog cues:
  - box top-right = 横折 with shoulder dab (form_catalog 149-153)
  - central hanging 竖 for 巾/中/甲: ~180 px long, extends ~100 px below base (115-120)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Box coords: top ~70, bottom ~180, left ~85, right ~215 (box ~130 wide, ~110 tall)
TOP, BOT, L, R = 70, 180, 85, 215
MID = (TOP + BOT) // 2  # ~125
CX = (L + R) // 2       # ~150

INK = "black"
W_STROKE = 6

def line(x1, y1, x2, y2, w=W_STROKE):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

def dab(cx, cy, r=4):
    d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=INK)

# Stroke 1: 竖 (left wall) — top-left to bottom-left
dab(L, TOP, 4)
line(L, TOP, L-2, BOT, w=W_STROKE)

# Stroke 2: 横折 — top 横 then shoulder then right 竖
#   top 横 from just-inside-left to right
line(L-2, TOP-1, R+2, TOP, w=W_STROKE)
#   small shoulder dab at top-right
dab(R+1, TOP+2, 5)
#   right wall down
line(R+2, TOP, R, BOT, w=W_STROKE)

# Stroke 3: 横 (mid cross-bar inside box) — spans wall to wall
line(L, MID, R, MID, w=W_STROKE)

# Stroke 4: 横 (bottom of box) — spans wall to wall, slight up-tilt
line(L-2, BOT, R+2, BOT-2, w=W_STROKE)

# Stroke 5: 竖 (long central hanging drop)
#   starts at TOP of box (touching top 横), extends WAY below bottom (~100 px below)
dab(CX, TOP-2, 4)
line(CX, TOP-2, CX, BOT + 95, w=W_STROKE+1)
# blunt terminal
dab(CX, BOT + 95, 4)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0157_甲/01_甲.png")
print("saved 01_甲.png")
