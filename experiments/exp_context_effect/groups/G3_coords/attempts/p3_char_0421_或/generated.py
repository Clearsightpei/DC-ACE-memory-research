# p3_char_0421_或 — 或 (huò), ~7-8 strokes.
# Structure (GT-observed):
#   1. small 口 in lower-left (3 strokes rendered as thin box)
#   2. a horizontal 一 across the middle, extending well to the right
#   3. 斜钩 xie_gou — long diagonal sweep from upper-mid down to lower
#      right, terminating in a small hook
#   4. 撇 pie crossing through the body from upper-right down-left
#   5. 丶 dian upper-right
#
# Bank fit review:
#   - draw_kou is a fine identity for the small 口 (compact box). Use it
#     at reduced scale.
#   - No bank primitive fits 斜钩 (wo_gou is a shallow lying hook, wrong
#     orientation). Inline fresh.
#   - Heng, pie, dian: inline for control of position/length.
# No BANK_DEVIATION — draw_kou is used as-is at a smaller scale.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from kou import draw_kou  # noqa: E402


def _line(D, p0, p1, w):
    D.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for (x, y) in (p0, p1):
        D.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _tapered_line(D, p0, p1, w0, w1, steps=24):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (x, y)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)

    W = 5

    # ---- 1. Small 口 lower-left (identity alias) ----
    # draw_kou is centered around (150,150) math-origin; use ox/oy in
    # math coords (+x right, +y up) to push it down-left.
    # ox=-58, oy=-58 puts kou's center near pixel (92, 208), scale=0.55
    # gives a ~55x55 box — matches GT's small lower-left mouth.
    draw_kou(D, ox=-65, oy=-40, scale=0.55)

    # ---- 2. Long 一 across middle ----
    # GT: horizontal spans roughly x=50..210 at y~130.
    _line(D, (50, 130), (215, 130), W)

    # ---- 3. 斜钩 xie_gou — big diagonal ----
    # From upper area (about 130, 65) sweeping to lower-right (245, 245)
    # with slight bow to the right. Terminal hook curls up-left.
    _tapered_bezier(D,
                    (128, 62),
                    (180, 165),
                    (245, 248),
                    4, 7, steps=48)
    # hook (curl up-left)
    _tapered_line(D, (245, 248), (222, 222), 7, 2, steps=12)

    # ---- 4. 撇 pie — sweeps upper-mid-right to lower-left ----
    # Starts near (170, 95) at the top-middle, curves down-left ending
    # near (75, 250), just under 口.
    _tapered_bezier(D,
                    (185, 88),
                    (155, 165),
                    (105, 245),
                    5, 2, steps=32)

    # ---- 5. 丶 dian upper-right ----
    # Small teardrop, points down-right.
    _tapered_bezier(D,
                    (215, 62),
                    (228, 76),
                    (243, 90),
                    2, 7, steps=16)

    out_path = os.path.join(_HERE, "01_或.png")
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
