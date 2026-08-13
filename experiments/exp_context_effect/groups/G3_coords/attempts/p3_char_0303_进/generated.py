# p3_char_0303_进 — 7 strokes: 井 (right, 4 strokes) + 辶 envelope (dian + 横折折撇 + 平捺, 3 strokes)
# Template adapted from p3_char_0239_过 attempt (PASSed structure with 辶 envelope + right comp).
# Right component 井 = two horizontals + left 撇/vertical + right 竖.
# Inline PIL — no bank imports needed (v8: inline fresh when composition needs it).

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


def draw_jin(D):
    W = 4

    # ---------- 井 (right-side component, 4 strokes) ----------
    # Occupies right ~55% of canvas, above the 平捺 sweep.
    # Two horizontals (top slightly higher on right; bottom slightly higher on right),
    # left "vertical" is a 撇 leaning slightly to the lower-left,
    # right vertical is roughly straight.

    # Stroke 1: 横 (upper horizontal, slight up-tilt to the right)
    h1_L = (130, 100)
    h1_R = (270, 92)
    _tapered_line(D, h1_L, h1_R, W, W + 1, 30)

    # Stroke 2: 撇 (left "vertical" of 井, slight lean to lower-left, tapering)
    pie_top = (175, 65)
    pie_bot = (150, 225)
    _tapered_line(D, pie_top, pie_bot, W, max(2, W - 1), 34)

    # Stroke 3: 横 (lower horizontal, longer, slight up-tilt to the right)
    h2_L = (120, 175)
    h2_R = (285, 165)
    _tapered_line(D, h2_L, h2_R, W, W + 1, 34)

    # Stroke 4: 竖 (right vertical, straight)
    v_top = (235, 70)
    v_bot = (240, 230)
    _tapered_line(D, v_top, v_bot, W, W, 34)

    # ---------- 辶 envelope (left + bottom, 3 strokes) ----------
    # Stroke 5: 点 (small dot at top-left of envelope area)
    e_dot_start = (75, 85)
    e_dot_ctrl = (84, 98)
    e_dot_end = (93, 110)
    _tapered_bezier(D, e_dot_start, e_dot_ctrl, e_dot_end, 2, W + 2, steps=18)

    # Stroke 6: 横折折撇 — small zigzag beneath the dot, on the left
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

    # Stroke 7: 平捺 — long flat sweep across the bottom, dips then rises
    pna_p0 = (40, 240)
    pna_p1 = (160, 272)
    pna_p2 = (290, 235)
    _tapered_bezier(D, pna_p0, pna_p1, pna_p2,
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_jin(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_进.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
