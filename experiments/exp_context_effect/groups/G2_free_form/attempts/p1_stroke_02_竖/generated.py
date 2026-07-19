"""
Render 竖 (shu) — vertical stroke, top-to-bottom — as a 300x300 PNG.

Free-form memory (G2). Memory file was empty; only prior item is 横
(horizontal), so I mirror its design principles rotated 90°:
- 300x300 canvas, white background, black ink.
- Vertical stroke centered horizontally, spanning ~64% of the height
  with equal top/bottom margins.
- 起笔 (small tick top-left, mimicking a light brush press-in from
  upper-left) and 收笔 (small tapered/pointed tail at the bottom —
  the "垂露" style ending, a rounded drop; "悬针" would be sharp,
  but 垂露 reads more unambiguously as a canonical 竖 stroke).
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Main vertical bar
# Top ~15% margin, bottom ~15% margin, horizontal center.
top_y = 45
bot_y = 255
mid_x = 150
thickness = 14  # bar thickness

# Draw the main bar as a filled rectangle.
draw.rectangle(
    [mid_x - thickness // 2, top_y, mid_x + thickness // 2, bot_y],
    fill="black",
)

# 起笔 (qibi) — small blob top with slight left-lean, simulating the
# brush landing and pressing before descending.
draw.ellipse(
    [mid_x - thickness // 2 - 4, top_y - 6,
     mid_x + thickness // 2 + 2, top_y + 8],
    fill="black",
)

# 收笔 (shoubi) — 垂露 (hanging-dew) rounded ending: a small round
# bulge at the bottom. (悬针 would be a needle point — omitted here
# to keep the canonical vertical read.)
draw.ellipse(
    [mid_x - thickness // 2 - 2, bot_y - 4,
     mid_x + thickness // 2 + 2, bot_y + 8],
    fill="black",
)

out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_02_竖/01_竖.png"
)
img.save(out_path)
print(f"Wrote {out_path} size={img.size}")
