# BANK_DEVIATION
# skipped: yong_use.py
# reason: bank primitive renders 用 with calligraphic ~10px widths and
#         bulbous end-caps, which clash with GT's uniformly thin ~4px
#         MMH-style strokes for this character.
# fresh_component: yong_thin_for_通 (thin 用 sized for 通's right slot)
#
# p3_char_0513_通 — 7 strokes:
#   right component 甬 = top 龴 (small pie + short heng) + 用 (5 strokes)
#   left/bottom envelope 辶 (dian + zig-zag + 平捺)
# All inline PIL, uniform thin widths, no bulbous endpoints.

from PIL import Image, ImageDraw
import os

CANVAS = 300


def _tapered_line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (x, y)], fill=(0, 0, 0), width=w)
        prev = (x, y)


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=48, belly=None, w_belly=None):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if belly is not None and w_belly is not None:
            if u <= belly:
                w = w0 + (w_belly - w0) * (u / belly)
            else:
                w = w_belly + (w1 - w_belly) * ((u - belly) / (1 - belly))
        else:
            w = w0 + (w1 - w0) * u
        w = max(1, int(round(w)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
        prev = (bx, by)


def draw_tong(D):
    W = 4  # uniform thin width matching GT

    # ---------- 甬 top (龴): small pie + short heng ----------
    # Small 撇 leaning left
    _tapered_bezier(D, (205, 45), (192, 58), (178, 72), 2, W, steps=20)
    # Short horizontal tick to the right
    _tapered_line(D, (180, 78), (218, 76), W, W, steps=14)

    # ---------- 甬 body (用): inlined thin, sized to upper-right slot ----------
    # Frame roughly x=140..255, y=90..225 (compact for right-of-辶 slot)
    X_LEFT = 140
    X_RIGHT = 255
    Y_TOP = 90
    Y_BOT = 225
    X_MID = (X_LEFT + X_RIGHT) // 2  # 197

    # 1) 撇 — left side, near-vertical with slight tail scoop
    _tapered_bezier(D, (X_LEFT + 4, Y_TOP + 2),
                    (X_LEFT - 2, Y_TOP + (Y_BOT - Y_TOP) * 0.65),
                    (X_LEFT - 10, Y_BOT + 15),
                    W, 2, steps=40)

    # 2) 横折钩 — top heng + right shu + small hook
    _tapered_line(D, (X_LEFT + 4, Y_TOP), (X_RIGHT, Y_TOP), W, W, steps=24)
    _tapered_line(D, (X_RIGHT, Y_TOP), (X_RIGHT, Y_BOT), W, W, steps=30)
    # hook (short, leftward)
    _tapered_line(D, (X_RIGHT, Y_BOT), (X_RIGHT - 12, Y_BOT - 10), W, 2, steps=12)

    # 3) Interior heng 1 (upper)
    Y_H1 = Y_TOP + (Y_BOT - Y_TOP) // 3  # ~135
    _tapered_line(D, (X_LEFT + 4, Y_H1), (X_RIGHT - 2, Y_H1), W, W, steps=20)

    # 4) Interior heng 2 (lower)
    Y_H2 = Y_TOP + 2 * (Y_BOT - Y_TOP) // 3  # ~180
    _tapered_line(D, (X_LEFT + 4, Y_H2), (X_RIGHT - 2, Y_H2), W, W, steps=20)

    # 5) Central 竖 — from just under top, extends past bottom
    _tapered_line(D, (X_MID, Y_TOP + 4), (X_MID, Y_BOT + 20), W, W, steps=32)

    # ---------- 辶 envelope (left + bottom), inline thin ----------
    # Stroke 1: 点 at top-left of envelope area
    _tapered_bezier(D, (70, 90), (80, 103), (90, 116), 2, W, steps=18)

    # Stroke 2: 横折折撇 — zig-zag under the dot on the left
    A = (48, 152)
    B = (95, 147)
    C = (60, 188)
    D_pt = (92, 220)
    _tapered_line(D, A, B, W, W, steps=18)
    _tapered_bezier(D, B,
                    (B[0] + 4, (B[1] + C[1]) / 2 + 2),
                    C, W, W, steps=26)
    _tapered_bezier(D, C,
                    ((C[0] + D_pt[0]) / 2 - 4, (C[1] + D_pt[1]) / 2 - 3),
                    D_pt, W, 2, steps=26)

    # Stroke 3: 平捺 — long flat sweep across the bottom
    _tapered_bezier(D, (35, 245), (160, 275), (290, 240),
                    w0=W, w1=2, steps=80,
                    belly=0.55, w_belly=W + 2)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_tong(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_通.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
