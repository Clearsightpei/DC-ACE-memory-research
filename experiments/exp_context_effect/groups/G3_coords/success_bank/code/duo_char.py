"""p3_char_0245_多 — 多 (duō, "many"), 6 strokes.
Composition: two 夕 stacked vertically (top smaller, bottom slightly
right and larger). Uses the frozen bank primitive draw_xi.
G3 v8: bank REFERENCE ONLY — signature (ox, oy, scale) is enough here
because the two 夕 differ only by translation + uniform scale.
"""

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from xi import draw_xi  # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Top 夕 — upper half, slightly left/higher
    draw_xi(d, ox=-15, oy=78, scale=0.62)

    # Bottom 夕 — larger, lower half, offset right so its 撇 tail
    # sweeps out below the top 夕's belly (standard 多 stacking).
    draw_xi(d, ox=10, oy=-38, scale=0.72)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_多.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()
