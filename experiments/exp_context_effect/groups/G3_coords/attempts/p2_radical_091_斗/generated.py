# p2_radical_091_斗 (dǒu, "dipper/ladle") — G3 coord attempt.
#
# GT observation (300x300 canvas):
#   4 strokes total.
#   1. Short slanted dot (点), upper-left region, tilted down-right,
#      around head (85, 100) → tail (115, 120) in PIL px.
#   2. Second short slanted dot below the first, also tilted down-right,
#      around head (95, 135) → tail (125, 155) in PIL px.
#   3. Long 横 (horizontal), spanning about x=55..245 at y=180 in PIL,
#      i.e. wider than a bank-default heng.
#   4. Long 竖 (vertical, non-hooked, straight shu), at x=195 in PIL,
#      spanning y ≈ 60..275 — extends from ABOVE the heng down through
#      the bottom, taller than a bank-default shu.
#
# TR8 inline-fresh test:
#   - dian primitive (heng-tail heavy) has default endpoints (-15,+25)
#     → (+18,-20) — good match for the slanted dots after scale 0.32
#     and appropriate ox/oy. USE dian (TR-compliant).
#   - heng primitive is 200 px wide default; GT heng is ~190 px so scale
#     0.95 is uniform-scale, no shape distortion. USE heng.
#   - shu primitive is 200 px tall default; GT shu is ~215 px so
#     scale 1.075 is uniform-scale. USE shu.
#
# All primitive calls have deliberate (ox, oy, scale) per TR1/TR3/TR6.

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian import draw_dian    # noqa: E402
from heng import draw_heng    # noqa: E402
from shu import draw_shu      # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Revision 1 note: first render had dots too tiny/thin. GT dots are
    # longer down-right slashes ~35 px long. Bumping dian scale from
    # 0.32 → 0.55, and shifting positions to match GT better.
    #
    # Stroke 1: upper dot 丶
    #   Target PIL center ≈ (100, 115). Math coords: ox = -50, oy = +35.
    draw_dian(t, ox=-50.0, oy=+35.0, scale=0.55)

    # Stroke 2: lower dot 丶 (below first, slightly right)
    #   Target PIL center ≈ (115, 148). Math: ox = -35, oy = +2.
    draw_dian(t, ox=-35.0, oy=+2.0, scale=0.55)

    # Stroke 3: long 横 (heng), spanning wider than default.
    #   Target PIL center ≈ (150, 180). Math: ox = 0, oy = -30.
    #   scale = 0.95 (uniform, near-default width).
    draw_heng(t, ox=0.0, oy=-30.0, scale=0.95)

    # Stroke 4: long 竖 (shu), tall vertical on the right side.
    #   Target PIL center ≈ (195, 167) — midpoint of (60..275 in y).
    #   Math: ox = 195-150 = +45, oy = 150-167 = -17.
    #   scale = 1.08 for the extra height.
    draw_shu(t, ox=+45.0, oy=-17.0, scale=1.08)

    out_path = os.path.join(HERE, "01_斗.png")
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
