# p3_char_0242_仲 — 仲 (zhòng), 6 strokes: 亻 (left) + 中 (right).
# Composition: compressed ren_pang on left (~35% width) + zhong on right
# (~65% width), both fit L-R in 300x300 canvas.
# Follows the men_plural.py recipe pattern (亻 + 门).
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from zhong import draw_zhong  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — larger scale so it fills left ~40% of canvas.
    draw_ren_pang(d, ox=-55.0, oy=0.0, scale=0.85)

    # 中 on right — zhong scaled up so it dominates the right ~60%.
    # zhong is centered on (0,0) internally; shift right + slightly bigger.
    draw_zhong(d, ox=50.0, oy=0.0, scale=0.75)

    out = os.path.join(os.path.dirname(__file__), "01_仲.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
