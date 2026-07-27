# p3_char_0169_疋 — G3 main attempt (revised)
# 疋 (pi/shu): 5 strokes per MMH.
# Layout from GT visual: top is a rectangular-ish 横+竖 (like 口 top-right corner),
# then a small 横 mid-right, then a long 撇 sweeping from upper-left down to lower-left,
# then a long 捺 sweeping from middle down to lower-right with a flat foot.

import os
from PIL import Image, ImageDraw

CANVAS = 300
IMG = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
t = ImageDraw.Draw(IMG)


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def line(x0, y0, x1, y1, w=4):
    p0 = _to_pixel(x0, y0)
    p1 = _to_pixel(x1, y1)
    t.line([p0, p1], fill=(0, 0, 0), width=w)


def bezier(x0, y0, mx, my, x1, y1, w_head=5, w_tail=2, segs=60):
    prev = None
    for i in range(segs + 1):
        u = i / segs
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


# Coordinate system: center origin, +y up.
# Character bounding: roughly x in [-90, 90], y in [-90, 90].

# Stroke 1: top 横 — from x=-55 to x=+50 at y=+70
line(-55, 70, 50, 70, w=4)

# Stroke 2: 竖 (short) — going down from right end of 横 at x=+50 to y=+30
# GT shows small angled tail at top-right (kaishu heng-end); include the short vertical
line(50, 70, 48, 30, w=4)

# Stroke 3: short 横 (middle) — from x=-10 to x=+48 at y=+30 (touches bottom of 竖)
line(-10, 30, 48, 30, w=4)

# Stroke 4: 撇 — long left-down sweep from upper-mid-left (~-25, +60) down-left to (-85, -85)
bezier(x0=-25, y0=60, mx=-45, my=-20, x1=-85, y1=-85, w_head=5, w_tail=2, segs=60)

# Stroke 5: 捺 — long right-down sweep from mid-lower (~-40, -20) to (+90, -80) with flat foot
bezier(x0=-40, y0=-20, mx=15, my=-55, x1=80, y1=-80, w_head=3, w_tail=6, segs=60)
# Flat foot extension
line(72, -80, 100, -82, w=5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_疋.png")
IMG.save(out_path)
print(f"Saved: {out_path}")
