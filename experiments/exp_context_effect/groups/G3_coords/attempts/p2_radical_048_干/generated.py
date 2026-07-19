# p2_radical_048_干 — G3 (coord-bank) attempt
#
# 干 (gan) is a 3-stroke radical:
#   1. short 横 at top          (upper heng, ~55% of standard width)
#   2. longer 横 in middle      (middle heng, ~85%)
#   3. 竖 descending through both, centered at ox=0, running from just
#      above the top heng down past the middle heng toward the lower
#      canvas edge with ~15 px bottom margin.
#
# TR6: transforms recorded below.
# - draw_heng canonical: 200 px wide, thickness 12, centered at (ox, oy).
# - draw_shu   canonical: 200 px tall, thickness 12, centered at (ox, oy).
# Math coords: center origin (150,150) in PIL; +y = up.
#
# --- Transform derivation ---
# GT observation: top heng is short and sits high (~y math +55, slightly
# right-of-center), middle heng is wide and sits just above canvas
# center (~y math +5). Shu descends from ~y=+55 (roughly at the top
# heng's midpoint) down to ~y=-95 (well below the middle heng, with
# some bottom margin). Total shu length ~150, so half_len=75 and
# scale = 75 / 100 = 0.75. Shu center oy = (55 + -95)/2 = -20.
#
# Top heng: scale=0.55 -> half_len=55, length=110. oy=+55. ox=+5 (GT
#   top heng centers a hair right of geometric center).
# Middle heng: scale=0.85 -> half_len=85, length=170. oy=+5. ox=0.
# Shu: scale=0.75, ox=0, oy=-20.

import sys, os
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "success_bank", "code",
    ),
)

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 1: 短横 (top short horizontal)
    # target center in math coords ~ (+5, +55)
    draw_heng(t, ox=+5, oy=+55, scale=0.55)

    # Stroke 2: 长横 (middle long horizontal)
    # target center ~ (0, +5)
    draw_heng(t, ox=0, oy=+5, scale=0.85)

    # Stroke 3: 竖 (vertical through both hengs)
    # target center ~ (0, -20), spans y from +55 down to -95
    draw_shu(t, ox=0, oy=-20, scale=0.75)

    out_path = os.path.join(os.path.dirname(__file__), "01_干.png")
    img.save(out_path)
    print("Wrote", out_path)


if __name__ == "__main__":
    main()
