# p2_radical_076_小 — G3 coord-format attempt
#
# Decomposition of 小 (3 strokes):
#   1. Central 竖钩 (shu gou): short vertical shaft ending in an up-left
#      hook. In 小 the shaft occupies roughly the middle 40% of the canvas
#      vertically, centered horizontally. Head starts a bit above center;
#      tail (with hook) drops below center.
#   2. Left "丿"-like dot/short pie: short slanted stroke sloping down-left,
#      positioned to the LEFT of the shaft, roughly at the shaft's midpoint
#      height. Head upper-right (near shaft mid), tail lower-left, tapered.
#   3. Right 丶 (dian): a short dot sloping down-right, positioned to the
#      RIGHT of the shaft at similar height. Head upper-left, thick lower-right.
#
# TR8 INLINE-FRESH TEST:
#   - shu_gou primitive: canonical shape (straight vertical + up-left hook)
#     matches the target after uniform scaling — pure translation, TR8 pass.
#   - dian primitive: 丶 is orthographically dian — direct fit after scale.
#   - Left stroke: inlined fresh — it's a short slanted taper, distinctly
#     shorter/steeper than standalone pie; the pie primitive at scale ~0.35
#     would fall below the scale<0.4 inline-warning threshold (TR5).
#
# Bank primitives used (with deliberate transforms per TR1-TR3):
#   - draw_shu_gou at (ox=0, oy=-15, scale=0.65)
#       standalone half_len=90 → 58.5. Shaft top ~y=+43, bot ~y=-73.
#       Hook flicks to (-16, -50) in math coords. Centered horizontally.
#   - draw_dian at (ox=+50, oy=+5, scale=0.6)
#       standalone dian head (-15,+25)→(+18,-20); scaled: (-9,+15)→(+11,-12).
#       Translated to place head near shaft-mid (right side), tail down-right.

import os
import sys
from PIL import Image, ImageDraw

# Import bank primitives from success_bank/code/
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK_CODE)

from shu_gou import draw_shu_gou  # noqa: E402
from dian import draw_dian  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _inline_left_pie(t, head_math, tail_math, w_head=8.0, w_tail=1.0):
    """Inlined short left pie: tapered bezier from thick head to fine tail,
    with a slight leftward bow at the belly (mimics 撇 taper at small scale).
    Endpoints in math coords.
    """
    x0, y0 = head_math
    x1, y1 = tail_math
    # Control point: shift belly slightly down-left of chord midpoint for scoop.
    mx = (x0 + x1) / 2.0 - 4.0
    my = (y0 + y1) / 2.0 - 2.0

    n_segments = 40
    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_xiao(img):
    t = ImageDraw.Draw(img)

    # 1. Central 竖钩 — shaft centered horizontally, spans upper-center to
    #    below-center. Bank primitive is a good fit (TR8 pure-translation
    #    condition met: standalone shape, no bend/tilt).
    #    scale=0.65 → half_len=58.5 → shaft from y=+44 to y=-73 (with oy=-15).
    #    Hook flicks to (-16, -50) in math coords.
    draw_shu_gou(t, ox=0.0, oy=-15.0, scale=0.65)

    # 2. Left stroke (丿-like short pie) — inlined fresh (TR8/TR5 inline call).
    #    Revised: slightly longer and more pronounced scoop; head starts
    #    farther from shaft.
    _inline_left_pie(
        t,
        head_math=(-12.0, 10.0),
        tail_math=(-65.0, -45.0),
        w_head=9.0,
        w_tail=1.0,
    )

    # 3. Right 丶 — bank dian at scale 0.65, positioned right of the shaft.
    #    Revised: slightly larger and shifted right so it's clearly separated.
    #    With ox=+48, oy=-5, scale=0.65: head ~(+38, +11), tail ~(+60, -18).
    draw_dian(t, ox=48.0, oy=-5.0, scale=0.65)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw_xiao(img)
    out_path = os.path.join(_HERE, "01_小.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
