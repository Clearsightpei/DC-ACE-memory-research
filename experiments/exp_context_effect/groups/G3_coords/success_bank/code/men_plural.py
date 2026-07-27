# p3_char_0156_们 — 们 (men), 5 strokes: 亻 (left) + 门 (right, 3 strokes).
# Composition: compressed ren_pang on left, men_char on right, both shifted
# and tall to fit character bounding box. GT shows 亻 taking ~35% width,
# 门 taking ~65% width, both tall (~180px height, centered vertically).
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from men_char import draw_men_char  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — smaller scale so pie stays on canvas, positioned in left ~35%.
    # ren_pang pie at scale 0.55 sweeps to about (-25 * 0.55) + ox_pie_shift.
    draw_ren_pang(d, ox=-45.0, oy=-5.0, scale=0.55)

    # 门 on right — men_char scaled 0.55 with big rightward ox so dian appears
    # in the top-middle of the right slot. men_char's dian is at ox-58*scale,
    # so with scale 0.55 and ox=50, dian lands at 50 + (-58*0.55) = ~18 (center-right).
    draw_men_char(d, ox=50.0, oy=0.0, scale=0.55)

    out = os.path.join(os.path.dirname(__file__), "01_们.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
