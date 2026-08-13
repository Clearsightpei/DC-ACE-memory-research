# 海 (hǎi) — p3_char_0511
# LR composition: 氵 (left, bank san_dian_shui) + 每 (right, inline fresh).
#
# 每 has no bank entry; the previous p3_char_0339_每 attempt is not in
# the bank. Inline fresh render of 每 (7 strokes):
#   1) 撇 sweeping down-left from upper right (top of 𠂉)
#   2) short 横 crossing the 撇 near its top
#   3) 竖折 (left vertical + bottom horizontal of 母)
#   4) 横折钩 (top horizontal + right vertical + tiny hook of 母)
#   5) 点 (upper interior dot)
#   6) 长横 crossing through 母's middle, extends past both sides
#   7) 点 (lower interior dot)
#
# No BANK_DEVIATION: san_dian_shui bank primitive is called as-is (it
# fits the LR-left 氵 slot perfectly); 每 has no bank entry so inline is
# the only option.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from san_dian_shui import draw_san_dian_shui  # noqa: E402

CANVAS = 300
INK = (0, 0, 0)


def to_px(mx, my):
    return (CANVAS / 2 + mx, CANVAS / 2 - my)


def tapered_line(d, p0, p1, w0, w1, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    if steps is None:
        steps = max(20, int(length * 2))  # ~0.5 px between samples
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def tapered_bezier(d, p0, p1, p2, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def line_mm(d, mx0, my0, mx1, my1, w=6):
    tapered_line(d, to_px(mx0, my0), to_px(mx1, my1), w0=w, w1=w)


def curve_mm(d, p0, ctl, p1, w_head=6, w_tail=3):
    tapered_bezier(d, to_px(*p0), to_px(*ctl), to_px(*p1),
                   w0=w_head, w1=w_tail)


def draw_mei_right(d, ox=+40, oy=0, s=0.85):
    """每 rendered inline. Coords in math space (y up), relative to (ox,oy).

    Envelope: roughly x in [-55, +60], y in [-100, +130].
    """
    def X(mx): return ox + mx * s
    def Y(my): return oy + my * s

    # ---------- TOP 𠂉 (撇 sweeps down-left; short heng crosses its top)
    # 1) 撇 — from upper-right, sweeps down and left (longer sweep, GT is bold)
    curve_mm(d,
             p0=(X(18),  Y(125)),
             ctl=(X(-25), Y(80)),
             p1=(X(-62), Y(25)),
             w_head=7, w_tail=2)

    # 2) short 横 crossing 撇 near its top
    line_mm(d, X(-25), Y(108), X(55), Y(102), w=6)

    # ---------- BOTTOM 母 — envelope roughly x in [-45,55], y in [45,-95]
    top_y = 45
    bot_y = -95
    xL = -45
    xR = 55

    # 3) 竖折 — left vertical then bottom horizontal (single stroke, drawn
    #    as two segments meeting at the lower-left corner)
    line_mm(d, X(xL), Y(top_y), X(xL + 3), Y(bot_y), w=6)
    line_mm(d, X(xL + 3), Y(bot_y), X(xR + 4), Y(bot_y - 2), w=6)

    # 4) 横折钩 — top horizontal + right vertical + small hook at bottom-left
    line_mm(d, X(xL + 2), Y(top_y), X(xR + 6), Y(top_y - 2), w=6)
    line_mm(d, X(xR + 6), Y(top_y - 2), X(xR + 3), Y(bot_y + 12), w=6)
    # hook: short stub toward lower-left
    line_mm(d, X(xR + 3), Y(bot_y + 12), X(xR - 10), Y(bot_y + 22), w=6)

    # 5) interior 点 — upper-left of the frame
    curve_mm(d,
             p0=(X(-15), Y(10)),
             ctl=(X(-11), Y(3)),
             p1=(X(-3), Y(-6)),
             w_head=3, w_tail=8)

    # 6) 长横 — long horizontal crossing through the 母 mid-height,
    #    extends past both envelope sides
    line_mm(d, X(xL - 40), Y(-25), X(xR + 30), Y(-28), w=6)

    # 7) interior 点 — lower-right of the frame (mirror the upper dot)
    curve_mm(d,
             p0=(X(15), Y(10)),
             ctl=(X(19), Y(3)),
             p1=(X(27), Y(-6)),
             w_head=3, w_tail=8)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # LEFT: 氵 bank primitive — pushed well left, moderate scale for LR
    draw_san_dian_shui(d, ox=-90, oy=+5, scale=0.85)

    # RIGHT: 每 inlined, centered around ox=+40 with s=0.85 for LR right slot
    draw_mei_right(d, ox=+40, oy=-5, s=0.85)

    out = os.path.join(os.path.dirname(__file__), "01_海.png")
    img.save(out)
    print("saved:", out)


if __name__ == "__main__":
    main()
