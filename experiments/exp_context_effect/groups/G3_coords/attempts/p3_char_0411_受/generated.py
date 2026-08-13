# p3_char_0411_受 — G3 attempt.
# Stacked vertical composition: 爫 (top) + 冖 (middle cap) + 又 (bottom).
# Uses bank primitives zhao_top, mi_radical, you at deliberate (ox,oy,scale).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from zhao_top import draw_zhao_top        # noqa: E402
from mi_radical import draw_mi_radical    # noqa: E402
from you import draw_you                  # noqa: E402


def draw_shou(t):
    # 爫 at top — shift up (+math y), slight shrink
    draw_zhao_top(t, ox=0, oy=52, scale=0.9)
    # 冖 middle cover — shift down a bit so it sits under the claw
    draw_mi_radical(t, ox=0, oy=-15, scale=1.05)
    # 又 bottom — larger, centered so 撇/捺 sweep spans the lower half
    draw_you(t, ox=-8, oy=-72, scale=0.78)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_shou(t)
    out = os.path.join(_HERE, "01_受.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
