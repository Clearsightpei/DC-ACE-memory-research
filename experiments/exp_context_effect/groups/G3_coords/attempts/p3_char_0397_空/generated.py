# p3_char_0397_空 (kōng "empty/sky")
# 8 strokes: 宀 (3) + 八 (2) + 工 (3).
#
# BANK_DEVIATION
# skipped: bao_gai_tou.py, ba.py, gong.py
# reason: bank primitives compose with baked-in canvas ranges that don't
#         nest cleanly when 空 needs three stacked components each in a
#         narrow horizontal band; direct PIL render lets each stroke land
#         where the GT actually places it.
# fresh_component: kong_char_inline (roof + 八 dots + 工)
#
# math coords: +x right, +y up, origin at (150,150).

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _to_px(x, y):
    return (_CANVAS / 2 + x, _CANVAS / 2 - y)


def _line(t, p0, p1, w):
    t.line([_to_px(*p0), _to_px(*p1)], fill="black", width=w)


def _tapered(t, head, tail, w_head, w_tail, steps=28):
    hx, hy = head
    tx, ty = tail
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        p0 = (hx + (tx - hx) * u0, hy + (ty - hy) * u0)
        p1 = (hx + (tx - hx) * u1, hy + (ty - hy) * u1)
        w = max(1, int(round(w_head + (w_tail - w_head) * u0)))
        t.line([_to_px(*p0), _to_px(*p1)], fill="black", width=w)


def render():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # --- 宀 roof ---
    # S1: 点 chimney tip (short slant, top-center).
    _tapered(t, head=(-4, 115), tail=(4, 100), w_head=4, w_tail=9)

    # S2: 横钩 roof — long horizontal from left to right, then short hook
    # dropping down-left.
    _line(t, (-75, 85), (75, 82), 7)          # horizontal roof
    _tapered(t, head=(75, 82), tail=(66, 65), w_head=8, w_tail=3)  # hook

    # S3: short left slanted 点 hanging from the roof's left edge.
    _tapered(t, head=(-72, 75), tail=(-80, 55), w_head=4, w_tail=8)

    # --- 八 (small, inside/under roof) ---
    # left 撇: short slant down-left
    _tapered(t, head=(-8, 40), tail=(-28, 10), w_head=6, w_tail=3)
    # right 点: short slant down-right
    _tapered(t, head=(8, 40), tail=(28, 15), w_head=3, w_tail=8)

    # --- 工 bottom ---
    _line(t, (-45, -15), (45, -15), 6)       # top 横 (shorter)
    _line(t, (0, -15), (0, -60), 7)          # middle 竖
    _line(t, (-80, -70), (80, -73), 8)       # bottom 横 (widest)

    out = os.path.join(os.path.dirname(__file__), "01_空.png")
    img.save(out)
    return out


if __name__ == "__main__":
    print(render())
