# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata entry p2_radical_079_弋: "斜钩 with cross dot; the 斜钩 lost its
#   belly. `variant_na` with tuned belly_u could work; or inline a bezier
#   with strong perpendicular bow." Prior attempt used a hand-rolled
#   quadratic bezier and control-point push was miscalibrated — belly ended
#   up bulging on the wrong side and the hook read as a tiny blob. Fix
#   idea: use `variant_na` (proper perpendicular bow computation) for the
#   斜钩 body with generous bow_perp so the rightward-bulge is unmistakable,
#   then draw an explicit tapered up-flick hook from the tail.
#
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   - 捺 | 大-family crossing arm | bow_perp +6, w_head 2, w_belly 11,
#     w_tail 2, belly_u 0.7 (mu.py) → template for a bowed diagonal
#     with belly.
#   - 捺 | 之 平捺 base | bow_perp -10 for sag → shows how bow_perp SIGN
#     controls which side of the chord the arc bulges toward.
#   - 横 | 木 crossing bar | thickness 7 (thinner than primitive) — 弋's
#     short cross-heng should also be thinner than the standalone heng.
#   - 点 | standalone | (-15,+25)→(+18,-20), bow_perp -3, w_head 3,
#     w_tail 13 (dian.py) — but for 弋 the upper-right dot is closer to
#     a short 撇/comma than a dot; use variant_dian with reversed
#     head/tail orientation.
#
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing / apex-kiss / cross-shaft weld → NO (弋 has no
#     apex-kiss; the heng simply crosses the 斜钩 body).
#   - Mirror-dot pair → NO (single dot only).
#   - Per-stroke form (angle/taper/bow) → YES: use `variant_na` for
#     the 斜钩 body (right-bowing bezier with belly). Use
#     `variant_dian` for the upper-right stroke.
#   - Uniform thin lines (MMH GT) → GT shows MMH-style thin uniform
#     lines (per P12). Use thin widths (~4-6) NOT calligraphic 10+.
#
# Plan:
#   Stroke 1: 横 (heng) — short thin heng, crosses through the 斜钩
#     body. Use draw_heng scale ~0.50 (about 100px long), thin.
#     Placed slightly below vertical center, offset a touch left.
#   Stroke 2: 斜钩 (xie gou) body — variant_na from upper-mid to lower-
#     right with POSITIVE bow_perp (bulge to the RIGHT of chord, which
#     is the +perp direction for a downward-going stroke) and thin
#     uniform-ish widths (MMH GT is thin). Then explicit small
#     upward hook flick.
#   Stroke 3: 点 (upper-right small stroke) — variant_dian oriented as
#     a small tilted downstroke (head upper-left, tail lower-right).

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
from _shared_helpers import variant_na, variant_dian, tapered_line, to_px  # noqa: E402

CANVAS_SIZE = 300


def draw_xie_gou_hook(draw, base_math, tip_math, w_head=6.0, w_tail=2.0):
    """Short tapered up-flick from tail of 斜钩. Uses tapered_line so
    it reads as a clear tapered flick, not a blob (per errata P1
    diagnosis and prior attempt's failure mode)."""
    tapered_line(draw, base_math, tip_math, w_head, w_tail, n=20)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 横 (short thin cross-bar, offset slightly left) ----
    # Short cross-heng, thin uniform (P12 — GT shows thin MMH-style
    # lines, not calligraphic). Use tapered_line for consistent thin
    # width (bank heng.py is 12px thick — too heavy for this MMH GT).
    # Position: y ≈ +5 in math coords (GT crossbar is near vertical
    # center, slightly above middle). Length ~100 px, offset left so
    # the crossbar center sits at math x ≈ -20 (the 斜钩 body crosses
    # slightly right of vertical center).
    heng_head = (-70.0, 5.0)
    heng_tail = (+30.0, 5.0)
    tapered_line(draw, heng_head, heng_tail, w0=6.0, w1=6.0, n=20)

    # ---- Stroke 2: 斜钩 body (variant_na, right-bulging bow) ----
    # Head at upper-mid (a bit right of the heng's left end); tail at
    # lower-right where the hook will originate.
    # Chord goes from (-15, +85) down-right to (+55, -95).
    # For variant_na: perpendicular bow with POSITIVE bow_perp pushes
    # the arc perpendicular to chord direction. For a down-right chord
    # (dx>0, dy<0), perp = (-dy/L, dx/L) = (+, +) — positive bow moves
    # UP-RIGHT of the chord. We want the belly to bulge DOWN-RIGHT
    # (outward from the concavity of the character), so use NEGATIVE
    # bow_perp of moderate magnitude.
    # Confirmed by 捺|之 平捺 example: bow_perp -10 for sag (arc below
    # chord). For 弋's 斜钩 the belly hangs below-right of the chord,
    # so bow_perp = -14 (strong perpendicular bow, matches errata
    # "strong perpendicular bow" fix idea).
    pie_head = (-15.0, 85.0)
    pie_tail = (+55.0, -95.0)
    variant_na(draw, head=pie_head, tail=pie_tail,
               bow_perp=-14.0,
               w_head=4.0, w_belly=6.5, w_tail=4.0,
               belly_u=0.65, n=64)

    # ---- Stroke 2b: hook flick UP from tail (P1 hook direction) ----
    # Short tapered flick from pie_tail up-and-slightly-left. Errata
    # for 斜钩 says: "tapered segment (width ~8→2 over ~35 px), heading
    # up and slightly left from p3. Do NOT collapse to ellipse."
    hook_base = pie_tail
    hook_tip = (+38.0, -55.0)  # up 40 px, left 17 px — clearer flick
    draw_xie_gou_hook(draw, hook_base, hook_tip,
                      w_head=8.0, w_tail=2.0)

    # ---- Stroke 3: 点 (upper-right small stroke, comma-like) ----
    # GT shows a short curved stroke in upper-right, oriented like a
    # small 撇/comma (head upper-left, tail lower-right, tail thicker).
    # Not a canonical dot — use variant_dian with tilted orientation.
    # Position: math (+55, +75) head → (+72, +55) tail. Small (~25 px
    # long), thin.
    dian_head = (+50.0, 78.0)
    dian_tail = (+72.0, 55.0)
    variant_dian(draw, head=dian_head, tail=dian_tail,
                 w_head=2.0, w_tail=6.0, bow_perp=-2.0, n=28)

    out_path = os.path.join(os.path.dirname(__file__), "01_弋.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
