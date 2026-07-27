# p3_char_0083_才 — 才 (cai, "talent"), 3 strokes:
#   1. 横 (horizontal, tilted slightly up, upper region, crosses shaft)
#   2. 竖钩 (vertical + hook, roughly centered horizontally)
#   3. 撇 (left-falling sweep, starts near heng/shaft junction, ends lower-left)
#
# Bank primitives reused: draw_heng, draw_shu_gou, draw_pie.
# All (ox, oy, scale) tuned deliberately for THIS composition per TR1-TR3.

import os
import sys

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402
from pie import draw_pie            # noqa: E402


def draw_cai(t, ox=0.0, oy=0.0, scale=1.0):
    """才: heng near top + long shu_gou through centre + long pie from junction."""
    # 1. 横 — placed in upper-third (oy=+40), spans ~72% width, roughly
    #    centered. Its right end passes noticeably beyond the shaft.
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 40 * scale, scale=0.72 * scale)

    # 2. 竖钩 — near horizontal centre, running from just above the heng
    #    down to lower area with a small left-flick hook.
    draw_shu_gou(t, ox=ox + 10 * scale, oy=oy - 15 * scale, scale=0.90 * scale)

    # 3. 撇 — long sweeping stroke. draw_pie's canonical head is at its
    #    +65,+90 offset (upper-right), tail at -45,-85 (lower-left). We
    #    want the HEAD to sit at ~(-15, +55) (just above the heng/shaft
    #    junction area) and the TAIL to reach ~(-90, -60) (lower-left).
    #    So ox_pie such that ox_pie + 65 ≈ -15 → ox_pie ≈ -80,
    #    oy_pie such that oy_pie + 90 ≈ 55 → oy_pie ≈ -35.
    draw_pie(t, ox=ox - 80 * scale, oy=oy - 35 * scale, scale=0.85 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_cai(d, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_才.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
