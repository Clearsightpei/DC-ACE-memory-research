"""Render 刁 (p3_char_0034) at 300x300, white bg, black ink.

刁 = 2 strokes:
  1) 横折钩 (heng-zhe-gou): short horizontal top-left → sharp fold →
     long curved descent down-right ending in a small hook flick
     up-and-left at the bottom.
  2) 提 (ti): a short rising stroke inside the character, starting
     lower-left and rising to upper-right, meeting/near the descending
     stroke around its middle.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(draw, pts, width=8):
    """Draw a polyline with rounded caps by connecting with thick lines
    and dabbing round caps at every vertex."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    r = width // 2
    for x, y in pts:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# ---------------- Stroke 1: 横折钩 ----------------
# Cursive slanted form (per GT): top plate slopes gently DOWN-RIGHT
# to a peak near (220, 90); then a long, right-leaning curved descent
# to about (200, 265); then a small hook flick up-and-left.
top = [(85, 105), (130, 100), (175, 95), (215, 92), (225, 92)]
brush_line(d, top, width=8)

# Descent leans right: starts (225, 92), bulges out to (232, 160),
# curves back down to (200, 265). Long — reaches near baseline.
descent = [
    (225, 92),
    (230, 130),
    (232, 165),
    (228, 200),
    (218, 235),
    (205, 265),
]
brush_line(d, descent, width=8)

# Hook flick: bottom curls up-and-left, slightly longer than before.
hook = [(205, 265), (188, 268), (172, 262)]
brush_line(d, hook, width=8)

# ---------------- Stroke 2: 提 (rising stroke inside) ----------------
# Short rising stroke from lower-left up to meet/near the descent
# around its mid-height. Per GT it starts ~(70, 180) and rises to
# ~(200, 145), landing pointed just inside the descent curve.
ti = [(70, 182), (110, 170), (150, 158), (195, 148)]
brush_line(d, ti, width=8)

# ------------------------------------------------
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0034_刁/01_刁.png"
img.save(out)
print(f"wrote {out}")
