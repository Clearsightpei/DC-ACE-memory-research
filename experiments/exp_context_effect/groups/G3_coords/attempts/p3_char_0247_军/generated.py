"""Render 军 (jun, "army") — 冖 top + 车 body.

Decomposition (from GT):
  - 冖: small 点 at top-left; long 横钩 covering from left to right, ends with
        a small downward hook.
  - 车: short 一 near top; 日/曰 rectangle (two verticals + inner heng);
        a middle 横 running wide across the whole char;
        a vertical shaft 丨 running from top down through everything;
        a bottom 一 (long, wide) below.
Approach: fresh PIL render, thin uniform lines to match MMH GT aesthetics.
"""
from PIL import Image, ImageDraw

SIZE = 300
W = 3  # thin uniform line to match GT

img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)


def line(x1, y1, x2, y2, w=W):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)


def dot(x, y, r=3):
    d.ellipse([(x - r, y - r), (x + r, y + r)], fill="black")


# --- 冖 top cover ------------------------------------------------------------
# Small 点 (dian) at top-left of the cover
line(78, 60, 90, 75)  # short slanted dot stroke
# 横钩: long horizontal from ~95 to 220, then hook down
line(90, 78, 225, 82)
line(225, 82, 220, 100)  # hook drop

# --- 车 body ----------------------------------------------------------------
# Short top 一 inside cover
line(115, 108, 200, 108)

# Rectangle (曰): left vertical, right vertical, inner horizontal, bottom
line(120, 108, 118, 175)   # left vertical
line(200, 108, 205, 175)   # right vertical (slight splay)
line(118, 142, 205, 142)   # middle horizontal (inner)
line(118, 175, 205, 175)   # bottom of曰

# Wide middle 横 that extends beyond the rectangle (crossbar of 车)
line(75, 195, 240, 198)

# Vertical shaft 丨 — starts just under the 冖 cover, drops through everything
line(158, 92, 158, 268)

# (Optional) small bottom heng at very bottom -- 车 in 军 usually ends with
# the shaft dropping past the wide heng; keep the shaft as the terminus.

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0247_军/01_军.png")
print("wrote 01_军.png")
