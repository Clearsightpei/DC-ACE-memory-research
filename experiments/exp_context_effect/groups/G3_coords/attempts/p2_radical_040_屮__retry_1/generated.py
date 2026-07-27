# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   p2_radical_040_屮 is listed in the B1 batch of FAILs (line 235) but
#   without a per-item fix idea (bulk-listed among 23 radicals). Prior
#   attempt (retry_0) rendered a too-tall shaft with disconnected/detached
#   arms rendered at CALLIGRAPHIC ink 11-12 px. Diagnosis vs GT: GT is
#   MMH thin-uniform ~4-5 px lines; shaft is only slightly taller than
#   the arms, not dominant; both arms weld INTO the shaft (not just kiss
#   near it). Fix idea: apply P12 thin-uniform widths (~4 px), shorten the
#   shaft, and inline the whole radical as 3 short polylines that share
#   pixels at the weld points.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   No exact 屮-context rows exist. Closest relevant:
#     - 竖 | full-standalone (shu.py, thickness ~12) — WRONG weight for MMH GT.
#     - Rule in "form_catalog 横 section" (line 82): "when composing with
#       a shu, MATCH the heng thickness to the shu thickness" — implies
#       uniform width across all 3 屮 strokes.
#     - B3 P12 candidate (line 148): "for MMH-median-style GTs use w_head
#       ~4 and w_tail ~2 regardless of stroke label". GT of 屮 is
#       MMH-style thin-uniform => use ~4 px uniform throughout.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing/apex-kiss/cross-shaft weld: NO — 屮's arms weld into the
#     shaft mid-body (T-junction), not an apex kiss. No suitable helper.
#   - Mirror-dot pair: NO — 屮 has no dots.
#   - Per-stroke form (variant_pie/na/dian): NO — all strokes are
#     straight lines / right-angle bends; no bow, no taper needed for MMH.
#   - Uniform thin lines (MMH GT): YES — this is the primary lever.
#     Use thin uniform ~4 px widths, straight lines, no calligraphic
#     brush. No helper import required; just uniform ImageDraw.line calls
#     with width=4.
#
# =====================================================================
# p2_radical_040_屮 (chè) retry_1 — G3 coord-bank
#
# Decomposition per GT (3 strokes, MMH order):
#   1. 竖 (central) — the LONGEST stroke; runs from ABOVE the arm-
#      junction line down to below it. In GT, the shaft is only ~1.2x
#      the arm heights, not 2x. Head at top of glyph.
#   2. 竖折 (left arm) — short vertical down on the left, right-angle
#      elbow, then horizontal RIGHT to weld into the shaft's middle.
#   3. 竖 (right arm) — short slanted vertical on the right side of
#      the shaft; head high (roughly same y as central shaft head),
#      tail near shaft's mid-body. Weld/near-weld to shaft at its base.
#
# Layout (math coords, +y up, origin center, canvas 300):
#   Central shaft: (0, +90) --> (0, -95)         length 185
#   Left arm     : (-55, +25) --> (-55, -30) elbow --> (0, -30) welded
#   Right arm    : (+45, +30) --> (+45, -30)      length 60
#
# Weld math:
#   - Left arm elbow-corner and left-arm horizontal tail both use x=0
#     so the horizontal welds INTO the central shaft.
#   - Right arm's y-range (+30 to -30) sits ENTIRELY inside the shaft's
#     y-range (+90 to -95), so its base coincides visually with shaft.
#
# Widths (P12 thin uniform, MMH-style):
#   ALL 3 strokes = 4 px uniform. No taper, no corner blob (P12 says
#   MMH GTs don't have brush profile; corner blobs add weight the GT
#   doesn't show).

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(mx, my):
    """Math coords (origin center, +y up) -> PIL pixel coords."""
    return (CANVAS // 2 + int(round(mx)), CANVAS // 2 - int(round(my)))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    INK = 4  # P12 thin uniform for MMH-style GT

    # Stroke 1: central 竖 (long vertical shaft).
    p_top = _to_pixel(0, 90)
    p_bot = _to_pixel(0, -95)
    draw.line([p_top, p_bot], fill=(0, 0, 0), width=INK)

    # Stroke 2: left 竖折 (short vertical + right-angle + horizontal
    # welding INTO central shaft at x=0).
    l_head = _to_pixel(-55, 25)
    l_elbow = _to_pixel(-55, -30)
    l_weld = _to_pixel(0, -30)
    draw.line([l_head, l_elbow], fill=(0, 0, 0), width=INK)
    draw.line([l_elbow, l_weld], fill=(0, 0, 0), width=INK)

    # Stroke 3: right short 竖 (slightly slanted upright on right).
    r_head = _to_pixel(45, 30)
    r_tail = _to_pixel(45, -30)
    draw.line([r_head, r_tail], fill=(0, 0, 0), width=INK)

    out = os.path.join(os.path.dirname(__file__), "01_屮.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
