"""
土 (tu) — 3-stroke radical.
Structure per memory principle 6:
  - top 横: SHORTER (~110 px)
  - vertical 竖: pass-through, top → bottom, no hook (blunt)
  - bottom 横: LONGER (~200 px), the visual foundation
Rendered PIL brush-dabs, 300x300 white, black ink.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_line(x0, y0, x1, y1, r_start, r_end, steps=400,
                start_press=True, end_press=True):
    # subtle end-press (r+1) — avoid ball-like balloons on standalone
    if start_press:
        dab(x0, y0, r_start + 1)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)
    if end_press:
        dab(x1, y1, r_end + 1)


# ---- Stroke 1: top 横 (SHORTER) ----
# canvas center ~150; top 横 centered around x=150, y=118, length ~110
top_x0, top_x1, top_y = 95, 205, 118
stroke_line(top_x0, top_y, top_x1, top_y - 3,  # tiny 3-5 deg up-tilt
            r_start=5, r_end=5, steps=250)

# ---- Stroke 2: 竖 (pass-through, blunt both ends) ----
# vertical centered on x=150, from just above top 横 to just above bottom 横
v_x = 150
v_y0, v_y1 = 78, 218
stroke_line(v_x, v_y0, v_x, v_y1,
            r_start=5, r_end=5, steps=250)

# ---- Stroke 3: bottom 横 (LONGER — the foundation) ----
bot_x0, bot_x1, bot_y = 45, 255, 235
stroke_line(bot_x0, bot_y, bot_x1, bot_y - 2,
            r_start=5.5, r_end=5.5, steps=300)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_072_土/01_土.png")
