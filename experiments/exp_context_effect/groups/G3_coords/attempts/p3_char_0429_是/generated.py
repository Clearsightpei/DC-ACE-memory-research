# BANK_DEVIATION
# skipped: ri.py (draw_ri)
# reason: draw_ri's coords are hard-pixel and fill the canvas; 是 needs a
#   compressed 日 in the upper-center zone (~65px tall) — scale arg only
#   affects widths, not coords, so calling draw_ri gives full-size 日.
# fresh_component: ri_compressed_top_for_stack (small centered 日 for
#   top-bottom stacks like 是, 显 etc.)

# 是 (shì) — p3_char_0429_是
# Composition: 日 (top, small centered) + 疋 (bottom, 5 strokes).
# 疋 = 一 (long heng) + 丨 (short vertical) + 一 (short heng)
#     + 撇 (down-left sweep) + 捺 (down-right sweep).
# Total 9 strokes.

from PIL import Image, ImageDraw


def draw_shi(canvas):
    """是 — 9 strokes total (4 日 + 5 疋)."""

    # ---- Top: small compressed 日 (upper-center) ----
    x_left = 115
    x_right = 180
    y_top = 35
    y_bot = 105
    y_mid = 70
    w = 7
    w_mid = 6

    # Stroke 1: left 竖
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right)
    canvas.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横
    canvas.line([(x_left + 2, y_mid), (x_right - 3, y_mid)],
                fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横
    canvas.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)

    # ---- Bottom: 疋 ----
    # Stroke 5: long 一 spanning wide (top of 疋 zone)
    canvas.line([(35, 145), (265, 143)], fill=(0, 0, 0), width=8)

    # Stroke 6: short 丨 (vertical) sitting on the long heng, centered-ish
    canvas.line([(135, 145), (135, 190)], fill=(0, 0, 0), width=7)

    # Stroke 7: short 横 crossing the 丨
    canvas.line([(105, 188), (175, 188)], fill=(0, 0, 0), width=7)

    # Stroke 8: 撇 — sweeps down-left from the short heng area
    pie_pts = [
        (135, 190),
        (115, 220),
        (85, 255),
        (55, 285),
    ]
    for i in range(len(pie_pts) - 1):
        canvas.line([pie_pts[i], pie_pts[i + 1]], fill=(0, 0, 0), width=8)

    # Stroke 9: 捺 — sweeps down-right from mid to far right
    na_pts = [
        (155, 195),
        (185, 225),
        (220, 255),
        (265, 280),
    ]
    for i in range(len(na_pts) - 1):
        canvas.line([na_pts[i], na_pts[i + 1]], fill=(0, 0, 0), width=9)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shi(d)
    img.save("01_是.png")
