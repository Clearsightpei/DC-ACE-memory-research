# 千 (qian) — 3 strokes: short 撇 top, wide 横 middle, long 竖 down.
# Composition inspired by gan.py (干) but top short-横 replaced by a 撇.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from pie import draw_pie    # noqa: E402


CANVAS_SIZE = 300


def draw_qian(t, ox=0.0, oy=0.0, scale=1.0):
    """千: short 撇 (top), wide 横 (middle), long 竖 (through center)."""
    # 1. Top 撇 — sweeps from upper-right down-left, sitting above 横.
    # Head near right of upper area, tail lands near-left where 横 starts.
    # With scale=0.5: head (+32, +45) -> tail (-22, -42) after ox/oy shift.
    draw_pie(t, ox=ox + (-5) * scale, oy=oy + 50 * scale, scale=0.5 * scale)

    # 2. Middle 横 — wide horizontal, slightly above canvas center.
    draw_heng(t, ox=ox + 0, oy=oy + 5 * scale, scale=0.85 * scale)

    # 3. Long 竖 — through the center, extends below the 横 to bottom.
    draw_shu(t, ox=ox + 0, oy=oy + (-20) * scale, scale=0.85 * scale)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_qian(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_千.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
