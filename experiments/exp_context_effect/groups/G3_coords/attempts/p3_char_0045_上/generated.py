# p3_char_0045_上 — three strokes: vertical 竖, short middle 横, long bottom 横.
# Uses frozen shu/heng primitives with deliberate (ox, oy, scale) per TR1-TR3.
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402


def draw_shang(t, ox=0, oy=0, scale=1.0):
    # Math coords: center origin, +y up.
    # Bottom long heng: near y=-80, roughly full width (scale ~1.05).
    draw_heng(t, ox=ox + 0 * scale, oy=oy + -80 * scale, scale=1.05 * scale)
    # Vertical shu: length ~150 px so scale=0.75. Centered at x=-20 (slight
    # left of center so the short middle heng can extend rightward), midpoint
    # at y = -80 + 75 = -5 (so top ~+70, base sits on bottom heng at -80).
    draw_shu(t, ox=ox + -20 * scale, oy=oy + -5 * scale, scale=0.75 * scale)
    # Short middle heng: length ~60 px (scale=0.30), on the right side of the
    # vertical. Left end at ~x=-15, right end ~x=45, so center x=+15.
    # Height y ≈ +20 (about a third up the vertical).
    draw_heng(t, ox=ox + 15 * scale, oy=oy + 20 * scale, scale=0.30 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shang(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_上.png")
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
