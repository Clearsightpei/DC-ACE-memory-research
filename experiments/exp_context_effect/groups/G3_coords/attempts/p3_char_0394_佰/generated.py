# p3_char_0394_佰 — 佰 (bǎi), 8 strokes: 亻 (left) + 百 (right).
# Composition (L-R):
#   - 亻 via bank ren_pang, compressed on the left (zhong_char pattern).
#   - 百 via bank bai_char_compressed_for_LR, shifted to the right half.
# Both are bank primitives; no BANK_DEVIATION.
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from bai_char_compressed_for_LR import draw_bai_compressed  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — zhong_char proven values (ox=-55, scale=0.85).
    draw_ren_pang(d, ox=-55.0, oy=0.0, scale=0.85)

    # 百 on right — compressed variant, wider box for balanced composition.
    draw_bai_compressed(d,
                        x_left=135, x_right=235,
                        y_top=95, y_bot=250)

    out = os.path.join(os.path.dirname(__file__), "01_佰.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
