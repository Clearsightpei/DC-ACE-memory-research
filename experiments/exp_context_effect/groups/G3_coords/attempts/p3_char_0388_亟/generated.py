"""亟 (jí) — character render (revision 1).

Structure (from GT):
  一          (top horizontal, ~85% width, near top y~50)
  口 (mid-left) + 了-like hook running through + 又 (mid-right)
  一          (bottom horizontal, ~95% width, near bottom y~260)

Composition uses bank primitives (heng, kou, you); the mid-hook
connective stroke is inlined fresh.
"""
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng, _to_pixel  # noqa: E402
from kou import draw_kou                # noqa: E402
from you import draw_you                # noqa: E402


CANVAS = 300


def draw_ji(t, ox=0.0, oy=0.0, scale=1.0):
    """亟 — approx 8-stroke character."""
    # 1) Top 一 (near top, pixel y ~ 50 => math oy = +100)
    draw_heng(t, ox=ox + 0, oy=oy + 100 * scale, scale=1.15 * scale)

    # 2) Left 口 — mid-left, moderate size
    #    Target pixel center approx (80, 135) => math (-70, +15).
    #    kou canonical spans about 130x100 at scale=1; want ~55x40 => scale 0.42.
    draw_kou(t, ox=ox + (-70) * scale, oy=oy + 15 * scale, scale=0.42 * scale)

    # 3) Right 又 — mid-right
    #    pixel center approx (200, 145) => math (+50, +5). scale ~0.60
    draw_you(t, ox=ox + 55 * scale, oy=oy + 5 * scale, scale=0.60 * scale)

    # 4) Middle connective hook stroke ("了"-like):
    #    Starts near top-right, drops down-left with a small hook.
    #    In GT it's a diagonal fold running across the middle.
    #    Points in math coords:
    #      P0 (start, upper mid)     : (-20,  +75)
    #      P1 (fold, upper right)    : (+15,  +75)  (short horizontal)
    #      P2 (drop, lower left)     : (-15,  +30)  (down-left diagonal)
    #      P3 (hook tail)            : (-25,  +38)  (small up-left flick)
    p0 = _to_pixel(ox + (-30) * scale, oy + 78 * scale)
    p1 = _to_pixel(ox + 20 * scale,   oy + 78 * scale)
    p2 = _to_pixel(ox + (-20) * scale, oy + 30 * scale)
    p3 = _to_pixel(ox + (-30) * scale, oy + 38 * scale)
    t.line([p0, p1], fill=(0, 0, 0), width=6)
    t.line([p1, p2], fill=(0, 0, 0), width=6)
    t.line([p2, p3], fill=(0, 0, 0), width=6)

    # 5) Bottom 一 — longer, near bottom (pixel y ~ 260 => math oy = -110)
    draw_heng(t, ox=ox + 0, oy=oy + (-110) * scale, scale=1.40 * scale)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ji(t)
    out = os.path.join(_HERE, "01_亟.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
