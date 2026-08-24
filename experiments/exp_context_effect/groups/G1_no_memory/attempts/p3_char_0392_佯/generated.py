"""Render 佯 (yang) — person radical + 羊."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(a, b, w=5):
    d.line([a, b], fill=BLACK, width=w)

# --- Left: 亻 (person radical) ---
# Piě (falling left stroke)
line((95, 75), (55, 200), w=6)
# Vertical stroke starts where piě begins descending
line((82, 120), (82, 250), w=5)

# --- Right: 羊 (sheep) ---
# Top two dots (⺷)
line((155, 70), (145, 95), w=5)   # left slanted dot
line((225, 70), (235, 95), w=5)   # right slanted dot

# Three horizontal strokes
line((145, 115), (240, 115), w=5)  # top horizontal
line((155, 155), (230, 155), w=5)  # middle horizontal
line((125, 205), (260, 205), w=6)  # bottom horizontal (longest)

# Central vertical, extends below bottom
line((193, 115), (193, 265), w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0392_佯/01_佯.png")
