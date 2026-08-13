# BANK_DEVIATION
# skipped: you.py (turtle math-coord 又) and ren_pang_pil_for_LR_left.py (only left slot 亻)
# reason: 难 is 又+隹 L-R; 又 needs compression into LR-left slot (PIL px), and 隹
#         has no bank entry (亻 + 4 hengs crossing shu — new radical family)
# fresh_component: you_char_for_LR_left_pil, zhui_radical_pil (亻 + 竖 with 4 crossing 横)

import math
import os
from PIL import Image, ImageDraw


def _bezier_stroke(d, p0, p1, p2, w_head, w_tail, n=45, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def _tapered_line(d, p0, p1, w_head, w_tail, n=30, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def draw_you_LR_left(d):
    """又 compressed into left ~40% of canvas, PIL px, MMH-thin.

    Stroke 1: 横撇 — a top heng that turns and sweeps down-left as a pie.
    Stroke 2: 捺 — starts near the corner and sweeps down-right.
    """
    # Stroke 1a: top heng segment (short, slightly rising).
    _tapered_line(
        d,
        (35, 90), (110, 88),
        w_head=5, w_tail=6, n=25,
    )
    # Stroke 1b: pie continuation from the heng's right end, sweeping down-left.
    _bezier_stroke(
        d,
        (108, 88),        # head at heng's right end (the corner)
        (85, 150),        # control
        (25, 240),        # tail lower-left
        w_head=6, w_tail=2, n=55,
    )
    # Stroke 2: 捺 — from upper-mid, sweep down-right with widening tail.
    _bezier_stroke(
        d,
        (60, 140),        # head on the pie shaft (upper-mid)
        (95, 190),        # control
        (135, 245),       # tail lower-right (fat)
        w_head=3, w_tail=9, n=55,
    )


def draw_zhui_LR_right(d):
    """隹 in right ~55% of canvas: short-pie top + 亻-vertical + 4 crossing hengs."""
    # Top small 撇 (very short slanting stroke at top-left of 隹)
    _bezier_stroke(
        d,
        (180, 45),
        (172, 60),
        (160, 80),
        w_head=5, w_tail=2, n=30,
    )
    # 亻 main pie: from upper-right sweeping down-left across the block
    _bezier_stroke(
        d,
        (200, 75),        # head upper
        (175, 140),       # control
        (140, 240),       # tail lower-left
        w_head=6, w_tail=2, n=55,
    )
    # 竖 — the main vertical of 隹, at x~220, from y~90 to y~265
    _tapered_line(
        d,
        (222, 90), (222, 268),
        w_head=6, w_tail=5, n=40,
    )
    # heng 1 (top short, just below top pie)
    _tapered_line(
        d,
        (200, 110), (255, 108),
        w_head=4, w_tail=5, n=25,
    )
    # heng 2
    _tapered_line(
        d,
        (190, 150), (270, 148),
        w_head=4, w_tail=6, n=25,
    )
    # heng 3
    _tapered_line(
        d,
        (185, 190), (272, 188),
        w_head=4, w_tail=6, n=25,
    )
    # heng 4 (bottom base heng, longest)
    _tapered_line(
        d,
        (170, 232), (280, 230),
        w_head=5, w_tail=8, n=25,
    )


def draw_nan(d):
    draw_you_LR_left(d)
    draw_zhui_LR_right(d)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_nan(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_难.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
