# p3_char_0102_天 — 4 strokes: top 一 (shorter) + mid 一 (wider) + 撇 + 捺.
# GT is MMH-thin-uniform style (per P12: w_head ~4, w_tail ~2).
# Compose using variant_pie / variant_na / tapered_line from _shared_helpers.
# 大-family crossing at midpoint (u_pie=0.5) per kiss_apex convention;
# for 天 the two legs originate near the middle of the second heng.

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_HELPERS = os.path.join(_HERE, "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(_HELPERS))

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, tapered_line, to_px,
)


def draw_tian(draw, ox=0, oy=0, scale=1.0):
    # Top heng — shorter than second, sits high, mildly tilted up-right.
    tapered_line(draw,
                 (-55 + ox, 78 + oy),
                 (55 + ox, 82 + oy),
                 3.5, 3.5, n=30)

    # Second heng — a bit wider than the top heng, mid-height.
    tapered_line(draw,
                 (-80 + ox, 18 + oy),
                 (85 + ox, 22 + oy),
                 3.5, 3.5, n=30)

    # 撇 leg — starts just above the second heng near center,
    # curves down-left past the heng.
    variant_pie(draw,
                head=(-2 + ox, 32 + oy),
                tail=(-85 + ox, -115 + oy),
                bow_perp=-8.0, w_head=4.5, w_tail=2.0, n=48)

    # 捺 leg — mirror crossing partner, starts near same apex,
    # sweeps down-right with belly.
    variant_na(draw,
               head=(0 + ox, 32 + oy),
               tail=(95 + ox, -115 + oy),
               bow_perp=+7.0, w_head=2.0, w_belly=5.5, w_tail=2.5,
               belly_u=0.7, n=60)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_tian(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_天.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
