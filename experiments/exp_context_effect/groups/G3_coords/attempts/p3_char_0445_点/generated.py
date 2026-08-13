# BANK_DEVIATION
# skipped: zhan_char.py
# reason: zhan_char.py bakes 占 into a right-side 亻+占 composition (x-offset,
#         narrow width); standalone 点 needs 占 centered and slightly compressed
#         to leave room for 灬 below.
# fresh_component: zhan_top_standalone (占 recentered for zhan+huo_bottom stack)

import os
import sys
from PIL import Image, ImageDraw

# Import huo_bottom bank primitive
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from huo_bottom import draw_huo_bottom  # noqa: E402

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def line_stroke(draw, p0, p1, w_head, w_tail, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        cur = (x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 占 (top, centered) ----------
    # Occupies math coord y from ~135 (top) to ~-20 (mid-bottom),
    # x from -40 to +45.

    # Stroke 1: 卜 vertical (丨), slightly left of center.
    line_stroke(d,
                to_px(-5, 130),
                to_px(-5, 55),
                w_head=5, w_tail=5, n=30)

    # Stroke 2: 卜 short 一, from vertical rightward, upper-mid height.
    line_stroke(d,
                to_px(-5, 90),
                to_px(48, 90),
                w_head=4, w_tail=5, n=25)

    # 口 rectangle below 卜.
    # Stroke 3: left 丨 of 口
    line_stroke(d,
                to_px(-40, 45),
                to_px(-40, -30),
                w_head=5, w_tail=5, n=30)

    # Stroke 4: 横折 (top heng + right shu)
    line_stroke(d,
                to_px(-40, 45),
                to_px(45, 45),
                w_head=5, w_tail=5, n=30)
    line_stroke(d,
                to_px(45, 45),
                to_px(45, -30),
                w_head=5, w_tail=5, n=30)

    # Stroke 5: bottom 一 of 口
    line_stroke(d,
                to_px(-40, -30),
                to_px(45, -30),
                w_head=5, w_tail=5, n=30)

    # ---------- 灬 (bottom) — bank primitive ----------
    draw_huo_bottom(d)

    out = os.path.join(HERE, "01_点.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
