# p3_char_0051_于 — G3 first attempt.
# 于 has 3 strokes: short 横 (top), long 横 (middle), 竖钩 with left hook (vertical descender).
# Structurally close to 干 (two heng + shu) but the last stroke is 竖钩 not 竖.
# Reuse draw_heng and draw_shu_gou from the bank; pick (ox, oy, scale) deliberately per TR1-TR3.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402


def draw_yu(t, ox=0.0, oy=0.0, scale=1.0):
    """于: short top 横 + wide middle 横 + 竖钩 vertical with left-pointing hook."""
    # Top short 横 — nudged slightly right; shorter than middle
    draw_heng(t, ox=ox + 8 * scale, oy=oy + 60 * scale, scale=0.50 * scale)
    # Middle long 横 — canvas-centered, longer than top
    draw_heng(t, ox=ox + 0, oy=oy + 10 * scale, scale=0.95 * scale)
    # 竖钩 — vertical shaft starts just above the middle 横 and extends well below,
    # ending with a left-pointing hook flick.
    draw_shu_gou(t, ox=ox + 5 * scale, oy=oy + (-50) * scale, scale=0.85 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_yu(t)
    out = os.path.join(_HERE, "01_于.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
