# 亓 (qi) — 4 strokes: short heng (top), long heng (middle), pie (left leg), shu (right leg).
# Revision 1: reduce widths to match MMH thin-GT convention (P12); refine pie/shu positions
# so pie head sits just under-left of the long heng and shu drops from just under-right.
# G3 coord format: inline PIL rendering with deliberately chosen numeric coords.
# (Frozen bank heng/pie/shu bake calligraphic 12px widths; inline thin-line variant matches GT.)

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_thin_heng(t, cx, cy, half_len, width=4):
    x1, y1 = _to_pixel(cx - half_len, cy)
    x2, y2 = _to_pixel(cx + half_len, cy)
    t.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=width)


def draw_thin_shu(t, cx, y_top, y_bot, width=4):
    x1, y1 = _to_pixel(cx, y_top)
    x2, y2 = _to_pixel(cx, y_bot)
    t.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=width)


def draw_thin_pie(t, head_xy, tail_xy, bow_perp=15.0, w_head=5, w_tail=2):
    """Quadratic Bezier pie curve, thin (MMH-GT match)."""
    hx, hy = head_xy
    tx, ty = tail_xy
    mx = (hx + tx) / 2.0 - bow_perp    # pull control point left for the bow
    my = (hy + ty) / 2.0 + 5.0
    n = 60
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * hx + 2 * (1 - u) * u * mx + u ** 2 * tx
        by = (1 - u) ** 2 * hy + 2 * (1 - u) * u * my + u ** 2 * ty
        px, py = _to_pixel(bx, by)
        w = max(1, int(round(w_head + (w_tail - w_head) * u)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w)
        prev = (px, py)


img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
t = ImageDraw.Draw(img)

# Stroke 1: short top 一. Sits high, moderate length. Slight downward-left slant in GT is subtle;
# render level for simplicity.
draw_thin_heng(t, cx=5.0, cy=75.0, half_len=32.0, width=5)

# Stroke 2: long middle 一. Wide horizontal near center.
draw_thin_heng(t, cx=0.0, cy=25.0, half_len=95.0, width=5)

# Stroke 3: 丿 left leg. Head just under-left of the long heng crossing point,
# tail sweeps down to lower-left.
draw_thin_pie(t, head_xy=(-25.0, 20.0), tail_xy=(-80.0, -100.0), bow_perp=18.0,
              w_head=6, w_tail=2)

# Stroke 4: 丨 right leg. Straight vertical from just under the long heng to bottom.
draw_thin_shu(t, cx=45.0, y_top=20.0, y_bot=-100.0, width=5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_亓.png")
img.save(out_path)
print(f"Wrote {out_path}")
