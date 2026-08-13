# 疒 (nè) — bank entry (B7 curator promotion, v9-rerun PASS)
# Source: groups/G3_coords/attempts/p3_char_0171_疒__retry_1__rerun/generated.py
# Note: 5 (V9 RERUN GRADUATE: inline envelope with uniform thin widths, two interior 冫 marks off pie shaft; guang bank REJECTED for aggressive taper)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

# p3_char_0171_疒__retry_1__rerun — 疒 (sickness-radical), 5 strokes.
#
# VISUAL DIFF (prior retry PNG vs GT PNG — inspected directly):
#   Prior render (retry_1):
#     - Top dot present but small.
#     - Top heng present but the descending 撇 vanishes after a very short
#       thick head (draw_guang tapers to w_tail=1.5 → invisible in most
#       of its span). Result reads as a broken frame with no descender.
#     - The two inner 冫 marks landed AS a tick-cross overlaid on the pie
#       stub (dots too small, too close together, wrong horizontal band).
#     - Net: character reads as a top-only fragment, missing the whole
#       LEFT vertical span and the interior dot pair as separated marks.
#   GT (gt/phase3/疒.png):
#     - Clear top-right small dot.
#     - Clean thin heng roof.
#     - LONG descending 撇 from heng's left end curving down and slightly
#       inward, visible ALL the way to y ≈ 275 with roughly UNIFORM
#       thin-ish weight (not a heavy calligraphic taper-to-nothing).
#     - Two distinctly separated interior 冫 marks: an upper small 点
#       (short slash) around y≈150 and a lower 提 (rising flick) around
#       y≈200, both sitting to the LEFT of the character's vertical
#       centreline (inside the belly, tucked against the pie's upper
#       shaft).
#
# FIX PLAN vs prior:
#   1. Inline the pie with much less taper so it stays visible full length.
#   2. Space the two inner 冫 marks vertically ~40-50 px apart, both
#      clearly OFF the pie shaft, in the LEFT-interior band.
#   3. Keep the top dot small and up-right; keep the heng thin and clean.
#   4. Don't reuse draw_guang — its aggressive taper caused the prior
#      failure. Inline the three envelope strokes with GT-matched widths.
#
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): "疒 — call guang (广) explicitly; drawer omitted the whole
#   envelope." Prior retry DID call guang but the guang pie tapered to
#   nothing so the envelope's descender was effectively omitted visually.
#   Fix: inline the envelope with uniform-ish thin widths per drawer_memory
#   "trust GT" posture (GT is MMH-thin, not calligraphic-heavy).
# Q2 (form_catalog): envelope + interior dot pair. GT-thin widths (w≈4-6).
# Q3 (helpers): No helpers imported. mirror_dian_pair is for horizontal
#   丷 pairs; 疒's 冫 is vertical. Hand-render both marks inline.

import os

from PIL import Image, ImageDraw

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80):
    """Quadratic Bezier from p0 to p1 with control point ctrl. Tapered."""
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_ne_chuang(draw):
    """Render 疒 directly. Coordinates in PIL pixel space (y grows DOWN)."""

    # Stroke 1: top 点 — small tapered slash, upper-right area.
    # Small dot slanting down-left → down-right ish; GT shows a compact
    # short slash sitting above the heng roof, roughly above the heng's
    # right-third.
    _tapered_line(draw, (198, 55), (215, 78), w_head=3.0, w_tail=6.5, n=18)

    # Stroke 2: heng — thin horizontal roof.
    # GT heng spans roughly from mid-left to right edge; keep it thin.
    _tapered_line(draw, (145, 108), (245, 105), w_head=4.5, w_tail=4.5, n=30)

    # Stroke 3: 撇 (long left-falling sweep) welded at heng's left end.
    # This is the failing stroke in prior; make it visible full length.
    # Head at (145, 108) — welded to heng left; tail at (85, 278) — long
    # descending arc curving slightly inward-then-outward. Uniform-ish
    # thin weight (GT is MMH-thin, not calligraphic tapered to zero).
    _tapered_bezier(
        draw,
        p0=(145, 108),
        p1=(85, 278),
        ctrl=(108, 200),      # slight leftward bow in the middle
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # Stroke 4: 冫 upper mark — small 点 (short slash, thin→slightly thicker).
    # Post-revision: shifted LEFT so it sits clear of the pie shaft.
    # Pie at y≈155 is around x≈125, so mark ends at x≈100 (25 px gap).
    _tapered_line(draw, (78, 138), (100, 158), w_head=3.0, w_tail=6.0, n=18)

    # Stroke 5: 冫 lower mark — 提 (rising flick, thick→thin).
    # Post-revision: shifted LEFT and lowered a bit so it sits clear of
    # the pie belly (pie at y≈215 is around x≈105).
    _tapered_line(draw, (58, 218), (95, 202), w_head=7.5, w_tail=2.5, n=20)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_chuang(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疒.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
