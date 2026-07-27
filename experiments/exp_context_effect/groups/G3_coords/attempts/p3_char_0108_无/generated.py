# p3_char_0108_无 — 无 (wú, "none"), 4 strokes.
# Composition: short 横 (top) + long 横 (mid) + 撇 (through mid heng, curving
# down-left) + 竖弯钩 (right leg). Structurally: 兀-family with an extra
# shorter heng on top. Recipe adapts wu_char (heng 0.85 + er_ren 0.95).
#
# Bank calls with deliberate (ox, oy, scale) per TR1-TR3.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng            # noqa: E402
from er_ren import draw_er_ren        # noqa: E402


def draw_wu(t, ox=0, oy=0, scale=1.0):
    # Stroke 1: short 横 on top (~45% width), slightly left of center,
    # close above the long heng.
    draw_heng(t, ox=ox - 10 * scale, oy=oy + 75 * scale, scale=0.45 * scale)
    # Stroke 2: long 横 (main) — full-length
    draw_heng(t, ox=ox, oy=oy + 45 * scale, scale=0.85 * scale)
    # Strokes 3+4: 儿 (撇 + 竖弯钩) below the long heng.
    draw_er_ren(t, ox=ox, oy=oy - 15 * scale, scale=1.00 * scale)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_wu(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_无.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
