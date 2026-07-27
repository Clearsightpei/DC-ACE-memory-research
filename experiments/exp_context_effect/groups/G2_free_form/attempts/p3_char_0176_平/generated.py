"""
Render 平 (píng) — 5 strokes.
Stroke order:
  1. 一 (short top horizontal)
  2. 丶 (left tick, sloping down-left)
  3. 丿 (right tick, sloping down-right — actually a small 撇)
  4. 一 (long middle horizontal, crossbar)
  5. 丨 (long vertical through center, descending down through crossbar)

Not in sibling checklist. Related-family reference: 干/千/于 — 平 has
a distinctive "two flicks flanking a short top horizontal" identity
above the long crossbar. The vertical is straight (no hook).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=10):
    """Draw a stroke as a polyline with rounded joints."""
    draw.line(pts, fill=BLACK, width=width, joint="curve")
    # cap the ends with small circles
    for (x, y) in (pts[0], pts[-1]):
        r = width // 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# 1. short top horizontal — sits just above center-top
stroke([(115, 70), (200, 65)], width=9)

# 2. left tick (丶) — short slope going down-left, below the top-horizontal
stroke([(115, 95), (95, 120)], width=9)

# 3. right tick (short 撇) — sloping down-right from top-right area
stroke([(195, 95), (220, 120)], width=9)

# 4. long middle horizontal (crossbar) — spans widely
stroke([(45, 160), (260, 155)], width=11)

# 5. long vertical through center, extending below the crossbar
stroke([(152, 90), (150, 275)], width=11)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0176_平/01_平.png"
)
print("saved")
