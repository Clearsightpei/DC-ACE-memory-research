# p2_radical_080_尢 (yóu) — 3-stroke radical
#
# Structural decomposition (from GT observation):
#   1. 一 (heng)          — short slightly-rising horizontal near upper-middle
#   2. 丿 (pie)           — long, nearly-vertical descending sweep from
#                            just above the heng down through the lower-left.
#                            NOTE: per P10, the pie primitive is too diagonal
#                            for a radical-form 丿 that needs a soft mostly-
#                            vertical scoop. Inline fresh as a tapered bezier.
#   3. 乚 (shu_wan_gou)   — starts at right end of heng, descends, curves
#                            right along the base with an up-flick hook.
#                            The shu_wan_gou primitive matches this cleanly
#                            after simple uniform scaling (TR8 pass).
#
# Layout (math coords, center=0, +y up, 300x300 canvas):
#   heng:  center ~ (-5, +30), length ~90 px  -> ox=-5, oy=+30, scale=0.45
#   pie:   inline — head at (-8, +55), scoop down to tail (-85, -85).
#          Mostly-vertical descent with slight leftward bow near the tail.
#   shu_wan_gou: shaft top at (+35, +25), scaled ~0.80. Primitive default
#          shaft top is (0, +70); target (+35, +25) needs ox=+35, oy=-45.
#          Actually: primitive shaft top = (ox, oy+70*s); with s=0.80,
#          shaft top y = oy + 56. Target shaft top y = +25 → oy = -31.
#          Shaft top x = ox = +35 → ox = +35.
#          Scale 0.80 gives shaft len ~80, arc r ~32, tail ~32 — matches GT.

import os
from PIL import Image, ImageDraw

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                 'success_bank', 'code'))

from heng import draw_heng           # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_inline_pie(d):
    """Inline-fresh 丿 for 尢 radical form: mostly-vertical, soft scoop.
    Per P10 the bank pie is too diagonal for a 丿 that needs a shallow
    scoop with thicker head. Head sits above heng at upper-mid, tail
    sweeps to lower-left just short of the canvas edge.
    """
    # Anchors in math coords
    p0 = (0.0, 65.0)      # head — near heng center, above heng
    p1 = (-25.0, -15.0)   # control — pulls the arc down and slightly left
    p2 = (-78.0, -95.0)   # tail — lower-left, near margin

    n = 60
    w_head = 10.0
    w_tail = 1.0

    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # Stroke 1: 一 (heng) — short, centered upper-middle
    # ox=-5 puts it slightly left of canvas center; scale 0.45 → half_len = 45,
    # length 90 px. oy=+30 puts it in the upper-middle band.
    draw_heng(d, ox=-5, oy=30, scale=0.45)

    # Stroke 2: 丿 (pie) — inline-fresh per P10
    draw_inline_pie(d)

    # Stroke 3: 乚 (shu_wan_gou) — starts at right-of-heng, descends & hooks
    # scale 0.80 → shaft ~80 px, arc r ~32, tail ~32, hook ~18
    # Target shaft top: (+35, +25); primitive shaft top = (ox, oy + 70*s)
    # so ox=+35, oy=+25 - 70*0.80 = +25 - 56 = -31
    draw_shu_wan_gou(d, ox=35, oy=-31, scale=0.80)

    out_path = os.path.join(os.path.dirname(__file__), "01_尢.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
