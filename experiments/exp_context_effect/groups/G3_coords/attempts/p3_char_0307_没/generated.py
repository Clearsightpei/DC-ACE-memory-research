# p3_char_0307_没 (mò) — 7 strokes.
# Structure: L-R.
#   Left 氵 (san_dian_shui, 3 strokes: dian + dian + ti).
#   Right 殳 (4 strokes):
#     s1: short 撇 top-left of right column.
#     s2: 横折弯 — flat top, turns down-right into a soft curve (几-like top).
#     s3: 横撇 (top of 又) crossing shaft in mid-right.
#     s4: 捺 (bottom-right 又 leg), sweeping down-right to a wide tail.
# Inline PIL rendering per B7 v9 "trust GT" posture. Widths kept thin
# (~3-4 px) to match GT's uniform thin ink.

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


def draw_mo(D):
    W = 4

    # ---------- 氵 (left) — 3 water drops ----------
    # dian 1 (top)
    _tapered_bezier(D, (55, 85), (63, 95), (73, 108), 2, W + 1, steps=18)
    # dian 2 (mid, slightly left of dian 1)
    _tapered_bezier(D, (35, 128), (48, 138), (62, 150), 2, W + 1, steps=18)
    # ti (bottom, rising to the right)
    _tapered_line(D, (40, 200), (78, 178), W + 2, 2, 24)

    # ---------- 殳 (right) — 4 strokes ----------
    # s1: short 撇 at top-left of right column (small diagonal down-left)
    _tapered_bezier(D, (152, 68), (146, 82), (135, 100), W - 1, 2, steps=20)

    # s2: 横折弯 — flat top, turns down, softly curves right (几-like top).
    # Top horizontal (narrower)
    _tapered_line(D, (155, 82), (238, 80), W, W, 24)
    # Down curve (short shu that leans in)
    _tapered_line(D, (238, 82), (232, 130), W, W, 20)
    # Soft curve (弯 kick to the right)
    _tapered_bezier(D, (232, 130), (232, 148), (260, 150), W, W - 1, steps=20)

    # s3: 横撇 (top of 又) — short horizontal + long 撇 sweeping down-left.
    # horizontal top of 又
    _tapered_line(D, (150, 180), (238, 178), W, W + 1, 22)
    # 撇 down-left from right end, crossing to lower-left
    _tapered_bezier(D, (238, 180), (200, 220), (140, 268), W + 1, 2, steps=30)

    # s4: 捺 (right leg of 又) — starts on 撇 shaft, sweeps down-right (X-cross).
    _tapered_bezier(D, (170, 200), (222, 235), (275, 265),
                    w0=2, w1=2, steps=48,
                    belly=0.65, w_belly=W + 3)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_mo(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_没.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
