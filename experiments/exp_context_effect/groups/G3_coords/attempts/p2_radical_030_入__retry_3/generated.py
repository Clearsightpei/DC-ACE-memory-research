# p2_radical_030_入 — retry #3 (fu.py-template inline recipe).
#
# Diagnosis from prior fails:
#   retry_0: 撇 nearly straight; 捺 too thin — read as an "X" with weak
#            crossing point, not 入.
#   retry_1: 撇 bowed better; 捺 still too thin/floppy; 捺 tail didn't
#            level off; overall silhouette not calligraphic. Both strokes
#            look like thin diagonals, not brush strokes.
#
# Retry_3 approach: use the fu.py PASSed template's _tb() tapered-bezier
# with per-context widths, matching the GT more carefully.
#
# KEY 入-vs-人 DISTINCTION (from B2 sandbox): in 入 the 捺 starts
# ~30% DOWN the 撇 shaft, not at the apex. The 撇 top sticks out
# above the 捺 head. (In 人 they share the apex.)
#
# GT reading (PIL coords, canvas 300x300):
#   撇: head ~(150, 85), bows LEFT through ctrl ~(90, 170),
#       tail ~(76, 253). Uniform brush width with subtle head 顿笔
#       and tail thin taper.
#   捺: head ~(148, 128) — SITS ON 撇 shaft. Sweeps down-right through
#       ctrl ~(205, 218), tail ~(248, 258). Classic 捺 taper: thin
#       head, thick belly (~u=0.72), taper to tail 顿笔.
#
# Widths chosen from form_catalog.md rows for 父 big-撇 / big-捺 and
# adjusted for 入's proportions:
#   撇: w_head 9, w_tail 1, ctrl_perp=-8 (bow left)  [~fu.py big 撇]
#   捺: w_head 2, w_belly 12, w_tail 3, belly_pos 0.72  [~fu.py big 捺
#       but slightly narrower belly since 入 is a lone radical, not
#       a full character]

import os
from PIL import Image, ImageDraw


def _tb(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    """Tapered quadratic bezier (fu.py-template).
    (x0,y0)->(x1,y1) in PIL px. ctrl_perp bows perpendicular to chord
    (positive = right of chord direction)."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_ru(draw):
    """入 radical, 2 strokes. All PIL pixel coords, canvas 300×300.

    REVISION (pass 2): pie was slightly too thick at head (9 read
    heavier than GT); reduced to 7. Also pushed the na belly lower
    (belly_pos 0.72 → 0.78) so the tail levels off nearer the base
    like the GT, and slightly reduced belly (12 → 11) to feel less
    heavy relative to the pie."""
    # Stroke 1: 撇 (pie) — bows left, moderate top → thin tail
    _tb(draw, 150, 85, 76, 253,
        ctrl_perp=-9, w_head=7, w_tail=1, n=70)

    # Stroke 2: 捺 (na) — head sits on 撇 shaft, belly lower, tail
    #   flares before its subtle tail-lift
    _tb(draw, 148, 130, 248, 258,
        ctrl_perp=10, w_head=2, w_belly=11, w_tail=3,
        belly_pos=0.78, n=70)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_ru(d)
    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_入.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
