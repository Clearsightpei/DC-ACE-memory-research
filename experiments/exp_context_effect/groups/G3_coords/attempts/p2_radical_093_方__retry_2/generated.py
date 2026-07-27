# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata p2_radical_093_方 fix idea: "inline 横折钩 with rounded corner +
#   variant_pie for 撇". Prior retry (batch B2) still failed. B4 diagnostics
#   further flag P12 violations: MMH thin-line GTs mis-rendered with a
#   calligraphic (~10-12 px) brush. GT for 方 shows uniform thin ~4-5 px
#   strokes; both prior attempts used 10-12 px. So the concrete rescue is
#   (a) drop widths to MMH-thin (~4-5 px uniform), (b) inline 横折钩 with a
#   rounded (not sharp) corner and a modest up-and-left hook, (c) use
#   variant_pie for the 撇 with matching thin widths and a real bow.
# Q2 (form_catalog): Search form_catalog.md for rows matching the stroke(s)
#   that caused the fail. Which rows are relevant?
#   Relevant rows: (1) 撇 in "envelope + interior" contexts (variant_pie
#   with modest bow_perp ~ -8 and thin widths); (2) 横折钩 in
#   envelope-frame radicals (fang / dao_pang family) — rounded corner, hook
#   up-and-inward. GT weight profile row: MMH radical PNGs are ~4-5 px
#   uniform; do NOT calligraphic-taper.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Per-stroke form (angle/taper/bow): YES — variant_pie for the 撇.
#   - Uniform thin lines (MMH GT): YES — P12: use thin widths (~4-5 px),
#     NOT calligraphic 10-12 px. This is the primary rescue lever missed
#     in both prior attempts.
#   - kiss_apex / pie_point / mirror_dian_pair: NOT applicable (方 has
#     neither an X-crossing nor a mirror-dot pair; 撇 does not share a
#     pixel with 横折钩 in this radical).
#   Import plan: variant_pie from _shared_helpers for the 撇; inline the
#   thin uniform 点, 横, and 横折钩 directly (no bank primitive because
#   fang.py in the bank is 匚, not 方, and heng/dian primitives render
#   heavier than MMH-thin).

"""p2_radical_093_方 — retry_2.

4 strokes: 点 (top), 横 (below), 横折钩 (right envelope), 撇 (left slash).

Prior retry failed because widths were calligraphic (~10-12 px) while
the MMH GT is uniform ~4-5 px. This retry: thin uniform widths (P12),
rounded 横折钩 corner, and variant_pie for the 撇 with modest bow.
"""

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie  # noqa: E402

CANVAS = 300


def _to_pixel(mx, my):
    """Math coords (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + mx, CANVAS / 2 - my)


def _thin_line(D, p0_math, p1_math, w=4):
    """Uniform thin line between two math-coord points."""
    D.line([_to_pixel(*p0_math), _to_pixel(*p1_math)], fill=(0, 0, 0), width=w)


def _thin_polyline(D, pts_math, w=4):
    pts_px = [_to_pixel(*p) for p in pts_math]
    D.line(pts_px, fill=(0, 0, 0), width=w, joint="curve")


def _thin_quad_bezier(D, p0, p1, p2, w=4, n=48):
    """Uniform-width quadratic bezier."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        p_px = _to_pixel(bx, by)
        if prev is not None:
            D.line([prev, p_px], fill=(0, 0, 0), width=w)
        prev = p_px


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)

    W = 5  # MMH-thin uniform stroke width (P12)

    # ---- Stroke 1: 点 — small tilted dot near top-center.
    # Short slanted segment, head upper-left, tail lower-right.
    dot_head = (2.0, 105.0)
    dot_tail = (18.0, 78.0)
    _thin_line(D, dot_head, dot_tail, w=W + 1)

    # ---- Stroke 2: 横 — long horizontal below the dot.
    # Spans ~-95 to +95 (math x), y ≈ +55.
    heng_left = (-95.0, 55.0)
    heng_right = (95.0, 55.0)
    _thin_line(D, heng_left, heng_right, w=W)

    # ---- Stroke 3: 横折钩 — right envelope (rounded corner + hook)
    # Vertical drops from ~top-right of the heng, curves slightly leftward
    # near the bottom, and terminates in a short up-and-left hook (P1).
    # Rounded corner: top few points curve down from horizontal to vertical.
    corner_top = (95.0, 55.0)
    corner_mid = (95.0, 40.0)     # rounded corner
    shaft_start = (92.0, 30.0)
    shaft_end = (72.0, -90.0)     # bows slightly leftward
    # Shaft: quadratic bezier with control point pulled slightly left of chord
    shaft_ctrl = (95.0, -30.0)
    # Draw the rounded corner as a short curve then the shaft as a bezier.
    _thin_polyline(D, [corner_top, corner_mid, shaft_start], w=W)
    _thin_quad_bezier(D, shaft_start, shaft_ctrl, shaft_end, w=W, n=48)

    # Hook: short flick up-and-left from shaft_end (P1).
    hook_start = shaft_end
    hook_end = (52.0, -70.0)  # up (higher y) and left (smaller x)
    _thin_line(D, hook_start, hook_end, w=W)

    # ---- Stroke 4: 撇 — left slash from mid-heng to lower-left.
    # variant_pie takes MATH coords (not pixels) and calls to_px internally.
    # Head near center of heng, tail at lower-left. Modest bow.
    pie_head_math = (-10.0, 55.0)
    pie_tail_math = (-95.0, -95.0)
    variant_pie(
        D,
        head=pie_head_math,
        tail=pie_tail_math,
        bow_perp=-9.0,   # modest leftward bow
        w_head=W + 1,
        w_tail=1.5,
        n=56,
    )

    out = os.path.join(_HERE, "01_方.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
