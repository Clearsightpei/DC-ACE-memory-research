# p3_char_0527_造 — 10 strokes: 辶 envelope (3) + 告 upper-right (7)
# 告 = 牛-top (丿 + 一 + 丨 + 一) + 口 at bottom (竖 + 横折 + 一)
# 辶 envelope adapted from guo_char.py (过).
# Right component (告) drawn inline; no bank primitive for 告 yet.

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


def draw_zao(D):
    W = 4

    # ---------- 告 (upper-right component: 牛-top + 口) ----------
    # Stroke 1: 丿 (small pie at very top)
    pie_start = (205, 50)
    pie_ctrl = (198, 60)
    pie_end = (188, 78)
    _tapered_bezier(D, pie_start, pie_ctrl, pie_end, W + 1, 2, steps=22)

    # Stroke 2: 一 (top short heng)
    top_heng_L = (175, 82)
    top_heng_R = (250, 80)
    _tapered_line(D, top_heng_L, top_heng_R, W, W + 1, 26)

    # Stroke 3: 丨 (vertical descending, crosses through)
    shu_top = (213, 68)
    shu_bot = (213, 148)
    _tapered_line(D, shu_top, shu_bot, W, W, 28)

    # Stroke 4: 一 (middle longer heng — top of 口 area? No, this is the wider 土 heng)
    mid_heng_L = (148, 128)
    mid_heng_R = (275, 126)
    _tapered_line(D, mid_heng_L, mid_heng_R, W, W + 1, 32)

    # ---------- 口 (small square at bottom of 告) ----------
    # Compact: tucked under the mid-heng, roughly square, moderate size
    ko_L = 175
    ko_R = 248
    ko_T = 152
    ko_B = 202

    # Stroke 5: 竖 (left vertical of 口)
    _tapered_line(D, (ko_L, ko_T), (ko_L, ko_B), W, W, 18)

    # Stroke 6: 横折 (top horizontal + right vertical)
    _tapered_line(D, (ko_L - 1, ko_T), (ko_R, ko_T), W, W, 24)
    _tapered_line(D, (ko_R, ko_T), (ko_R, ko_B), W, W, 18)

    # Stroke 7: 一 (bottom horizontal of 口)
    _tapered_line(D, (ko_L - 1, ko_B), (ko_R + 1, ko_B), W, W, 24)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 8: 点 (small dot at top-left of envelope)
    e_dot_start = (72, 82)
    e_dot_ctrl = (82, 96)
    e_dot_end = (92, 110)
    _tapered_bezier(D, e_dot_start, e_dot_ctrl, e_dot_end, 2, W + 2, steps=18)

    # Stroke 9: 横折折撇 — zigzag beneath the dot, on the left
    A = (48, 148)
    B = (98, 143)
    C = (60, 185)
    D_pt = (92, 218)
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

    # Stroke 10: 平捺 — long flat sweep across the bottom
    pna_p0 = (38, 242)
    pna_p1 = (158, 274)
    pna_p2 = (290, 236)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_zao(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_造.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
