"""Render 在 (p3_char_0219) at 300x300, black ink on white.

Structure (6 strokes):
1. 一 top-short horizontal (upper-right area)
2. 丿 long slanted 撇 crossing the top-横 and diving down-left
3. 一 middle horizontal (crossbar of 土)
4. 丨 vertical of 土 (right side of char)
5. 一 bottom horizontal (base of 土)
   -> plus a small stub at right of the 一 for balance
Character composition: 大-like frame on top-left + 土 nested bottom-right.
Radical-position note: bottom 土 is compressed and shifted right.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
T = 6  # base stroke thickness


def stroke(pts, width=T):
    d.line(pts, fill=INK, width=width, joint="curve")
    # dab endpoints for round terminals
    for (x, y) in (pts[0], pts[-1]):
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# 1) Top short 横 — sits high, slightly right of center
stroke([(95, 78), (205, 72)], width=T)

# 2) Long 撇 — starts near right end of the top 横, sweeps down-left to bottom-left corner
# Slightly curved: use a few segments approximating a gentle bow
pian = [
    (172, 55),
    (155, 95),
    (130, 140),
    (100, 190),
    (70, 240),
    (48, 275),
]
stroke(pian, width=T)

# 3) Middle 横 — crossbar for 土, spans mid-right region, crosses the 撇
stroke([(105, 155), (245, 152)], width=T)

# 4) 丨 vertical of 土 — from just below middle-横 down to bottom
stroke([(168, 155), (168, 260)], width=T)

# 5) Bottom 横 — base of 土, slightly wider than the middle 横
stroke([(95, 258), (250, 258)], width=T)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0219_在/01_在.png")
print("wrote 01_在.png")
