"""
Render 丢 (diu, "lose") — 6 strokes.

# SIGNATURE CHECK (千 top component, from sibling_signature_checklist):
#   千: 撇-LID top + straight through-竖 (no hook)
# Distinct from 干 (whose top 一 is shorter, ~65%) and 于 (two 一 + hooked 亅).
# For 丢, the "千"-like top actually has TWO horizontals (upper short, lower
# long), a straight vertical through both, and a 撇-lid on top.
# Bottom is 厶 (a small 撇折 + a 点).

Layout (300x300 canvas):
  1. 丿  short slanted pie, top center-left, aimed lower-left
  2. 一  upper short horizontal (through the pie's midpoint area)
  3. 一  lower long horizontal
  4. 丨  vertical through both horizontals (NO hook)
  5. 厶: 撇折  starts mid-lower, drops left then bends right
  6. 厶: 点   short slanted dot on the right side of 厶
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=7):
    """Draw a polyline with rounded ends and joints (brush-dab style)."""
    d.line(pts, fill=BLACK, width=width, joint="curve")
    r = width // 2
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- 1. 丿  top pie (LONGER + more slant, per GT)
stroke([(170, 45), (120, 100)], width=6)

# --- 2. 一  upper short horizontal
stroke([(100, 115), (205, 108)], width=6)

# --- 3. 一  lower long horizontal (widest stroke, sets the width)
stroke([(55, 180), (250, 175)], width=7)

# --- 4. 丨  straight vertical through both horizontals (no hook)
stroke([(152, 100), (150, 195)], width=6)

# --- 5. 厶 撇折: starts high-mid, drops steep down-left, bends horizontal-right
stroke([(150, 200), (115, 250), (170, 258)], width=6)

# --- 6. 厶 点: short slanted dot closing the 厶 on the right side
stroke([(175, 232), (205, 268)], width=6)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0220_丢/01_丢.png"
)
