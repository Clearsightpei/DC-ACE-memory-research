# p3_char_0103_亢 — character 亢 (kang).
# Decomposition: 亠 (dot + heng) on top + 几 (pie + heng_zhe_wan_gou) on bottom.
# Both components are mastered in the bank:
#   - tou_radical (亠) at pos 65 (B1)
#   - ji (几) at pos 54 (B1)
# Analogous to wu_char (兀) which composes heng + er_ren; here we compose
# tou_radical + ji. Since 亢's bottom 几 fills more canvas than the standalone
# radical, keep ji at near-full scale; tou_radical sits on top.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from tou_radical import draw_tou_radical  # noqa: E402
from ji import draw_ji                    # noqa: E402


def draw_kang(t, ox=0.0, oy=0.0, scale=1.0):
    """亢 = 亠 (top) + 几 (bottom)."""
    # Revision: in 亢 the 亠 heng and 几 top-heng are visually the SAME line —
    # dot floats above, then one wide horizontal, then pie + 竖弯钩 hang from it.
    # Align ji's top-heng (math y=+55 native, scaled 0.85 = +46.75) with
    # tou_radical's heng (math y=+65+(-15) = +50) by setting ji oy ≈ +3.
    draw_tou_radical(t, ox=ox, oy=oy + 65 * scale, scale=1.0 * scale)
    draw_ji(t, ox=ox, oy=oy + 3 * scale, scale=0.85 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_kang(draw, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_亢.png")
    img.save(out)
    print(f"wrote {out}")
