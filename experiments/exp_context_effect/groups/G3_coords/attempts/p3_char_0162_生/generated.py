# generated.py — 生 (shēng, "birth/life"), 5 strokes.
# Stroke order: 丿 (top pie), 一 (short upper heng), 一 (mid heng),
#               丨 (long shu through both hengs), 一 (long bottom heng).
#
# Composition is close to 牛 (niu.py) but:
#   - the top pie is more centered and shorter (not offset far left),
#   - there is an EXTRA heng at the very bottom (longest of all),
#   - the shu runs from the top short heng down to just above the bottom heng.
#
# Numbers derived from GT observation + niu.py / tu.py precedents.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from pie import draw_pie    # noqa: E402


def draw_sheng(t, ox=0.0, oy=0.0, scale=1.0):
    """生 character, 5 strokes."""
    # 1. 丿 top pie — short, slants down-left, starts near top center
    draw_pie(t, ox=ox + (-8) * scale, oy=oy + 78 * scale, scale=0.40 * scale)
    # 2. 一 short upper heng — sits at top, right of pie's tail
    draw_heng(t, ox=ox + 10 * scale, oy=oy + 55 * scale, scale=0.32 * scale)
    # 3. 一 middle heng — a bit wider than upper heng, centered
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 10 * scale, scale=0.55 * scale)
    # 4. 丨 vertical shu — runs from the top short heng down through the mid heng
    draw_shu(t, ox=ox + 2 * scale, oy=oy + 5 * scale, scale=0.85 * scale)
    # 5. 一 long bottom heng — the longest stroke of all
    draw_heng(t, ox=ox + 0 * scale, oy=oy - 80 * scale, scale=1.10 * scale)


if __name__ == "__main__":
    CANVAS = 300
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_sheng(d, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_生.png")
    img.save(out)
    print("wrote", out)
