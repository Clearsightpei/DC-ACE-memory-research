# BANK_DEVIATION
# skipped: zou_zhi.py (bank 辶) and er_ren.py (bank 儿)
# reason: 选 needs a slim/thin uniform-ink envelope in guo_char-style, and 儿
#         must sit UNDER the 土-top of 先 (top-right composition), not as a
#         standalone character; bank 儿 and heavy zou_zhi don't fit.
# fresh_component: xian_top_right (先 inline: short pie + short heng + shu +
#         longer heng + pie + shu-wan-gou); zou_zhi envelope inlined
#         guo_char-style
#
# p3_char_0465_选 — 9 strokes: 先 top-right (丿 一 丨 一 丿 乚) + 辶 envelope
# (dian + 横折折撇 + 平捺). Adapts guo_char.py's inline 辶 template; right
# component 先 rendered fresh.

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


def draw_xuan(D):
    W = 4

    # ---------- 先 (top-right component) ----------
    # Stroke 1: 短撇 (short 丿 at top-left of 先, small slanting stroke)
    _tapered_line(D, (150, 55), (135, 80), W, max(1, W - 1), 14)

    # Stroke 2: 短横 (short 一 across mid-top, meeting the pie's foot)
    _tapered_line(D, (135, 82), (215, 82), W, W + 1, 20)

    # Stroke 3: 竖 (丨 vertical through the top heng, going down to near
    # the mid-line of 先; this is the vertical of the "土-like" top)
    _tapered_line(D, (175, 62), (175, 145), W, W, 24)

    # Stroke 4: 长横 (long 一 across, below the shu, top of the 儿-half)
    _tapered_line(D, (128, 145), (250, 143), W, W + 1, 28)

    # Stroke 5: 撇 (丿 left leg of 儿, curved down-left)
    _tapered_bezier(D,
                    (170, 150),
                    (150, 195),
                    (128, 235),
                    W + 1, 2, steps=32)

    # Stroke 6: 竖弯钩 (乚 right leg — down, curve right, hook up)
    # segment A: vertical down
    _tapered_line(D, (200, 150), (203, 205), W, W, 22)
    # segment B: curved bottom sweep right
    _tapered_bezier(D,
                    (203, 205),
                    (215, 235),
                    (260, 232),
                    W, W, steps=26)
    # segment C: small hook up
    _tapered_line(D, (260, 232), (258, 215), W, max(1, W - 2), 10)

    # ---------- 辶 envelope (left + bottom wrap) ----------
    # Stroke 7: 点 (small dot at top-left of envelope area)
    _tapered_bezier(D, (60, 100), (68, 113), (77, 126),
                    2, W + 2, steps=18)

    # Stroke 8: 横折折撇 — zigzag under the dot, on the left
    A = (38, 165)
    B = (82, 160)
    C = (48, 200)
    D_pt = (78, 230)
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

    # Stroke 9: 平捺 — long flat sweep across the bottom, dips then rises
    _tapered_bezier(D, (32, 250), (155, 282), (290, 240),
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_xuan(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_选.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
