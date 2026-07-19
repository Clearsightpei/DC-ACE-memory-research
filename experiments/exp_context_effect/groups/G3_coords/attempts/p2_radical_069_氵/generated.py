# p2_radical_069_氵 — sān diǎn shuǐ (three drops of water)
# Composition: dian (top) + dian (middle, shifted left) + ti (bottom-rising).
#
# Strategy per TR8 (INLINE-FRESH TEST):
#  - dian (top and middle): bank `dian` primitive geometry (thin head ->
#    heavy tail curved down-right) matches 氵's dot shape cosmetically
#    after uniform scale ~0.45. Reuse primitive with deliberate (ox, oy,
#    scale).
#  - ti (bottom): bank `ti` primitive is a rising stroke with thick pressed
#    head and needle tip — this is exactly what 氵's third stroke is.
#    Reuse primitive scaled to ~0.4 with a chosen offset.
#
# Per TR6, transforms are recorded below.
#
# Canvas center = (150,150). Math coords: +y up.
# GT observation (looked at gt/phase2/氵.png):
#   - top dian center approximately pixel (155, 95)  -> math (5, +55)
#   - middle dian center approximately pixel (125, 155) -> math (-25, -5)
#   - bottom ti head approximately pixel (120, 245), tip (165, 195)
#     -> head math (-30, -95), tip math (+15, -45); center ~(-8, -70)
#
# dian default (math): head (-15,+25), tail (+18,-20), center ~(+1,+2)
# ti default (math): head (-70,-70), tip (+80,+60), center ~(+5,-5)

import os
import sys
from PIL import Image, ImageDraw

# Ensure success_bank/code on sys.path for primitive imports.
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from dian import draw_dian  # noqa: E402
from ti import draw_ti      # noqa: E402


def draw():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # REVISION 1 (after pass 1):
    #  - dots were rendering too thin (like small pie strokes); bump scale
    #    to 0.55 so the tail-heavy 点 shape shows properly.
    #  - ti was too long/curved; reduce scale to 0.35 for a shorter cleaner
    #    rising stroke and tighten the position.

    # Stroke 1: top dian. Target center ~(5, +55) math.
    # scale=0.55, dian scaled center ~(+0.5, +1). ox=+5, oy=+54.
    draw_dian(t, ox=+5, oy=+54, scale=0.55)

    # Stroke 2: middle dian. Target center ~(-25, -5) math.
    draw_dian(t, ox=-26, oy=-6, scale=0.55)

    # Stroke 3: bottom ti. Target head math (-30, -95), tip math (+15, -45).
    # At scale 0.35: default head (-70,-70)*0.35 = (-24.5, -24.5); tip
    # (+80,+60)*0.35 = (+28, +21). Chord = 60 px diag — good for a short ti.
    # Center of scaled ti ~ (+2, -1). Target center = (-7.5, -70).
    # ox = -7.5 - 2 = -9.5 → -10; oy = -70 - (-1) = -69.
    draw_ti(t, ox=-10, oy=-69, scale=0.35)

    out = os.path.join(HERE, "01_氵.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    draw()
