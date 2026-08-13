# BANK_DEVIATION
# skipped: zhe_char.py
# reason: zhe_char.py is baked for full-canvas 者 (x ~ 35..255); 都 needs 者
#   compressed into left ~60% column so 阝 fits on the right.
# fresh_component: zhe_left_for_LR (compressed 耂+日 for L-R left slot)
#
# 都 (dū) — L-R composition: 者 (left, ~60%) + 阝 (right ear, ~40%).
# Right 阝 recipe adapted (with shift/scale) from prior 那 attempt at
# p3_char_0233_那/generated.py.

from PIL import Image, ImageDraw

CANVAS = 300


def _tapered_line(draw, p0, p1, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _cubic_taper(draw, p0, p1, c1, c2, w0, w1, steps=140):
    for i in range(steps + 1):
        u = i / steps
        omu = 1 - u
        bx = (omu ** 3 * p0[0] + 3 * omu ** 2 * u * c1[0]
              + 3 * omu * u ** 2 * c2[0] + u ** 3 * p1[0])
        by = (omu ** 3 * p0[1] + 3 * omu ** 2 * u * c1[1]
              + 3 * omu * u ** 2 * c2[1] + u ** 3 * p1[1])
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_zhe_left(canvas):
    """者 compressed to left ~60% of canvas (x ~ 15..180)."""
    # ---- Top: 耂 ----
    # S1 short top 横
    canvas.line([(50, 55), (140, 55)], fill=(0, 0, 0), width=7)

    # S2 short 竖 crossing above the long heng
    canvas.line([(95, 25), (95, 90)], fill=(0, 0, 0), width=7)

    # S3 long 横 (spans wide across the left slot)
    canvas.line([(15, 120), (185, 120)], fill=(0, 0, 0), width=8)

    # S4 long sweeping 撇 (from upper-right of top, sweeps down-left)
    pie_pts = [
        (140, 50),
        (120, 100),
        (90, 155),
        (55, 215),
        (25, 265),
    ]
    for i in range(len(pie_pts) - 1):
        canvas.line([pie_pts[i], pie_pts[i + 1]], fill=(0, 0, 0), width=7)

    # ---- Bottom: 日 (shifted right to sit inside the pie's crook) ----
    x_left = 85
    x_right = 175
    y_top = 165
    y_bot = 265
    y_mid = 215
    w = 7
    w_mid = 6

    # S5 left 竖
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # S6 横折 (top + right)
    canvas.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # S7 middle 横
    canvas.line([(x_left + 2, y_mid), (x_right - 4, y_mid)],
                fill=(0, 0, 0), width=w_mid)
    # S8 bottom 横
    canvas.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


def draw_right_ear(draw):
    """阝 right-ear — adapted from p3_char_0233_那 (shifted to right side)."""
    # Top hump — upper-left start, sweep right & down to waist
    p0 = (210, 70)
    p1 = (240, 130)
    c1 = (285, 65)
    c2 = (290, 120)
    _cubic_taper(draw, p0, p1, c1, c2, 7.0, 8.0, steps=120)

    # Bottom hump + tail down to shu top
    p0 = (240, 130)
    p1 = (225, 180)
    c1 = (285, 155)
    c2 = (275, 190)
    _cubic_taper(draw, p0, p1, c1, c2, 8.0, 4.0, steps=120)

    # Long 竖 descender for the ear
    top = (220, 130)
    bot = (220, 290)
    _tapered_line(draw, top, bot, 9.0, 9.0, steps=120)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_zhe_left(d)
    draw_right_ear(d)
    out = ("/Users/peilinwu/Documents/AI memory research/experiments/"
           "exp_context_effect/groups/G3_coords/attempts/"
           "p3_char_0503_都/01_都.png")
    img.save(out)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
