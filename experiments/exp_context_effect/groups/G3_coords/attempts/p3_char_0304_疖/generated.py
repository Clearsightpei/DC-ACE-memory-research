# p3_char_0304_疖 — 疖 (jie, "boil") = 疒 envelope + 卩 nested inside.
#
# Plan (v9 posture: trust GT; inline, uniform thin widths):
#   - Envelope 疒 (5 strokes): top dot, thin heng roof, long descending
#     pie on left, two interior 冫 marks (upper 点 + lower 提).
#     Recipe borrowed from bank ne_sick.py (v9 GRADUATE, row 203) but
#     the pie is trimmed and shifted left to leave belly space for 卩.
#   - 卩 (2 strokes): small 横折钩 (D-shape) at top-right inside belly
#     + long 竖 descending from top of D, extending near envelope base.
#
# GT observation: envelope roof spans ~mid-canvas; pie stops around
# y≈255 (short of ne_sick's y=278 because 卩's 竖 lives to its right);
# 卩 sits under the right half of the heng, its 竖 is the tallest
# stroke of the character.
#
# No helper hazards (no aggressive taper-to-nothing). All hand-inline
# uniform-ish thin widths per drawer_memory "trust GT" posture.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=24):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_jie_boil(draw):
    # === 疒 envelope (adapted from ne_sick.py — pie trimmed for 卩) ===

    # Stroke 1: top 点 — small tapered slash upper-right above heng.
    _tapered_line(draw, (188, 50), (205, 75), w_head=3.0, w_tail=6.5, n=18)

    # Stroke 2: heng — thin horizontal roof.
    _tapered_line(draw, (105, 100), (235, 100), w_head=4.5, w_tail=4.5, n=32)

    # Stroke 3: 撇 (long left-falling sweep) welded at heng's left end.
    # Trimmed vs ne_sick (y=278 → y=258) and shifted slightly left to
    # avoid stepping on 卩's 竖 territory.
    _tapered_bezier(
        draw,
        p0=(105, 100),
        p1=(55, 258),
        ctrl=(78, 190),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # Stroke 4: 冫 upper mark — small 点, positioned inside belly RIGHT
    # of pie shaft (pie at y≈140 is around x≈91).
    _tapered_line(draw, (98, 132), (118, 155), w_head=3.0, w_tail=6.0, n=18)

    # Stroke 5: 冫 lower mark — 提 (rising flick, thick→thin), inside
    # belly right of pie shaft (pie at y≈200 is around x≈74).
    _tapered_line(draw, (85, 205), (122, 190), w_head=7.5, w_tail=2.5, n=20)

    # === 卩 nested inside envelope (2 strokes) ===
    # Sits under the right half of the roof (x≈140–210 band).
    # Its 竖 is the tallest stroke, extending near the envelope base.

    # Stroke 6a: 横 top segment of 横折钩 — thin horizontal.
    _tapered_line(draw, (145, 128), (208, 128), w_head=5.0, w_tail=5.5, n=20)

    # Stroke 6b: 折 (vertical drop) + 钩 (small hook left).
    # Right edge of D descends from (208,128) to about (205, 175),
    # ending with a small leftward hook.
    _tapered_line(draw, (208, 128), (204, 178), w_head=5.5, w_tail=6.0, n=20)
    # small 钩 flicking up-left
    _tapered_line(draw, (204, 178), (188, 168), w_head=6.0, w_tail=2.0, n=12)

    # Stroke 7: 竖 (long vertical) — from the top-left of the D descending
    # well down, becoming the tallest stroke on the right side of the
    # character.
    _tapered_line(draw, (152, 118), (150, 275), w_head=6.0, w_tail=5.0, n=40)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jie_boil(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疖.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
