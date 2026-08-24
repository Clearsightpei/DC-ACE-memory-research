# BANK_DEVIATION
# skipped: shi.py (十 turtle-based) and ju_char.py (具 inline recipe)
# reason: 真 = 十 + 目 + 一 + 八 stacked. shi.py is turtle-based and mixes badly
#         with inline PIL; ju_char's box is sized for standalone 具 and its box
#         needs to shrink to leave room for the top 十. Full inline is cleaner.
# fresh_component: zhen_char (top 十 + inline 目 box with 2 inner hengs + long
#                  base heng + splay feet, all PIL)
# 真 (zhēn) — Phase 3 character, 10 strokes.
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)

def line(p1, p2, w=6):
    d.line([p1, p2], fill=BLACK, width=w)

# --- Top 十 (2 strokes) ---
# Small cross above the box; shu extends closer to the box top
# Stroke 1: 横 (short top horizontal)
line((113, 40), (188, 40), w=6)
# Stroke 2: 竖 (vertical of 十, extends through the heng down toward box)
line((150, 15), (150, 75), w=6)

# --- Middle box with 3 inner hengs (5 strokes) ---
# Box occupies roughly x=[92, 208], y=[80, 205]
LEFT_X = 92
RIGHT_X = 208
TOP_Y = 80
INNER_Y1 = 111
INNER_Y2 = 142
INNER_Y3 = 173
BOT_Y = 205

# Stroke 3: 竖 (left vertical of box)
line((LEFT_X, TOP_Y), (LEFT_X, BOT_Y), w=6)
# Stroke 4: 横折 (top heng + right vertical)
line((LEFT_X, TOP_Y), (RIGHT_X, TOP_Y), w=6)
line((RIGHT_X, TOP_Y), (RIGHT_X, BOT_Y), w=6)
# Stroke 5: inner heng 1
line((LEFT_X + 6, INNER_Y1), (RIGHT_X - 6, INNER_Y1), w=5)
# Stroke 6: inner heng 2
line((LEFT_X + 6, INNER_Y2), (RIGHT_X - 6, INNER_Y2), w=5)
# Stroke 7: inner heng 3 / bottom of box interior
line((LEFT_X + 6, INNER_Y3), (RIGHT_X - 6, INNER_Y3), w=5)
# Stroke 8 (part of box): bottom heng closes the box
line((LEFT_X, BOT_Y), (RIGHT_X, BOT_Y), w=6)

# --- Bottom 一 (base heng, 1 stroke) ---
# Long baseline 横 wider than the box
BASE_Y = 240
line((38, BASE_Y), (262, BASE_Y), w=6)

# --- 八 feet (2 strokes) ---
# 撇 (left foot slanting down-left)
line((118, BASE_Y + 3), (82, 285), w=6)
# 点 (right foot slanting down-right)
line((182, BASE_Y + 3), (218, 285), w=6)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0517_真/01_真.png"
img.save(out_path)
print(f"Wrote {out_path}")
