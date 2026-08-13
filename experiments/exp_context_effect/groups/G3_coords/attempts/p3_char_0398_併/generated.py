# p3_char_0398_併 — 併 (bìng, "combine"), 8 strokes: 亻 (left) + 并 (right).
# 并 = 丷 (asymmetric top dots) + long horizontal + long left pie + crossbar
#     + right vertical (6 strokes).
# Composition: left 亻 (bank ren_pang compressed) + right 并 (bank ba_dot top
# + inline 廾-like base, similar to nian_horns structure).
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from ba_dot import draw_ba_dot  # noqa: E402


CANVAS = 300


def P(bx, by, ox=0, oy=0, scale=1.0):
    return (CANVAS / 2 + ox + bx * scale, CANVAS / 2 - (oy + by * scale))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — compressed ren_pang.
    draw_ren_pang(d, ox=-70.0, oy=0.0, scale=0.85)

    # 并 on right — spans roughly (+10..+120, -100..+100).
    # Center of 并 region at ox=+55.
    RIGHT_OX = 55.0
    scale_r = 1.0
    w = max(1, int(round(6 * scale_r)))

    # (1) 丷 on top — asymmetric dots (left 点 + right 撇), larger.
    draw_ba_dot(d, ox=RIGHT_OX + 0, oy=+95.0, scale=0.75)

    # (2) upper horizontal (top bar of 廾 base).
    d.line([P(-40, +30, RIGHT_OX, 0, scale_r),
            P(+55, +30, RIGHT_OX, 0, scale_r)],
           fill=(0, 0, 0), width=w)

    # (3) long left 撇 — starts near right of upper horizontal, curves down-left.
    def _curve(p0, p1, p2, width, steps=40):
        pts = []
        for i in range(steps + 1):
            u = i / steps
            x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
            y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
            pts.append((x, y))
        d.line(pts, fill=(0, 0, 0), width=width)

    _curve(P(+5, +40, RIGHT_OX, 0, scale_r),
           P(-25, -20, RIGHT_OX, 0, scale_r),
           P(-55, -100, RIGHT_OX, 0, scale_r),
           width=w)

    # (4) long crossbar horizontal (lower bar).
    d.line([P(-65, -30, RIGHT_OX, 0, scale_r),
            P(+65, -30, RIGHT_OX, 0, scale_r)],
           fill=(0, 0, 0), width=w)

    # (5) right 竖 — vertical from above upper horizontal down through crossbar.
    d.line([P(+40, +40, RIGHT_OX, 0, scale_r),
            P(+45, -105, RIGHT_OX, 0, scale_r)],
           fill=(0, 0, 0), width=w)

    out = os.path.join(os.path.dirname(__file__), "01_併.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
