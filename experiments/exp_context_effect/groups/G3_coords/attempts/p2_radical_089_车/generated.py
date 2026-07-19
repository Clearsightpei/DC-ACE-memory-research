# p2_radical_089_车 — 车 (chē, "vehicle") 4-stroke radical.
#
# Analysis of GT:
#   4 strokes:
#     (1) top short 横 — a short horizontal near top
#     (2) 撇折 — from top-right corner descends down-left then reverses to
#         a short horizontal (forms the small parallelogram "cab" top)
#     (3) middle short 横 — the second horizontal, slightly wider than (1)
#     (4) 竖 — long vertical piercing from top through the bottom heng
#         (actually stroke 4 in 车 order is 竖, but in simplified 车 the
#         final stroke IS the vertical after the bottom heng — combined here
#         as one long shu)
#   Plus a bottom long 横 which is actually part of stroke (3) or (4)? — in
#   simplified 车, the order is 横/撇折/横/竖 = 4 strokes total. The bottom
#   long heng belongs to stroke (3)? Actually stroke order:
#     1. 横 (top)
#     2. 撇折 (top-right descent + hook)
#     3. 横 (bottom long) — this is the widest, longest heng
#     4. 竖 (final long vertical piercing through)
#   So the "middle" short heng I saw is actually a small part of the 撇折's
#   reverse — reads as if there are 5 elements but only 4 stroke atoms.
#
# TR8 note: this radical uses the primitive `heng` (well-suited for the
# uniform long bottom heng) and the primitive `shu` (well-suited for the
# long piercing vertical). The top compact "cab" is INLINED fresh because
# no primitive captures its short-heng-plus-撇折 idiom cleanly.
#
# Composition (math coords, +y up, 300x300 canvas, center = origin):
#   Stroke 1 (top short 横): from (-30, +55) to (+35, +55), width 6 tapered
#   Stroke 2 (撇折): from (+35, +55) descending to (-30, +20), then
#            small heng reverse from (-30, +20) to (+40, +20) — the reverse
#            arm becomes the "middle" short heng visually
#   Stroke 3 (bottom long 横): from (-90, -30) to (+90, -30), width 8 — use bank
#            `draw_heng` at scale ~0.9
#   Stroke 4 (long piercing 竖): from (0, +80) to (0, -85), width 7 — use bank
#            `draw_shu` scaled ~0.83
#
# TR6: comments above document every transform.

import os
import sys

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'success_bank', 'code'
    )
)

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu

CANVAS = 300
CX, CY = CANVAS / 2, CANVAS / 2


def to_px(mx, my):
    """math (center origin, +y up) -> PIL pixel."""
    return (CX + mx, CY - my)


def stroke_taper(draw, p0_math, p1_math, w0, w1, n=40):
    """Tapered line via stamped circles from math coords."""
    x0, y0 = p0_math
    x1, y1 = p1_math
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        px, py = to_px(x, y)
        r = max(0.5, w / 2)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def bezier_taper(draw, p0, p1, p2, w0, w1, n=50):
    """Quadratic bezier taper in math coords."""
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w0 + (w1 - w0) * t
        px, py = to_px(x, y)
        r = max(0.5, w / 2)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Revised layout — more vertical spread, wider bottom heng, taller shu.
    # Canvas spans y = -110 (bottom margin) to +110 (top margin).
    #
    # Stroke 1 (top short 横):  y ≈ +85, x ∈ [-30, +30]
    # Stroke 2 (撇折):          top-right (+30, +85) down-left to (-30, +45)
    #                           reverse arm from (-30, +45) to (+35, +48)
    # Stroke 3 (bottom long 横): y ≈ -55, wide (x ∈ [-100, +100])
    # Stroke 4 (long piercing 竖): from (0, +90) down to (0, -95)

    # --- Stroke 1: top short 横 — inlined tapered line
    stroke_taper(d, (-30, 85), (30, 85), 5, 6)

    # --- Stroke 2: 撇折 — two inlined tapered segments joined at corner
    # 撇 arm: from (+30, +82) down-left to (-30, +45), thickens slightly
    stroke_taper(d, (30, 82), (-30, 45), 4, 8)
    # reverse arm (提-like): from (-30, +45) to (+38, +48), tapered
    stroke_taper(d, (-30, 45), (38, 48), 8, 5)
    # small 顿笔 at the corner (P6)
    cx_blob, cy_blob = to_px(-30, 45)
    d.ellipse([cx_blob - 4, cy_blob - 4, cx_blob + 4, cy_blob + 4],
              fill=(0, 0, 0))

    # --- Stroke 3: bottom long 横 — bank primitive
    # heng canonical: 200 px long. Want ~200 px wide at y = -55.
    # scale = 1.0 -> full 200 px, thickness 12. Center at (0, -55).
    draw_heng(d, ox=0, oy=-55, scale=1.0)

    # --- Stroke 4: long piercing 竖 — bank primitive
    # Want vertical from y ≈ +90 (above top heng) to y ≈ -95 (below bottom heng).
    # Total length ≈ 185 px. shu canonical 200 px -> scale 0.93.
    # Vertical center = ( +90 + (-95) ) / 2 = -2.5, but rounded to -2 for
    # slight top-bias (top heng sits above the shu head).
    # draw_shu draws from (ox, oy + half_len) down to (ox, oy - half_len),
    # so oy = midpoint. Use oy = -2, scale=0.93.
    draw_shu(d, ox=0, oy=-2, scale=0.93)

    out_path = os.path.join(os.path.dirname(__file__), "01_车.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
