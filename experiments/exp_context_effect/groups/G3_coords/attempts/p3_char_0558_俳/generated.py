# p3_char_0558_俳 — 亻 (LR-left) + 非 (right side)
#
# Uses the canonical PIL 亻 bank primitive on the left.
# 非 has no dedicated bank primitive, so inlined fresh: two verticals
# with 3 short horizontal ticks each. Standard modern-print form has
# left vertical's horizontals extending RIGHTWARD (into the middle gap)
# and right vertical's horizontals extending RIGHTWARD (outward east).

import os
import sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, BANK)
from ren_pang_pil_for_LR_left import draw_ren_pang_pil_for_LR_left, _tapered_line


def draw():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 亻 on the left (canonical PIL bank primitive) ----
    draw_ren_pang_pil_for_LR_left(
        d, cx=70, y_top=80, y_bot=250,
        w_pie_head=6, w_pie_tail=2, w_shu=5,
    )

    # ---- 非 on the right ----
    # Standard 非 orthography: ALL horizontals point rightward.
    # Left vertical: 3 short horizontals extend RIGHT (into middle gap).
    # Right vertical: 3 short horizontals extend RIGHT (outward east).
    left_vx = 150
    right_vx = 220
    y_top = 75
    y_bot = 270

    # Left vertical of 非 (thin uniform)
    _tapered_line(d, (left_vx, y_top), (left_vx, y_bot),
                  w_head=5, w_tail=5, n=40)

    # Right vertical of 非 (slightly heavier since it is the dominant/last)
    _tapered_line(d, (right_vx, y_top), (right_vx, y_bot),
                  w_head=6, w_tail=6, n=40)

    tick_ys = [98, 165, 232]
    # Horizontals from LEFT vertical, going RIGHT into the middle gap.
    tick_len_L = 45
    for hy in tick_ys:
        _tapered_line(d, (left_vx, hy), (left_vx + tick_len_L, hy),
                      w_head=4, w_tail=3, n=15)

    # Horizontals from RIGHT vertical, going RIGHT (outward east).
    tick_len_R = 45
    for hy in tick_ys:
        _tapered_line(d, (right_vx, hy), (right_vx + tick_len_R, hy),
                      w_head=4, w_tail=3, n=15)

    out = os.path.join(os.path.dirname(__file__), "01_俳.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    draw()
