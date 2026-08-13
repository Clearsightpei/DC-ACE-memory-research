# BANK_DEVIATION
# skipped: ren_pang.py, dao_pang.py
# reason: bank primitives are turtle-based; this composition uses PIL inline
#   (matching bie_char.py style) for a tight 3-column layout 亻|禾|刂
# fresh_component: li_char_inline_for_LMR (亻 + 禾 + 刂 left-middle-right)

# 俐 = 亻 (left) + 利 (right).  利 = 禾 (middle) + 刂 (far right).
# Effective 3-column composition, tall & thin (P12 thin widths ~5px).

from PIL import Image, ImageDraw
import os

CANVAS = 300


def _line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _bezier(D, p0, p1, p2, w0, w1, steps=48):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_li(D):
    W = 5

    # ============================================================
    # LEFT COMPONENT: 亻 (person radical) — x ~30..75, y 70..270
    # 2 strokes: 撇 (long sweep down-left) + 竖 (short vertical)
    # ============================================================
    # 撇 from top-right down-left, curving
    _bezier(D, (72, 78), (55, 145), (32, 230), W + 1, 1, steps=60)
    # 竖: starts on the 撇 mid-shaft (kiss), goes straight down
    _line(D, (55, 140), (55, 270), W, W, 30)

    # ============================================================
    # MIDDLE COMPONENT: 禾 — x ~90..190, y 70..270
    # 5 strokes: top 撇 (short), 一 (heng), 丨 (shu), 撇, 捺
    # ============================================================
    # Top short 撇 (slash on top of 禾)
    _bezier(D, (158, 80), (145, 100), (128, 122), W + 1, 1, steps=32)
    # 一 (heng) — horizontal, sits below the top 撇
    _line(D, (95, 138), (195, 135), W, W, 32)
    # 丨 (shu) — center vertical
    _line(D, (143, 135), (143, 272), W + 1, W, 40)
    # 撇 lower — from center intersection down-left
    _bezier(D, (140, 165), (118, 215), (92, 268), W, 1, steps=48)
    # 捺 lower — from center intersection down-right, thickening then flick
    _bezier(D, (146, 165), (172, 215), (200, 262), 2, W + 3, steps=48)

    # ============================================================
    # RIGHT COMPONENT: 刂 — x ~215..280, y 80..270
    # short left 竖 + long right 竖钩
    # ============================================================
    # Short left 竖
    _line(D, (225, 115), (225, 205), W, W, 26)
    # Long right 竖钩
    _line(D, (272, 82), (272, 265), W, W, 40)
    # Hook up-left
    _line(D, (272, 265), (250, 250), W, max(1, W - 2), 14)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_li(D)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_俐.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
