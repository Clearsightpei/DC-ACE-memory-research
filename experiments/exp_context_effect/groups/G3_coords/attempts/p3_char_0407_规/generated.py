# BANK_DEVIATION
# skipped: fu.py (夫 has hengs but is written as 父 in that file; 夫 not in bank)
# skipped: er_ren.py / heng_zhe.py combo (see p3_char_0114_见 result — didn't match GT)
# reason: 规 = 夫 (left, with na reduced to a dot) + 见 (right). Bank has no
#         dedicated 夫 or clean 见. Inlining fresh for tight L-R fit and to
#         keep uniform thin-line weight matching MMH GT.
# fresh_component: gui_char_inline (fresh 夫-left + 见-right composition)

import math
from PIL import Image, ImageDraw

CANVAS = 300


def _px(x, y):
    return CANVAS / 2 + x, CANVAS / 2 - y


def _bezier(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
            w_head=6, w_tail=6, belly_pos=1.0, w_belly=None, n=60):
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, math.hypot(dx, dy))
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        px, py = _px(bx, by)
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _heng(draw, xc, yc, half, w=5):
    xL, yL = _px(xc - half, yc)
    xR, yR = _px(xc + half, yc)
    draw.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=w)


def _shu(draw, xc, yT, yB, w=5):
    xt, yt = _px(xc, yT)
    xb, yb = _px(xc, yB)
    draw.line([(xt, yt), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_gui(t):
    # ---- LEFT: 夫 (compressed, na → 点) — centered around x=-70 ----
    # heng1 (top short)
    _heng(t, xc=-70, yc=65, half=28, w=5)
    # heng2 (middle, longer)
    _heng(t, xc=-70, yc=15, half=52, w=5)
    # pie: from mid-heng crossing (~-70, 15) down-left to (-125, -100)
    _bezier(t, -50, 20, -130, -105,
            ctrl_perp=-6, w_head=7, w_tail=1, n=60)
    # 点 (reduced na in left position): short thick tapered from center down-right
    _bezier(t, -55, -10, -20, -85,
            ctrl_perp=6, w_head=2, w_tail=9, belly_pos=0.85, w_belly=10, n=40)

    # ---- RIGHT: 见 (frame + legs) — centered around x=+60 ----
    # 1) Left 竖 of 冂 (from top down to about mid)
    _shu(t, xc=15, yT=80, yB=-30, w=5)
    # 2) 横折 = heng (top) + right vertical
    #    top heng from (~15,80) to (~120,80)
    _heng(t, xc=67, yc=80, half=52, w=5)
    #    right shu from (~120,80) to (~118,-30)
    _shu(t, xc=118, yT=80, yB=-30, w=5)
    # 3) 撇 (inside-left leg): from just under left竖 bottom, down-left,
    #    ends inside canvas (not way off-left)
    _bezier(t, 22, -28, -18, -120,
            ctrl_perp=-6, w_head=6, w_tail=1, n=50)
    # 4) 竖弯钩 (inside-right leg): starts at right-shu bottom, goes down,
    #    curves right, hooks up.
    _bezier(t, 82, -28, 82, -100,
            ctrl_perp=0, w_head=5, w_tail=5, n=30)
    # sweeping curve right along the bottom
    _bezier(t, 82, -100, 122, -118,
            ctrl_perp=-10, w_head=5, w_tail=6, n=40)
    # hook up at the right end
    x_h0, y_h0 = _px(122, -118)
    x_h1, y_h1 = _px(126, -92)
    t.line([(x_h0, y_h0), (x_h1, y_h1)], fill=(0, 0, 0), width=5)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_gui(d)
    import os
    out = os.path.join(os.path.dirname(__file__), "01_规.png")
    img.save(out)
    print("wrote", out)
