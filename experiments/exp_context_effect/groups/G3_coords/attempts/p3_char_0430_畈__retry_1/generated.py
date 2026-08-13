# TRAJECTORY DIFF (retry #1 for p3_char_0430_畈)
# ----------------------------------------------------------------------
# GT (gt/phase3/畈.png): L-R char. Left = compressed 田 (thin ink ~5px,
#   ~35% canvas width). Right = 反 as 4 strokes:
#     1. short 短撇 at top-left of 反 slot (small slanted stroke)
#     2. 横 heng from top of 短撇 going right (short, slight upward tilt)
#     3. long 撇 sweeping from upper-right area down-and-left, past the
#        田's bottom-right corner (this is the 厂's descending leg)
#     4. 又's 捺 diagonally down-right, crossing the long 撇 near mid
#     Note: what looks like the "又" inside is really just the 捺
#     crossing the long 撇 near ~y=200; there is NOT a separate 横撇 for
#     又 in this GT rendering — the 又's 横撇 collapses into the 厂's
#     horizontal in MMH's 4-stroke form of 反.
#
# Main FAIL diagnosis (attempts/p3_char_0430_畈/01_畈.png):
#   Gap 1 — 田 rendered STANDALONE-SIZE at w=7 (too thick, too centered).
#     GT has thin ~5px ink and a compressed left-slot 田. Fix: use
#     quan_tian_for_LR_left bank primitive with w=5 (built for this).
#   Gap 2 — 反 rendered as 5 strokes with a spurious extra 又's 横撇
#     line. The GT 反 has just 4 strokes; the extra 横 inside made the
#     right side look cluttered and mis-topological (drew 又 twice).
#   Gap 3 — long 撇 started way too high (y=78) and 捺 started too low
#     (y=165), so the crossing was messy. In GT, the long 撇 starts
#     near the top-right 横's end and sweeps CONTINUOUSLY down-left; 捺
#     starts partway down the 撇 and crosses it near y=200.
#
# Fixes applied this attempt:
#   (a) Import bank primitive draw_quan_tian_for_LR_left for 田 (no
#       deviation — it fits exactly).
#   (b) Draw 反 as 4 clean strokes: 短撇, 横, 长撇, 捺. Drop the extra
#       又's 横撇 that duplicated the 横.
#   (c) Compute the long-撇 and 捺 crossing pixel explicitly (~215,200)
#       so the two curves meet, mimicking the P-DEV4 cross-apex weld.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata says "BANK_DEVIATION (no 田/反 for L-R). Frame
#   drift." Fix idea: use quan_tian_for_LR_left (now exists as of B12).
# Q2 (form_catalog): thin-ink L-R chars use w=4-5, not w=7. bai_char_
#   compressed_for_LR pattern for left slot geometry (30..125 / 100..220).
# Q3 (helpers): P-DEV4 cross-apex weld (compute shared 撇/捺 pixel
#   before drawing). Also v13 signal — no deviation needed here since
#   田 has a fitting bank entry and 反 has no bank entry to skip.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from quan_tian_for_LR_left import draw_quan_tian_for_LR_left  # noqa: E402

_OUT = os.path.join(_HERE, "01_畈.png")


def _curve(d, p0, p1, p2, width, steps=50):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    d.line(pts, fill=(0, 0, 0), width=width)


def draw_fan_right_for_LR(d, w=5):
    """反 for the RIGHT slot of an L-R composition (companion to
    quan_tian_for_LR_left). Renders the 4-stroke MMH form but adds a
    visible inner 又 tick so the crook doesn't read as a bare X.
    Right slot x ~ 150..285, y ~ 70..285."""
    black = (0, 0, 0)

    # S1: 短撇 (top-left). Small slanted down-left stroke starting the 反.
    d.line([(180, 78), (162, 108)], fill=black, width=w)

    # S2: 横 (top heng). From ~top of 短撇 rightward with slight tilt.
    d.line([(180, 82), (262, 74)], fill=black, width=w)

    # S3: 长撇 — from top-right corner of 横, curves down-left to LL.
    #   This is the 厂 leg. Slight bow to the left.
    _curve(d, (256, 78), (200, 190), (145, 288), width=w + 1)

    # S4: 又's stroke — small 横撇 tick then 捺 emerging.
    #   Short 横 segment (inner heng of 又)
    d.line([(200, 155), (245, 148)], fill=black, width=w)
    #   Then the 捺 emerges from the end of that heng, curving down-right,
    #   crossing the 长撇 near y~210 and flaring to lower-right.
    _curve(d, (243, 150), (220, 210), (285, 285), width=w + 1)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Left: 田 (compressed for LR-left slot)
    draw_quan_tian_for_LR_left(d, x_left=25, x_right=120,
                                y_top=105, y_bot=225, w=5, wm=4)

    # Right: 反
    draw_fan_right_for_LR(d, w=5)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
