# p3_char_0070_夂 (zhǐ) — 3 strokes:
#   1) short 撇 (top-left, going down-right → short pie head)
#   2) 横撇 (heng turning into pie, short heng on top then down-left pie)
#   3) long 捺 crossing pie at apex (X-family, apex on the pie shaft)
#
# From errata: prior FAIL diagnosed "apex geometry lost" (both dixis
# not sharing a pixel). Fix: use kiss_apex to weld 横撇's pie tail with
# 捺's head so they share the exact apex pixel.
#
# Reads form_catalog X-crossing recipe as base. 夂 differs from 乂:
# top is a heng-pie not a plain pie, and a small top pie sits above.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(_BANK))

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, tapered_bezier, tapered_line,
    kiss_apex, to_px,
)

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # ---- Stroke 2 first: 横撇 (define apex geometry) ----
    # Short heng on top from ~(-45,+45) to (+30,+45), then pie going down-left
    # from (+30,+45) to (-55,-40). The pie tail is (approximately) the apex
    # where 捺 crosses.
    heng_head = (-40.0, 55.0)
    heng_tail = (35.0, 55.0)
    pie_head = (35.0, 55.0)      # continues from heng tail
    pie_tail = (-95.0, -90.0)    # goes down-left, long

    # The 捺 (stroke 3) — head crosses pie ~midway, tail far down-right.
    # Compute weld point on pie shaft so they share exact pixel.
    na_tail = (110.0, -95.0)
    # kiss_apex returns adjusted (pie_head_out, na_head_out) that share apex
    _, na_head = kiss_apex(pie_head, pie_tail, na_tail,
                           u_pie=0.40, bow_pie=-5.0)

    # ---- Stroke 1: small top-left 撇 (short slash) ----
    variant_pie(draw,
                head=(-15.0, 90.0),
                tail=(-40.0, 65.0),
                bow_perp=-3.0, w_head=5.0, w_tail=1.5, n=30)

    # ---- Stroke 2 (draw): 横撇 as two connected segments ----
    # Heng portion (thin, slight taper)
    tapered_line(draw, heng_head, heng_tail, w0=3.0, w1=5.5, n=24)
    # Pie portion (bow left, taper to point) — long sweeping down-left
    variant_pie(draw,
                head=pie_head,
                tail=pie_tail,
                bow_perp=-5.0, w_head=6.5, w_tail=1.0, n=60)

    # ---- Stroke 3: long 捺 crossing the pie, sweeping far down-right ----
    variant_na(draw,
               head=na_head,
               tail=na_tail,
               bow_perp=+8.0, w_head=2.0, w_belly=12.0, w_tail=2.5,
               belly_u=0.70, n=80)

    out = os.path.join(_HERE, "01_夂.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
