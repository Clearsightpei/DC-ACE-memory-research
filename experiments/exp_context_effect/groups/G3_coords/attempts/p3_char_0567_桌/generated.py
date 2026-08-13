# BANK_DEVIATION
# skipped: mu.py, ri.py
# reason: 桌 stacks 卜/日 on top with a wide bottom heng+shu+pie+na, so mu's
#   crossing origin at (0,+25) misplaces the crossbar and ri's absolute
#   pixel rectangle sits mid-canvas — both need bespoke placement here.
# fresh_component: zhuo_stacked_inline (top 卜 + tall 日 + wide bottom 木 base)

import math
import os
from PIL import Image, ImageDraw

CANVAS = 300


def _pie(t, x0, y0, x1, y1, w_head=7.0, w_tail=1.5, bow_perp=-5.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _na(t, x0, y0, x1, y1, w_head=2.0, w_belly=10.0, w_tail=2.0, bow_perp=6.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    u_belly = 0.72
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        if u <= u_belly:
            w = w_head + (w_belly - w_head) * (u / u_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - u_belly) / (1 - u_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_zhuo(t):
    """桌 — inline stacked 卜 + 日 + 木-base."""
    w = 7
    # --- top 卜 area ---
    # short top 一 (slightly left of center, per GT)
    t.line([(138, 40), (172, 40)], fill=(0, 0, 0), width=w)
    # short 丨 dropping from that top 横 into the 日 (卜's shu)
    t.line([(150, 40), (150, 78)], fill=(0, 0, 0), width=w)

    # --- 日 rectangle ---
    xL, xR = 108, 192
    yT, yB = 78, 158
    yM = 120
    t.line([(xL, yT), (xL, yB)], fill=(0, 0, 0), width=w)          # left 竖
    t.line([(xL, yT), (xR, yT)], fill=(0, 0, 0), width=w)          # top 横
    t.line([(xR, yT), (xR, yB)], fill=(0, 0, 0), width=w)          # right 竖 (横折)
    t.line([(xL + 2, yM), (xR - 4, yM)], fill=(0, 0, 0), width=6)  # middle 横
    t.line([(xL, yB), (xR, yB)], fill=(0, 0, 0), width=w)          # bottom 横

    # --- bottom 木 base ---
    # long crossing 一 well below 日
    yH = 188
    t.line([(38, yH), (262, yH)], fill=(0, 0, 0), width=w)
    # long 丨 through the middle (from top of 日 continuation? No — just from 一 down)
    t.line([(150, yB), (150, 268)], fill=(0, 0, 0), width=w)
    # 撇 down-left from crossbar
    _pie(t, x0=150, y0=yH, x1=60, y1=268,
         w_head=7.5, w_tail=1.5, bow_perp=-6.0)
    # 捺 down-right from crossbar
    _na(t, x0=150, y0=yH, x1=248, y1=268,
        w_head=2.0, w_belly=10.0, w_tail=2.0, bow_perp=7.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_zhuo(t)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_桌.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
