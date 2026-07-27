# p2_radical_088_长 — RETRY 2 (B5)
#
# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata (B2 diagnosis): "5-stroke ... distinctive 竖提 + long swept 捺.
#     Force-fit lost long 捺 sweep. Fix: inline 捺 with variant_na,
#     bow_perp≈+12."
#   B3 retry_1 result: fail mode SHIFTED — 捺 sweep OK, but top-heng
#     and 撇 didn't compose with the shaft into 长. Retry_2 lever:
#     rebuild composition so shaft is CENTRAL (not offset left), heng
#     crosses shaft near TOP, 撇 is a small welded flick at heng's left
#     end, and 捺 originates at heng's right end (a shared pixel).
# Q2 (form_catalog): Search form_catalog for stroke rows that apply.
#   - 捺: 大-family crossing arm (mu.py) — head (0,+25), tail
#     (+95,-110), bow +6, w_belly 11, belly_u 0.7. But 长's 捺 wants
#     LONGER, STRONGER belly (bow +12 per errata).
#   - 捺: 久 long sweep (jiu_long_char.py) — head math(-10,-20),
#     tail (+105,-125), bow +10, w_belly 14, belly_u 0.72. Better
#     match to 长's dominant 捺.
#   - 竖提 as one continuous polyline: no direct catalog row; inline
#     as tapered_line shaft + tapered_line ti flick.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Yes: this is a CROSS-SHAFT WELD problem (heng crosses shaft;
#     捺 head must share the heng right-end pixel; 撇 tail must share
#     the heng left-end pixel). Use `line_point` to compute the
#     heng's left-end and right-end pixels EXPLICITLY, then place the
#     dependent strokes' endpoints AT those pixels.
#   - Also uses `variant_pie`, `variant_na`, `tapered_line` from
#     _shared_helpers.
#
# --------------- After the checklist: layout plan ---------------
# Math coords: origin (150,150), +y up.
#
# 长 is 4 strokes. Reading the GT (300x300, thin ink ~5-7 px):
#   (1) 撇 — a short flick starting near the top, tail welding into
#       the LEFT END of the horizontal (2). Reads as a diagonal tick.
#   (2) 横 — short horizontal crossing THROUGH the shaft near its
#       upper portion. Extends both to the LEFT of the shaft (short
#       stub) and to the RIGHT (longer).
#   (3) 竖提 — dominant left backbone: tall thin vertical shaft with
#       a strong up-right ti flick at the bottom. Shaft sits at the
#       LEFT-of-center portion of the character (roughly x=-25).
#   (4) 捺 — DOMINANT: sweeps from just above/at the heng's RIGHT
#       END downward and to the far lower-right with strong belly.
#
# Cohesion trick: pre-compute heng_left and heng_right in math coords;
# then place 撇 tail = heng_left and 捺 head = heng_right (both are
# now shared-pixel welds instead of visually detached).

import os
import sys
from PIL import Image, ImageDraw

BANK_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_DIR)

from _shared_helpers import (  # noqa: E402
    variant_pie,
    variant_na,
    tapered_line,
    line_point,
    to_px,
)

CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- Layout anchors (math coords, +y up) ----
    # Shaft (竖提) x-position: slightly left of center.
    # REV: shift everything DOWN by ~20 to center on canvas
    #      (retry_1 attempt sat too high); slim stroke widths to
    #      better match GT's thin MMH ink profile (P12).
    shaft_x = -25
    shaft_top_y = +60
    shaft_bot_y = -80

    # Heng crosses shaft near top-third; stub-left + longer-right.
    heng_y = +32
    heng_left = (-60, heng_y)
    heng_right = (+50, heng_y)

    # ---- Stroke 3 (backbone drawn FIRST for compositional layering):
    #      竖提 = tall vertical shaft + strong up-right ti flick.
    shaft_top = (shaft_x, shaft_top_y)
    shaft_bot = (shaft_x, shaft_bot_y)
    # Thin, GT-like widths.
    tapered_line(d, shaft_top, shaft_bot, w0=6, w1=8, n=44)
    # Ti flick: strong up-right, tapered heavy -> thin.
    ti_end = (+35, -40)
    tapered_line(d, shaft_bot, ti_end, w0=8, w1=2, n=34)

    # ---- Stroke 2 (横 — crossing through the shaft) ----
    tapered_line(d, heng_left, heng_right, w0=6, w1=5, n=28)

    # ---- Stroke 1 (short 撇 — welded near heng_left) ----
    # Head above and slightly right of heng_left; tail near heng_left.
    pie_head = (heng_left[0] + 18, heng_left[1] + 48)  # (-42, +80)
    pie_tail = (heng_left[0] + 2, heng_left[1] + 2)    # near-weld
    variant_pie(
        d,
        head=pie_head,
        tail=pie_tail,
        bow_perp=-4.0,
        w_head=7.0,
        w_tail=2.5,
    )

    # ---- Stroke 4 (long 捺 — DOMINANT; head welded near heng_right) ----
    # Head slightly ABOVE heng_right so 捺 origin appears at the
    # upper-right corner then sweeps through the heng end.
    na_head = (heng_right[0] - 5, heng_right[1] + 12)  # (+45, +44)
    na_tail = (+125, -115)
    variant_na(
        d,
        head=na_head,
        tail=na_tail,
        bow_perp=+12.0,
        w_head=2.5,
        w_belly=14.0,
        w_tail=3.0,
        belly_u=0.72,
    )

    out_path = os.path.join(os.path.dirname(__file__), "01_长.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
