# p3_char_0329_运 — 7 strokes: 云 (right, 4 strokes) + 辶 envelope (left+bottom, 3 strokes)
# 云 = 二 (2 hengs stacked) + 厶 (撇折 + 点)
# 辶 = 点 (top-left) + 横折折撇 (zigzag) + 平捺 (bottom sweep)
# Adapted from guo_char.py (辶 + 寸) — replaced 寸 with 云.

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


def draw_yun(D):
    W = 4

    # ---------- 云 (right-side component) ----------
    # 横1 (short top horizontal)
    h1_L = (160, 90)
    h1_R = (235, 88)
    _tapered_line(D, h1_L, h1_R, W, W + 1, 22)

    # 横2 (longer horizontal below)
    h2_L = (140, 130)
    h2_R = (265, 128)
    _tapered_line(D, h2_L, h2_R, W, W + 1, 30)

    # 撇折 — starts as pie (down-left) then folds to horizontal (right)
    # part a: pie from upper-right down-left
    pz_start = (200, 145)
    pz_mid = (175, 175)     # elbow
    pz_end = (260, 195)     # horizontal fold end
    # descending pie stroke
    _tapered_line(D, pz_start, pz_mid, W, W + 1, 20)
    # horizontal fold stroke going right
    _tapered_line(D, pz_mid, pz_end, W + 1, W, 26)

    # 点 (small dot at bottom, closing 厶)
    dot_start = (225, 165)
    dot_ctrl = (232, 178)
    dot_end = (245, 195)
    _tapered_bezier(D, dot_start, dot_ctrl, dot_end, 2, W + 2, steps=18)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 1: 点 (small dot at top-left of envelope area)
    e_dot_start = (72, 100)
    e_dot_ctrl = (82, 115)
    e_dot_end = (92, 130)
    _tapered_bezier(D, e_dot_start, e_dot_ctrl, e_dot_end, 2, W + 2, steps=18)

    # Stroke 2: 横折折撇 — zigzag beneath the dot, on the left
    A = (50, 170)
    B = (100, 165)
    C = (62, 205)
    D_pt = (95, 235)
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
    pna_p0 = (40, 250)
    pna_p1 = (160, 280)  # belly control
    pna_p2 = (290, 245)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_yun(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_运.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
