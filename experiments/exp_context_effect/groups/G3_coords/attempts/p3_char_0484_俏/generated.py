# p3_char_0484_俏 — 俏 (qiào), L-R composition: 亻 (left) + 肖 (right).
# 肖 decomposes as top 3-stroke crown (⺌-like: short pie, center tick,
# right short slant) + 月 below.
#
# Composition strategy: bank ren_pang (compressed) for 亻;
# inline top-3-stroke crown for 肖-top (no bank entry fits — 小 has a
# hook and different aspect); bank yue for 月.
#
# COORD CONVENTIONS:
#   ren_pang, variant_pie, tapered_line: MATH coords (center origin, +y up).
#   yue: PIL pixel OFFSETS from canvas center (150, 150), +y down.
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from yue import draw_yue  # noqa: E402
from _shared_helpers import variant_pie, tapered_line  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left (math coords). Shift left, scale 0.65 keeps sweep tall.
    draw_ren_pang(d, ox=-58.0, oy=8.0, scale=0.65)

    # 肖-top three-stroke crown, upper right in math coords.
    # Math y +95 = top area, math y +50 = crown baseline. Math x from
    # +10 (left) to +90 (right) sits in the right slot.
    # (1) left short 撇 — head upper, tail lower-left, thin
    variant_pie(d,
                head=(35.0, 95.0), tail=(10.0, 50.0),
                bow_perp=-3.0, w_head=7.0, w_tail=1.0)
    # (2) center short vertical tick
    tapered_line(d, (55.0, 95.0), (55.0, 50.0),
                 w0=5.0, w1=7.0, n=20)
    # (3) right short slant (pie-like, inward down-left)
    variant_pie(d,
                head=(88.0, 95.0), tail=(70.0, 50.0),
                bow_perp=2.5, w_head=6.0, w_tail=1.0)

    # 月 on lower-right — draw_yue takes PIL px offsets from (150,150).
    # Shift right (+55) and down (+35), scale 0.62 to fill right slot.
    draw_yue(d, ox=55.0, oy=35.0, scale=0.62)

    out = os.path.join(os.path.dirname(__file__), "01_俏.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
