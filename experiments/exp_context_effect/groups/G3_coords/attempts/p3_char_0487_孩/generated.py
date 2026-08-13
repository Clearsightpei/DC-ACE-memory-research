# p3_char_0487_孩 (hái "child")
# 9 strokes: 子 left (3) + 亥 right (6).
#
# BANK_DEVIATION
# skipped: zi_char.py
# reason: zi_char's turtle-based recipe is coord-system incompatible with
#         inline PIL; and its baked scale/ox conventions don't cleanly
#         compress into 孩's narrow left column (~45% of width). Inlining
#         both halves lets each stroke land where GT places it.
# fresh_component: hai_char_inline (compressed 子 left + inline 亥 right)
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


def _bezier(t, p0, p1, p2, w, steps=32):
    prev = p0
    for i in range(1, steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        t.line([_to_px(*prev), _to_px(x, y)], fill="black", width=w)
        prev = (x, y)


def _tapered_bezier(t, p0, p1, p2, w_head, w_tail, steps=32):
    prev = p0
    for i in range(1, steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        w = max(1, int(round(w_head + (w_tail - w_head) * (u - 1 / steps))))
        t.line([_to_px(*prev), _to_px(x, y)], fill="black", width=w)
        prev = (x, y)


def render():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # =========================================================
    # LEFT — 子 (compressed to left column ~ x in [-135, -25])
    # =========================================================
    # S1: 横撇/横钩 top — horizontal then short down-left hook.
    _line(t, (-130, 85), (-45, 85), 6)         # horizontal
    _tapered(t, head=(-45, 85), tail=(-75, 55), w_head=7, w_tail=3)  # hook down-left

    # S2: 弯钩 descender — begins near top-mid of 子, curves gently
    # down-and-slightly-left with a bottom-left hook.
    _tapered_bezier(
        t,
        p0=(-70, 78),
        p1=(-72, 0),
        p2=(-82, -90),
        w_head=5,
        w_tail=7,
    )
    # small hook flick left at bottom
    _tapered(t, head=(-82, -90), tail=(-115, -80), w_head=7, w_tail=2)

    # S3: 长横 crossing bar — crosses the descender around mid
    _line(t, (-135, -5), (-30, -5), 6)

    # =========================================================
    # RIGHT — 亥 (right column ~ x in [-5, 140])
    # =========================================================
    # S1: 点 (top dot, slight right slant)
    _tapered(t, head=(45, 115), tail=(55, 95), w_head=3, w_tail=8)

    # S2: 短横 (short heng below the dot — top of 亥's 亠)
    _line(t, (10, 78), (135, 78), 6)

    # S3: 撇折 — starts near right end of heng, drops down-left, then
    # turns into a short heng at mid-height.
    _tapered(t, head=(55, 70), tail=(15, 40), w_head=6, w_tail=4)
    _line(t, (15, 40), (65, 40), 5)

    # S4: 撇 — long left-descending diagonal, main left arm (upper
    # attach point starts under the 撇折's endpoint).
    _tapered_bezier(
        t,
        p0=(105, 35),
        p1=(55, -20),
        p2=(0, -95),
        w_head=8,
        w_tail=3,
    )

    # S5: shorter inner 撇 — crosses through mid to form X with 捺
    _tapered(t, head=(70, -10), tail=(30, -55), w_head=5, w_tail=3)

    # S6: 捺 — long right-descending sweep, crosses the long 撇 near
    # its middle to form the characteristic X.
    _tapered_bezier(
        t,
        p0=(35, 15),
        p1=(85, -35),
        p2=(140, -100),
        w_head=4,
        w_tail=10,
    )

    out = os.path.join(os.path.dirname(__file__), "01_孩.png")
    img.save(out)
    return out


if __name__ == "__main__":
    print(render())
