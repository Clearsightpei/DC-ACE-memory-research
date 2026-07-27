# p3_char_0109_仄 — 仄 (zè), 4 strokes: 一 + 丿 (厂 envelope) + 丿 + ㇏ (人 inside)
# Strategy: reuse draw_chang for the 厂 envelope, then place a small 人
# (pie + na) inside the envelope. The 人 sits in the lower-right pocket
# under the horizontal, with its apex tucked below the heng.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from chang import draw_chang  # noqa: E402
from pie import draw_pie      # noqa: E402
from na import draw_na        # noqa: E402


def draw_ze(t, ox=0.0, oy=0.0, scale=1.0):
    # 1) 厂 envelope: heng on top + long descending 丿 on the left.
    #    Shift chang a bit right so 人 has room; keep envelope tall.
    draw_chang(t, ox=ox + 20 * scale, oy=oy + 15 * scale, scale=0.95 * scale)

    # 2) 人 inside the 厂 pocket. Center 人 apex under the middle of the
    #    heng and let strokes reach near bottom of canvas.
    #    Slightly bigger scale (0.65) so it dominates the pocket like GT.
    draw_pie(t, ox=ox + (-5) * scale,  oy=oy + (-40) * scale, scale=0.65 * scale)
    draw_na(t,  ox=ox + 55 * scale,    oy=oy + (-40) * scale, scale=0.60 * scale)


def main():
    canvas = 300
    img = Image.new("RGB", (canvas, canvas), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ze(t, ox=0, oy=-10, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_仄.png")
    img.save(out)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
