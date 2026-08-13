# p3_char_0409_油 — 油 (yóu), 8 strokes.
# Structure: L-R composition — 氵 (san_dian_shui) on left + 由 on right.
# 由 = rectangular frame + middle heng + central 竖 extending ABOVE the top.
#
# BANK_DEVIATION
# skipped: jia_first.py
# reason: 甲's central 竖 extends BELOW the box; 由's extends ABOVE the box. Mirror-shape mismatch — cannot uniform-scale.
# fresh_component: you_frame_up (rectangular frame with central 竖 extending upward through top)

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from san_dian_shui import draw_san_dian_shui  # noqa: E402

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_油.png")


def draw_you_frame(canvas, x_left, x_right, y_top, y_bot, y_extend_top):
    """由's right-side frame: box + middle heng + central 竖 extending UP.

    Modern stroke order (5 strokes): 竖(left) + 横折(top+right) +
    横(middle) + 竖(central, extends above box) + 横(bottom).
    """
    y_mid = (y_top + y_bot) // 2
    x_center = (x_left + x_right) // 2

    w = 8
    w_mid = 6
    w_vert = 8

    # Stroke: left 竖
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke: 横折 (top heng + right shu)
    canvas.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke: middle heng
    canvas.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=w_mid)
    # Stroke: bottom heng
    canvas.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke: central 竖 — extends from ABOVE top of box down to bottom
    canvas.line([(x_center, y_extend_top), (x_center, y_bot - 2)],
                fill=(0, 0, 0), width=w_vert)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 氵 on left. Bank primitive uses math coords (center 150,150 with +y up).
    # ox=-95 shifts it to left column, scale=0.85 to compress vertically.
    draw_san_dian_shui(d, ox=-95, oy=0, scale=0.85)

    # 由 on right, occupies ~x[130..250], y[95..240], with 竖 extending to y=55.
    draw_you_frame(d, x_left=130, x_right=250,
                   y_top=95, y_bot=240, y_extend_top=55)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
