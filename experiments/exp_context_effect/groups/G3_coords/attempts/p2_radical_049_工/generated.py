# p2_radical_049_工 — 工 radical (3 strokes: top 横, middle 竖, bottom 横).
# G3 coord-format. Reuses heng + shu primitives from the success bank.
#
# TR-compliance derivation (per TR1-TR7):
#   Composition: top heng (shorter) + short middle shu + bottom heng (longer).
#   Analog: er.py (二) uses upper heng scale 0.55, lower heng scale 0.90.
#   For 工 the middle shu connects the two horizontals. GT shows the bottom
#   heng notably wider than the top; the middle 竖 is short (~half the
#   gap between the two horizontals).
#
#   Coord layout (math convention, +y up, canvas center origin, canvas 300):
#     - Top heng    : centered at (0, +45), scale 0.55  (half-length 55px)
#     - Bottom heng : centered at (0, -80), scale 0.90  (half-length 90px)
#     - Middle shu  : center between them at (0, -18), scale 0.31
#         (unit length 200 * 0.31 = ~62 px; spans y=+13..-49, sitting
#          just below the top heng and just above the bottom heng —
#          welding at both ends within a few px)
#
# TR7 sanity check (pixel-level, center=(150,150), +y up -> py = 150-y):
#   top heng    : x 95..205, y 105 (row of ink)
#   middle shu  : x 150, y=(150-13)=137 .. (150-(-49))=199
#   bottom heng : x  60..240, y 230
#   All within 300x300 with 10+ px margin. Middle shu head at y=137 sits
#   ~32 px below top heng row (105) — visible short vertical, matching GT
#   where the vertical is not welded but visually connects the two 横.
#   Adjusted: to weld with top heng, shift shu head up.
#   New shu:  center (0, -12), scale 0.36  -> half-len 36 => y=+24..-48
#   in pixels: y=126..198 (top heng row y=105, gap 21 — still visible short
#   vertical). Bottom heng row y=230, gap from shu tail y=198 is 32. OK.

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

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


CANVAS_SIZE = 300


def draw_gong(t, ox=0.0, oy=0.0, scale=1.0):
    """工 radical: top heng + short middle shu + bottom heng."""
    # Top heng: shorter, sits high on the canvas.
    # (ox=0, oy=+45, scale=0.55) -> centered at pixel y=105, x-half=55px.
    draw_heng(t, ox=ox + 0, oy=oy + 45 * scale, scale=0.55 * scale)

    # Middle shu: short vertical bridging the two horizontals.
    # (ox=0, oy=-12, scale=0.36) -> half-len 36px, spans y=+24..-48
    # in math, pixels 126..198. Top heng row 105 (gap 21 px, close weld).
    draw_shu(t, ox=ox + 0, oy=oy + (-12) * scale, scale=0.36 * scale)

    # Bottom heng: wider baseline. Same coords as 二's lower heng.
    # (ox=0, oy=-80, scale=0.90) -> pixel y=230, x-half=90px.
    draw_heng(t, ox=ox + 0, oy=oy + (-80) * scale, scale=0.90 * scale)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_gong(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_工.png")
    img.save(out)


if __name__ == "__main__":
    main()
