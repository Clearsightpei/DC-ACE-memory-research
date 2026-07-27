"""
Draw 工 (gong) — 3 strokes:
  1) top 横 (shorter, upper horizontal)
  2) 竖 (vertical, centered, connects the two horizontals)
  3) bottom 横 (longer, lower horizontal — the base)

Silhouette: I-shape, wider at the bottom than the top.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(p1, p2, width=10):
    draw.line([p1, p2], fill=BLACK, width=width)
    # round the ends a bit
    r = width // 2
    for (x, y) in (p1, p2):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# Top 横 — upper horizontal, shorter, slightly rising to the right
top_y = 95
top_left = (90, top_y + 4)
top_right = (215, top_y - 2)
stroke(top_left, top_right, width=9)

# Bottom 横 — lower horizontal, longer, spans the base, slightly rising
bot_y = 220
bot_left = (55, bot_y + 3)
bot_right = (250, bot_y - 3)
stroke(bot_left, bot_right, width=10)

# Middle 竖 — vertical, centered, connects top 横 to bottom 横
mid_x = 152
stroke((mid_x, top_y + 2), (mid_x + 2, bot_y - 1), width=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0087_工/01_工.png")
print("saved")
