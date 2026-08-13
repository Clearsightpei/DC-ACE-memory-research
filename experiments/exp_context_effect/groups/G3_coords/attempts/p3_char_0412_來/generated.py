# p3_char_0412_來 — 來 (lái, "come"), 8 strokes
# Structure: 木 base + 从 (two small 人) inserted between top heng and mid heng
# Uses draw_mu (bank #81) shape for the base; inlines top-short-heng + two small 人.
#
# Decomposition against GT:
#   1. top short 横 (small heng, upper region)
#   2-3. left small 人 (pie + na), between top and mid
#   4-5. right small 人 (pie + na), between top and mid
#   6. long 横 (mid, main heng)
#   7. long 竖 (through both hengs, extends well below)
#   8-9. bottom 撇 + 捺 from crossing at (0, mid_y) — like 木 legs
#
# No BANK_DEVIATION: draw_mu fits the lower-木 base cleanly at scale=1.0
# with slight downward shift so the top region has room for 一 + 从.

import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "success_bank" / "code"))
from mu import _inline_heng, _inline_pie, _inline_na  # noqa: E402


CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_lai(t, ox=0.0, oy=0.0):
    # We inline everything to keep widths thin (~5-6px) matching MMH GT.
    # Vertical layout (math coords, y up, center=0):
    #   top short heng    at y ≈ +100
    #   two small 人 apex at y ≈  +75, legs to y ≈ +15
    #   mid long heng     at y ≈  +5
    #   long shu          from y≈+110 down to y≈-130
    #   bottom pie/na     from crossing (0, +5) to y≈-140, wide spread

    # ---- Top short 横 ----
    _inline_heng(t, xc=ox + 0, yc=oy + 70, half_len=22, thickness=5)

    # ---- Left small 人 ----
    lx = ox - 38
    left_apex_y = oy + 55
    _inline_pie(t,
                x0=lx, y0=left_apex_y,
                x1=lx - 24, y1=oy + 5,
                w_head=5.0, w_tail=1.0, bow_perp=-2.5)
    _inline_na(t,
               x0=lx, y0=left_apex_y,
               x1=lx + 22, y1=oy + 5,
               w_head=1.5, w_belly=4.0, w_tail=1.5, bow_perp=2.0)

    # ---- Right small 人 ----
    rx = ox + 38
    _inline_pie(t,
                x0=rx, y0=left_apex_y,
                x1=rx - 24, y1=oy + 5,
                w_head=5.0, w_tail=1.0, bow_perp=-2.5)
    _inline_na(t,
               x0=rx, y0=left_apex_y,
               x1=rx + 22, y1=oy + 5,
               w_head=1.5, w_belly=4.0, w_tail=1.5, bow_perp=2.0)

    # ---- Mid long 横 (main heng) ----
    _inline_heng(t, xc=ox + 0, yc=oy - 15, half_len=95, thickness=6)

    # ---- Long central 竖 (shu) ----
    # from just above the mid heng (top overhang small) down to bottom
    xT, yT = _to_pixel(ox + 0, oy + 75)
    xB, yB = _to_pixel(ox + 0, oy - 140)
    t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=6)

    # ---- Bottom 撇 from crossing (0, -15) down-left ----
    _inline_pie(t,
                x0=ox + 0, y0=oy - 15,
                x1=ox - 85, y1=oy - 130,
                w_head=6.0, w_tail=1.0, bow_perp=-5.0)

    # ---- Bottom 捺 from crossing (0, -15) down-right ----
    _inline_na(t,
               x0=ox + 0, y0=oy - 15,
               x1=ox + 90, y1=oy - 130,
               w_head=2.0, w_belly=9.0, w_tail=2.0, bow_perp=5.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_lai(t, ox=0, oy=0)
    out = Path(__file__).parent / "01_來.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
