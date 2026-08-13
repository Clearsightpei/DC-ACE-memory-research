# BANK_DEVIATION
# skipped: jie_radical.py  (right half 卩 — bank primitive has a bezier D-shape
#   with heavy tapered 竖 that reads too calligraphic vs GT's thin uniform lines)
# reason: GT shows thin ~4px uniform strokes for both halves; the frozen
#   jie_radical uses tapered widths (8-10px) that would visually overweight
#   the right side relative to the inlined-thin left side.
# fresh_component: jie_radical_thin_for_ji
#
# p3_char_0343_即 (jí) — 7 strokes.
# Left component 皀 (5 strokes): 撇 + 横折 + 横 (inside) + 横 (bottom) + 竖提.
# Right component 卩 (2 strokes): 横折钩 + long 竖.
# Follows the 卬 (p3_char_0153) recipe of thin uniform lines (P12).

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_即.png")

W = 4


def _line(draw, pts, w=W):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)


def _bez(p0, p1, p2, steps=24):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def draw_ji(t):
    # ---- LEFT half: 皀 component ----
    # Occupies roughly x=45..135, y=70..250.
    # REVISION: box compressed to y=100..165 (was 105..160 but too centered),
    # with 竖提 shu clearly extending below box to bottom of canvas.
    # Left vertical anchor at x=60, box right at x=125.

    # Stroke 1: 撇 (short top pie) — from (95, 78) curving down-left
    # to top-left of the box at (60, 108).
    pie_pts = _bez((95, 78), (78, 94), (60, 108), 24)
    _line(t, pie_pts)

    # Stroke 2: 横折 — top of box then right side, compact.
    # 横 from (60, 108) to (125, 104), 折 down to (125, 150).
    _line(t, [(60, 108), (125, 104)])
    _line(t, [(125, 104), (125, 150)])

    # Stroke 3: 横 middle — inside the box, from (66, 128) to (122, 126).
    _line(t, [(66, 128), (122, 126)])

    # Stroke 4: 横 bottom — closes the box, from (60, 150) to (125, 150).
    _line(t, [(60, 150), (125, 150)])

    # Stroke 5: 竖提 — long vertical from top-left of box (60, 108)
    # straight down to (60, 240), then rising tail sweeping up-right
    # to about (145, 215).
    _line(t, [(60, 108), (60, 240)])
    ti_pts = _bez((60, 240), (95, 236), (145, 215), 20)
    _line(t, ti_pts)

    # ---- RIGHT half: 卩 component ----
    # Occupies roughly x=170..245, y=90..270.
    # Fresh thin-line render (jie_radical_thin_for_ji).

    # Stroke 6: 横折钩 — top-right D shape.
    # 横 from (172, 108) to (232, 102), 折 curving down to (222, 175),
    # tiny 钩 back to (210, 178).
    _line(t, [(172, 108), (232, 102)])
    zhe_pts = _bez((232, 102), (238, 145), (222, 175), 24)
    _line(t, zhe_pts)
    _line(t, [(222, 175), (210, 178)])

    # Stroke 7: 竖 — long vertical for the right leg,
    # starting near the 横起笔 at (192, 118) going down to (192, 272).
    _line(t, [(192, 118), (192, 272)])


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ji(draw)
    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
