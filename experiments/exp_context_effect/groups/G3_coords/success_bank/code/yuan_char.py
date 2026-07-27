# 元 (yuan) — 4 strokes: short 一 (top) + long 一 + 撇 + 竖弯钩.
# Structural family = 兀 (wu_char) with an extra short 一 on top.
# Reusing draw_heng + draw_er_ren from the bank, similar to wu_char.py
# but with shifted heng positions to make room for the top short heng.
# TR-compliant: every primitive call has deliberate (ox, oy, scale).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng            # noqa: E402
from er_ren import draw_er_ren        # noqa: E402


def draw_yuan(t, ox=0, oy=0, scale=1.0):
    # Stroke 1: short top 一 (短横). Near y=+95, short (scale ~0.35).
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 95 * scale, scale=0.35 * scale)
    # Stroke 2: long main 一. Slightly lower than in 兀 to leave room above.
    # Length ~170 px => scale 0.85. Place at y=+55.
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 55 * scale, scale=0.85 * scale)
    # Strokes 3+4: 儿 below (撇 + 竖弯钩). Shifted up vs wu_char so 撇
    # doesn't fall off canvas bottom; slightly smaller scale.
    draw_er_ren(t, ox=ox + 0 * scale, oy=oy + 5 * scale, scale=0.85 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_yuan(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_元.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
