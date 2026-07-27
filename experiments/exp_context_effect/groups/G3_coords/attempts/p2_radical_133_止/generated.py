# p2_radical_133_止 — attempt 1 (G3 coord-bank), REVISED once (v6 self-check).
#
# 止 (zhǐ, "stop"), 4 strokes.
#
# From GT (gt/phase2/止.png):
#   - Tall main 竖 is at CENTER (slightly right-of-center), starts near
#     top of upper zone, descends all the way to the baseline.
#   - A SHORTER 竖 is on the LEFT, starts at middle heng level, descends
#     to baseline.
#   - A short 横 is at middle height, connecting the two verticals and
#     extending a bit to the right.
#   - The bottom 横 is the LONGEST, spans most of the canvas.
#
# First render mirrored the tall/short verticals; revised to put tall
# shu on the CENTER-RIGHT and short shu on the LEFT.
#
# Bank calls only: draw_shu (main + left short), draw_heng (middle + long
# bottom). Every (ox, oy, scale) chosen deliberately per TR1-TR3.

from PIL import Image, ImageDraw
import os
import sys

_BANK = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "success_bank", "code"
    )
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def draw_zhi(t, ox=0.0, oy=0.0, scale=1.0):
    """止 radical, 4 strokes."""
    # Stroke: main tall 竖, near center (slightly right-of-center).
    # Canonical shu = 200 px. Want ~150 px tall → scale 0.75.
    # Center at (x=+8, y=+5). Top ≈ +80, bottom ≈ -70 (baseline).
    draw_shu(t, ox=ox + 8 * scale, oy=oy + 5 * scale, scale=0.75 * scale)

    # Stroke: short LEFT 竖, from middle-heng level to baseline.
    # Want ~70 px tall → scale 0.35. Center at (x=-32, y=-35).
    # Top ≈ -0, bottom ≈ -70 (baseline).
    draw_shu(t, ox=ox + (-32) * scale, oy=oy + (-35) * scale, scale=0.35 * scale)

    # Stroke: middle short 横, connects left shu to a bit right of main shu.
    # Want ~100 px → scale 0.50. Center at (x=+5, y=-5).
    # Left end ≈ x=-45, right end ≈ x=+55.
    draw_heng(t, ox=ox + 5 * scale, oy=oy + (-5) * scale, scale=0.50 * scale)

    # Stroke: long bottom 横 (base). Widest stroke.
    # Want ~200 px → scale 1.00. Center at (x=0, y=-75).
    draw_heng(t, ox=ox + 0 * scale, oy=oy + (-75) * scale, scale=1.00 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zhi(d)
    out = os.path.join(os.path.dirname(__file__), "01_止.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
