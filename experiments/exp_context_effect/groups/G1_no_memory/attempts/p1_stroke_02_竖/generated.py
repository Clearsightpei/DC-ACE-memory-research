"""
G1 no-memory attempt: p1_stroke_02_竖
Draws 竖 (vertical stroke, top-to-bottom) using PIL.
300x300, white background, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Vertical stroke: 竖 goes top-to-bottom, centered horizontally.
# Slight taper: start slightly narrower (顿笔 at top), body full width,
# taper gently at the bottom (悬针-ish look kept modest for a canonical 竖).
cx = W // 2
top_y = 40
bot_y = 260

# Draw the main body as a filled rectangle with rounded ends.
half_w_top = 8
half_w_mid = 9
half_w_bot = 4  # taper for a subtle 悬针

# Approximate a tapered stroke by drawing a polygon.
polygon = [
    (cx - half_w_top, top_y),
    (cx + half_w_top, top_y),
    (cx + half_w_mid, (top_y + bot_y) // 2),
    (cx + half_w_bot, bot_y),
    (cx - half_w_bot, bot_y),
    (cx - half_w_mid, (top_y + bot_y) // 2),
]
draw.polygon(polygon, fill="black")

# 顿笔 (small emphasis) at the top: a small filled ellipse.
draw.ellipse(
    [cx - half_w_top - 1, top_y - 3, cx + half_w_top + 1, top_y + 6],
    fill="black",
)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p1_stroke_02_竖/01_竖.png"
img.save(out)
print(f"Saved: {out} size={img.size}")
