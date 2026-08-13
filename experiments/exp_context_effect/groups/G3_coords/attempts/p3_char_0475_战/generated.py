# p3_char_0475_战 — 战 (zhàn), L-R composition: 占 (left) + 戈 (right).
# Left 占 = 卜 (bu) stacked on 口 (kou) — same recipe as ji_divine's left half.
# Right 戈 = 弋 (yi_ge: 横 + 斜钩 + 点) + one extra middle 撇.
# yi_ge is used as-is (already fits the 3-of-4 strokes of 戈); the 4th
# stroke (middle 撇) is inlined via _shared_helpers.tapered_line.
# No BANK_DEVIATION — bank primitives kept intact; only augmenting.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from bu import draw_bu                       # noqa: E402
from kou import draw_kou                     # noqa: E402
from yi_ge import draw_yi_ge                 # noqa: E402
from _shared_helpers import tapered_line      # noqa: E402


def draw_zhan_battle(t, ox=0.0, oy=0.0, scale=1.0):
    # Left: 占 (卜 on top, 口 on bottom) centered on left half.
    draw_bu(t, ox=ox + (-82) * scale, oy=oy + 40 * scale, scale=0.55 * scale)
    draw_kou(t, ox=ox + (-82) * scale, oy=oy + (-58) * scale, scale=0.55 * scale)

    # Right: 戈. Use yi_ge (横 + 斜钩 + 点) placed on right half at scale ~0.90.
    gx, gy, gs = ox + 35 * scale, oy + (-10) * scale, 0.90 * scale
    draw_yi_ge(t, ox=gx, oy=gy, scale=gs)

    # Extra middle 撇 to convert 弋 → 戈. In yi_ge local coords the 横
    # sits at y~+15 spanning x=-58..48. The 撇 originates above the
    # heng's right third and sweeps down-left through the crossing,
    # ending near the 斜钩 body's mid-lower region.
    # Local head ~ (25, +40); local tail ~ (-55, -40).
    p_head = (gx + 25 * gs, gy + 40 * gs)
    p_tail = (gx + (-55) * gs, gy + (-40) * gs)
    tapered_line(t, p_head, p_tail, 7, 3)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_zhan_battle(t)
    out = os.path.join(_HERE, "01_战.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
