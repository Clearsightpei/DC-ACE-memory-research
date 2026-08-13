# TRAJECTORY DIFF (retry #1 of p3_char_0463_神)
# GT (gt/phase3/神.png): thin uniform strokes, calligraphic hand-drawn feel.
#   Left 礻: 点 top-left, 横撇 with corner blob, long 竖, right 点.
#   Right 申: rectangular box with 竖 through center; strokes THIN (~4-6 px),
#            slightly irregular, NOT block-perfect.
# main attempt (verdict: C): 礻 side reasonable (uses bank tapered_bezier);
#   BUT 申 right side rendered with plain PIL d.line at width 7-9 → looks
#   like a mechanical box, too thick, no calligraphic feel. Center 竖 too
#   thick (9 px) vs GT's uniform-thin.
# Fixes this attempt:
#   1. Reuse shi_ceremony_pang for 礻 (worked).
#   2. Rewrite 申 using tapered_line helpers with THINNER widths (4-5 px)
#      so it matches GT's thin calligraphic strokes.
#   3. Keep the box slightly narrower and better proportioned in right half.

# RETRY MEMORY CHECKLIST
# Q1 (errata): errata says "shen_extend canvas-abs; inline compressed 申 in
#   right slot". Fix: inline 申 using math-coord-ish helpers, not
#   canvas-absolute; also thin the strokes to match GT.
# Q2 (form_catalog): 申 box strokes — treat as thin heng + shu (~4-5 px
#   uniform). Center 竖 is one long stroke through the box.
# Q3 (helpers): use tapered_line for uniform-thin strokes; no
#   X-crossing/mirror-dot/dog helpers apply here.

# BANK_DEVIATION
# skipped: shen_extend.py
# reason: bank primitive uses full-canvas absolute coords and cannot compress
#   into the right slot of an L-R composition; also its widths are too thick
#   for MMH GT's thin calligraphic strokes.
# fresh_component: shen_variant_for_LR_right_thin

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_ceremony_pang import draw_shi_ceremony_pang  # noqa: E402
from _shared_helpers import tapered_line  # noqa: E402

CANVAS = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_神.png")


def draw_shen_right_thin(d):
    """申 in the right slot, thin calligraphic strokes to match MMH GT.

    Uses math coords (center origin, +y up) as expected by tapered_line.
    Canvas center (150, 150). Right slot spans approx mx=15..108,
    box vertical span my=45..-65.
    """
    mx_left = 15
    mx_right = 100
    my_top = 45
    my_bot = -60
    my_mid = -8
    mx_center = (mx_left + mx_right) // 2  # 57
    w = 4.5

    # Stroke 1: left 竖 of box
    tapered_line(d, (mx_left, my_top), (mx_left, my_bot), w, w, n=20)
    # Stroke 2: 横折 — top heng
    tapered_line(d, (mx_left, my_top), (mx_right, my_top), w, w, n=20)
    # Stroke 2b: right 竖
    tapered_line(d, (mx_right, my_top), (mx_right, my_bot), w, w, n=20)
    # Stroke 3: middle 横
    tapered_line(d, (mx_left + 2, my_mid), (mx_right - 2, my_mid), w, w, n=20)
    # Stroke 4: bottom 横
    tapered_line(d, (mx_left, my_bot), (mx_right, my_bot), w, w, n=20)
    # Stroke 5: central 竖 protruding above (~+95) and below (~-115).
    tapered_line(d, (mx_center, 95), (mx_center, -115), w + 0.5, w + 0.5, n=30)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    # Left: 礻 (bank primitive, math coords converted internally).
    draw_shi_ceremony_pang(d, ox=-75.0, oy=0.0, scale=0.62)
    # Right: 申 (fresh inline, thin strokes).
    draw_shen_right_thin(d)
    img.save(OUT_PNG)
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
