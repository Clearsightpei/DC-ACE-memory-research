# BANK_DEVIATION
# skipped: ren_pang_pil_for_LR_left.py
# reason: left radical here is 彳 (double-person, 3 strokes), not 亻 (2 strokes); needs an extra short 撇 above the main pie.
# fresh_component: chi_double_pil_for_LR_left
#
# 得 (dé) — 11 strokes. Left: 彳 (3 strokes). Right stack: 日 (4) + 一 (1) + 寸-partial (3).
# Layout: L-R, left ~1/3, right ~2/3. Right is a vertical stack of 3 groups.

import math
import os
from PIL import Image, ImageDraw


def _bezier_stroke(d, p0, p1, p2, w_head, w_tail, n=50, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def _tapered_line(d, p0, p1, w_head, w_tail, n=30, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def draw_de(d):
    black = (0, 0, 0)

    # ============ LEFT: 彳 ============
    # cx = 65; runs from y=55 (top short pie) to y=245 (shu bottom)
    cx = 65

    # S1: short 撇 at top (angled down-left)
    _bezier_stroke(
        d,
        (cx + 18, 55),
        (cx + 8, 78),
        (cx - 10, 95),
        w_head=5, w_tail=2, n=40, black=black,
    )
    # S2: main 撇 below S1
    _bezier_stroke(
        d,
        (cx + 22, 95),
        (cx + 4, 130),
        (cx - 32, 175),
        w_head=6, w_tail=2, n=55, black=black,
    )
    # S3: 竖 — vertical, from mid-shaft of S2 down
    _tapered_line(
        d,
        (cx + 3, 140),
        (cx + 3, 245),
        w_head=6, w_tail=5, n=40, black=black,
    )

    # ============ RIGHT: 日 (top) + 一 (mid) + 寸-partial (bottom) ============
    # Right slot: x from ~135 to ~270
    rx_l = 140
    rx_r = 258

    # ---- 日 (top-right): tall narrow rectangle with one inner heng ----
    ri_l = 165
    ri_r = 245
    ri_top = 50
    ri_bot = 135
    ri_mid = 92
    w = 5
    # S4: left 竖
    d.line([(ri_l, ri_top), (ri_l + 1, ri_bot)], fill=black, width=w)
    # S5: 横折 (top heng + right shu)
    d.line([(ri_l, ri_top), (ri_r, ri_top + 1)], fill=black, width=w)
    d.line([(ri_r, ri_top + 1), (ri_r + 1, ri_bot)], fill=black, width=w)
    # S6: middle 横
    d.line([(ri_l + 3, ri_mid), (ri_r - 3, ri_mid + 1)], fill=black, width=w - 1)
    # S7: bottom 横 (closes)
    d.line([(ri_l, ri_bot), (ri_r + 2, ri_bot + 1)], fill=black, width=w)

    # ---- 一 (heng across right side) ----
    y_heng = 170
    d.line([(148, y_heng), (268, y_heng + 1)], fill=black, width=6)

    # ---- 寸 (bottom): 横 + 竖钩 + 点 ----
    # S9: 横 (short, sits just below the long 一)
    d.line([(160, 205), (260, 206)], fill=black, width=6)
    # S10: 竖钩 (vertical stem with hook curling left at bottom)
    stem_x = 210
    _tapered_line(
        d,
        (stem_x, 195),
        (stem_x, 265),
        w_head=6, w_tail=6, n=40, black=black,
    )
    # hook curling up-left
    d.line([(stem_x, 265), (stem_x - 12, 262), (stem_x - 22, 253)],
           fill=black, width=6)
    # S11: 点 (short slash) to the right of stem, upper-right
    d.line([(232, 220), (247, 234)], fill=black, width=8)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_de(d)
    out = os.path.join(os.path.dirname(__file__), "01_得.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
