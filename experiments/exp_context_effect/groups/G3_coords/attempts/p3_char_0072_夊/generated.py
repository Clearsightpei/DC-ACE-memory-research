"""p3_char_0072_夊 — 3 strokes: small 撇 top, 横撇 middle, long 捺 crossing.

Shape (from GT):
  S1: small 撇 — from around (+5, +85) slanting down-left to (-12, +55).
  S2: 横撇 — short heng from about (-25, +42) to (+30, +40), then a
       pie bending down-left from (+30, +40) to (-55, +5).
  S3: long 捺 — sweeps from near the S2 heng-pie kink (~+10, +30)
       down-right to (+75, -70).
  The pie of S2 and the na of S3 cross ("X"), similar to X-crossing
  family, but here the X sits mid-canvas rather than at the top.
"""
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, tapered_line, to_px,
)


def draw_sui(draw):
    # S1: small top 撇 — thin, slanting down-left. Placed slightly right of center.
    variant_pie(
        draw,
        head=(+15, +95),
        tail=(-8, +55),
        bow_perp=-3.0,
        w_head=5.0,
        w_tail=1.5,
        n=32,
    )

    # S2: 横撇 — a short heng, then a long pie bending down-left.
    # 2a: short heng at the top of the middle-band, from mid-left rightward.
    tapered_line(
        draw,
        (-38, +32),
        (+22, +30),
        4.0,
        4.0,
        n=20,
    )
    # 2b: pie from end of heng, long sweep down-left to lower-left corner.
    variant_pie(
        draw,
        head=(+22, +30),
        tail=(-95, -95),
        bow_perp=-10.0,
        w_head=9.0,
        w_tail=1.5,
        n=64,
    )

    # S3: long 捺 crossing S2's pie roughly mid-shaft, sweeping down-right.
    # Head sits on S2's pie shaft (~mid); tail at lower-right corner.
    variant_na(
        draw,
        head=(-18, -12),
        tail=(+105, -95),
        bow_perp=+8.0,
        w_head=2.0,
        w_belly=14.0,
        w_tail=3.0,
        belly_u=0.75,
        n=72,
    )


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_sui(draw)
    out = os.path.join(_HERE, "01_夊.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
