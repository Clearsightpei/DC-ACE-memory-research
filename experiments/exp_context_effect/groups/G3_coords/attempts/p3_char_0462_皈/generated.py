# BANK_DEVIATION
# skipped: bai_char_compressed_for_LR.py (used as base but overridden)
#          you.py / chang.py (turtle-style, incompatible with PIL canvas)
# reason: GT is uniformly THIN (~4-5px MMH lines), not calligraphic;
#         bank's compressed 白 defaults to w=9 which reads too heavy in a
#         L-R composition next to the thin 反. Also 反 needs a long
#         sweeping 厂-envelope pie under which 又 nests — no bank entry
#         combines those into one PIL primitive.
# fresh_component: fan_right_thin (a thin-line 反 in PIL coords),
#                  bai_thin_LR (a thin-line 白 in PIL coords)

import os

from PIL import Image, ImageDraw


def draw_bai_thin_LR(d, x_left=35, x_right=112, y_top=95, y_bot=245, w=5):
    """Compressed 白 built in PIL, thin uniform lines to match MMH GT.
    5 strokes: top 撇, left 竖, 横折 (top + right 竖), middle 横, bottom 横."""
    y_mid = (y_top + y_bot) // 2

    # Stroke 1: top short 撇 — starts above body, tail lands top-left
    pie_head = (x_left + 40, y_top - 28)
    pie_tail = (x_left + 3, y_top + 3)
    d.line([pie_head, pie_tail], fill=(0, 0, 0), width=w)

    # Stroke 2: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 3: 横折
    d.line([(x_left - 1, y_top), (x_right, y_top - 1)],
           fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top - 1), (x_right, y_bot)],
           fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横
    d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)],
           fill=(0, 0, 0), width=w)

    # Stroke 5: bottom 横
    d.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


def _bezier(d, p0, p1, p2, w_head, w_tail, n=90):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        wv = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(wv)))
        if prev is not None:
            d.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = wv / 2.0
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_fan_right(d, x0=140, x1=282, y_top=60, y_bot=270, w=5):
    """反 (4 strokes): top 横, long 撇 (厂 envelope), 横撇 (top of 又), 捺."""
    # Stroke 1: short top 横 — very short bar at top-left of 反 region
    heng_l = (x0 + 8, y_top + 18)
    heng_r = (x0 + 62, y_top + 15)
    d.line([heng_l, heng_r], fill=(0, 0, 0), width=w)

    # Stroke 2: long descending 撇 — from just under the top heng
    # sweeping down and left to the bottom-left corner
    pie_head = (heng_r[0] - 4, heng_r[1] + 3)
    pie_tail = (x0 - 5, y_bot)
    ctrl = (pie_head[0] - 55, (pie_head[1] + pie_tail[1]) / 2 - 15)
    _bezier(d, pie_head, ctrl, pie_tail, w_head=6, w_tail=2, n=100)

    # Stroke 3: 横撇 — top of internal 又. Short horizontal then downward pie
    hp_l = (x0 + 40, y_top + 85)
    hp_corner = (x0 + 108, y_top + 82)
    hp_tail = (x0 + 78, y_top + 130)
    d.line([hp_l, hp_corner], fill=(0, 0, 0), width=w)
    d.line([hp_corner, hp_tail], fill=(0, 0, 0), width=w)

    # Stroke 4: 捺 — long sweep from near the 又 top down to lower-right,
    # tapered (thin head, thicker mid, tapered end)
    na_head = (x0 + 82, y_top + 100)
    na_tail = (x1 - 2, y_bot - 4)
    na_ctrl = ((na_head[0] + na_tail[0]) / 2 - 4,
               (na_head[1] + na_tail[1]) / 2 + 8)
    _bezier(d, na_head, na_ctrl, na_tail, w_head=3, w_tail=8, n=100)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_bai_thin_LR(d, x_left=35, x_right=112, y_top=100, y_bot=240, w=5)
    draw_fan_right(d, x0=140, x1=282, y_top=55, y_bot=270, w=5)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_皈.png")
    img.save(out)


if __name__ == "__main__":
    main()
