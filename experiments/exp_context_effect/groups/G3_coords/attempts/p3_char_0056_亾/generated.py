# 亾 — variant of 亡. Composition per GT:
#   1) left vertical (shu) descending on the left half
#   2) 人-like pie + na tucked to the right (small)
#   3) bottom horizontal spanning most of the width
# Uses bank primitives draw_shu, draw_pie, draw_na, draw_heng.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from shu import draw_shu       # noqa: E402
from pie import draw_pie       # noqa: E402
from na import draw_na         # noqa: E402
from heng import draw_heng     # noqa: E402

CANVAS = 300
OUT = Path(__file__).with_name("01_亾.png")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # 1) Left vertical — on the left, descends to meet bottom horizontal
    #    forming an L. Length ~170 px (scale 0.85), center slightly high.
    draw_shu(d, ox=-75, oy=5, scale=0.85)

    # 2) 人 in the upper-right region: pie apex near top-center,
    #    both strokes descend to meet the bottom horizontal.
    #    Canonical pie: head (+65,+90) tail (-45,-85); with scale=0.6
    #    head ~ (+39,+54) tail ~ (-27,-51). Offset so tail lands near
    #    bottom horizontal (y≈-75) and head near top (y≈+60).
    draw_pie(d, ox=15, oy=5, scale=0.6)
    # Canonical na: head (-70,+80) tail (+80,-90); with scale=0.55
    # head ~ (-38.5,+44) tail ~ (+44,-49.5). Offset so head meets pie apex
    # at approx (+15+39, +5+54) = (+54, +59), i.e. shift na ox=+92, oy=+15.
    draw_na(d, ox=92, oy=15, scale=0.55)

    # 3) Bottom horizontal — spans width, at y≈-75.
    draw_heng(d, ox=0, oy=-75, scale=1.15)

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
