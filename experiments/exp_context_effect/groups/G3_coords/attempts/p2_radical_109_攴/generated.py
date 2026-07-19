# p2_radical_109_攴 — G3 (coord-bank) attempt.
# 攴 (pu) — 4 strokes: 竖 + 横 (top: 卜-like) + 横撇 + 捺 (bottom: 又-shape).
# GT shows: top = short vertical with a small horizontal on its right (卜),
# bottom = 又 (横撇 crossing 捺).
#
# Composition plan (canvas 300x300, math coords: center origin, +y up):
#   Top 卜 unit occupies upper 40% of canvas (~y in +30..+90).
#   Bottom 又 unit occupies lower 60% (~y in -100..+10), centered horizontally.
#
# Bank primitives reused (all called with deliberate (ox, oy, scale) per TR1):
#   draw_shu       (top 竖)
#   draw_heng      (top 横, short + slightly rising)
#   draw_heng_pie  (upper stroke of 又)
#   draw_na        (捺 crossing 横撇)

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu           # noqa: E402
from heng import draw_heng         # noqa: E402
from heng_pie import draw_heng_pie # noqa: E402
from na import draw_na             # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # --- Top: 卜 (short 竖 + small 横 to its right) ---
    # 竖: shorter than standalone, placed upper-center-left.
    # Standalone 竖 = 200px tall. We want ~60px, so scale ~0.30.
    # Target center of 竖 in math coords ≈ (-8, +65) (canvas upper area).
    draw_shu(t, ox=-8, oy=65, scale=0.30)

    # 横: short horizontal to the right of 竖's midpoint.
    # Standalone 横 = 200px wide. We want ~40px, so scale ~0.20.
    # Target center in math coords ≈ (+22, +55).
    draw_heng(t, ox=22, oy=55, scale=0.20)

    # --- Bottom: 又 (横撇 + 捺 crossing) ---
    # Revision: scale up to ~0.75 to fill the lower half like the GT.
    # 横撇 standalone geometry (scale 1.0): heng from math(-80,+40)->(+65,+50),
    # 撇 down-left to math(-15,-85). At scale=0.75:
    #   heng spans math ~(-60,+30)->(+49,+37) + origin offset
    #   撇 tail lands at math ~(-11,-64) + origin offset
    # Place origin at (-5, -10): heng bar sits around math y ≈ +25, spans
    # roughly math x=-65..+44; 撇 tail lands near math (-16, -74) i.e.
    # canvas pixel ≈ (134, 224) — a bit left of center, near bottom. Good.
    draw_heng_pie(t, ox=-5, oy=-10, scale=0.75)

    # 捺: crosses through the middle of the 横撇's 撇 descent, extending
    # further right to canvas edge.
    # Standalone 捺 sweeps from math(-70,+80) to (+80,-90) at scale 1.0.
    # At scale=0.70: from math(-49,+56) to (+56,-63) relative to origin.
    # Place origin at (+15, -15): head sits near math(-34,+41) (upper-left,
    # meeting the 横撇 turn area) and tail lands near math(+71,-78) i.e.
    # canvas pixel ≈ (221, 228) — bottom-right. Matches GT sweep.
    draw_na(t, ox=15, oy=-15, scale=0.70)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_攴.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
