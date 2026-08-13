# p3_char_0531_速 — 速 = 辶 envelope (left+bottom) + 束 (right/upper).
# 束 = 一 (top heng) + 口 (rectangle mid) + 丨 (vertical through) + 撇 + 捺.
# 辶 envelope pattern reused from guo_char.py (adapted, thin ~4px MMH-style).
# Inline PIL — no bank imports (guo template also inlines).

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


def draw_su(D):
    W = 4

    # ---------- 束 (right-upper component) ----------
    # 一 (top horizontal — spans across right side)
    heng_L = (135, 60)
    heng_R = (275, 58)
    _tapered_line(D, heng_L, heng_R, W, W + 1, 30)

    # 口 (small rectangle in the middle of 束) — compact
    kou_TL = (170, 95)
    kou_TR = (240, 95)
    kou_BL = (170, 150)
    kou_BR = (240, 150)
    # left 竖
    _tapered_line(D, kou_TL, kou_BL, W, W, 22)
    # top 横 (short — actually 口 top is a 横折; simplify as heng + right shu)
    _tapered_line(D, kou_TL, kou_TR, W, W, 22)
    # right 竖
    _tapered_line(D, kou_TR, kou_BR, W, W, 22)
    # bottom 横
    _tapered_line(D, kou_BL, kou_BR, W, W, 22)

    # 丨 (long vertical passing through top heng + 口 + down)
    shu_top = (205, 40)
    shu_bot = (205, 210)
    _tapered_line(D, shu_top, shu_bot, W, W, 40)

    # 撇 (from crossing area, sweeps down-left)
    pie_top = (200, 145)
    pie_ctrl = (170, 190)
    pie_end = (140, 235)
    _tapered_bezier(D, pie_top, pie_ctrl, pie_end, W + 1, 2, steps=32)

    # 捺 (from crossing area, sweeps down-right, ends with tail)
    na_top = (210, 145)
    na_ctrl = (245, 190)
    na_end = (282, 232)
    _tapered_bezier(D, na_top, na_ctrl, na_end, 2, W + 3, steps=32)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 1: 点 (small dot at top-left of envelope area)
    e_dot_start = (55, 85)
    e_dot_ctrl = (64, 98)
    e_dot_end = (73, 110)
    _tapered_bezier(D, e_dot_start, e_dot_ctrl, e_dot_end, 2, W + 2, steps=18)

    # Stroke 2: 横折折撇 — zigzag beneath the dot
    A = (35, 150)
    B = (80, 145)
    C = (45, 185)
    D_pt = (80, 215)
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

    # Stroke 3: 平捺 — long flat sweep across the bottom
    pna_p0 = (30, 245)
    pna_p1 = (155, 278)
    pna_p2 = (290, 240)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_su(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_速.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
