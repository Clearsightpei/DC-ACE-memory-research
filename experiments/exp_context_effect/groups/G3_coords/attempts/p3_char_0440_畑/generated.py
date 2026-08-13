# p3_char_0440_畑 — 畑 (hatake, Japanese-coined kanji): 火 (left) + 田 (right).
# Structure: L-R composition, 9 strokes total (4 for 火, 5 for 田).
#
# BANK_DEVIATION
# skipped: bi_field_over_ji.py
# reason: bi_field's 田 is baked full-width (x=80..220) for a top-stack
#         context; 畑 needs 田 compressed into the right ~45% of the canvas.
# fresh_component: tian_field_for_LR_right — compact 田 box at x=155..270
#
# No 火 primitive exists in bank — inlining fresh.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畑.png")


def _line(D, p0, p1, w):
    D.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for (x, y) in (p0, p1):
        D.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=28):
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


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)

    # ============ 火 (LEFT) ============
    # 4 strokes: upper-left 点, upper-right 撇(short), main 撇, main 捺.
    # Left component occupies x ~20..130, y ~55..270.

    # Stroke 1: upper-left 点 (small dian, drops down-left slightly)
    _tapered_bezier(D, (73, 75), (68, 90), (60, 108), 3, 8, steps=18)

    # Stroke 2: upper-right 短撇 (short pie sweeping down-left from apex area)
    _tapered_bezier(D, (95, 85), (88, 105), (78, 125), 8, 3, steps=20)

    # Stroke 3: main 撇 (large pie from upper-center down-left, curved)
    _tapered_bezier(D, (85, 130), (55, 200), (25, 268), 9, 3, steps=32)

    # Stroke 4: 捺 (na, from near apex down-right, thickening then flick)
    _tapered_bezier(D, (85, 140), (110, 200), (140, 258), 4, 12, steps=32)
    # 捺 flick tail
    _line(D, (140, 258), (152, 252), 5)

    # ============ 田 (RIGHT) ============
    # Compact box at x=155..270, y=95..225. 5 strokes.
    x_left = 158
    x_right = 268
    y_top = 95
    y_bot = 225
    x_mid = (x_left + x_right) // 2
    y_mid = (y_top + y_bot) // 2

    w = 7   # box edge width
    wm = 6  # inner cross width

    # Stroke 5: left 竖
    _line(D, (x_left, y_top), (x_left, y_bot), w)
    # Stroke 6: 横折 (top heng + right shu)
    _line(D, (x_left - 3, y_top), (x_right + 3, y_top), w)
    _line(D, (x_right, y_top), (x_right, y_bot), w)
    # Stroke 7: middle 竖 (inside)
    _line(D, (x_mid, y_top + 3), (x_mid, y_bot - 2), wm)
    # Stroke 8: middle 横 (inside)
    _line(D, (x_left + 3, y_mid), (x_right - 3, y_mid), wm)
    # Stroke 9: bottom 横 (closes box)
    _line(D, (x_left - 3, y_bot), (x_right + 3, y_bot), w)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
