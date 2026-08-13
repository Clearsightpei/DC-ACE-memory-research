# BANK_DEVIATION
# skipped: (no bank entry for 兩 / 两 exists)
# reason: 亻 uses bank canonical; 兩 has no bank primitive so right-side
#         rendered fresh inline (top heng + 冂 with hook envelope + inner
#         heng + two inline 入 marks). MMH-thin uniform widths per P12.
# fresh_component: liang_traditional_for_LR_right
#
# 倆 (liǎ) = 亻 (left, ~30% width) + 兩 (right, ~65% width)
# 亻: bank ren_pang_pil_for_LR_left at cx=70
# 兩 stroke plan (right slot, x roughly 125..285):
#   1. top heng: short horizontal near top (y=70)
#   2. left shu (frame left): vertical from y=95 to y=250
#   3. 横折钩 (frame top-right + right vertical + tiny hook):
#      horizontal from left-shu top to x=280, then down to y=250, small hook
#   4. inner heng: horizontal inside frame at y=140
#   5-6. left inner 入: pie + na inside left half
#   7-8. right inner 入: pie + na inside right half

import os
import sys
import math
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang_pil_for_LR_left import draw_ren_pang_pil_for_LR_left  # noqa: E402


def _bezier(d, p0, p1, p2, w_head, w_tail, n=45, black=(0, 0, 0)):
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


def draw_liang_right(d, x_left=130, x_right=282, y_top=70, y_bot=252,
                     w=5, black=(0, 0, 0)):
    """兩 rendered fresh in right slot of an LR composition (PIL px)."""
    frame_top_y = 105
    inner_y = 160

    # 1. top heng: short, centered above the frame, well above frame_top
    x_head = x_left + 30
    x_tail = x_right - 20
    _tapered_line(d, (x_head, y_top + 3), (x_tail, y_top - 3),
                  w_head=w, w_tail=w, n=30, black=black)

    # 2. left shu (frame left vertical)
    _tapered_line(d, (x_left + 5, frame_top_y - 3), (x_left + 3, y_bot),
                  w_head=w, w_tail=w, n=30, black=black)

    # 3. 横折钩: top heng of frame + right shu, with small hook at bottom
    #    part A: horizontal top of frame
    _tapered_line(d, (x_left + 2, frame_top_y),
                  (x_right, frame_top_y),
                  w_head=w, w_tail=w, n=30, black=black)
    #    part B: right vertical
    _tapered_line(d, (x_right, frame_top_y),
                  (x_right, y_bot - 8),
                  w_head=w, w_tail=w, n=30, black=black)
    #    part C: small hook leftward (gou)
    _tapered_line(d, (x_right, y_bot - 8),
                  (x_right - 12, y_bot - 20),
                  w_head=w + 1, w_tail=1, n=20, black=black)

    # 4. inner heng — horizontal separator inside frame
    _tapered_line(d, (x_left + 8, inner_y), (x_right - 4, inner_y),
                  w_head=w, w_tail=w, n=30, black=black)

    # 5-6. left inner 入 (small)
    mid_x = (x_left + x_right) / 2
    left_c = (x_left + mid_x) / 2  # center of left half
    right_c = (mid_x + x_right) / 2
    apex_y = inner_y + 20
    bot_y = y_bot - 20

    # left 入 pie
    _bezier(d,
            (left_c, apex_y),
            (left_c - 8, apex_y + 22),
            (left_c - 22, bot_y),
            w_head=w, w_tail=1, n=35, black=black)
    # left 入 na
    _bezier(d,
            (left_c - 3, apex_y + 6),
            (left_c + 5, apex_y + 22),
            (left_c + 20, bot_y),
            w_head=1, w_tail=w + 2, n=35, black=black)

    # 7-8. right inner 入
    _bezier(d,
            (right_c, apex_y),
            (right_c - 8, apex_y + 22),
            (right_c - 22, bot_y),
            w_head=w, w_tail=1, n=35, black=black)
    _bezier(d,
            (right_c - 3, apex_y + 6),
            (right_c + 5, apex_y + 22),
            (right_c + 20, bot_y),
            w_head=1, w_tail=w + 2, n=35, black=black)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Left: 亻 canonical PIL (bank)
    draw_ren_pang_pil_for_LR_left(d, cx=68, y_top=85, y_bot=230,
                                  w_pie_head=6, w_pie_tail=2, w_shu=5)

    # Right: 兩 fresh inline
    draw_liang_right(d, x_left=130, x_right=282, y_top=68, y_bot=248, w=5)

    out = os.path.join(os.path.dirname(__file__), "01_倆.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
