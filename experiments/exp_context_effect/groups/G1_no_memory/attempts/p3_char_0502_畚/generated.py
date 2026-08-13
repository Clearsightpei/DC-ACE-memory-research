"""Render 畚 (běn) — G1 no-memory attempt.

Structure: 厶 (top) + 大-like radical with long horizontal (middle) + 田 (bottom).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 3  # stroke thickness


def line(a, b, w=T):
    d.line([a, b], fill=INK, width=w)


# ---- Top: 厶 (small folded shape near top-center) ----
# Left-falling piě
line((155, 30), (135, 60))
# Small folded diagonal (like a hook right-then-down)
line((138, 55), (165, 75))
line((165, 75), (150, 90))

# ---- Middle: 大-like with long horizontal ----
# Long horizontal stroke (broad, spans most of width)
line((55, 110), (255, 105), w=T)
# Left-falling diagonal (piě) from just above horizontal, sweeping down-left
line((150, 90), (85, 175))
# Right-falling diagonal (nà) from center, sweeping down-right, long
line((150, 115), (265, 200))

# ---- Bottom: 田 (field box with cross) ----
# Box coordinates
bx1, by1, bx2, by2 = 110, 180, 210, 275
# Left vertical
line((bx1, by1), (bx1, by2))
# Top horizontal
line((bx1, by1), (bx2, by1))
# Right vertical
line((bx2, by1), (bx2, by2))
# Bottom horizontal
line((bx1, by2), (bx2, by2))
# Inner vertical
line(((bx1 + bx2) // 2, by1), ((bx1 + bx2) // 2, by2))
# Inner horizontal
line((bx1, (by1 + by2) // 2), (bx2, (by1 + by2) // 2))

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0502_畚/01_畚.png"
img.save(out)
print(f"saved {out}")
