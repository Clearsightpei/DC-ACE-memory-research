# p2_radical_088_长 — draw 长 (4 strokes) on 300x300 canvas.
#
# GT analysis (from gt/phase2/长.png):
#   1. 撇 (pie)  — short, upper-left area, descends down-left,
#                  its tail landing on the heng.
#   2. 横 (heng) — horizontal crossing through the middle-upper region;
#                  span roughly 170 px, sits above canvas center.
#   3. 竖提 (shu ti) — vertical descending on the LEFT (crossing the heng
#                       near its left end), then a flick up-right off the bottom.
#   4. 捺 (na)  — long diagonal sweeping from the heng-crossing area
#                  down and to the right, ending near lower-right;
#                  this is the dominant stroke visually.
#
# Revision (pass 2): first render had the short 撇 too small, the
# vertical too short/thin, the 捺 too thin and starting too low, and
# overall too compressed. This revision: bigger short 撇, taller more
# prominent 竖提 vertical, larger 捺 starting from the heng, and the
# whole character shifted down to fill more of the canvas vertically.
#
# Per shared_rules v6 and G3 TR1-TR9: bank primitives called with
# DELIBERATE (ox, oy, scale). The short upper 撇 remains INLINE fresh
# (TR8) — it does not match pie primitive's tall diagonal geometry.
#
# Math-coord convention: origin at canvas center, +y up.
# Canvas 300x300, PIL ImageDraw.

import os
import sys
from PIL import Image, ImageDraw

BANK_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_DIR)

from heng import draw_heng          # noqa: E402
from shu_ti import draw_shu_ti      # noqa: E402
from na import draw_na              # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_short_pie(t, x0, y0, x1, y1, w_head=11, w_tail=2):
    """Inline-fresh short 撇 (TR8): tapered bezier head->tail.

    (x0, y0) is head (upper-right, thick), (x1, y1) is tail
    (lower-left, tapered). Control point pulled slightly left of chord
    to bow the sweep, following pie.py's recipe.
    """
    mx = (x0 + x1) / 2.0 - 5.0
    my = (y0 + y1) / 2.0 + 4.0
    n = 50
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Layout plan (math coords, +y up):
    #   heng runs across the upper-middle at oy=+15 (PIL y ~ 135),
    #     from math x=-85 to x=+85 (170 px wide, scale 0.85).
    #   short 撇 sits above the heng, its tail welded onto the heng at
    #     around math (-55, +15). Head above at (-30, +55).
    #   shu_ti: shaft on the LEFT of heng (~x=-55), top just above the heng
    #     (~y=+45), bottom well below heng (~y=-95). Ti flicks up-right.
    #   na: from heng-crossing (~(-25, +15)) sweeping to lower-right
    #     (~(+95, -100)). Long and prominent.

    # ---- Stroke 2 (heng first as backbone) ----
    # draw_heng: scale=0.85 -> 170 px long, thickness ~10.
    # ox=0, oy=+15 places PIL y ~ 135.
    draw_heng(t, ox=0, oy=15, scale=0.85)

    # ---- Stroke 1 (short 撇, INLINE fresh per TR8) ----
    # Sits above heng on the LEFT side. Head at math (-32, +58), tail
    # welded onto the heng near math (-58, +14).
    draw_short_pie(t, x0=-32, y0=58, x1=-58, y1=14, w_head=11, w_tail=2)

    # ---- Stroke 3 (竖提) ----
    # Standalone shu_ti: shaft (0,+95) to (0,-85), ti to (+95,-25).
    # Target: shaft top math (-55, +45), shaft bot math (-55, -95).
    #   Shaft height desired: 140 px. Standalone: 180 px. Scale ~0.78.
    # At scale=0.78: shaft top = +74.1, bot = -66.3, center = +3.9.
    # Target center math y = (45 + -95) / 2 = -25.
    #   oy = -25 - 3.9 = -28.9. Round to -29.
    # ox = -55 (translate shaft in x).
    # Verify: shaft top = (-55, 74.1 - 29) = (-55, +45.1)  ✓
    #         shaft bot = (-55, -66.3 - 29) = (-55, -95.3)  ✓
    #         ti end   = (-55 + 95*0.78, -25*0.78 - 29)
    #                  = (-55 + 74.1, -19.5 - 29)
    #                  = (+19.1, -48.5)  — flicks up-right, inside canvas.
    draw_shu_ti(t, ox=-55, oy=-29, scale=0.78)

    # ---- Stroke 4 (long 捺) ----
    # Standalone na: head (-70, +80) -> foot (+80, -90). Chord = 150 x 170.
    # Target: head near heng-crossing at math (-25, +18), foot at math
    # (+100, -100). Chord = 125 x 118 — slightly narrower/shorter.
    # Scale ~0.82: head = (-57.4, +65.6), foot = (+65.6, -73.8).
    #   ox = -25 - (-57.4) = +32.4  -> +32
    #   oy = +18 - 65.6 = -47.6      -> -48
    # Verify: foot = (+65.6 + 32, -73.8 - 48) = (+97.6, -121.8).
    # PIL foot = (150 + 97.6, 150 + 121.8) = (247.6, 271.8) — near
    # bottom-right, inside canvas (need <290 both). y=272 is snug but OK.
    # Shrink slightly for safety: scale=0.78.
    #   head = (-54.6, +62.4), foot = (+62.4, -70.2).
    #   ox = -25 - (-54.6) = +29.6 -> +30
    #   oy = +18 - 62.4 = -44.4    -> -44
    #   foot at (+92.4, -114.2) -> PIL (242.4, 264.2). Comfortable.
    draw_na(t, ox=30, oy=-44, scale=0.78)

    out_path = os.path.join(os.path.dirname(__file__), "01_长.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
