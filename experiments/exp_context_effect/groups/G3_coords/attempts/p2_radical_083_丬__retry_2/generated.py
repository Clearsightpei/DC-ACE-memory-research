# p2_radical_083_丬 — G3 retry_2.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   retry_n=2 (SHIFT): "distance-from-shaft-too-large" — the two dots+提
#   don't visually merge into the 丬 shape. Original fix idea:
#   variant_dian w_tail≈5 at compact position. From B4 diagnosis of
#   related radicals: (a) P12 violation — GT is MMH thin ink ~4px
#   uniform, NOT calligraphic; must use thin uniform widths not heavy
#   tapered. (b) Composition still off — the three strokes must sit as
#   a compact tight cluster on the LEFT of the spine, not sprawled.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   Compact 撇/dian in radicals (upper-left position, small span);
#   短提 in radicals (tip must stop AT shaft, not cross it); thin
#   uniform-width spine (see wang/tu recipe pattern per P12).
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Uniform thin lines (MMH GT) → thin widths per P12, NOT calligraphic
#   - Per-stroke form → variant_pie / variant_dian for the two upper
#     strokes with SMALL w_tail (~4) to stay thin.
#   Import: variant_pie (short pie), variant_dian (compact dian),
#   tapered_line (spine as uniform-width polyline). Emphasise thin
#   ink (P12) and tip-stops-at-shaft (P9).
#
# Coord convention: math (center origin, +y up). Canvas 300x300.
# All rendered directly in PIL.

from PIL import Image, ImageDraw
import os, sys

CANVAS_SIZE = 300

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)
from _shared_helpers import (  # noqa: E402
    tapered_bezier, tapered_line, variant_pie, variant_dian,
)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ------------------------------------------------------------------
    # GT observation:
    # - Thin uniform ink (~4-5 px), NOT calligraphic (P12).
    # - Right-side long vertical spine with a very small hook/curl at top
    #   pointing left (like the right side of 爿/日 but no full roof).
    # - Two short strokes on the LEFT of the spine, tight cluster:
    #     (a) upper short 撇 (pie) — sits in upper-left, tips down-left,
    #         short (~35 px), slight bow.
    #     (b) middle 提 (rising) — starts lower-left, tip rises to and
    #         stops AT the spine near its middle-upper (P9).
    # - Two left strokes are close together, not sprawled.
    # ------------------------------------------------------------------

    # Spine geometry (position spine on right at x≈+35, span y +100 to y -120)
    SPINE_X = +35
    SPINE_TOP = +105
    SPINE_BOT = -120
    INK = 4  # thin uniform ink per P12

    # Stroke 3: spine. Small leftward curl at top (~8 px), then long shu.
    tapered_line(draw, (SPINE_X - 8, SPINE_TOP - 2), (SPINE_X, SPINE_TOP), INK, INK, n=10)
    tapered_line(draw, (SPINE_X, SPINE_TOP), (SPINE_X, SPINE_BOT), INK, INK, n=50)

    # Stroke 1: upper short 撇 (thin, short, in upper-left cluster).
    # Head at (-5, +75), tail at (-40, +40). Short, thin, subtle bow.
    variant_pie(draw, head=(-5, +75), tail=(-40, +40),
                bow_perp=-2.0, w_head=4.5, w_tail=3.0, n=30)

    # Stroke 2: 提 (rising). Starts (-40, -5), tip STOPS AT spine (+34, +25).
    # Thin, per GT — head slightly heavier than tip.
    tapered_line(draw, (-40, -5), (+33, +25), w0=5, w1=3, n=36)

    out_path = os.path.join(_HERE, "01_丬.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
