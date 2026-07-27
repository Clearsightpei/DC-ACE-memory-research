"""
p3_char_0032_凵 — the 3-sided box open at TOP (kǎn).

Structure (from GT):
  Two strokes.
  Stroke 1: 竖折 — left 竖 drops from mid-upper-left down to bottom-left,
            then folds RIGHT along the bottom to about the right wall.
  Stroke 2: right 竖 — drops from top down PAST the bottom horizontal
            (extends slightly below the base line, visible small tail).

Aspect-ratio family: off-center 匚 — 3-sided box, 1 side open (top).
Bottom-heavy per radical_position_rules.md. Verticals are TALL
(~150 px) — the empty space is above the glyph, not below.

Revision 1 notes vs first pass:
- verticals were too short (~100 px); GT verticals span y=115→270.
- right 竖 extends BELOW the bottom horizontal in GT (small overshoot).
- top of each vertical shows a small inward curl (顿 press) — render
  as a slightly inward-tilting head-dab.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLACK)


def taper_line(x1, y1, x2, y2, w1, w2, steps=80):
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        w = w1 + (w2 - w1) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# ---------- Stroke 1: 竖折 (left vertical + bottom horizontal) ----------
# Left 竖: taller — starts (73, 118) with a small inward-right curl at
# the top (the GT's 顿-then-slight-drift-right head), drops to corner
# (72, 268). The head-curl is a mini leftward dab shift.
dab(78, 118, 6)   # very top mini press (inward curl start)
taper_line(78, 118, 72, 135, w1=8, w2=9, steps=25)  # brief curl inward
# main vertical body
taper_line(72, 135, 72, 268, w1=9, w2=9, steps=140)
# Corner (顿 press at bottom-left)
dab(72, 268, 9)
# Bottom horizontal, runs right to ~x=228, tiny up-tilt
taper_line(72, 268, 228, 262, w1=9, w2=8, steps=120)
dab(228, 262, 6)  # blunt terminal on bottom (this is where stroke 1 ends)

# ---------- Stroke 2: right 竖 ----------
# Starts higher, has a small inward curl at top like left vertical.
# Extends BELOW the bottom horizontal — small overshoot tail visible
# in GT (right vertical passes through the base and sticks out ~10 px).
dab(230, 120, 6)   # top mini press
taper_line(230, 120, 235, 138, w1=8, w2=9, steps=25)  # brief curl
# main body — drops all the way past the base
taper_line(235, 138, 232, 278, w1=9, w2=9, steps=150)
dab(232, 278, 6)  # blunt terminal (below the bottom horizontal)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0032_凵/01_凵.png"
)
print("wrote 01_凵.png")
