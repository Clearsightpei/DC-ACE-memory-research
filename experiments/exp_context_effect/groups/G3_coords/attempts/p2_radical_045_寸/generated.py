# p2_radical_045_寸 (cun) — G3 coord-bank attempt.
#
# Decomposition of 寸 (3 strokes):
#   1) 一 (heng)     — horizontal, slightly above vertical center, spans most of canvas width.
#   2) 亅 (shu_gou)  — vertical hook, crosses the heng near its right-of-center point,
#                      shaft descends well below the heng, hook flicks up-left at the base.
#   3) 丶 (dian)     — small dot, sits inside the "L" pocket, below-left of the crossing.
#
# Bank primitives used (each with a DELIBERATE (ox, oy, scale) per TR1-TR7):
#   - draw_heng
#   - draw_shu_gou  (invoked directly rather than through the 亅 wrapper because
#                    the wrapper's canonical +22,-5 offset shifts the shaft too far right
#                    for the tighter 寸 composition — TR5 says inline / call the base
#                    primitive when the wrapper's transform doesn't fit).
#   - draw_dian
#
# Canvas: 300x300, math-coord convention (center origin, +y up) applied through each
# primitive's own _to_pixel. All (ox, oy) values below are in math coords.
#
# Layout targets (math coords, center = (0,0)):
#   heng: horizontal centered at (0, +5), scale 0.75 -> half_len=75 px, thickness ~9 px.
#         Ranges x in [-75, +75] at y = +5. In pixels: [(75,145) -> (225,145)].
#   shu_gou: vertical shaft centered at (+15, -25), scale 0.75 -> half_len=67.5 px,
#            so shaft in math y in [+42, -92] (crossing the heng at y=+5 exactly).
#            Hook at base at math (+15, -92) flicks up-left ~19 px.
#   dian: centered at (-15, -35), scale 0.6 -> compact dot in lower-left pocket.
#
# TR4 join check: shu_gou shaft passes THROUGH heng (crossing, not welded). The
# shaft's math y range +42..-92 fully contains the heng's y=+5, so the two strokes
# cross with shared pixels near (+15, +5) — the calligraphic weld happens naturally.
# TR7 canvas fit: heng x-range [75, 225] (margin >=75 px). shu_gou pixel column
# at x=165 spans y=108 to y=242. dian pocket comfortably inside canvas.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402
from dian import draw_dian          # noqa: E402


def main():
    canvas = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(canvas)

    # Stroke 1: 一 (heng). Slightly above center, moderately long.
    # scale 0.75 -> length ~150 px, thickness ~9 px.
    draw_heng(t, ox=0.0, oy=5.0, scale=0.75)

    # Stroke 2: 亅 (shu_gou), called directly (see TR5 note in header).
    # Shaft crosses the heng at math y=+5. Vertical center at (+15, -25) with
    # scale 0.75 gives shaft y range +42..-92 (math). Hook flicks up-left ~19 px.
    draw_shu_gou(t, ox=15.0, oy=-25.0, scale=0.75)

    # Stroke 3: 丶 (dian). Small dot in the lower-left pocket of the L.
    # scale 0.6 shrinks the standard dian so it reads as a compact 点.
    draw_dian(t, ox=-15.0, oy=-35.0, scale=0.6)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_寸.png",
    )
    canvas.save(out_path, "PNG")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
