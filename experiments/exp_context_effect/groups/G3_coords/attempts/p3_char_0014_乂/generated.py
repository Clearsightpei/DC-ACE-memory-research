# generated.py — 乂 (yì), 2 strokes: 撇 + 捺 crossing X.
# Retrieval:
#   form_catalog: 撇 "父 big-撇" and 捺 "父 big-捺" rows are closest matches
#   (source: fu.py). 乂 is essentially fu.py's two big crossing strokes
#   on their own — no small top strokes.
# Approach: use `variant_pie` and `variant_na` adaptive helpers from
# _shared_helpers with numbers derived from fu.py's big-撇 / big-捺 PIL
# coords, converted to math coords (P5): math_x = px - 150, math_y = 150 - py.
#   fu.py big-撇 head (180,118)->math (+30,+32);  tail (55,268)->math (-95,-118)
#   fu.py big-捺 head (120,118)->math (-30,+32); tail (248,268)->math (+98,-118)
# 乂 lacks the two small top strokes, so we shift the crossing slightly
# upward and widen the spread so the character fills the canvas naturally.
# Adjustments vs fu.py numbers:
#   - shift big-撇 head slightly right (+35,+55) so 撇 top sits high-right
#     matching GT (there's a small hook-like curl at the top-right).
#   - shift big-捺 head to (-40,+42) so it starts upper-left.
#   - lower both tails to y=-105 to keep character centered vertically.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "success_bank", "code"))

from PIL import Image, ImageDraw
from _shared_helpers import variant_pie, variant_na, to_px

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)

# Revision (self-check): first render had 撇 too far right, 捺 too clubby,
# crossing sat too high & offset. GT shows a lighter, more balanced X with
# the crossing near geometric center and both strokes reaching similar
# bottom heights. Adjustments:
#   - Move 撇 head slightly left; extend its tail a bit further so both
#     strokes reach ~y=-110 bottom band.
#   - Reduce 捺 belly (13 -> 10) and shift belly_u earlier (0.72 -> 0.65)
#     so it looks like a smoother crescent, not a bulb.
#   - Center the crossing at math (~-5, -20) i.e. PIL (~145, 170).

# Stroke 1: 撇 — from upper-right down-left, gentle rightward bow.
# head math (+45, +65) -> PIL (195, 85)  (small notch top-right per GT)
# tail math (-105, -110) -> PIL (45, 260)
variant_pie(draw,
            head=(+45, +65),
            tail=(-105, -110),
            bow_perp=-7.0,
            w_head=7.0,
            w_tail=1.0,
            n=60)

# Stroke 2: 捺 — from upper-left down-right, gentle belly, thin tail.
# head math (-45, +40) -> PIL (105, 110)
# tail math (+100, -110) -> PIL (250, 260)
variant_na(draw,
           head=(-45, +40),
           tail=(+100, -110),
           bow_perp=+6.0,
           w_head=2.0,
           w_belly=10.0,
           w_tail=2.0,
           belly_u=0.65,
           n=70)

out_path = os.path.join(os.path.dirname(__file__), "01_乂.png")
img.save(out_path)
print(f"wrote {out_path}")
