# p1_stroke_14_竖钩 — vertical stroke ending in a small upward-left hook.
# G3 coord-bank format: pure numeric coords, no anchors/joints.
# 300x300, white bg, black ink.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Vertical shaft: from top-center-ish down to near-bottom.
# Coord choices (numbers only):
shaft_x = 165          # slightly right of center — 竖钩's shaft typically sits right of the grid center
shaft_top_y = 55
shaft_bot_y = 235
shaft_width = 12

# Draw the vertical shaft as a filled rectangle with slight taper (calligraphic feel):
# Top a hair thinner, bottom a hair thicker where the hook launches.
top_half = 9
bot_half = 7  # narrower near hook root before the tick
d.polygon(
    [
        (shaft_x - top_half, shaft_top_y),
        (shaft_x + top_half, shaft_top_y),
        (shaft_x + bot_half, shaft_bot_y),
        (shaft_x - bot_half, shaft_bot_y),
    ],
    fill="black",
)

# Round the top (顿笔 head) with a small filled ellipse.
d.ellipse(
    [shaft_x - top_half - 2, shaft_top_y - 6, shaft_x + top_half + 2, shaft_top_y + 8],
    fill="black",
)

# The hook (钩) — flick up-and-left from the bottom of the shaft.
# Triangular hook: starts at bottom of shaft, extends left and slightly upward.
hook_root_x = shaft_x - bot_half
hook_root_y = shaft_bot_y
hook_tip_x = shaft_x - 40      # 40px to the left
hook_tip_y = shaft_bot_y - 30  # 30px up

# Base of hook (its thick root at the shaft's bottom)
hook_base_top = (shaft_x - bot_half, shaft_bot_y - 6)
hook_base_bot = (shaft_x + bot_half, shaft_bot_y)
hook_tip = (hook_tip_x, hook_tip_y)

d.polygon(
    [hook_base_top, hook_base_bot, hook_tip],
    fill="black",
)

# Smooth the outer corner where shaft meets hook with a small filled ellipse
d.ellipse(
    [shaft_x - bot_half - 3, shaft_bot_y - 8, shaft_x + bot_half + 3, shaft_bot_y + 4],
    fill="black",
)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_14_竖钩/01_竖钩.png"
img.save(out)
print("wrote", out)
