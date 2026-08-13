# zhe_char.py — 者 — promoted from p3_char_0373_者 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# 者 (zhě) — p3_char_0373_者
# Composition: 耂 (top) + 日 (bottom, right-shifted).
# Bank primitives lao_radical.py and ri.py exist, but 者 requires:
#   - 耂 sweep (撇) that extends BELOW center, wrapping down-left past
#     where 日 sits (the pie must clear the 日 body).
#   - 日 shifted right so pie's tail can sweep past its left edge.
# lao_radical/ri were tuned as standalone radicals filling the canvas;
# using them raw wouldn't compose. Inlining fresh with PIL, adapting
# the bank's geometry vocabulary (widths, straight-line strokes).

from PIL import Image, ImageDraw


def draw_zhe(canvas):
    """者 — 8 strokes total (4 耂 + 4 日)."""

    # ---- Top: 耂 ----
    # Stroke 1: short top 横 (upper cross-bar)
    canvas.line([(95, 60), (200, 60)], fill=(0, 0, 0), width=8)

    # Stroke 2: short 竖 (crossing above the long heng, sits above top-heng)
    canvas.line([(145, 30), (145, 95)], fill=(0, 0, 0), width=8)

    # Stroke 3: long 横 (spans wide, middle of upper zone)
    canvas.line([(35, 130), (255, 128)], fill=(0, 0, 0), width=9)

    # Stroke 4: long sweeping 撇 (from upper-right area down to lower-left,
    # curves past 日's left edge). Draw as a smooth 3-segment polyline
    # approximating the calligraphic sweep.
    pie_pts = [
        (195, 55),
        (175, 100),
        (140, 155),
        (95, 220),
        (55, 275),
    ]
    for i in range(len(pie_pts) - 1):
        canvas.line([pie_pts[i], pie_pts[i + 1]], fill=(0, 0, 0), width=8)

    # ---- Bottom: 日 (shifted right so pie tail clears its left edge) ----
    x_left = 130
    x_right = 220
    y_top = 175
    y_bot = 275
    y_mid = 225
    w = 8
    w_mid = 7

    # Stroke 5: left 竖
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 6: 横折 (top + right)
    canvas.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 7: middle 横 (with small right gap)
    canvas.line([(x_left + 2, y_mid), (x_right - 4, y_mid)],
                fill=(0, 0, 0), width=w_mid)
    # Stroke 8: bottom 横
    canvas.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zhe(d)
    img.save("01_者.png")
