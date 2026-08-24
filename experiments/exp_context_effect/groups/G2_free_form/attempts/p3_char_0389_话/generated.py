"""Render 话 (speak) — 讠 (speech radical, left) + 舌 (tongue, right).

Revision 2 fixes:
- 口 was too large; shrink and raise it.
- 舌's top 丿 should attach to horizontal 一.
- 讠 tighter, second stroke shaped as z-like fold+rise.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=7):
    d.line(pts, fill="black", width=w, joint="curve")
    for (x, y) in (pts[0], pts[-1]):
        r = w / 2 - 0.5
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---------- LEFT: 讠 ----------
# 点 (dot at top-left, small tick going down-right)
stroke([(60, 75), (78, 100)], w=8)
# 横折提 — small horizontal, fold sharply down-left, then rise up-right
stroke([(55, 135), (95, 140), (55, 205), (105, 220)], w=7)

# ---------- RIGHT: 舌 ----------
# 丿 (flick from upper-right down-left, meeting the horizontal)
stroke([(215, 50), (175, 100)], w=8)
# 一 (long horizontal across top of 舌)
stroke([(135, 100), (275, 100)], w=8)
# 丨 (vertical descending through)
stroke([(200, 100), (200, 175)], w=8)
# 一 (mid horizontal — shorter, inside 十)
stroke([(155, 143), (255, 143)], w=7)
# 口 (small box at bottom — compact)
# 竖 (left vertical)
stroke([(160, 190), (160, 250)], w=7)
# 横折 (horizontal on top, fold down right side)
stroke([(160, 190), (250, 190), (250, 250)], w=7)
# 横 (bottom closing horizontal)
stroke([(160, 250), (250, 250)], w=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0389_话/01_话.png")
