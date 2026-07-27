# p3_char_0131_冗 — 冗 (redundant), 4 strokes = 冖 (top: 点 + 横钩) + 几 (撇 + 横折弯钩).
# G3 first attempt. Compose bank primitives: mi_radical + ji.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from mi_radical import draw_mi_radical  # noqa: E402
from ji import draw_ji                    # noqa: E402


def render(out_path):
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # 冖 (roof) — bank recipe centers roof bar at raw PIL y≈118 (canvas center 150).
    # Shift up (math oy positive) so roof sits in the upper region of 冗.
    # scale ~1.0 so roof spans wide enough to cover the 几 below.
    draw_mi_radical(draw, ox=0, oy=42, scale=1.0)

    # 几 (bottom) — bank recipe spans raw PIL y ≈ 95..260.
    # Shift down (math oy negative) so it sits under the roof; keep scale ~0.9.
    draw_ji(draw, ox=0, oy=-40, scale=0.9)

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_冗.png")
    render(out)
    print("wrote", out)
