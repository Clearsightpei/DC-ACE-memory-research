"""
彐 (yi) — 3-stroke radical (comb/broom hand)

Structure from GT:
  1. Top 横折 (heng-zhe): horizontal top-left → top-right, then squared
     shoulder press, then vertical down to bottom-right area. Blunt end
     (no hook, this is 横折 not 横折钩).
  2. Middle 横: short horizontal, roughly midway between top and bottom,
     starts at same left x as top 横, ends BEFORE the right vertical
     (does not touch it).
  3. Bottom 横: long horizontal, starts at same left x, ends AT the
     right vertical (closes the shape).

Renderer: PIL brush-dabs (per drawer_memory.md general technique).
Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(p0, p1, r_start, r_end, steps=400):
    """Straight tapered stroke, endpoint-inclusive brush-dabs."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(p, r):
    x, y = p
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Layout in image coords (y grows DOWN) -----------------------------
# Looking at GT: the radical sits centered-ish, occupies roughly x=60..230,
# y=80..235. Top 横 has a very slight upward tilt (left low, right high?
# actually looking again: left slightly higher, right slightly lower — a
# tiny down-tilt is normal for the top of 彐/日/目-family). We'll keep
# it near-horizontal with a small down-tilt (~3px).

LEFT_X   = 60
RIGHT_X  = 225

TOP_Y    = 88
MID_Y    = 155
BOT_Y    = 228

R_MAIN   = 4.5   # main stroke radius (uniform-ish 横/竖 lines)
R_JOINT  = 6.5   # slightly larger 顿 press at the shoulder / endpoints

# ---- Stroke 1: 横折 (top horizontal + right vertical) -----------------
# 顿-dab at left start
dab((LEFT_X, TOP_Y + 4), R_JOINT - 0.5)
# Top 横: left→right, uniform, ramp up slightly toward the corner.
# Slight UP-tilt (right end higher) — 3–5° per drawer_memory.md.
stroke((LEFT_X, TOP_Y + 4), (RIGHT_X, TOP_Y - 2),
       r_start=R_MAIN, r_end=R_MAIN + 1.0, steps=400)
# 顿-press dab at the shoulder (corner)
CORNER = (RIGHT_X, TOP_Y - 2)
dab(CORNER, R_JOINT)
# Vertical down: right side, from corner down to bottom-right area.
# Ends BLUNTLY (no hook), and its endpoint is where the bottom 横 will
# meet it — so both strokes share the same corner pixel.
V_BOT = (RIGHT_X - 2, BOT_Y)   # tiny lean-in for calligraphic feel
stroke(CORNER, V_BOT,
       r_start=R_JOINT, r_end=R_MAIN + 0.5, steps=400)
# Blunt terminal press at the bottom of the vertical
dab(V_BOT, R_JOINT - 0.5)

# ---- Stroke 2: middle 横 (short, does NOT touch right vertical) ------
MID_LEFT  = (LEFT_X + 4, MID_Y)
MID_RIGHT = (RIGHT_X - 40, MID_Y + 1)   # stops short of the vertical
dab(MID_LEFT, R_JOINT - 1)
stroke(MID_LEFT, MID_RIGHT,
       r_start=R_MAIN, r_end=R_MAIN, steps=300)
dab(MID_RIGHT, R_MAIN + 0.5)   # small end press, tapered feel

# ---- Stroke 3: bottom 横 (long, meets the right vertical) ------------
BOT_LEFT  = (LEFT_X - 2, BOT_Y)          # extends slightly left for weight
BOT_RIGHT = (RIGHT_X - 2, BOT_Y)         # meets the vertical's endpoint
dab(BOT_LEFT, R_JOINT)
stroke(BOT_LEFT, BOT_RIGHT,
       r_start=R_MAIN + 0.5, r_end=R_MAIN + 0.5, steps=400)
dab(BOT_RIGHT, R_JOINT)   # shared corner press with vertical's end

# ---- Save -----------------------------------------------------------
import os
out_path = os.path.join(os.path.dirname(__file__), "01_彐.png")
img.save(out_path)
print(f"wrote {out_path}")
