# BANK_DEVIATION
# skipped: (no 车 or 专 primitive in bank)
# reason: 车 and 专 are novel components; no bank entry fits directly.
# fresh_component: che_left_for_LR, zhuan_right_for_LR
#
# 转 = 车 (left, 4 strokes) + 专 (right, 4 strokes) — L-R composition.
# Inline PIL, thin uniform widths (P12 / drawer_memory L-R scale).
# Coords in PIL pixel space, canvas 300x300, following bie_char.py template.

from PIL import Image, ImageDraw
import os

CANVAS = 300


def _line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _bezier(D, p0, p1, p2, w0, w1, steps=48):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_zhuan(D):
    W = 5

    # ============================================================
    # LEFT COMPONENT: 车 (~x 30..145)
    # ============================================================
    # Stroke 1: top 横 — short horizontal near top
    _line(D, (55, 78), (128, 72), W, W, 22)

    # Stroke 2: 撇折 — short slanted 撇 down-left from top-right area, then折 horizontal
    # slant from around (75, 82) down-left to (48, 130), then horizontal turn right to (135, 128)
    _line(D, (75, 82), (48, 130), W, W, 20)
    _line(D, (48, 130), (135, 128), W, W, 24)

    # Stroke 3: middle 横 — long crossing horizontal
    _line(D, (28, 168), (148, 162), W, W, 28)

    # Stroke 4: 竖 — vertical from top 横 down through, extending below character
    _line(D, (93, 72), (91, 258), W, W, 40)

    # ============================================================
    # RIGHT COMPONENT: 专 (~x 160..275)
    # ============================================================
    # Stroke 1: top 横 — short horizontal
    _line(D, (172, 80), (258, 72), W, W, 24)

    # Stroke 2: middle 横 — slightly longer
    _line(D, (168, 130), (270, 122), W, W, 28)

    # Stroke 3: 竖折折钩 — vertical from top 横 down, then zigzag ending with hook
    # short vertical from top down to just above middle
    _line(D, (200, 80), (200, 128), W, W, 18)
    # continues past middle 横: down to bottom-left area
    _line(D, (200, 132), (195, 205), W, W, 22)
    # 折 horizontal right at bottom
    _line(D, (195, 205), (258, 200), W, W, 22)
    # 折 curving down-left
    _bezier(D, (258, 200), (248, 232), (210, 258), W, W, steps=32)
    # 钩 up-left flick
    _line(D, (210, 258), (194, 245), W, max(1, W - 2), 12)

    # Stroke 4: 点 (small dot) upper-right corner of 专
    _bezier(D, (255, 60), (263, 72), (270, 88), W - 1, W + 1, steps=16)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_zhuan(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_转.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
