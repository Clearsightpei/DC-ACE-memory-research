"""Radical 氏 (4 strokes) — PIL brush-dab rendering, 300x300 white.

Revision 1 — cleaner top hood, straighter 竖提, dominant 斜钩.

Stroke order:
  1. 撇 — short throw-away starting at top of the 横, down-and-left.
  2. 横 — short horizontal to the RIGHT of the 撇's start; the two
     meet at a shared top-left vertex (like a hood).
  3. 竖提 — 竖 drops from the RIGHT end of the 横 (with a subtle
     inward lean), then a SHORT 提 rises up-and-right.
  4. 斜钩 — long sweeping diagonal from the top hood down to
     lower-right, hook flicks up-left. Dominates the character.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        L = math.hypot(x1 - x0, y1 - y0)
        steps = max(30, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=220, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# Shared top-left vertex where the 撇 starts and the 横 also begins.
V_x, V_y = 100, 90   # top-left corner of the "hood"

# ---------------------------------------------------------------------------
# Stroke 1: 撇 — from the vertex (V_x, V_y) sweeping down-and-left.
# In 氏 the 撇 is short and steep, ending near (65, 145).
# ---------------------------------------------------------------------------
dab(V_x, V_y, 7)  # 顿笔 at shared vertex
bezier_taper((V_x, V_y), (92, 115), (62, 148),
             r0=6.5, r1=1.4, steps=180, ease=1.2)

# ---------------------------------------------------------------------------
# Stroke 2: 横 — starts at the vertex and runs rightward to about x=195.
# Slight up-tilt. Small terminal press seats the 竖提's start.
# ---------------------------------------------------------------------------
line_taper(V_x, V_y + 2, 200, 85, r0=5, r1=5)
dab(200, 85, 7)  # right-end shoulder — the 竖提 hangs from here

# ---------------------------------------------------------------------------
# Stroke 3: 竖提 — 竖 drops from (200, 85) area down to about (135, 205),
# a subtle inward (left) lean. Then a SHORT 提 rises up-and-right.
# ---------------------------------------------------------------------------
# 竖 with slight left-lean (Bezier so it curves gently, not straight):
bezier_taper((200, 90), (175, 145), (135, 205),
             r0=6, r1=5.5, steps=200, ease=1.0)
# joining dab at bottom
dab(135, 205, 7.5)
# 提 rising up-and-right — SHORT, thick→thin
line_taper(135, 205, 190, 178, r0=6, r1=1.2)

# ---------------------------------------------------------------------------
# Stroke 4: 斜钩 — long dominant diagonal. Starts high near the top
# hood area (around (155, 95)) and sweeps down-and-right to (265, 245).
# Belly on lower-left (Bezier ctrl pulled to lower-left of chord).
# Hook flicks up-left ~-115°, length ~45 px.
# ---------------------------------------------------------------------------
tip = (265, 245)
start = (155, 95)
ctrl = (185, 225)  # belly-on-lower-left
bezier_taper(start, ctrl, tip, r0=8, r1=2.8, steps=280, ease=1.0)

# Hook flick
hx0, hy0 = tip
ang = math.radians(-115)
hL = 46
hx1 = hx0 + hL * math.cos(ang)
hy1 = hy0 + hL * math.sin(ang)
dab(hx0, hy0, 4)
line_taper(hx0, hy0, hx1, hy1, r0=3.8, r1=1.1)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_115_氏/01_氏.png"
)
print("wrote 01_氏.png (revision 1)")
