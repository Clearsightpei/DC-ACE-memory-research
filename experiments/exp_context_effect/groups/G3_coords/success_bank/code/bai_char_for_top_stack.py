# bai_char_for_top_stack.py — 白 variant (compact, top-half)
# Promoted from p3_char_0356_皃 (B10 main PASS, BANK_DEVIATION).
# Curator B10 (2026-07-31, position 500).
#
# CONTEXT (v13 variant policy). The bank's `bai_char.py` fills the full
# canvas vertically (body ~ y=95..265). For top-of-stack compositions
# (皃, 貌, 皂, 皇), 白 must occupy only the TOP half of the canvas so
# a bottom radical (儿, 十, etc.) fits below. This variant sits in
# y≈62..155 with a slightly compact width — the exact recipe that
# PASSed for 皃 (see attempts/p3_char_0356_皃 for the compound).
#
# The original `bai_char.py` remains untouched. Use this when 白 sits
# ATOP a lower radical; use `bai_char_compressed_for_LR.py` when 白 is
# LEFT of a right component; use `bai_char.py` for standalone.

from PIL import Image, ImageDraw


def draw_bai_top(canvas, x_left=112, x_right=198,
                 y_top=62, y_bot=155):
    """Draw a top-stack 白 (5 strokes) into a PIL ImageDraw canvas."""
    y_mid = (y_top + y_bot) // 2
    w = 6
    w_mid = 5

    # Stroke 1: 短撇 (short pie above the body, tail dropping into top-left)
    canvas.line([(162, y_top - 24), (x_left + 4, y_top + 2)],
                fill=(0, 0, 0), width=5)

    # Stroke 2: 竖 (left vertical)
    canvas.line([(x_left, y_top), (x_left + 1, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 3: 横折 (top 横 + right 竖)
    canvas.line([(x_left, y_top), (x_right, y_top + 3)],
                fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 3), (x_right + 1, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横
    canvas.line([(x_left + 3, y_mid), (x_right - 4, y_mid)],
                fill=(0, 0, 0), width=w_mid)

    # Stroke 5: bottom 横 (closes body)
    canvas.line([(x_left + 1, y_bot), (x_right + 2, y_bot + 1)],
                fill=(0, 0, 0), width=w)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_bai_top(d)
    img.save("01_bai_top.png")
