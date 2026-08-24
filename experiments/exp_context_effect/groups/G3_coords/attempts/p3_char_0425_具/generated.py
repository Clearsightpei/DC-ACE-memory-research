# BANK_DEVIATION
# skipped: ri.py (日 box) and ba.py (八 feet)
# reason: 具's top box needs 3 internal hengs (ri.py only has 1) and its feet sit
#         below a broad base heng and are much shorter/thinner than a standalone 八
#         — neither primitive slots without extreme transformation.
# fresh_component: ju_char (inline box with 3 inner hengs + long base + short splay feet)
# 具 (jù) — Phase 3 character, 8 strokes.
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p1, p2, w=6):
    d.line([p1, p2], fill=BLACK, width=w)

# --- Top box (目 shape) ---
# Box occupies roughly x=[90, 210], y=[45, 195]
LEFT_X = 92
RIGHT_X = 208
TOP_Y = 50
INNER_Y1 = 88
INNER_Y2 = 126
INNER_Y3 = 164
BOT_Y = 200

# Stroke 1: 竖 (left vertical)
line((LEFT_X, TOP_Y), (LEFT_X, BOT_Y), w=6)

# Stroke 2: 横折 (top heng + right vertical, one stroke)
line((LEFT_X, TOP_Y), (RIGHT_X, TOP_Y), w=6)
line((RIGHT_X, TOP_Y), (RIGHT_X, BOT_Y), w=6)

# Stroke 3: inner heng 1
line((LEFT_X + 8, INNER_Y1), (RIGHT_X - 8, INNER_Y1), w=5)

# Stroke 4: inner heng 2
line((LEFT_X + 8, INNER_Y2), (RIGHT_X - 8, INNER_Y2), w=5)

# Stroke 5: inner heng 3
line((LEFT_X + 8, INNER_Y3), (RIGHT_X - 8, INNER_Y3), w=5)

# Stroke 6: bottom heng of box (closes box)
line((LEFT_X, BOT_Y), (RIGHT_X, BOT_Y), w=6)

# Stroke 6: long baseline 横 (spans wider than the box)
BASE_Y = 235
line((45, BASE_Y), (255, BASE_Y), w=6)

# Stroke 7: 撇 (left foot) — from around baseline center-left, slanting down-left
line((115, BASE_Y + 3), (85, 285), w=6)

# Stroke 8: 点 (right foot) — from around baseline center-right, slanting down-right
line((185, BASE_Y + 3), (215, 285), w=6)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0425_具/01_具.png"
img.save(out_path)
print(f"Wrote {out_path}")
