# p3_char_0310_伯 — 伯 (bó), 7 strokes: 亻 (left, 2) + 白 (right, 5).
# Rev2: bank ren_pang produced disconnected pie/shu at composed scales.
# Under v8 (trust GT + REJECT baked-in helper), inline both halves so
# the 亻 pie/shu actually kiss and the 白 top 撇 sits above the body.
# Thin uniform ink (P12): GT looks like ~4-6 px lines.
import os
from PIL import Image, ImageDraw


def draw_ren_pang_inline(canvas):
    """Tall 亻 on left: pie sweeps down-left, shu meets its mid-shaft."""
    # Pie: upper head around (95, 55), tail to lower-left (35, 220).
    pts = []
    x0, y0 = 95, 55
    x1, y1 = 35, 220
    # Slight bow left of chord.
    mx, my = (x0 + x1) / 2 - 8, (y0 + y1) / 2 + 5
    n = 40
    prev = None
    w_head, w_tail = 7, 3
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = int(round(w_head + (w_tail - w_head) * u))
        if prev is not None:
            canvas.line([prev, (bx, by)], fill=(0, 0, 0), width=max(1, w))
            r = w / 2
            canvas.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)

    # Shu: vertical from pie's mid-shaft down to bottom.
    # Pie midpoint approx (67, 137) — anchor shu top slightly below.
    canvas.line([(78, 120), (80, 265)], fill=(0, 0, 0), width=6)


def draw_bai_right(canvas):
    """Inline 白 on right half."""
    x_left = 145
    x_right = 258
    y_top = 100
    y_bot = 258
    y_mid = 180
    w = 6
    w_mid = 5

    # Stroke 1: 撇 (short top pie) — tail rests on top-left corner of body,
    # head above and to the right (short, near y_top - ~50).
    canvas.line([(180, 65), (x_left + 4, y_top + 3)],
                fill=(0, 0, 0), width=6)

    # Stroke 2: 竖 (left vertical)
    canvas.line([(x_left, y_top), (x_left + 2, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 3: 横折 (top 横 + right 竖)
    canvas.line([(x_left, y_top), (x_right, y_top + 3)],
                fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 3), (x_right + 1, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横
    canvas.line([(x_left + 3, y_mid), (x_right - 5, y_mid)],
                fill=(0, 0, 0), width=w_mid)

    # Stroke 5: bottom 横
    canvas.line([(x_left + 1, y_bot), (x_right + 1, y_bot + 1)],
                fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ren_pang_inline(d)
    draw_bai_right(d)
    out = os.path.join(os.path.dirname(__file__), "01_伯.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
