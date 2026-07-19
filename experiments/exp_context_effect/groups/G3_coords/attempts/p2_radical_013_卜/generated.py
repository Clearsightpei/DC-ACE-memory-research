# p2_radical_013_卜 — 2 strokes: 竖 (left) + 点 (right)
# GT reading (math coords, center origin, +y up):
#   竖: vertical on left side, canvas x ~130 -> ox ~= -20; runs from
#       ~y_top=+65 (px 85) down to ~y_bot=-125 (px 275). Center ≈ (-20, -30),
#       half_len ≈ 95 → scale ≈ 0.95. Slight lean but treat as straight shu.
#   点: mid-canvas (~150, 155) curving to lower-right (~210, 200).
#       Dian primitive maps (-15,+25)→(+18,-20) with scale 1 = 33 px wide.
#       Target width ≈ 60 px → scale ≈ 1.4; but dian's shape is a
#       down-right dot which matches this radical form. Center of the
#       dian bounding box in canvas coords ≈ (180, 178) →
#       math (ox=+30, oy=-28). Use scale 1.3.
# TR1: deliberate placement. TR3: origin = center-of-mass offset.
# TR6: transforms recorded above.
# TR7 sanity:
#   竖 top pixel: cx+ox=150-20=130, cy-(oy+half_len*scale)=150-(-30+95)=85 ✓
#   竖 bot pixel: 130, 150-(-30-95)=275 ✓ (within 300 canvas w/ ~25px margin)
#   dian head math: ox+(-15*1.3)=30-19.5=+10.5, oy+(25*1.3)=-28+32.5=+4.5
#     → PIL (160, 145)
#   dian tail math: ox+(18*1.3)=30+23.4=+53.4, oy+(-20*1.3)=-28-26=-54
#     → PIL (203, 204)
#   Dian sits to the RIGHT of the 竖 shaft (shaft at x=130, dian starts x=160) ✓

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from shu import draw_shu   # noqa: E402
from dian import draw_dian  # noqa: E402

CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # REVISION 1: GT's dot is thinner and longer (arc-like), not a heavy
    # teardrop. Reduce dian scale to 1.1 (less bulge at tail) and shift
    # right slightly. Keep 竖 as-is (position matched GT well).
    # 竖 (left-side vertical): shift left, slightly down, scale 0.95
    draw_shu(d, ox=-20, oy=-30, scale=0.95)

    # 点 (right side): scale 1.1, positioned to start near shaft midpoint
    # and curve to lower-right. Center at (ox=+30, oy=-25).
    draw_dian(d, ox=+30, oy=-25, scale=1.1)

    out = os.path.join(HERE, "01_卜.png")
    img.save(out)
    print(out)


if __name__ == "__main__":
    main()
