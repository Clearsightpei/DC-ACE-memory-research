# p3_char_0211_冯 — 冯 (féng), 5 strokes.
# Structure: 冫 (left) + 马 (right, 3 strokes: 横折 + 竖折折钩 + 横).
# GT (MMH) uses uniform thin ~4-5px lines. Per P12 / L-R scale table:
# left radical ~30% width, right ~65% width.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import tapered_bezier, tapered_line, variant_pie  # noqa: E402


def _px(cx, cy):
    """Math coords to pixel: origin (150,150), y-up."""
    return (150 + cx, 150 - cy)


def draw_feng(draw):
    W = 5  # thin per P12

    # ============ Left 冫 (compact, x ~ -110..-55) ============
    # Top pie/dot: short down-left slash
    tapered_bezier(
        draw,
        _px(-70, +55), _px(-80, +40), _px(-95, +20),
        w_head=W - 1, w_tail=W, n=24,
    )
    # Bottom stroke: down-left curve with up-right hook flick
    tapered_bezier(
        draw,
        _px(-55, +10), _px(-80, -25), _px(-110, -65),
        w_head=W - 1, w_tail=W, n=36,
    )
    # Small up-right hook flick at bottom
    tapered_line(
        draw,
        _px(-110, -65), _px(-90, -55),
        w0=W, w1=W - 3, n=14,
    )

    # ============ Right 马 (x ~ -20..+110) ============

    # Stroke 1: 横折 — top horizontal + turn down
    # Top horizontal
    tapered_line(
        draw,
        _px(-20, +65), _px(+80, +65),
        w0=W, w1=W, n=32,
    )
    # Turn down (short vertical descent)
    tapered_line(
        draw,
        _px(+80, +65), _px(+80, +20),
        w0=W, w1=W, n=18,
    )

    # Stroke 2: 竖折折钩 — starts left, goes down, right, down with hook
    # Left vertical
    tapered_line(
        draw,
        _px(-20, +65), _px(-20, +20),
        w0=W, w1=W, n=18,
    )
    # Middle horizontal (connects across, slightly above the turn)
    tapered_line(
        draw,
        _px(-20, +20), _px(+85, +20),
        w0=W, w1=W, n=30,
    )
    # Down-right descent (slightly curving out)
    tapered_bezier(
        draw,
        _px(+85, +20), _px(+100, -20), _px(+105, -60),
        w_head=W, w_tail=W, n=36,
    )
    # Hook curl at bottom (down-right then up)
    tapered_bezier(
        draw,
        _px(+105, -60), _px(+110, -75), _px(+90, -70),
        w_head=W, w_tail=W - 2, n=20,
    )
    # Hook flick up-left
    tapered_line(
        draw,
        _px(+90, -70), _px(+70, -55),
        w0=W - 2, w1=1, n=14,
    )

    # Stroke 3: 横 — long bottom horizontal (crosses through)
    tapered_line(
        draw,
        _px(-35, -35), _px(+95, -35),
        w0=W, w1=W, n=40,
    )


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_feng(d)
    out = os.path.join(_HERE, "01_冯.png")
    img.save(out)
    print(f"wrote {out}")
