# p3_char_0528_疽 — 疽 (jū, "abscess") = 疒 envelope + 且 interior (11 strokes total: 5+5+1? Actually 疒=5, 且=5 = 10 strokes)
#
# DECOMPOSITION:
#   - 疒 envelope (5 strokes): top dot, heng roof, long pie, two interior 冫 marks
#   - 且 interior (5 strokes): left 竖, top 横折 (turn to right vertical),
#     middle heng 1, middle heng 2, bottom heng (extends wider)
#
# BANK USE:
#   - ne_sick.py: 疒 envelope used AS-IS (same 疒 shape as in shan_hernia B10 PASS)
#   - 且: no bank entry — inline fresh
#
# 且 placement: to the right of pie shaft (which passes ~x=95 at y=245).
# 且 occupies roughly x=145-235, y=128-248.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
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


def draw_ne_envelope(draw):
    """疒 envelope, ported from ne_sick.py (B7 v9-rerun PASS bank entry).
    Widened slightly to make room for 且 on the right. Heng and top-dot
    shifted a touch to give 且 room; pie kept as bank."""
    # Top 点
    _tapered_line(draw, (180, 55), (198, 78), w_head=3.0, w_tail=6.5, n=18)
    # Heng roof
    _tapered_line(draw, (140, 108), (255, 105), w_head=4.5, w_tail=4.5, n=30)
    # Long pie
    _tapered_bezier(
        draw,
        p0=(140, 108),
        p1=(78, 278),
        ctrl=(102, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )
    # 冫 upper 点
    _tapered_line(draw, (72, 138), (96, 158), w_head=3.0, w_tail=6.0, n=18)
    # 冫 lower 提
    _tapered_line(draw, (52, 218), (92, 200), w_head=7.5, w_tail=2.5, n=20)


def draw_qie_interior(draw):
    """且 placed inside the 疒 envelope, right of the pie shaft.
    5 strokes: 竖, 横折 (top+right vert), 2 middle hengs, bottom heng."""
    # Bounding box for 且: x 145..238, y 128..248
    x_left = 148
    x_right = 240
    y_top = 128
    y_bot = 248

    # Stroke 1: left 竖
    _tapered_line(draw, (x_left, y_top + 2), (x_left, y_bot),
                  w_head=5.0, w_tail=5.0, n=30)

    # Stroke 2: 横折 — top heng then turn down as right 竖
    # Top heng
    _tapered_line(draw, (x_left, y_top), (x_right, y_top),
                  w_head=4.5, w_tail=5.0, n=30)
    # Right 竖 (down from top-right corner)
    _tapered_line(draw, (x_right, y_top), (x_right, y_bot - 3),
                  w_head=5.0, w_tail=5.0, n=30)

    # Stroke 3: middle heng 1
    y_mid1 = y_top + int((y_bot - y_top) * 0.36)  # ~171
    _tapered_line(draw, (x_left + 3, y_mid1), (x_right - 3, y_mid1),
                  w_head=4.0, w_tail=4.0, n=30)

    # Stroke 4: middle heng 2
    y_mid2 = y_top + int((y_bot - y_top) * 0.68)  # ~209
    _tapered_line(draw, (x_left + 3, y_mid2), (x_right - 3, y_mid2),
                  w_head=4.0, w_tail=4.0, n=30)

    # Stroke 5: bottom heng — extends beyond the frame slightly, thicker
    _tapered_line(draw, (x_left - 10, y_bot), (x_right + 10, y_bot),
                  w_head=5.5, w_tail=5.5, n=30)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_envelope(draw)
    draw_qie_interior(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疽.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
