"""
Render 横 (heng) — horizontal stroke, left-to-right — as a 300x300 PNG.

Free-form memory (G2) first item. No prior memory, no GT PNG.

Design choices:
- 300x300 canvas, white background, black ink.
- Horizontal stroke centered vertically, spanning ~64% of the width
  with equal left/right margins.
- Slight thickness taper: standard calligraphic 横 has a subtle
  起笔 (small down-tick on the left) and 收笔 (small triangular
  press on the right). Rendered as a thick horizontal bar with tiny
  end embellishments so the shape reads unambiguously as 横.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

# Main horizontal bar
# Left ~15% margin, right ~15% margin, vertical center.
left_x = 45
right_x = 255
mid_y = 150
thickness = 14  # bar thickness

# Draw the main bar as a filled rectangle with rounded look via
# multiple overlapping strokes.
draw.rectangle(
    [left_x, mid_y - thickness // 2, right_x, mid_y + thickness // 2],
    fill="black",
)

# 起笔 (qibi) — small subtle blob at the left end (slight downward tick)
draw.ellipse(
    [left_x - 6, mid_y - thickness // 2 - 2,
     left_x + 8, mid_y + thickness // 2 + 4],
    fill="black",
)

# 收笔 (shoubi) — small triangular press at right end
# A small triangle jutting slightly down-right of the terminus.
draw.polygon(
    [
        (right_x - 4, mid_y - thickness // 2),
        (right_x + 10, mid_y + thickness // 2 + 2),
        (right_x - 4, mid_y + thickness // 2 + 4),
    ],
    fill="black",
)

out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_01_横/01_横.png"
)
img.save(out_path)
print(f"Wrote {out_path} size={img.size}")
