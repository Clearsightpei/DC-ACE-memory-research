"""
Render 龹 to a 300x300 PNG.

Structure observed from GT:
- Top: two symmetric short flicks (left-flick and right-flick) high up
- A short vertical/dot between them (small)
- A horizontal stroke crossing the middle
- Bottom: a long 撇 (down-left) and long 捺 (down-right) meeting
  slightly below the horizontal
Overall: silhouette like 关 with an added upper vertical dot.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=7):
    d.line(pts, fill=INK, width=width, joint="curve")
    # cap the ends
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# --- Top two symmetric flicks (like the top of 半 / 关) ---
# left flick: from mid-upper going down-left
stroke([(115, 55), (95, 95)], width=6)
# right flick: from mid-upper going down-right
stroke([(185, 55), (205, 95)], width=6)

# small vertical stub between the two flicks (top center)
stroke([(150, 60), (150, 85)], width=6)

# --- Middle horizontal (crosses whole middle) ---
stroke([(55, 135), (245, 135)], width=7)

# --- Bottom 撇 (long, from center-top going down-left) ---
# curved 撇
撇_pts = [
    (150, 130),
    (135, 165),
    (110, 205),
    (75, 245),
    (45, 275),
]
stroke(撇_pts, width=7)

# --- Bottom 捺 (long, from center-top going down-right) ---
捺_pts = [
    (150, 140),
    (175, 175),
    (205, 215),
    (240, 255),
    (265, 275),
]
stroke(捺_pts, width=8)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0284_龹/01_龹.png"
)
