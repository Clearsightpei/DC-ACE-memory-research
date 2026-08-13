# p3_char_0321_把 — 把 (bǎ, "grasp"), 7 strokes.
# Left: 扌 (shou_pang, 3 strokes) — bank primitive.
# Right: 巴 (bā, 4 strokes) — inline PIL, MMH-thin widths (P12).
# Math-coord composition (center origin, +y up).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shou_pang import draw_shou_pang  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
t = ImageDraw.Draw(img)


def to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


# ---- LEFT: 扌 ----
# scale 0.75, shifted well left, slight downward bias to align with 巴 body
draw_shou_pang(t, ox=-80, oy=5, scale=0.75)


# ---- RIGHT: 巴 (4 strokes, inline) ----
# Positioned right of center. Top box narrow; bottom envelope sweeps
# out wider (per GT). Widths ~7 px.
import math
W = 7

# Left vertical anchor for the top box (narrower than bottom).
LX = 5      # left vertical shu (spans whole char)
TX = 55     # top-right of small top box
TY = 65     # top edge y
MY = 10     # middle interior heng y
BX = 80     # bottom-right of bottom envelope (wider than TX)
BY = -70    # bottom of envelope

# Stroke 1 — 横折 (top edge + right-side of top box)
t.line([to_px(LX, TY), to_px(TX, TY)], fill="black", width=W)
t.line([to_px(TX, TY), to_px(TX, MY)], fill="black", width=W)

# Stroke 2 — 竖 (left vertical, spans whole char, from top to bottom-left corner)
t.line([to_px(LX, TY), to_px(LX, BY)], fill="black", width=W)

# Stroke 3 — 横 (interior middle heng, closes top box's bottom)
t.line([to_px(LX, MY), to_px(TX, MY)], fill="black", width=W)

# Stroke 4 — 竖弯钩 (bottom envelope):
#   From top-right of top box (TX, MY), the stroke slants gently down-and-out
#   (widening the belly), curves through the bottom-right corner, sweeps
#   left along the bottom, then hooks up.
#   Path: (TX, MY) -> (BX, -40) as a slanted shaft, arc through (BX, BY),
#   tail leftward to (LX, BY) (closing bottom with left shu), then hook up.

# Slanted shaft (top-right of top box, out and down to belly-right):
shaft_a = (TX, MY)
shaft_b = (BX, -40)
# Draw as short bezier-ish poly for a slight bulge outward
nshaft = 10
prev = None
for i in range(nshaft + 1):
    u = i / nshaft
    # Simple quadratic: control point pulled right for bulge
    cx, cy = BX + 5, -15
    x = (1 - u) ** 2 * shaft_a[0] + 2 * (1 - u) * u * cx + u ** 2 * shaft_b[0]
    y = (1 - u) ** 2 * shaft_a[1] + 2 * (1 - u) * u * cy + u ** 2 * shaft_b[1]
    curr = to_px(x, y)
    if prev is not None:
        t.line([prev, curr], fill="black", width=W)
    prev = curr

# Quarter-circle arc at bottom-right: center (BX-15, -55), radius ~18,
# from ~340deg (upper-right) sweeping through 270deg (bottom) to 180deg (left).
# Simpler: arc from (BX, -40) to (BX, BY) then bend left to (LX, BY).
# Use a cubic feel: shaft ended at (BX, -40); now curve to (BX, BY):
arc_a = shaft_b            # (BX, -40)
arc_b = (BX, BY)           # bottom-right corner
narc = 8
prev = to_px(*arc_a)
for i in range(1, narc + 1):
    u = i / narc
    # Slight outward bulge
    cx, cy = BX + 3, -55
    x = (1 - u) ** 2 * arc_a[0] + 2 * (1 - u) * u * cx + u ** 2 * arc_b[0]
    y = (1 - u) ** 2 * arc_a[1] + 2 * (1 - u) * u * cy + u ** 2 * arc_b[1]
    curr = to_px(x, y)
    t.line([prev, curr], fill="black", width=W)
    prev = curr

# Tail: sweep left along the bottom from (BX, BY) to just past (LX, BY),
# meeting the left vertical.
t.line([to_px(BX, BY), to_px(LX, BY)], fill="black", width=W)

# Hook up from bottom-right corner (small upward flick, tapered).
# For 巴 the hook is at the bottom-right, flicking up-and-left slightly.
hook_base = (BX, BY)
hook_tip = (BX - 8, BY + 20)
nseg = 6
for i in range(nseg):
    u0 = i / nseg
    u1 = (i + 1) / nseg
    x0 = hook_base[0] + u0 * (hook_tip[0] - hook_base[0])
    y0 = hook_base[1] + u0 * (hook_tip[1] - hook_base[1])
    x1 = hook_base[0] + u1 * (hook_tip[0] - hook_base[0])
    y1 = hook_base[1] + u1 * (hook_tip[1] - hook_base[1])
    w = max(2, int(round(W * (1 - (u0 + u1) / 2)) + 1))
    t.line([to_px(x0, y0), to_px(x1, y1)], fill="black", width=w)


out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_把.png")
img.save(out_path)
print("saved", out_path)
