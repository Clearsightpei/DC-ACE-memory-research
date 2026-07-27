# p3_char_0050_亍 (chu) — 3 strokes:
#   1) short 横 (top hat)
#   2) wide 横 (middle beam)
#   3) 亅 (shu with left hook) hanging below the middle beam
#
# Composition strategy: reuse draw_heng for the two horizontals,
# reuse draw_jue_char for the hooked vertical. All (ox, oy, scale)
# chosen deliberately from GT visual inspection (TR1-TR3).

import os
import sys
from PIL import Image, ImageDraw

_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng            # noqa: E402
from jue_char import draw_jue_char    # noqa: E402


def draw_chu(t, ox=0, oy=0, scale=1.0):
    # 1) short top 横 — sits well above center, ~50% width
    draw_heng(t, ox=ox + (-5), oy=oy + 75 * scale, scale=0.50 * scale)
    # 2) middle wide 横 — the beam that anchors the hook, ~90% width
    draw_heng(t, ox=ox + 0, oy=oy + 25 * scale, scale=0.95 * scale)
    # 3) 亅 (shu_gou) hanging from the middle beam, centered horizontally.
    #    jue_char shaft_top defaults to +95, we want it at +25 (top of hook
    #    starts a hair below the middle heng). Offset oy by (25-95)=-70.
    #    jue_char shaft_x default is +20 -> offset ox by -20 to bring shaft to 0.
    #    scale 1.0 gives a full-height descender with visible hook.
    draw_jue_char(t, ox=ox + (-20), oy=oy + (-70), scale=1.0)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_chu(t)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0050_亍/01_亍.png"
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
