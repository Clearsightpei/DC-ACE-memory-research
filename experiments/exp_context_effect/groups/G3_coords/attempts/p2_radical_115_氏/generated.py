# p2_radical_115_氏 — 氏 (shi), 4 strokes.
#
# Revised (pass 2) — reflection notes:
#  - v1's 撇 was too horizontal; needs to be a shorter angled dash.
#  - v1's 横 extended too far right; the horizontal should be a small
#    inner heng roughly aligned with the top of the box on the left side.
#  - v1's 竖提 was too small and cramped; the vertical needs more length
#    and the 提 needs a longer up-right flick.
#  - v1's 斜钩 tail-hook was too short and the arc bowed the wrong way.
#    In GT the 斜钩 originates near the top-center, sweeps down and to
#    the right in a long shallow arc, then flicks up.
#
# Coord convention: math coords (center origin, +y up), converted to
# 300x300 PIL pixels via _to_pixel.
#
# Per TR8: all four strokes inlined fresh — no bank primitive matches
# 氏's specific compositional geometry.

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _draw_tapered_bezier(t, x0, y0, mx, my, x1, y1, w_head, w_tail, n=80):
    """Draw a quadratic bezier as a tapered ink stroke."""
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


def _draw_tapered_line(t, x0, y0, x1, y1, w_head, w_tail, n=50):
    """Draw a straight tapered line."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_shi(t):
    """Render 氏 into ImageDraw t."""
    # Overall layout target (math coords, +y up):
    #   - 撇 at top-left, short angled dash from about (-20, +90) to (-55, +50)
    #   - Inner 横 sits at y ≈ +55, spans roughly (-50, +10)
    #   - 竖提: vertical from about (-45, +50) down to (-45, -25),
    #     then 提 flicks up-right to about (+5, -5)
    #   - 斜钩: long sweep from about (-25, +75) down-right to (+90, -95),
    #     then hook up to about (+80, -70)

    # ── Stroke 1: 撇 (short angled dash at top-left) ──
    x0, y0 = -18.0, 90.0
    x1, y1 = -55.0, 45.0
    mx = (x0 + x1) / 2 - 4
    my = (y0 + y1) / 2 + 2
    _draw_tapered_bezier(t, x0, y0, mx, my, x1, y1,
                         w_head=8.0, w_tail=2.0)

    # ── Stroke 2: 横 (short horizontal) ──
    # Sits just below stroke-1's tail level, spanning across the middle-left region.
    _draw_tapered_line(t, x0=-55.0, y0=48.0, x1=15.0, y1=52.0,
                       w_head=7.0, w_tail=7.0)
    # small 顿笔 blobs at both ends
    for (bx, by) in [(-55.0, 48.0), (15.0, 52.0)]:
        px, py = _to_pixel(bx, by)
        t.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(0, 0, 0))

    # ── Stroke 3: 竖提 (vertical + up-right flick) ──
    # Vertical shaft (left column of the enclosure).
    _draw_tapered_line(t, x0=-50.0, y0=48.0, x1=-45.0, y1=-25.0,
                       w_head=8.0, w_tail=7.0)
    # 提 flick: pressed thick head at bottom of vertical, tapers to needle up-right.
    _draw_tapered_line(t, x0=-45.0, y0=-25.0, x1=15.0, y1=-8.0,
                       w_head=10.0, w_tail=1.0)

    # ── Stroke 4: 斜钩 (long slanting hook) ──
    # Head near the top-center (starts where stroke 2 ends visually),
    # sweeps down-right in a shallow arc, ends with hook flicking up.
    sx0, sy0 = -15.0, 75.0
    sx1, sy1 = 95.0, -100.0
    # Bow outward (down-right of chord) for the 斜钩's characteristic
    # gentle rightward curl.
    smx = (sx0 + sx1) / 2 + 12
    smy = (sy0 + sy1) / 2 - 8
    _draw_tapered_bezier(t, sx0, sy0, smx, smy, sx1, sy1,
                         w_head=9.0, w_tail=4.5, n=100)
    # Hook: from tail flicks nearly vertical up-left.
    _draw_tapered_line(t, x0=95.0, y0=-100.0, x1=78.0, y1=-70.0,
                       w_head=6.0, w_tail=1.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_shi(t)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_氏.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
