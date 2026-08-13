# p3_char_0302_疔 — 疔 (dīng, "boil/carbuncle"), 7 strokes.
# Decomposition: 疒 envelope (5 strokes) + 丁 inside (2 strokes: heng + shu_gou).
#
# Bank references (v8 REFERENCE ONLY):
#   - ne_sick.py — 疒 envelope with two inner 冫 marks (B7 v9 GRADUATE recipe).
#     Uses inline uniform-thin widths and a bezier pie (NOT draw_guang).
#   - ding_char.py — 丁 = heng + shu_gou.
#
# Strategy: inline the ne_sick envelope-and-marks recipe directly (proven
# under GT-thin ink), then add the 丁 inside the belly (heng across upper-
# right interior + shu_gou descending from that heng's middle to bottom).
# Following drawer_memory playbook: MMH-thin widths, trust GT.

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


def draw_ding_boil(draw):
    # ---- 疒 envelope (inline from ne_sick.py, v9 graduate recipe) ----
    # S1: top 点 (small slash upper-right).
    _tapered_line(draw, (198, 55), (215, 78), w_head=3.0, w_tail=6.5, n=18)
    # S2: heng roof (thin, spans mid-left to right).
    _tapered_line(draw, (145, 108), (245, 105), w_head=4.5, w_tail=4.5, n=30)
    # S3: 撇 — long descending sweep from heng's left end.
    _tapered_bezier(
        draw,
        p0=(145, 108),
        p1=(85, 278),
        ctrl=(108, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )
    # S4: 冫 upper 点 (short slash, left interior).
    _tapered_line(draw, (78, 138), (100, 158), w_head=3.0, w_tail=6.0, n=18)
    # S5: 冫 lower 提 (rising flick).
    _tapered_line(draw, (58, 218), (95, 202), w_head=7.5, w_tail=2.5, n=20)

    # ---- 丁 inside envelope (right-interior) ----
    # REVISION: GT shows 丁's heng merged with 疒's top heng (one shared
    # horizontal), not a separate lower interior heng. So drop the extra
    # heng; only the shu (with a small hook) is a distinct new stroke.
    # S6: shu_gou — long vertical descending from the shared top heng
    # (~x=200, y=107) down to near the bottom, small leftward hook end.
    _tapered_line(draw, (200, 107), (200, 282), w_head=5.0, w_tail=4.5, n=50)
    # hook: short leftward flick at the bottom.
    _tapered_line(draw, (200, 282), (180, 270), w_head=4.5, w_tail=2.5, n=12)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ding_boil(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疔.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
