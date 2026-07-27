"""
Render 曰 (radical 129, 4画) at 300x300.

Structure:
- 曰 is a wide-flat box with one internal horizontal (middle divider).
- Similar to 日 but wider (more horizontal aspect) and slightly shorter.
- 4 strokes:
    1. 竖 (left wall): top-left down to bottom-left
    2. 横折 (top + right wall): starts top-left, goes right across top,
       shoulder dab, descends right wall to bottom-right
    3. 横 (middle): inside horizontal, touches both walls
    4. 横 (bottom close): closes the bottom of the box
- Silhouette: wide square-ish box, centered.
- Aspect ratio: slightly wider than tall (~1.1:1) — the classic 曰
  differs from 日 (nearly square, taller) by being flatter/wider.

Match to GT: GT shows a hand-drawn-ish wide box with visible slight
gaps/roughness at corners, but topologically a closed rectangle with
one middle divider.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Box coordinates — wide-flat family, centered
LEFT  = 70
RIGHT = 235
TOP   = 70
BOT   = 230
MID_Y = TOP + (BOT - TOP) * 4 // 10  # slightly ABOVE center — 曰 signature

STROKE_W = 8

def line(p0, p1, w=STROKE_W):
    draw.line([p0, p1], fill="black", width=w)

def dab(p, r=5):
    draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

# --- Stroke 1: 竖 (left wall) ---
line((LEFT, TOP), (LEFT, BOT))
dab((LEFT, TOP), r=5)  # 顿 dab at start
dab((LEFT, BOT), r=4)

# --- Stroke 2: 横折 (top + right wall) ---
# Top horizontal
line((LEFT, TOP), (RIGHT, TOP))
dab((LEFT, TOP), r=5)
# Shoulder dab at top-right corner
dab((RIGHT, TOP), r=6)
# Right wall going down
line((RIGHT, TOP), (RIGHT, BOT))
dab((RIGHT, BOT), r=4)

# --- Stroke 3: middle 横 (internal divider) ---
# Touches both walls (曰/日 signature: it spans wall-to-wall)
line((LEFT + 3, MID_Y), (RIGHT - 3, MID_Y), w=7)
dab((LEFT + 3, MID_Y), r=4)

# --- Stroke 4: bottom 横 (closing) ---
line((LEFT, BOT), (RIGHT, BOT))
dab((LEFT, BOT), r=5)
dab((RIGHT, BOT), r=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_129_曰/01_曰.png")
print("saved 01_曰.png")
