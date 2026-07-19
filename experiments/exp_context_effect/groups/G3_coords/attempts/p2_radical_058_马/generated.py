# p2_radical_058_马 — G3 coord-format attempt.
# 马 has 3 strokes (modern simplified form):
#   1. 横折 — small top: short horizontal, then drop-down (forms top-right of the little box).
#   2. 竖折折钩 — main body: down (left side), across right, down, hook up-left.
#   3. 横 — bottom horizontal crossing through the shaft, extending past both sides.
#
# Bank use plan (per TR1/TR5/TR6):
# - The bank's `heng_zhe` primitive is close in shape to stroke-1's 横折, but its
#   canonical geometry (span ~170px wide, drop 135px) is far too big for 马's
#   compact top rectangle. Scaling it down to ~0.4 would trigger TR5's "scale<0.4"
#   inline signal. So I INLINE stroke-1 with small custom coords.
# - The bank has NO `shu_zhe_zhe_gou` (3-fold-with-hook) primitive — this needs
#   inlining. `shu_zhe_zhe` exists but it's downward at the end, not a hook.
#   I inline the whole 竖折折钩 with a manual hook at the terminal.
# - Stroke 3 (横): the `heng` primitive fits well (uniform horizontal). Its
#   canonical span is 200px — but the bottom 横 of 马 wants ~140px, so scale=0.7.
#   Center it at (ox=+10, oy=-60): shifted slightly right so it visually crosses
#   under the vertical shaft area and extends slightly past both ends.
#
# Coord convention: math coords, center origin (150,150), +y up.
# Bottom-of-canvas is y=-150, top is y=+150.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=20):
    """Draw a straight tapered segment in math coords."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        pa = _to_pixel(xa, ya)
        pb = _to_pixel(xb, yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def _blob(draw, p, r):
    """Small filled ellipse at math-coord point p — hides miters (P6)."""
    x, y = _to_pixel(*p)
    draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_stroke1_heng_zhe(draw):
    """Stroke 1: 横折 — top segment forming the upper box.
    REVISION: scaled up ~1.7x from pass 1, shifted left to center the character.
    Horizontal top from (-60, +90) to (+40, +90), then drops down to (+40, +25).
    Compact box-top; inlined because bank heng_zhe canonical geometry doesn't match.
    """
    p_h_start = (-60, 90)
    p_corner = (40, 90)
    p_v_end = (40, 25)
    _tapered_segment(draw, p_h_start, p_corner, 9, 10, steps=22)
    _blob(draw, p_corner, 6)  # 顿笔 at the fold
    _tapered_segment(draw, p_corner, p_v_end, 10, 9, steps=16)
    _blob(draw, p_h_start, 4)
    _blob(draw, p_v_end, 4)


def draw_stroke2_shu_zhe_zhe_gou(draw):
    """Stroke 2: 竖折折钩 — the main body of 马.
    REVISION: enlarged so the shaft reaches near bottom of canvas, and hook is
    a proper up-and-left flick from the shaft's base (P1, P9 — hook belongs on
    the SHAFT and flicks UP-AND-LEFT, tapered).
    Path (math coords):
      start (-60, +85)      [welds under stroke 1 left end]
        → down to (-60, +25)  [left vertical of the top-box]
        → right to (+40, +25) [middle horizontal, welds with stroke 1 v_end]
        → down to (+40, -85)  [long right vertical — this is 马's main descending stroke]
        → hook up-left to (0, -55)  [钩 flicking up-and-left, tapered to point]
    """
    p1 = (-60, 85)
    p2 = (-60, 25)
    p3 = (40, 25)
    p4 = (40, -85)
    p_hook_tip = (0, -55)

    _tapered_segment(draw, p1, p2, 10, 11, steps=18)
    _blob(draw, p2, 6)
    _tapered_segment(draw, p2, p3, 11, 10, steps=22)
    _blob(draw, p3, 6)
    _tapered_segment(draw, p3, p4, 11, 11, steps=26)
    _blob(draw, p4, 6)
    # hook: up-and-left, tapered to a point (P1, P9)
    _tapered_segment(draw, p4, p_hook_tip, 11, 2, steps=16)
    _blob(draw, p1, 4)


def draw_stroke3_heng(draw):
    """Stroke 3: bottom 横 — the horizontal that crosses through 马's bottom.
    REVISION: enlarged and placed lower.
    heng primitive canonical: 200 px long, thickness 12, centered on (0,0).
    Target for 马: ~180 px wide, centered at math (ox=-10, oy=-95).
    scale = 180/200 = 0.9.
    ox=-10 centers it so it spans from math x=-100 to x=+80 — passing under the
    left vertical (-60) and past the right vertical/hook zone (+40).
    oy=-95: below the shaft bottom (+40, -85) so the hook has clearance.
    """
    # sanity-check placement (TR7):
    # heng at scale=0.9 draws from math (-90-10, -95) to (+90-10, -95)
    #   = (-100, -95) to (+80, -95).
    # Shaft bottom at (+40, -85). Vertical gap 10 math px. Hook tip at (0, -55).
    # Hook does NOT cross heng (both are above and separated). OK.
    # Canvas margin: y=-95 → PIL y=245. 55px margin below. OK.
    draw_heng(draw, ox=-10, oy=-95, scale=0.9)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_stroke1_heng_zhe(draw)
    draw_stroke2_shu_zhe_zhe_gou(draw)
    draw_stroke3_heng(draw)

    out_path = os.path.join(_HERE, "01_马.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
