# p3_char_0291_这 — 7 strokes: 文 (dian + heng + pie + na) + 辶 (dian + 横折折撇 + 平捺)
# Adapted from guo_char.py (辶 + right component). Right component here is 文 (bank wen.py).
# Inline 辶 envelope (same recipe as guo_char). 文 called via bank wen.draw_wen, shifted into
# the top-right region that the envelope leaves open.

from PIL import Image, ImageDraw
import os, sys

CANVAS = 300

# Import bank wen
_BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(_BANK))
from wen import draw_wen  # noqa: E402


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


def draw_zhe(D):
    W = 4

    # ---------- 文 (top-right component) ----------
    # bank wen coords are centered at (150,150); shift to (200,130), scale 0.72
    # → 文 occupies roughly x=[142, 265], y=[62, 210], leaving envelope room.
    draw_wen(D, ox=50, oy=-20, scale=0.72)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 1: 点 (small dot at top-left of envelope area)
    e_dot_start = (75, 85)
    e_dot_ctrl = (84, 98)
    e_dot_end = (93, 110)
    _tapered_bezier(D, e_dot_start, e_dot_ctrl, e_dot_end, 2, W + 2, steps=18)

    # Stroke 2: 横折折撇 — small zigzag beneath the dot, on the left
    A = (50, 150)
    B = (95, 145)
    C = (60, 185)
    D_pt = (90, 215)
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
    pna_p0 = (40, 240)
    pna_p1 = (160, 272)
    pna_p2 = (290, 235)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_zhe(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_这.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
