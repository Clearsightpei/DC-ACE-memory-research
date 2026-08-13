# p3_char_0256_伐 — 伐 (fá, "to cut/attack"), 6 strokes.
# Composition: 亻 (left, 2 strokes) + 戈 (right, 4 strokes: 横 + 斜钩 + 撇 + 点).
# Left-right L-R composition. Uses ren_pang_char for 亻 and adapts yi_ge (弋)
# for 戈, adding the crossing 撇 through the belly of the 斜钩.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang_char import draw_ren_pang_char  # noqa: E402
from _shared_helpers import tapered_bezier, tapered_line  # noqa: E402

CANVAS = 300


def _sh(mx, my, ox, oy, scale):
    return (mx * scale + ox, my * scale + oy)


def draw_ge(t, ox=0.0, oy=0.0, scale=1.0):
    """戈 — 4 strokes: 横 (short, upper) + 斜钩 (belly, hook) + 撇 (crossing) + 点."""
    # Stroke 1: short heng, upper-middle. Slightly tilted up-right.
    tapered_line(t, _sh(-55, 15, ox, oy, scale), _sh(50, 22, ox, oy, scale), 4, 4)

    # Stroke 2: 斜钩 belly bezier + short hook (starts from upper-left of heng).
    tapered_bezier(
        t,
        _sh(-38, 55, ox, oy, scale),
        _sh(25, -30, ox, oy, scale),
        _sh(50, -95, ox, oy, scale),
        w_head=4, w_tail=5,
        n=64,
    )
    tapered_line(t, _sh(50, -95, ox, oy, scale), _sh(74, -78, ox, oy, scale), 5, 3)

    # Stroke 3: 撇 — crossing from upper-right area down to lower-left,
    # cuts through the belly of the 斜钩.
    tapered_bezier(
        t,
        _sh(15, 50, ox, oy, scale),
        _sh(-25, 5, ox, oy, scale),
        _sh(-60, -55, ox, oy, scale),
        w_head=5, w_tail=2,
        n=48,
    )

    # Stroke 4: 点 — small dot upper-right corner.
    tapered_line(t, _sh(35, 62, ox, oy, scale), _sh(52, 47, ox, oy, scale), 3, 6)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # Wrap ImageDraw so bank primitives (which expect a turtle-like object
    # with .line/.ellipse) work. ImageDraw already has those methods.

    # 亻 on the left — shift left ~-65, compressed to ~0.75.
    # Previous pass: pie was too tall/dominant; tighten scale.
    draw_ren_pang_char(d, ox=-65, oy=-5, scale=0.75)

    # 戈 on the right — shift right ~+30, scale ~0.95.
    draw_ge(d, ox=30, oy=-5, scale=0.95)

    out = os.path.join(os.path.dirname(__file__), "01_伐.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
