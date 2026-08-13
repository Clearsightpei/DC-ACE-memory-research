# generated.py — 爱 (ài, "love"). Top-down stack: 爫 + 冖 + 一 + 丿 + 又.
# Uses bank primitives zhao_top (爫), mi_char (冖), heng_pie + na (for 又).
# Top-heng and long pie of 友 are inlined fresh.
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from zhao_top import draw_zhao_top       # noqa: E402
from mi_char import draw_mi_char         # noqa: E402
from heng_pie import draw_heng_pie       # noqa: E402
from na import draw_na                   # noqa: E402

CANVAS = 300


def _to_pixel(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _draw_heng(draw, x0, x1, y, width=6):
    p0 = _to_pixel(x0, y)
    p1 = _to_pixel(x1, y)
    draw.line([p0, p1], fill=(0, 0, 0), width=width)


def _draw_long_pie(draw, x0, y0, x1, y1, w_head=8, w_tail=2, bow=8):
    """Tapered curved pie from (x0,y0) to (x1,y1), bowing to the left."""
    mx = (x0 + x1) / 2.0 - bow
    my = (y0 + y1) / 2.0
    n = 50
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        p = _to_pixel(bx, by)
        w = max(1, int(round(w_head + (w_tail - w_head) * u)))
        if prev is not None:
            draw.line([prev, p], fill=(0, 0, 0), width=w)
            r = w / 2.0
            draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))
        prev = p


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # 1. 爫 top (claw). Compact at the top, narrower.
    draw_zhao_top(draw, ox=0, oy=68, scale=0.65)

    # 2. 冖 middle. Compressed narrower, sits just below 爫.
    draw_mi_char(draw, ox=0, oy=25, scale=0.80)

    # 3. Long 一 (top of 友): the main horizontal below 冖
    _draw_heng(draw, -85, 85, -5, width=7)

    # 4. Long 丿 pie of 友: from upper-right sweep across down-left,
    #    crossing the heng and going into the lower-left area
    _draw_long_pie(draw, 40, 0, -70, -90, w_head=8, w_tail=2, bow=18)

    # 5. 又 (crossing X-shape) at lower-right below the heng
    # heng_pie: horizontal top + pie down-left, positioned right-of-center
    draw_heng_pie(draw, ox=35, oy=-55, scale=0.50)
    # na: crosses through the 撇 shaft (rightward downward sweep)
    draw_na(draw, ox=50, oy=-80, scale=0.55)

    out_path = os.path.join(_HERE, "01_爱.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
