# generated.py — 三 (san, "three"). 3 strokes: short top 横, short middle 横,
# long bottom 横. Composed from draw_yi (tapered 横 primitive) at three
# vertical positions with different scales.
#
# GT reading (300x300, math coords, +y up, origin center):
#   top    横: oy ≈ +65, length ≈ 0.55 × canonical (176 px)
#   middle 横: oy ≈  0,  length ≈ 0.50 × canonical
#   bottom 横: oy ≈ -90, length ≈ 1.00 × canonical
#
# TR-compliance: every draw_yi call passes deliberate (ox, oy, scale).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from yi import draw_yi  # noqa: E402


def draw_san_char(t, ox=0, oy=0, scale=1.0):
    # NOTE: draw_yi's `scale` scales WIDTH only, not length_px. Length must
    # be passed explicitly. Canonical length_px = 176.
    # top 横 — short (~95 px)
    draw_yi(t, ox=ox + 0, oy=oy + 65 * scale, scale=0.85 * scale, length_px=95)
    # middle 横 — short (~80 px)
    draw_yi(t, ox=ox + 0, oy=oy + 0 * scale,  scale=0.80 * scale, length_px=80)
    # bottom 横 — long (~180 px)
    draw_yi(t, ox=ox + 0, oy=oy - 90 * scale, scale=1.00 * scale, length_px=180)


def main():
    canvas = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(canvas)
    draw_san_char(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_三.png")
    canvas.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
