# p3_char_0581_望 — G3 coord-bank attempt.
#
# 望 (wàng, "gaze at / hope") — 11 strokes. Structural composition:
#   Top-left:  亡 (3 strokes) — dian + heng + inline 竖折
#   Top-right: 月 (4 strokes) — pie + 横折钩 + 2 interior heng
#   Bottom:    王 (4 strokes) — 3 stacked heng + centered shu
#
# Bank fit (v13 check):
#   - wang_char.py fits 亡 role (identical structure); scale it down + shift.
#   - yue.py fits 月 role (identical structure); scale it down + shift.
#   - heng.py + shu.py compose 王 (per p2_radical_122_王 recipe, scaled).
# All three primitives fit without reshape. No BANK_DEVIATION.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from wang_char import draw_wang_char  # noqa: E402
from yue import draw_yue  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # -- TOP-LEFT: 亡 --
    # wang_char uses math coords (center origin, +y up).
    # Want centered around math (-58, +75), scale ~0.45.
    draw_wang_char(t, ox=-58, oy=+75, scale=0.45)

    # -- TOP-RIGHT: 月 --
    # yue.py uses PIL-px offset: ox pushes right in px, oy pushes down in px.
    # Base yue center is (150, 150) canvas. Want new center at ~(210, 75).
    # ox = 210 - 150 = +60, oy = 75 - 150 = -75. scale ~0.42.
    draw_yue(t, ox=+60, oy=-75, scale=0.42)

    # -- BOTTOM: 王 -- (recipe from p2_radical_122_王, shifted down + slimmer)
    # GT strokes are thin; reduce scale on wide heng to trim thickness while
    # keeping span reasonable. Use ink-only overrides via smaller scales.
    y_shift = -55
    # top heng (medium length)
    draw_heng(t, ox=0, oy=y_shift + 40, scale=0.50)
    # middle heng (shortest)
    draw_heng(t, ox=+3, oy=y_shift + 5, scale=0.40)
    # centered shu piercing all
    draw_shu(t, ox=0, oy=y_shift + 0, scale=0.55)
    # long bottom heng — slightly slimmer to match GT weight
    draw_heng(t, ox=0, oy=y_shift - 55, scale=0.80)

    out = os.path.join(os.path.dirname(__file__), "01_望.png")
    img.save(out)
    return out


if __name__ == "__main__":
    p = render()
    print(p)
