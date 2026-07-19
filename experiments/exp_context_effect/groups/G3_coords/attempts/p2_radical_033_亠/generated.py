# p2_radical_033_亠 (tou, "lid" radical) — G3 coord-bank drawer.
#
# Decomposition (from GT + label 亠, 2画):
#   Stroke 1: 点 (dian) — small dot on top, slanted head-to-tail down-right.
#             Centered near top-middle of canvas.
#   Stroke 2: 一 (heng) — wide horizontal below the dot, spanning most of
#             canvas width. This is the "lid" bar.
#
# Bank primitives used (per TR1/TR6, deliberate (ox, oy, scale)):
#   draw_dian: standalone default center is (0,0) math coords, drawn as
#              a bezier from (-15,+25) to (+18,-20). We want the dot
#              centered near top-middle: target math center (0, +45).
#              Scale down slightly (0.6) so the dot is a compact
#              radical-position 点.
#   draw_heng: standalone default is a 200 px bar at math y=0. For 亠's
#              lid we place it below the dot, math y ≈ -15, and slightly
#              shrink to scale=0.90 (target width ~180 px) so it reads
#              as a proper radical horizontal, wider than the dot span.
#
# TR7 eyeball sanity check:
#   - 点 head: math (-9, +60), tail (+11, +33) → PIL (141, 90) to (161, 117).
#     Sits in upper third, small and centered — matches GT.
#   - 一 spans math (-90, -15) to (+90, -15) → PIL (60, 165) to (240, 165).
#     Horizontal below dot with ~30 px gap between dot's tail and bar.
#   - Both fit within 300x300 with >55 px margin all sides.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Ensure the success_bank/code directory is importable
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from dian import draw_dian
from heng import draw_heng


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 1: 点 (top center, small)
    # Default dian center is (0,0). Target center (0, +45) math coords.
    # ox = 0 - 0 = 0; oy = 45 - 0 = 45; scale = 0.6.
    draw_dian(t, ox=0.0, oy=45.0, scale=0.6)

    # Stroke 2: 一 (horizontal bar, wide, below dot)
    # Default heng center is (0,0). Target center (0, -15) math coords.
    # scale = 0.90 gives half_len = 90 → total width 180 px.
    draw_heng(t, ox=0.0, oy=-15.0, scale=0.90)

    out = Path(__file__).with_name("01_亠.png")
    img.save(out)


if __name__ == "__main__":
    main()
