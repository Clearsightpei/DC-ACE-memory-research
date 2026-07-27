# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata p2_radical_098_火 (B2 fail + B3 retry_1 fail) -> "2 side dots +
#   central 人-shape (pie + na). Pie/na apex-kiss failed same as 人/入.
#   Fix: inline both with shared apex pixel -- validated in fu.py."
#   B3 retry_1 fail mode: "no variant helpers used; drawer went inline-fresh.
#   Fail mode SAME." Additionally the retry_1 PNG shows heavy calligraphic
#   ink (~10px belly on 捺) that dominates the character, while the GT
#   shows THIN uniform ~4-5px lines (P12 violation).
# Q2 (form_catalog): Search form_catalog.md for rows matching the stroke(s)
#   that caused the fail. Which rows are relevant?
#   - "Mirror-dot family (忄, 丷, 火, 犬 side dot)" section: use
#     mirror_dian_pair for the two side dots (do NOT hand-tune each).
#   - P12 (form_catalog line 148): "for GTs rendered in MMH-median style
#     (thin uniform lines, no brush profile), use w_head ~4 and w_tail ~2".
#     This applies here -- gt/phase2/火.png is a thin-uniform MMH render.
#   - 撇 row "丿-char thin uniform (MMH-style)": w_head 4, w_tail 2, bow -10.
#   - 捺 rows: "亼 right arm (thin, kiss_apex)" w=4/0.7. Thin-uniform captures
#     the GT weight.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Mirror-dot pair (忄, 丷, 火, 犬 side dot) -> mirror_dian_pair : YES,
#     use it for the two side dots (leftmost + rightmost). NOTE: 火's side
#     dots are actually a left-dot (点, thick head lower-left) and a
#     right-short-pie (thick head upper-right, thin tail lower-left) -- they
#     do NOT mirror perfectly on the shaft, but mirror_dian_pair gives a
#     reasonable base geometry which we adjust manually per B3 P12 evidence.
#   - X-crossing (pie + na sharing pixel) -> kiss_apex: YES for the central
#     人-shape, but 火's pie/na cross MID-shaft (not at apex like 人). Use
#     kiss_apex with u_pie ~0.25 (na starts ~1/4 down the pie shaft).
#   - Thin uniform lines (MMH GT) -> use thin widths per P12: YES. All
#     strokes rendered with w<=5.
"""
火 (huǒ) — 4-stroke radical, retry_2.

Fix strategy vs retry_1:
1. THIN UNIFORM WIDTHS (P12): all strokes ~3-5 px, no calligraphic belly.
   retry_1's fatal flaw was a w_belly=14 on the 捺, giving a heavy
   swordfish body that dominated the character.
2. USE mirror_dian_pair for the two side dots (memory helper).
3. USE kiss_apex to compute the exact pie-shaft pixel where 捺 welds --
   fixes the disconnected na-head from retry_1.
4. Central 撇 slightly bowed left; 捺 branches off pie's u=0.25 and
   sweeps down-right to the bottom-right.

Convention: math coords (center origin, +y up); helpers do the flip.
"""
from PIL import Image, ImageDraw
import os
import sys

# Import the shared helpers from success_bank/code.
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)
from _shared_helpers import (  # noqa: E402
    variant_dian, variant_pie, variant_na,
    mirror_dian_pair, kiss_apex,
)

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


# ---- Central 撇 (long, slight left bow, thin uniform) ----
# Math coords: head near top-center, tail bottom-left.
pie_head = (5, 85)     # ~PIL (155, 65) — top-center
pie_tail = (-70, -100) # ~PIL (80, 250) — bottom-left
BOW_PIE = -8.0         # bow LEFT (perp of down-left dir)

# ---- 捺 branches off pie mid-shaft (u=0.25) and sweeps down-right ----
# Use kiss_apex to compute the exact weld pixel on the pie curve.
_, na_head = kiss_apex(pie_head, pie_tail, na_tail=None,
                       u_pie=0.25, bow_pie=BOW_PIE)
na_tail = (75, -100)   # ~PIL (225, 250) — bottom-right

# ---- Side dots via mirror_dian_pair (thin, per P12) ----
# REVISION vs pass 1: dots were too HIGH (above pie apex) and too long.
# GT shows the two side dots FLANK the crossing region (mid-height of
# the 人 body), not above the apex. Move y_center DOWN and shorten.
left_dot, right_dot = mirror_dian_pair(
    shaft_x=pie_head[0], y_center=+15,   # was +40 -- flank crossing
    spread=40.0,          # slightly tighter so dots hug the body
    w_head=2.0, w_tail=4.0,  # THIN per P12
    tilt=7.0,             # was 10 -- shorter, more compact dots
)

# 火-specific adjustment: the LEFT dot is a standard 点 (head upper-right,
# thick tail lower-left) — mirror_dian_pair's `left` gives head upper-LEFT,
# so we swap head/tail to flip the direction.
lh, lt = left_dot["head"], left_dot["tail"]
left_dot["head"], left_dot["tail"] = lt, lh
# Right dot is a short 撇: head upper-right (thin), tail lower-left (thick).
# mirror_dian_pair's `right` already has that geometry; keep as-is but
# swap so head is thin -> tail thick (standard short-pie is thick to thin
# actually, but for a compact "right dot" in 火 the terminal is toward the
# central shape, so head should be upper-outer thin, tail lower-inner thick).
# Actually keep default: right head is upper-left (near shaft), tail lower-right.
# For 火 the right dot points DOWN-LEFT toward the central shape, so we
# want head upper-RIGHT, tail lower-LEFT (inner). Flip head/tail.
rh, rt = right_dot["head"], right_dot["tail"]
right_dot["head"], right_dot["tail"] = rt, rh

# ---- Draw the two dots ----
variant_dian(draw, **left_dot)
variant_dian(draw, **right_dot)

# ---- Draw the central 撇 (thin uniform per P12) ----
variant_pie(draw, head=pie_head, tail=pie_tail,
            bow_perp=BOW_PIE, w_head=5.0, w_tail=2.0, n=60)

# ---- Draw the 捺 (thin, slight belly, per P12 kept small) ----
# Weld head = na_head from kiss_apex; sweep to na_tail.
variant_na(draw, head=na_head, tail=na_tail,
           bow_perp=+7.0, w_head=2.0, w_belly=5.5, w_tail=3.0,
           belly_u=0.7, n=60)


out_path = os.path.join(HERE, "01_火.png")
img.save(out_path)
print(f"Wrote {out_path}")
