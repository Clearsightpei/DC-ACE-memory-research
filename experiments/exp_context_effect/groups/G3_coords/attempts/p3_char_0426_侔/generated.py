# p3_char_0426_侔 — 侔 (móu), 8 strokes: 亻 (left) + 牟 (right).
# 牟 = 厶 (top, 2 strokes: pie + hengzhepie/short curve) + 牛 (bottom, 4 strokes).
# Composition: bank ren_pang on left (~35% width), inline 牟 on right (~65% width).
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402

CANVAS = 300


def to_px(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def inline_pie(d, x0, y0, x1, y1, w_head=8, w_tail=2, bow=8):
    """Tapered curved pie from (x0,y0) upper-right to (x1,y1) lower-left."""
    mx = (x0 + x1) / 2.0 - bow
    my = (y0 + y1) / 2.0 + bow * 0.4
    n = 50
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = to_px(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def inline_line(d, x0, y0, x1, y1, w=6):
    p0 = to_px(x0, y0)
    p1 = to_px(x1, y1)
    d.line([p0, p1], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- LEFT: 亻 (ren_pang), compressed at left ~35% width ----
    draw_ren_pang(d, ox=-80.0, oy=15.0, scale=0.65)

    # ---- RIGHT: 牟, inline centered around ox=+40 ----
    # 厶 top (2 strokes):
    #   S1: pie from upper-right down-left
    inline_pie(d, x0=65, y0=115, x1=15, y1=60, w_head=7, w_tail=2, bow=8)
    #   S2: 横折 (short) — from S1's mid area right, then hooks down slightly.
    p_a = to_px(22, 78)
    p_b = to_px(80, 72)
    p_c = to_px(72, 50)
    d.line([p_a, p_b], fill=(0, 0, 0), width=6)
    d.line([p_b, p_c], fill=(0, 0, 0), width=6)

    # 牛 bottom (4 strokes), stretched with long shu extending below.
    # Pie (short) from upper right down-left, above the long heng:
    inline_pie(d, x0=60, y0=30, x1=15, y1=-15, w_head=8, w_tail=2, bow=6)
    # Short heng crossing pie (upper heng of 牛):
    inline_line(d, x0=40, y0=5, x1=90, y1=5, w=6)
    # Long heng (the wide horizontal spanning most of right):
    draw_heng(d, ox=40.0, oy=-35.0, scale=0.85)
    # Long shu — from just above long heng down well past baseline:
    draw_shu(d, ox=48.0, oy=-85.0, scale=0.90)

    out = os.path.join(os.path.dirname(__file__), "01_侔.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
