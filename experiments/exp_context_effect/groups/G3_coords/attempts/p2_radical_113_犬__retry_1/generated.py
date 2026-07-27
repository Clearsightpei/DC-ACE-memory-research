# p2_radical_113_犬__retry_1 (quǎn, "dog") — G3 coord-bank drawer
#
# 4-stroke radical: 大 (heng + pie + na) + 丶 (dian) upper-right.
# Order: 横 → 撇 → 捺 → 丶
#
# === RETRY_1 FIX (per errata.md) ===
# Prior attempt (retry_0):
#   - Pie/na met BELOW the heng, creating an A-shape rather than 大.
#   - Strokes too thin/uniform; dian floated far right and detached.
#   - Overall proportions felt spidery vs GT's compact ink profile.
#
# Fix (per errata line 390-393 "犬 needs inline-crossing-X recipe, see
# fu.py 父 PASS as template"):
#   - Follow fu.py's inline crossing-X recipe: pie starts from top-center
#     (small head above heng), extends through heng to lower-left.
#   - Na starts from near pie's origin (slight offset right), sweeps
#     down-right with a proper belly. Both pie/na cross ABOVE the heng
#     near its middle and diverge below to form the 大 skeleton.
#   - Heng is placed slightly ABOVE horizontal center so pie/na body
#     dominates lower half (matches GT).
#   - Widths bumped: pie w_head=8, na w_belly=11 (was 6/7 — too thin).
#   - Dian placed at upper-right (above heng, near its right end), NOT
#     detached far-right — GT shows it sitting close to the character.
#
# Following the v7 memory_index read order: form_catalog.md gives
#   撇 | 大-family crossing arm | (0, +25) → (-95, -110) | bow -6, w 7→1
#   捺 | 大-family crossing arm | (0, +25) → (+95, -110) | bow +6, w 2→11→2, belly_u 0.7
# I use these numbers, shifted upward so heng sits at y≈+20 and pie/na
# heads sit at y≈+70 (above heng).
#
# Uses _shared_helpers.variant_pie / variant_na / variant_dian
# (v7 adaptive helpers) — TR-compliant: every call has deliberate
# head/tail/bow/widths chosen for THIS composition.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                "../../success_bank/code"))
from _shared_helpers import (variant_pie, variant_na, variant_dian,
                              tapered_line, to_px)
from PIL import Image, ImageDraw

CANVAS = 300


def draw_quan_radical(draw):
    # === REVISION (pass 2) — GT comparison notes ===
    # v1 had apex too high above heng (~+75 while heng at +20 → 55px
    # gap gave A-triangle look). GT's pie head is a small nub only
    # ~15-25px above the heng. Lowering apex head to +40, making it
    # closer to the heng crossing. Also thinning strokes slightly.
    # Dian was too heavy — reduced tail width.

    # === Stroke 1: 横 (heng) — mid horizontal, slightly above center ===
    tapered_line(draw, (-90, +18), (+92, +22), 6, 7, n=32)

    # === Stroke 2: 撇 (pie) — small head just above heng, sweeps
    # down-left THROUGH the heng to lower-left ===
    # Head lowered from +75 → +42 so apex is closer to heng (GT-like).
    variant_pie(
        draw,
        head=(0, +42),
        tail=(-98, -115),
        bow_perp=-5.0,
        w_head=7.0,
        w_tail=1.5,
        n=60,
    )

    # === Stroke 3: 捺 (na) — from near pie's origin, sweeps down-right
    # with a swelling belly to lower-right ===
    variant_na(
        draw,
        head=(+2, +40),
        tail=(+108, -115),
        bow_perp=+6.0,
        w_head=2.0,
        w_belly=10.0,
        w_tail=2.0,
        belly_u=0.72,
        n=60,
    )

    # === Stroke 4: 丶 (dian) — short right-slanting dot in upper-right,
    # distinguishes 犬 from 大. ===
    variant_dian(
        draw,
        head=(+50, +62),   # thin head upper-left
        tail=(+75, +42),   # heavier tail lower-right
        w_head=2.0,
        w_tail=6.0,
        bow_perp=-2.0,
        n=36,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_quan_radical(draw)
    out_path = os.path.join(os.path.dirname(__file__), "01_犬.png")
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
