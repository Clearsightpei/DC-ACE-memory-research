# p3_char_0305_还 (huán) — 7 strokes.
# Structure: 不 (top-right, 4 strokes: heng + pie + shu + dian)
#            + 辶 envelope (3 strokes: dian + 横折折撇 + 平捺) wrapping bottom-left.
# Adapted from guo_char.py (same 辶 envelope) and bu_char.py (不 recipe).
# Trust-GT: 不 is inline-rendered to fit the right-side box the envelope leaves.

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
            r = w / 2.0
            D.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
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
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_huan(D):
    W = 4

    # ---------- 不 (right-side / upper component) ----------
    # 横 (top horizontal) — spans roughly the right half of the canvas
    heng_L = (125, 105)
    heng_R = (275, 103)
    _tapered_line(D, heng_L, heng_R, W, W + 1, 30)

    # 丿 (pie) — starts near heng center, sweeps down-left
    pie_start = (200, 110)
    pie_ctrl = (170, 165)
    pie_end = (135, 215)
    _tapered_bezier(D, pie_start, pie_ctrl, pie_end, W + 2, 2, steps=32)

    # 丨 (shu) — short vertical dropping from heng center-right
    _tapered_line(D, (208, 115), (208, 215), W, W, 24)

    # 丶 (dian) — small dot on the right, below heng
    _tapered_bezier(D, (230, 145), (238, 160), (250, 178), 2, W + 2, steps=18)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 1: 点 (small dot at top-left of envelope area)
    _tapered_bezier(D, (60, 90), (68, 103), (77, 118), 2, W + 2, steps=18)

    # Stroke 2: 横折折撇 — small zigzag beneath the dot, on the left
    A = (40, 155)
    B = (85, 150)
    C = (50, 190)
    D_pt = (82, 222)
    _tapered_line(D, A, B, W, W + 1, 18)
    _tapered_bezier(D,
                    B,
                    (B[0] + 4, (B[1] + C[1]) / 2 + 2),
                    C,
                    W + 1, W + 1, steps=26)
    _tapered_bezier(D,
                    C,
                    ((C[0] + D_pt[0]) / 2 - 4, (C[1] + D_pt[1]) / 2 - 3),
                    D_pt,
                    W + 1, 2, steps=26)

    # Stroke 3: 平捺 — long flat sweep across the bottom, dips then rises
    pna_p0 = (35, 245)
    pna_p1 = (160, 275)  # belly control
    pna_p2 = (285, 240)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_huan(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_还.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
