# p3_char_0140_反 — 反 = 厂 (envelope, top-left) + 又 (tucked bottom-right)
# GT observation: 厂 spans top; heng starts mid-canvas and runs right-ish;
# 丿 falls down the left. The 又 sits in the lower-right, its 横撇 tucking
# under the 厂's heng, 捺 sweeping down-right to bottom-right corner.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from chang import draw_chang  # noqa: E402
from you import draw_you      # noqa: E402


def draw(t):
    # 厂 envelope: only occupies the upper portion of the canvas.
    # Shrink to ~0.55, shift up so heng sits near top and 丿 falls to mid-left.
    draw_chang(t, ox=25, oy=45, scale=0.55)

    # 又 fills the lower-right region, larger scale so it's the visual bulk.
    # Its 横撇 starts inside 厂's frame (upper-mid), 捺 sweeps to bottom-right.
    draw_you(t, ox=25, oy=-25, scale=0.80)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw(t)
    out = os.path.join(_HERE, "01_反.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
