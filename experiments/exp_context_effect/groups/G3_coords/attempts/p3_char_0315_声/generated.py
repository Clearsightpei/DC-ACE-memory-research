# p3_char_0315_声 — G3 attempt.
# 声 = 士 (top) stacked on 尸 (bottom, but with its top-heng shared
# with 士's bottom-heng conceptually). Simpler: compose bank primitives
# shi_male (士) + shi_radical (尸), positioning 尸's top-heng to sit
# just below 士 so their shapes form 声's overall silhouette.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(
    _HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_radical import draw_shi_radical  # noqa: E402


def _line(t, x0, y0, x1, y1, w=7):
    """math coords → pixel (canvas 300, math origin at centre)."""
    def _p(x, y):
        return (150 + x, 150 - y)
    ink = max(1, int(round(w)))
    t.line([_p(x0, y0), _p(x1, y1)], fill=(0, 0, 0), width=ink)
    r = ink / 2
    for (x, y) in ((x0, y0), (x1, y1)):
        px, py = _p(x, y)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # 声's top: a short 士-style top heng + short vertical stub.
    # The long horizontal that would be 士's bottom-heng is unified
    # with 尸's top-heng below (they draw as one wide bar).

    # Short top 横 (士 top): ~40% width.
    _line(t, -40, 100, 30, 100, w=6)
    # Short vertical stub connecting top heng down toward wide bar.
    _line(t, -6, 100, -6, 60, w=6)

    # Bottom 尸-body, scaled larger and positioned so its top-heng
    # spans wide and sits just below the stub.
    # shi_radical top-heng is at local (bx from -55 to +50, by=+90).
    # With scale=0.85, ox=-5, oy=-22 → top-heng spans x∈[-52, +47],
    # y ≈ -22 + 90*0.85 = 54. Close to y=60 stub base.
    draw_shi_radical(t, ox=-5, oy=-22, scale=0.85)

    out = os.path.join(_HERE, "01_声.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
