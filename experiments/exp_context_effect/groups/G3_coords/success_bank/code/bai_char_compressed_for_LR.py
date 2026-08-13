# bai_char_compressed_for_LR.py — 白 variant (compressed, ~80px wide)
# Promoted from p3_char_0359_的 (B10 main PASS, BANK_DEVIATION).
# Curator B10 (2026-07-31, position 500).
#
# CONTEXT (v13 variant policy). The bank's `bai_char.py` is a full-canvas
# 白 (body 120px wide, x=95..215). For L-R chars where 白 occupies the
# LEFT slot (e.g. 的, 帕, 皎, 皖), that width overruns into the right
# component. This variant compresses the body to ~80px wide and shifts
# to the left third of the canvas — the exact recipe that PASSed for 的.
#
# The original `bai_char.py` remains untouched. Use this when 白 is
# LEFT-of a right component; use `bai_char.py` when 白 is standalone or
# top-stacked (see also `bai_char_for_top_stack.py` if promoted).

from PIL import Image, ImageDraw


def draw_bai_compressed(canvas, x_left=42, x_right=122,
                        y_top=92, y_bot=252):
    """Draw a compressed 白 (5 strokes) into a PIL ImageDraw canvas.

    Defaults are the exact values that PASSed for 的; override to
    slide/scale into other left-position slots.
    """
    y_mid = (y_top + y_bot) // 2
    w = 9
    w_mid = 7

    # Stroke 1: top 撇 (short pie, tail lands at top-left of body)
    pie_head_x = x_left + 46   # ≈ 88 in the reference frame
    pie_head_y = y_top - 27    # ≈ 65
    canvas.line([(pie_head_x, pie_head_y), (x_left + 6, y_top + 2)],
                fill=(0, 0, 0), width=7)

    # Stroke 2: left 竖
    canvas.line([(x_left, y_top), (x_left + 2, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 3: 横折 (top 横 + right 竖)
    canvas.line([(x_left, y_top), (x_right, y_top + 3)],
                fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 3), (x_right + 2, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横 (with small gap to right)
    canvas.line([(x_left + 4, y_mid), (x_right - 6, y_mid)],
                fill=(0, 0, 0), width=w_mid)

    # Stroke 5: bottom 横 (closes body)
    canvas.line([(x_left + 2, y_bot), (x_right + 2, y_bot + 2)],
                fill=(0, 0, 0), width=w)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_bai_compressed(d)
    img.save("01_bai_compressed.png")
