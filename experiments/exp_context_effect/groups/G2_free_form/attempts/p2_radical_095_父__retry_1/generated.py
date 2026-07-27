"""
父 (4 画) — Phase-2 radical. RETRY #1.

Prior failure diagnosis (errata):
  "top two dots splay OUTWARD (LEFT flicks down-LEFT, RIGHT flicks
   down-RIGHT — mirror pair). Body 撇 + 捺 cross at center-middle
   forming an X."

Prior attempt error: the top-right stroke curved inward (down-left)
like a 撇/横撇 rather than flicking OUT (down-right). Also top-left
stroke could be a bit more assertive as a short 撇.

Fix applied:
  - Top-left stroke: short 撇 flicking DOWN-LEFT from ~(130, 65) → (85, 115).
  - Top-right stroke: short 点 flicking DOWN-RIGHT from ~(180, 65) →
    (215, 115). MIRROR pair, both slanting AWAY from center.
  - Long 撇: from upper-right (200, 115) → lower-left (55, 260).
  - Long 捺: from upper-left (105, 130) → lower-right (255, 255).
  - The 撇/捺 cross near canvas middle (~150, 190).

Renderer: PIL brush-dabs, 300×300, black on white.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(P0, P1, P2, r_start, r_end, steps=400, ease=1.0):
    """Quadratic Bezier, brush-dab stack with linear (or eased) taper."""
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ----- Stroke 1: top-left 撇 (short, flicks DOWN-LEFT) --------------
# Small throw-away from ~(130, 65) sweeping down-and-left to (85, 115).
# 顿 (thick) at start (upper-right end), thin tail at lower-left end.
bezier_stroke(
    P0=(130, 65),
    P1=(115, 88),
    P2=(82, 118),
    r_start=6.5,
    r_end=1.5,
    ease=1.2,
)
dab(130, 65, 7.5)  # 顿 dab at start

# ----- Stroke 2: top-right 点 (short, flicks DOWN-RIGHT) ------------
# Mirror of stroke 1. From ~(180, 65) sweeping DOWN-AND-RIGHT to (218, 118).
# 顿 (thick) at start (upper-left end), thin tail at lower-right end.
# This is the CRITICAL fix vs prior attempt (which curved inward).
bezier_stroke(
    P0=(180, 65),
    P1=(195, 88),
    P2=(220, 120),
    r_start=6.5,
    r_end=1.5,
    ease=1.2,
)
dab(180, 65, 7.5)  # 顿 dab at start

# ----- Stroke 3: long 撇 (body, upper-right → lower-left) -----------
# From ~(205, 118) sweeping down through center to lower-left (55, 260).
# Gentle rightward bow (control point pulled toward interior).
bezier_stroke(
    P0=(205, 118),
    P1=(165, 175),
    P2=(55, 260),
    r_start=9.0,
    r_end=1.5,
    ease=1.15,
)
dab(205, 118, 10.0)  # 顿 dab at start

# ----- Stroke 4: long 捺 (body, upper-left → lower-right) -----------
# From ~(105, 130) sweeping down through center to lower-right (255, 258).
# Thin→thick, broad terminal foot. Crosses stroke 3 near (150, 190).
bezier_stroke(
    P0=(105, 130),
    P1=(155, 195),
    P2=(245, 252),
    r_start=2.0,
    r_end=9.5,
    ease=1.4,
)
# broad terminal foot
dab(245, 252, 10.5)
dab(252, 255, 9.5)
dab(258, 256, 7.5)
dab(263, 256, 5.0)

out_path = os.path.join(os.path.dirname(__file__), "01_父.png")
img.save(out_path)
print(f"wrote {out_path}")
