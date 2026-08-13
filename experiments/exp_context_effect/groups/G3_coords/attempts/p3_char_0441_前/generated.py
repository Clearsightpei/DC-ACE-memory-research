# BANK_DEVIATION
# skipped: yue.py, dao_pang.py
# reason: 前's bottom is a fused 月+刂 compound with a wider aspect than
#   yue.py's tall standalone 月, and yue.py uses (D)-based PIL inline widths
#   while dao_pang.py uses turtle primitives (incompatible), so inline fresh.
# fresh_component: qian_bottom_body (月-frame + interior + 刂 stroke)

# p3_char_0441_前 — 9 strokes:
#   1. 丷 left short (leans in)
#   2. 丷 right short (leans in)
#   3. 一 (long horizontal spanning canvas)
#   4. 撇 (down-left curve from top-left of body)
#   5. 横折钩 top+right of 月 frame — split into top 横 + right 竖 + hook
#      (counted as one stroke: top 横 + right 竖)
#   6-7. two interior 横 (upper and lower interior horizontals)
#   8. 刂 short 竖 (mid-right)
#   9. 刂 长竖钩 (right vertical with hook)
# Inline PIL, thin uniform widths per P12.

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


def draw_qian(D):
    W = 5

    # ============================================================
    # TOP: 丷  (two short strokes, slight inward lean)
    # ============================================================
    # left short pie-dot: slants down-left
    _line(D, (135, 35), (118, 68), W, max(1, W - 2), 14)
    # right short dian: slants down-right
    _line(D, (175, 35), (192, 68), max(1, W - 2), W, 14)

    # ============================================================
    # 一  (long horizontal across canvas)
    # ============================================================
    _line(D, (28, 92), (275, 88), W, W + 1, 40)

    # ============================================================
    # BODY LEFT: 月-like frame
    # ============================================================
    # 撇 — top-left of body sweeping down-left (mostly vertical, mild lean)
    _bezier(D, (100, 108), (92, 200), (68, 278), W + 2, 1, steps=60)

    # 横折钩 (top 横 + right 竖 with hook)
    # top 横 of frame
    _line(D, (100, 108), (178, 105), W, W, 28)
    # right 竖 down
    _line(D, (178, 105), (178, 258), W + 1, W, 40)
    # hook up-left
    _line(D, (178, 258), (158, 246), W, max(1, W - 2), 12)

    # Interior 横 upper (stops inside the 撇, doesn't cross it)
    _line(D, (100, 158), (170, 156), W - 1, W - 1, 22)
    # Interior 横 lower
    _line(D, (95, 210), (170, 208), W - 1, W - 1, 24)

    # ============================================================
    # RIGHT: 刂 (short 竖 + 长竖钩)
    # ============================================================
    # short 竖
    _line(D, (218, 118), (218, 180), W, W, 20)
    # 长竖钩
    _line(D, (258, 100), (258, 268), W, W, 44)
    # hook up-left
    _line(D, (258, 268), (238, 254), W, max(1, W - 2), 12)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_qian(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_前.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
