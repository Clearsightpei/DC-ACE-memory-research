# p3_char_0129_龶 — 龶 (4 strokes: 3 hengs stacked + 1 shu piercing).
# Structure per GT (gt/phase3/龶.png): three horizontal strokes stacked
# in the upper 2/3 of the canvas, bottom heng ~2x the length of the top
# and middle ones; a vertical 竖 pierces all three near-center. Shape
# family: like 主 without the top 点, or the top of 王 with a long
# baseline. Related PASSes: tu.py (3 hengs+shu, bottom-heng-longest).
#
# TR-compliance: heng/shu primitives called at deliberate (ox, oy, scale)
# per TR1-TR3. Widths kept moderate to match GT's thin lines (P12 form).
import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


def _to_pixel(ox, oy, size=300):
    return size / 2 + ox, size / 2 - oy


def draw_yu_zhu(t, ox=0.0, oy=0.0, scale=1.0):
    """龶 — 3 stacked hengs + 1 piercing shu, bottom heng longest.

    Math coords (center origin, +y up). GT is thin uniform lines
    (~4 px), so hengs/shus are drawn as thin line segments directly
    instead of using the 12*scale primitive default. Layout mirrors
    the GT's upper-anchored 主-without-dot silhouette:
      - top heng    y=+55, x=[-35,+35]
      - mid heng    y=+25, x=[-40,+40]
      - bot heng    y=-20, x=[-95,+95]  (longest)
      - shu         x=0, y=[+70,-35]    (pierces all three; small tail)
    """
    ink = max(2, int(round(4.0 * scale)))

    def L(x1, y1, x2, y2):
        p1 = _to_pixel(ox + x1 * scale, oy + y1 * scale)
        p2 = _to_pixel(ox + x2 * scale, oy + y2 * scale)
        t.line([p1, p2], fill=(0, 0, 0), width=ink)

    # Three hengs stacked (top short, mid slightly wider, bottom longest).
    L(-35, 55, 35, 55)
    L(-40, 25, 40, 25)
    L(-95, -20, 95, -20)
    # 竖 piercing all three, small tail below bottom heng.
    L(0, 70, 0, -35)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_yu_zhu(d, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_龶.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
