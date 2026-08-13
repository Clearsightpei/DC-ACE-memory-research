# BANK_DEVIATION
# skipped: ne_sick.py
# reason: ne_sick renders 疒 filling the full canvas; for 痃 the 疒
#         envelope must be compressed to the top-left ~60% so 玄 can
#         nest in the lower-right interior.
# fresh_component: ne_compressed_for_enclosure (thin, MMH-style)
#
# 痃 (xián) = 疒 (envelope, left/top) + 玄 (inside, right/bottom).
# GT PNG: thin uniform strokes (MMH-thin), 玄 = 亠 + 幺.

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


def draw_xian(draw):
    # ---- 疒 (compressed to top-left, envelope) ----
    # Stroke 1: top 点 (small slash upper area, above heng right end)
    _tapered_line(draw, (150, 45), (168, 68), w_head=3.0, w_tail=6.0, n=18)
    # Stroke 2: heng roof — thin, spans left→right across top
    _tapered_line(draw, (95, 88), (250, 85), w_head=4.5, w_tail=4.5, n=32)
    # Stroke 3: long descending 撇 from heng's left end
    _tapered_bezier(
        draw,
        p0=(95, 88),
        p1=(45, 275),
        ctrl=(65, 190),
        w_head=6.0,
        w_tail=4.0,
        n=90,
    )
    # Strokes 4-5: 冫 upper 点 + lower 提, tucked left-interior
    _tapered_line(draw, (58, 130), (78, 150), w_head=3.0, w_tail=6.0, n=18)
    _tapered_line(draw, (40, 210), (73, 195), w_head=7.0, w_tail=2.5, n=20)

    # ---- 玄 (nested in right-bottom interior) ----
    # 亠 top dot
    _tapered_line(draw, (185, 100), (200, 118), w_head=3.0, w_tail=6.0, n=16)
    # 亠 heng — spans right interior
    _tapered_line(draw, (135, 140), (275, 138), w_head=4.5, w_tail=4.5, n=30)

    # 幺 — upper 撇折 (small 厶-like)
    # small pie down-left then折 rising right
    _tapered_line(draw, (215, 155), (185, 185), w_head=4.5, w_tail=4.0, n=20)
    _tapered_line(draw, (185, 185), (235, 178), w_head=4.0, w_tail=4.5, n=20)

    # 幺 — lower 撇折
    _tapered_line(draw, (215, 195), (170, 235), w_head=4.5, w_tail=4.0, n=22)
    _tapered_line(draw, (170, 235), (255, 228), w_head=4.0, w_tail=5.0, n=25)

    # 玄 final 点 (small tail dot lower right)
    _tapered_line(draw, (250, 245), (270, 268), w_head=3.0, w_tail=6.5, n=18)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_xian(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_痃.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
