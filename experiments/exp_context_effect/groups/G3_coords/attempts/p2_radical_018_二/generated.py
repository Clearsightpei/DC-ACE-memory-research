# p2_radical_018_二 — G3 coord-bank drawer attempt.
#
# 二 (er, "two") = two horizontal strokes stacked.
# - Upper 横: shorter, sits in the upper third of the canvas.
# - Lower 横: longer, sits in the lower third.
#
# Per TR1-TR7:
#   Both use bank primitive draw_heng with deliberate (ox, oy, scale).
#   heng canonical unit is 200x12 px centered on 300x300 (half_len 100 * scale).
# TR2: 二 is a full-standalone radical (not embedded); overall composition
#      spans most of canvas vertically. Neither heng is a "component in a
#      corner slot" — they ARE the whole radical, so scales stay close to 1.0.
# TR3: Origins in math-coord (center origin, +y UP).
#   Upper heng target center pixel ≈ (150, 110)  -> math coord (0, +40)
#   Lower heng target center pixel ≈ (150, 220)  -> math coord (0, -70)
# TR4/TR7: No joint — the two strokes don't touch. Sanity check pixel
#   bounds:
#     Upper: half_len = 100*0.55 = 55 → x ∈ [95, 205], y = 110  (canvas OK, ~10px margin fine).
#     Lower: half_len = 100*0.85 = 85 → x ∈ [65, 235], y = 220  (canvas OK).
# TR5: No extreme scaling (both scales are ≥ 0.55). Reuse the primitive.
# TR6: Transform recorded in-comments above.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from heng import draw_heng


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Revision 1 (post self-check vs GT):
    #  - Upper heng OK on length; GT places it a touch higher → oy +45.
    #  - Lower heng was slightly short and slightly too high vs GT →
    #    push oy down to -80 and bump scale to 0.90 for a longer stroke.
    #
    # Upper 横 — shorter, upper third of canvas.
    # ox=0, oy=+45 (math) → pixel center (150, 105). scale=0.55 → length 110 px.
    draw_heng(t, ox=0, oy=45, scale=0.55)

    # Lower 横 — longer, lower third of canvas.
    # ox=0, oy=-80 (math) → pixel center (150, 230). scale=0.90 → length 180 px.
    draw_heng(t, ox=0, oy=-80, scale=0.90)

    out_path = os.path.join(os.path.dirname(__file__), "01_二.png")
    img.save(out_path)
    print(out_path)


if __name__ == "__main__":
    main()
