# 边 (biān) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0188_边/generated.py
# Note: 5 (walk-radical + inline right; PIL)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

# p3_char_0188_边 — 5 strokes: 力 (横折钩 + 撇) top-right, 辶 envelope (dian + 横折折撇 + 平捺)
# Inline PIL. 力 body borrowed in spirit from ban_char.py, offset up-right.
# 辶 envelope adapted from zou_zhi.py, sitting to the left / bottom.

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


def draw_bian(D):
    W = 4

    # ---------- 力 (right-side component) ----------
    # 横折钩: horizontal top, then down-right corner, then vertical shaft, tiny hook
    hzg_start  = (150,  85)
    hzg_corner = (225,  78)
    hzg_bot    = (218, 195)
    _tapered_line(D, hzg_start, hzg_corner, W, W + 1, 24)
    _tapered_line(D, hzg_corner, hzg_bot,   W + 1, W, 32)
    hook_end   = (200, 185)
    _tapered_line(D, hzg_bot, hook_end, W, max(1, W - 2), 12)

    # 撇: crosses the 横 near its left, sweeps down-left
    pie_start = (170,  62)
    pie_ctrl  = (150, 150)
    pie_end   = (130, 230)
    _tapered_bezier(D, pie_start, pie_ctrl, pie_end, W + 1, 1, steps=60)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 1: 点 (small dot at top-left of envelope area)
    dot_start = (90,  95)
    dot_ctrl  = (99, 108)
    dot_end   = (108, 120)
    _tapered_bezier(D, dot_start, dot_ctrl, dot_end, 2, W + 2, steps=18)

    # Stroke 2: 横折折撇 — small zigzag beneath the dot, on the left
    A = (60, 155)
    B = (105, 150)
    C = (70, 190)
    D_pt = (100, 220)
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
    pna_p0 = (50, 245)
    pna_p1 = (165, 275)  # belly control
    pna_p2 = (290, 240)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_bian(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_边.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
