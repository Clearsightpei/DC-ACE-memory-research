# p3_char_0089_义 — 义 (yì), 3 strokes: top small 点 (pie-like) + 撇 + 捺 X-crossing.
# GT is MMH thin-uniform style (P12); calligraphic widths are too fat.
# Recipe: variant_pie for all three strokes with thin widths (w_head 4-5, w_tail 2).
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie, variant_na  # noqa: E402


def render(path):
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # Stroke 1: top small mark — short diagonal 撇, upper-center of canvas.
    # GT position ~PIL(130, 90)→(150, 115): head math(+2, +75) to tail math(-22, +55).
    variant_pie(draw,
                head=(+5, +75),
                tail=(-22, +55),
                bow_perp=-2.5, w_head=4.5, w_tail=2.0, n=30)

    # Stroke 2: 撇 — large left-falling from upper-right to lower-left.
    # GT: starts near PIL(180, 105) descends to PIL(65, 265).
    # math: head (+30, +45) → tail (-85, -115).
    variant_pie(draw,
                head=(+30, +45),
                tail=(-85, -115),
                bow_perp=-6.0, w_head=5.0, w_tail=2.0, n=60)

    # Stroke 3: 捺 — large right-falling from upper-left to lower-right.
    # GT: starts near PIL(115, 115) descends to PIL(245, 260).
    # math: head (-35, +35) → tail (+95, -110). Thin uniform, gentle belly.
    variant_na(draw,
               head=(-35, +35),
               tail=(+95, -110),
               bow_perp=+5.0, w_head=2.0, w_belly=5.5, w_tail=2.5,
               belly_u=0.7, n=70)

    img.save(path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_义.png")
    render(out)
    print(f"wrote {out}")
