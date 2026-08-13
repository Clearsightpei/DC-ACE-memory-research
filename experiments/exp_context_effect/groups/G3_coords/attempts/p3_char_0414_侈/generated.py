"""p3_char_0414_侈 — 侈 (chǐ, "extravagant"), 8 strokes.
Composition: 亻 (left, 2 strokes) + 多 (right, 6 strokes = two 夕 stacked).
Uses bank primitives draw_ren_pang for 亻 and draw_xi twice for 多.
L-R layout: 亻 on left ~1/3, 多 on right ~2/3.
"""

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from ren_pang import draw_ren_pang  # noqa: E402
from xi import draw_xi              # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left, compressed tall on left third. Kept small so its 撇
    # sweep doesn't invade 多's territory (ding_ren precedent used 0.70).
    draw_ren_pang(d, ox=-85, oy=-5, scale=0.72)

    # 多 on right: replicate duo_char's stacking but shifted right (+30)
    # and slightly smaller (uniform scale 0.88) so it fits the right 2/3.
    right_shift = 30
    s = 0.88
    # Top 夕 — upper half, slightly left/higher (from duo_char)
    draw_xi(d, ox=-15 * s + right_shift, oy=78 * s, scale=0.62 * s)
    # Bottom 夕 — larger, lower, offset right so 撇 sweeps out below.
    draw_xi(d, ox=10 * s + right_shift, oy=-38 * s, scale=0.72 * s)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_侈.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
