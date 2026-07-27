# 仗 = 亻 (left) + 丈 (right).
# 丈 = short heng (top) + pie sweeping down-left + na sweeping down-right,
# pie and na cross just under the heng.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from ren_pang import draw_ren_pang  # noqa: E402

CANVAS = 300


def _to_pixel(mx, my, canvas=CANVAS):
    return canvas / 2 + mx, canvas / 2 - my


def _inline_na(t, x0, y0, x1, y1, w_head=3, w_tail=11, n=60):
    """Tapered 捺: thin head (upper-left) to thick tail (lower-right).
    Slight downward bow (control below the chord)."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0 - 8.0
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # --- Left 亻 ---
    # place ren_pang shifted left of center
    draw_ren_pang(t, ox=-55, oy=0, scale=1.0)

    # --- Right 丈 ---
    # Short heng near top-right
    draw_heng(t, ox=45, oy=70, scale=0.35)

    # Pie: sweeps from just under heng down-left to far lower-left.
    # We want start ~(+55, +55), end ~(-15, -85). Use pie primitive:
    # canonical goes (+65,+90) -> (-45,-85), so shifting oy down works.
    draw_pie(t, ox=15, oy=-25, scale=0.85)

    # Na: starts near the pie/heng crossing (~+15, +40), sweeps down-right
    # to (~+95, -85). Thin head, thick tail.
    x0, y0 = 15, 40
    x1, y1 = 100, -85
    _inline_na(t, x0, y0, x1, y1, w_head=3, w_tail=12)

    out = os.path.join(os.path.dirname(__file__), "01_仗.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    draw()
