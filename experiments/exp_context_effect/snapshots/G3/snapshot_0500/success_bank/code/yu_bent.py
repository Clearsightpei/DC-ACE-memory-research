# generated.py — 伛 (yǔ), 6 strokes: 亻 (left) + 区 (right).
# Composition: bank ren_pang (compressed, left-shifted) + inline 区
# (top heng + pie + na X-crossing + bottom 竖折 wrapping).
#
# GT observation (phase3/伛.png):
#   - 亻 sits in left third, pie sweeps down-left from ~top, shu drops
#     from pie mid-shaft down to bottom.
#   - 区 sits in right two-thirds. Top 一 spans right ~half. Inside is
#     a small 乂 (pie + na crossing). Bottom-left 竖折 wraps: short 竖
#     down the left side of 区, then 横 across the bottom.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402

_CANVAS = 300
_INK = 8


def _to_px(bx, by, ox=0, oy=0, scale=1.0):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _line(t, p0, p1, w=_INK):
    r = max(1, w // 2)
    t.line([p0, p1], fill=(0, 0, 0), width=w)
    for p in (p0, p1):
        t.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))


def draw_yu(t, ox=0, oy=0, scale=1.0):
    # ----- Left: 亻 taller, sits in left third -----
    draw_ren_pang(t, ox=ox + (-75) * scale, oy=oy + 0 * scale,
                  scale=0.95 * scale)

    # ----- Right: 区 in right two-thirds -----
    # Bounding box of 区 wrapper (math coords, y up): x in [0, 90], y in [-80, 55]
    rx0, rx1 = 0, 90
    ry_top = 55
    ry_bot = -80

    # Stroke 1: top 一 (heng) — starts near left, sweeps right across
    # the top with slight rise.
    p0 = _to_px(rx0 + 5, ry_top - 2, ox, oy, scale)
    p1 = _to_px(rx1 - 2, ry_top + 4, ox, oy, scale)
    _line(t, p0, p1)

    # Inner 乂 sits comfortably inside the 匚 wrapper (not full-height).
    ix0, ix1 = rx0 + 18, rx1 - 8
    iy_top, iy_bot = ry_top - 20, ry_bot + 20

    # Stroke 2: 撇 (pie) — upper-right → lower-left inside the box.
    p0 = _to_px(ix1 - 5, iy_top, ox, oy, scale)
    p1 = _to_px(ix0, iy_bot, ox, oy, scale)
    _line(t, p0, p1)

    # Stroke 3: 捺 (na) — upper-left → lower-right, crosses the pie.
    p0 = _to_px(ix0 + 5, iy_top - 3, ox, oy, scale)
    p1 = _to_px(ix1, iy_bot - 3, ox, oy, scale)
    _line(t, p0, p1)

    # Stroke 4: 竖折 (shu-zhe) — vertical from just under the top-heng's
    # left end down, then horizontal across the bottom to the right edge.
    v_top = _to_px(rx0, ry_top - 5, ox, oy, scale)
    v_bot = _to_px(rx0, ry_bot, ox, oy, scale)
    h_right = _to_px(rx1 + 3, ry_bot, ox, oy, scale)
    _line(t, v_top, v_bot)
    _line(t, v_bot, h_right)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_yu(t)
    out = os.path.join(os.path.dirname(__file__), "01_伛.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
