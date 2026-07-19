# p2_radical_068_扌 — hand radical (shou-pang), 3 strokes.
# Composition (per TR6, transforms declared up-front, math-coord center origin +y up):
#
#   1. 横 (short, slightly tilted): top of radical.
#      canonical heng = 200x12 centered at (0,0). We want a SHORT horizontal
#      in the upper-third, roughly x in [-30, +30], at y ~ +60.
#      -> ox = 0 (center-ish), oy = +60, scale = 0.30 (100*0.30 = 30 px half-length).
#      This lands its left end near (-30, +60) and right end near (+30, +60).
#
#   2. 竖钩 (long, offset slightly right): main vertical shaft w/ hook at bottom.
#      canonical shu_gou = shaft y in [-90, +90], thickness 12, hook 25 px UL from base.
#      GT shows the shaft crossing through the right end of the 横 (around x=+15),
#      going all the way down past y ~ -85. Standalone half-length 90 fits.
#      -> ox = +15, oy = -5, scale = 0.95.
#      Head at (+15, -5+85.5) = (+15, +80.5) — just below the 横's y=+60 (good weld).
#      Base at (+15, -90.5), hook tip at (+15-24, -90.5+21) = (-9, -69).
#
#   3. 提 (rising stroke crossing the shaft on the left): middle-ish, small.
#      canonical ti = bezier from (-70,-70) to (+80,+60). Standalone spans 150px wide.
#      GT shows a short rising stroke starting well LEFT of the shaft, tail
#      hitting the shaft midway (around y=-5, x=+15). So target: head at
#      about (-25, -25), tail at (+18, -3).
#      canonical head (-70,-70), tail (+80,+60): head->tail vector (+150,+130).
#      We want head->tail vector ~ (+43, +22). scale = 0.30 gives (+45, +39) — tail
#      too low. scale=0.30 with oy_shift moves it. Simpler: scale=0.30, ox=+7, oy=+9.
#      That places head at (+7-21, +9-21) = (-14, -12) and tail at (+7+24, +9+18) =
#      (+31, +27). That's a bit HIGH and RIGHT. Adjust: ox=-3, oy=-5 -> head
#      (-24, -26), tail (+21, +13). Head sits mid-left; tail crosses shaft (+15)
#      around y=+9 (mid-upper on shaft). Good.
#
# Eyeball sanity (TR7):
#   - 横 spans x=-30..+30 at y=+60.
#   - 竖钩 shaft spans y=-95..+80 at x=+15; crosses 横 at (+15,+60) — WELD OK.
#   - 提 head at (-24,-26), tail at (+21,+13). Tail crosses shaft (x=+15) at y~+11.
#   - All within 300x300 canvas.

from PIL import Image, ImageDraw
import sys
import os

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, BANK)

from heng import draw_heng
from shu_gou import draw_shu_gou
from ti import draw_ti

CANVAS = 300


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # Stroke 1: 横 — short horizontal, upper third; shifted slightly left so
    # its right end aligns with the shaft (x=+10 shaft — heng spans -30..+30 -> OK).
    # Revision: pulled down to oy=+55, kept centered, scale bumped for visibility.
    draw_heng(t, ox=-5, oy=55, scale=0.33)

    # Stroke 2: 竖钩 — main vertical + hook. Revision: shifted slightly left
    # (ox=+10) so the character sits more centered on canvas.
    draw_shu_gou(t, ox=10, oy=-5, scale=0.95)

    # Stroke 3: 提 — rising stroke crossing shaft near vertical middle.
    # Revision: dropped oy from -5 to -25 so tail crosses shaft at y~-9 (middle).
    # scale 0.32 for a bit more length.
    draw_ti(t, ox=-8, oy=-25, scale=0.32)

    out = os.path.join(os.path.dirname(__file__), "01_扌.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
